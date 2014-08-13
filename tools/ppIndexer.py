import urllib2
import re
import time
import string
import json


userNum = 10000
userPerPage = 50
maxpp = 600
sleeptime = 0.02

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
    time.sleep(sleeptime)
    #indexer
    if len(mapresult) == 50 and len(ppresult) == 50 and len(weightresult) == 50:
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




#fetch top player
playerID_list = []
print 'fetching...'
for i in range(1, userNum/userPerPage+1) :
    print str(i*50)
    response = urllib2.urlopen(url_performance+str(i)).read()
    p = re.compile("<td><img class='flag' src=.*?(\d+).*?</a></td>")
    m = p.findall(response)
    for i in m:
        playerID_list.append(i)
    time.sleep(2*sleeptime)
    

#playerID_list = ['352328']
print 'indexing...'
num = 0
for playerID in playerID_list :
    num += 1
    print str(num)
    fetchplayer(playerID)
    

#fetchplayer('352328')
#print index

output = open('ppIndex.txt', 'w')
output.write(json.dumps(index))
output.close()

