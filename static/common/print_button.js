(function($){  
	$.fn.print_button = function(){
		$(this).click(function(){
			window.print();
		});
	};  
})(jQuery);  