##	osu!谱面下载镜像(osu! Beatmap Download Mirrors)

拖拽镜像后的![pic][4]到书签栏。
Drag the pic ![pic][4] of mirror sites to the bookmark bar.
在谱面下载页面单击书签。
Click the bookmark in the Beatmap download pages.
<!--more-->

*	[bloodcat][1]: <a href="javascript:(function(b){if(b.host==&quot;osu.ppy.sh&quot;&amp;&amp;b.pathname.match(/\/[bs]\/.+/)){songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);b.href=&quot;http://bloodcat.com/osu/m/&quot;+songid;}})(window.location);">![bloodcat][4]</a> (Korea)
	*	한국어
	*	English
	*	中文

```javascript
javascript:
(function(b){
	if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
		songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
		b.href="http://bloodcat.com/osu/m/"+songid;
	}
})(window.location);
```

*	[loli.al][2]: <a href="javascript:(function(b){if(b.host==&quot;osu.ppy.sh&quot;&amp;&amp;b.pathname.match(/\/[bs]\/.+/)){songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);b.href=&quot;http://loli.al/s/&quot;+songid;}})(window.location);">![loli.al][4]</a> (China)
	*	English
	*	简体中文
	*	繁體中文
	*	日本語
	*	韓語
	*	Pусский
	*	Українська

```javascript
javascript:
(function(b){
	if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
		songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
		b.href="http://loli.al/s/"+songid;
	}
})(window.location);
```

*	[osu.mengsky.net][3]: <a href="javascript:(function(b){if(b.host==&quot;osu.ppy.sh&quot;&amp;&amp;b.pathname.match(/\/[bs]\/.+/)){songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);b.href=&quot;http://osu.mengsky.net/d.php?id=&quot;+songid;}})(window.location);">![osu.mengsky.net][4]</a> (China)
	*	English

```javascript
javascript:
(function(b){
	if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
		songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
		b.href="http://osu.mengsky.net/d.php?id="+songid;
	}
})(window.location);
```

希望你能喜欢！
Enjoy it!

更新记录：
Update log:

*	2014-08-09:
	Fix bug for "osu.mengsky.net" in "osu.ppy.sh/s/".
	Other small changes.
*	2014-08-07:
	Create the page.
	Add "osu.mengsky.net".

[1]:http://bloodcat.com/osu/
[2]:http://loli.al/
[3]:http://osu.mengsky.net/
[4]:./bookmark.png