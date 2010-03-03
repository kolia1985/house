(function($){
	$.fn.popup = function(options) { 
		var opts = $.extend({}, $.fn.popup.defaults, options);
		$.fn.popup.opts = opts;
		var $dialog = get_dialog('#' + opts.dialog_id);
		$(this).click(function() {
			var link = $(this);
			$.get(link.attr('href'), {}, function(data){
				var width = $(data).attr('width');
				if (width != 0) {
					$dialog.dialog('option', 'width', width + 'px');
				}
				$dialog.html(data);
            });
			$dialog.dialog('open');
			return false;
		}).hover(
			function(){ 
				//$(this).addClass("ui-state-hover"); 
			},
			function(){ 
				//$(this).removeClass("ui-state-hover"); 
			}
		)

		$dialog.dialog({
			bgiframe: true,
			autoOpen: false,
			height: $.fn.popup.opts.height,
			width: $.fn.popup.opts.width,
			modal: true,
			title: opts.title,
			buttons: {
				'Save': function() {
					var $form = $('#' + opts.dialog_id + ' form');
					var queryString = $form.formSerialize();
					var $url = $form.attr('action');
					$.post($url, queryString, function(data){
						var content = $('#' + opts.dialog_id);
						content.html(data);

						var $errors = content.find('.errorlist');
			            if ($errors.length == 0) {
			                content.dialog('close');
			            }
					});
				},
				Cancel: function() {
					$dialog.dialog('close');
				}
			},
			close: function() {
				$dialog.html('Loading...');
			}
		});
	};

	function get_dialog(dialog_selector){
		var $dialog = $(dialog_selector);
		if ($dialog.length == 0) {
			$('body').append('<div id="'+ $.fn.popup.opts.dialog_id +'">Loading...</div>');
			$dialog = $(dialog_selector);
		}
		return $dialog;
    }

	$.fn.popup.defaults = {
	    dialog_id: "dialog",
	    height: 500,
	    width: 600,
	    title: 'ROA'
	};
})(jQuery);  