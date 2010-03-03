(function($){  
    $.fn.configure_menu = function(options){
        var opts = $.extend({}, $.fn.configure_menu.defaults, options);
        $.fn.configure_menu.opts = opts;
        
        var items = $(this).find("li");
        items.removeClass('active');
        items.each(function(){
            var menu_item = $(this);
            var href = menu_item.find("a").attr('href').split("/", 4)[opts.offset];
            if (href != '/' && location.href.indexOf(href) != -1){
              	menu_item.addClass('active');
              	return;
            }
       });
    };
    $.fn.configure_menu.defaults = {
            offset: 1
        };
})(jQuery);
