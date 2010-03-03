(function($) {
    $.fn.aforms = function(options) {
    	var opts = $.extend({}, $.fn.aforms.defaults, options);
    	$.fn.aforms.opts = opts;
    	
    	var $form = $(this);
    	configure_form($form);
    	var $hid_mode = $('#' + $form[0].id + '_mode');
    	
    	$form.find(opts.edit_button_selector).click(function(){
    		switch_mode($form, $hid_mode, 'edit');
    	});
    	
    	$form.find(opts.edit_selector + ' input[type="submit"]').click(function(){
    		$form.find('.errorlist').remove();
    		var queryString = $form.formSerialize(); 
    		$.post($form.attr('action'), queryString, function(data){
    			if (data.result == 'ok') {
    				// Saved successful 
    				switch_mode($form, $hid_mode, 'view');
    				// updating values
    				for (field in data.obj) {
    					var value = data.obj[field];
    					$("." + field + opts.value_selector).text(value);
    				}
    			}
    			else {
    				// Error occurred
    				for (field in data.errors) {
    					var error = data.errors[field];
    					if (error != '') {
    						if (error != '__all__') {
    							$("#id_" + field).after(error);
    						}
    						else alert(error);
    					}
    				}
    			}
    		}, "json")
    		
    		return false;
    	});
    };

    function configure_form($form, $hid_mode) {
    	$form.append('<input type="hidden" value="view" id="' + $form[0].id + '_mode" />');
    	var $hid_mode = $('#' + $form[0].id + '_mode');
    	switch_mode($form, $hid_mode, 'view');
    };
    
    function switch_mode($form, $hid_mode, $mode){
    	$hid_mode.val($mode);
    	if ($mode == 'edit') {
			$form.find($.fn.aforms.opts.value_selector).hide();
			$form.find($.fn.aforms.opts.edit_selector).show();
    	}
    	else {
    		$form.find($.fn.aforms.opts.value_selector).show();
			$form.find($.fn.aforms.opts.edit_selector).hide();
    	}
    }

	$.fn.aforms.defaults = {
		edit_selector: '.edit',
		edit_button_selector: '.edit-btn',
	    value_selector: '.value',
	};
})(jQuery);