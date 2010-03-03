(function($) {
    $.fn.sortedtable = function(options) {
    	var opts = $.extend({}, $.fn.sortedtable.defaults, options);
    	$.fn.sortedtable.opts = opts;
    
    	var $container = $(this);
    	
    	$(".sorted-table .ordering").live("click", function(){
    		var id = $(this).attr("id");
    		if ($(this).hasClass('checked')){
    			id = "-" + id;
    			};
    		$("#id_order_by").attr("value", id);
    		$(opts.form_selector).submit();
    	});

    	$("#id_per_page").live("change", function(){
    		$(opts.form_selector).submit();
    		});

    	$(opts.paging_selector+" a").live("click", function(){
    	    var can_change_page = opts.can_change_page();
    	    if (can_change_page) {
               var id = $(this).text();
               $("#id_page").attr("value", id);
               $(opts.form_selector).submit();
    	    }
    		return false;
    	});

    	$(opts.paging_selector+" .prev-page, "+opts.paging_selector+" .next-page").live("click", function(){
    	    var can_change_page = opts.can_change_page();
                if (can_change_page) {
        		var id = $(this).attr("id").replace("page_", "");
        		$("#id_page").attr("value", id);
        		$(opts.form_selector).submit();
            }
    		return false;
    		});
    	
    	var update_handler = function(){
        	$(opts.form_selector).submit(function(){
        		var data = $("#table-form").formSerialize();
        		if (opts.extend_form_selector != ''){
        			data = data + '&' + $(opts.extend_form_selector).formSerialize();
        		};
        		if ($.fn.sortedtable.data != ''){
        			data = data + '&' + $.fn.sortedtable.data;
        		};
        		$.ajax({ url: opts.url,
        				type: "POST",
        				data: data, 
        				success: function(data){
        					$container.html($(data)[0]);
        	       	 		$(opts.paging_selector).html($(data)[2]);
        	      	}});
        		return false;
        		});
        	};
        if (opts.url != ''){
        	update_handler();
        };
        
        if (opts.extend_form_selector != ''){
        	$(opts.extend_form_selector).submit(function(){
        		$(opts.form_selector).submit();
        		return false;
        	});	
        };
    };
    
    function update(data){
    	$.fn.sortedtable.data = data;
    	$(opts.form_selector).submit();
    };
    
	$.fn.sortedtable.defaults = {
		form_selector: '#table-form',
		paging_selector: '.paging',
		url: '',
		extend_form_selector: '',
        can_change_page: function() { return true; }
    };
})(jQuery);
