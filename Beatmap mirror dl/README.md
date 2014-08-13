osu!谱面下载镜像(osu! Beatmap Download Mirrors)
------
###使用方法/How to
####油候脚本/UserScript
Pending...
####书签/Bookmark
拖拽镜像后的代码到书签栏，<br>
或新建书签并更改链接为代码。<br>
重命名书签。<br>
Drag the codes of each mirror site into the bookmark bar.<br>
Or add a new bookmark and change the link to the codes.<br>
Rename the bookmark.<br>
在谱面下载页面单击书签。<br>
Click the bookmark in the beatmap download pages.

<!--more-->

*	[bloodcat.com][1] (Korea)
	*	한국어
	*	English
	*	中文

	代码/Codes:
	```javascript
	javascript:
	(function(b){
		if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
			songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
			b.href="http://bloodcat.com/osu/m/"+songid;
		}
	})(window.location);
	```

*	[loli.al][2] (China)
	*	English
	*	简体中文
	*	繁體中文
	*	日本語
	*	韓語
	*	Pусский
	*	Українська

	代码/Codes:
	```javascript
	javascript:
	(function(b){
		if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
			songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
			b.href="http://loli.al/s/"+songid;
		}
	})(window.location);
	```

*	[osu.mengsky.net][3] (China)
	*	English

	代码/Codes:
	```javascript
	javascript:
	(function(b){
		if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
			songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
			b.href="http://osu.mengsky.net/d.php?id="+songid;
		}
	})(window.location);
	```

希望你能喜欢<br>
Enjoy it!

更新记录/Change log:

*	2014-08-09:
	Fix bug for "osu.mengsky.net" in "osu.ppy.sh/s/".
	Other small changes.
*	2014-08-07:
	Create the page.
	Add "osu.mengsky.net".

[1]:http://bloodcat.com/osu/
[2]:http://loli.al/
[3]:http://osu.mengsky.net/
