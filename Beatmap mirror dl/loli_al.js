javascript:
(function(b){
	if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
		songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
		b.href="http://loli.al/s/"+songid;
	}
})(window.location);
