(function () {

$(document).ready(function () {
	$('ul.lang-switch a').attr('href', '#').click(function (e) {
		e.preventDefault();
		
		location.pathname = zwp.translatePath(
			location.pathname,
			this.getAttribute('data-lang-code')
		);
	});

	// Refresh lightbox after a new directory was loaded. This is necessary
	// for lightbox to register event handlers on newly added images.
	$('#zwp-nav').on("load_node.jstree", function (node, status) {
			if (!status)
				return;

			lightbox.enable();
	});
});

}());
