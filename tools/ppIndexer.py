import urllib2
import re
import time
import string
import json
import thread
import threading

userNum = 10000
userPerPage = 50
maxpp = 600
sleeptime = 0.5
fetchlock = threading.RLock()
indexlock = threading.RLock()

url_performance = "http://osu.ppy.sh/p/pp/?page="
url_bp= "http://osu.ppy.sh/pages/include/profile-leader.php?u="

index = range(0, maxpp+1)
for i in range(0, maxpp+1):
    index[i] = {}

def fetchplayer(playerID):
    #get best performance, get rid of first place ranks
    bpresponse = urllib2.urlopen(url_bp+playerID).read()
    
    p = re.compile("Best .*?Performance([\S\s]*?)First Place Ranks")
    bpresponse = p.findall(bpresponse)[0]
    
    pmap = re.compile('<b>(<a href=.*?</a>).*?</b>')
    mapresult = pmap.findall(bpresponse)
    #print len(mapresult)
    pp = re.compile("<b>(\d+)pp</b>")
    ppresult = pp.findall(bpresponse)
    #print len(ppresult)
    weight = re.compile("weighted <b>(\d+)%</b>")
    weightresult = weight.findall(bpresponse)
    #print len(weightresult)
    
    #indexer
    if len(mapresult) == 50 and len(ppresult) == 50 and len(weightresult) == 50:
        indexlock.acquire()
        for i in range(0, 50):
            mapvalue = mapresult[i]
            ppvalue = string.atoi(ppresult[i])
            weightvalue = string.atoi(weightresult[i])
            if ppvalue > maxpp:
                continue
            if not index[ppvalue].has_key(mapvalue):
                index[ppvalue][mapvalue] = weightvalue
            else:
                index[ppvalue][mapvalue] += weightvalue
        finish_list.append(playerID)
        indexlock.release()

def fetchperformance(i):
    #print url_performance+str(i)
    response = urllib2.urlopen(url_performance+str(i)).read()
    p = re.compile("<td><img class='flag' src=.*?(\d+).*?</a></td>")
    m = p.findall(response)
    fetchlock.acquire()
    for i in m:
        playerID_list.append(i)
    fetchlock.release()


#fetch top player
playerID_list = []
print 'start fetching...'
for i in range(1, userNum/userPerPage+1) :
    thread.start_new_thread(fetchperformance, (i,))
    if i % 20 == 0:
        print str(i*50)
    time.sleep(sleeptime)

print 'waiting for threads to exit...'
count = 0
while len(playerID_list) < userNum:
    print 'finished: '+str(len(playerID_list))+'  '+str(count)+' ticks'
    time.sleep(5)
    count = count+1
    if count > 20:
        break

#playerID_list = ['352328']
print 'start indexing...'
num = 0
finish_list = []
for playerID in playerID_list :
    num += 1
    if num % 100 == 0:
        print str(num)
    thread.start_new_thread(fetchplayer, (playerID,))
    time.sleep(sleeptime)

print 'waiting for threads to exit...'
count = 0
while len(finish_list) < userNum:
    print 'finished: '+str(len(finish_list))+'  '+str(count)+' ticks'
    time.sleep(5)
    count = count+1
    if count > 20:
        break

#fetchplayer('352328')
#print index

output = open('ppIndex.txt', 'w')
output.write(json.dumps(index))
output.close()

