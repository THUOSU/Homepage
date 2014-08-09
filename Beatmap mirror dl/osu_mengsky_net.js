javascript:
(function(b){
	if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
		songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
		b.href="http://osu.mengsky.net/d.php?id="+songid;
	}
})(window.location);
