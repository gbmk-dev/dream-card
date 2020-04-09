$(document).ready(function(){
	$("#first-page-scroll").css({ height: $(window).innerHeight() });
			$(window).resize(function(){
			$("#first-page-scroll").css({ height: $(window).innerHeight() });
		});
});