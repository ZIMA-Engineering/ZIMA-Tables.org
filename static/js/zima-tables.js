(function () {

$(document).ready(function () {
	console.log('ul.lang-switch a');
	$('ul.lang-switch a').attr('href', '#').click(function (e) {
		e.preventDefault();
		
		location.pathname = zwp.translatePath(
			location.pathname,
			this.getAttribute('data-lang-code')
		);
	});
});

}());
