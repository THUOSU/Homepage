javascript:(function(b,c){
	c=b.pathname.match(/[bus]\/.+/);
	if(b.host=='osu.ppy.sh'&&c){
		b.href='http://osu.mengsky.net/d.php?id='+(/return play\((\d+)/.exec(document.body.innerHTML) [1])
	}
})
(window.location)