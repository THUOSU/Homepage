javascript:
(function(b){
	if(b.host=="osu.ppy.sh"&&b.pathname.match(/\/[bs]\/.+/)){
		songid=$('.beatmapDownloadButton:last a').attr('href').match(/\d+/);
		b.href="http://bloodcat.com/osu/m/"+songid;
	}
})(window.location);
