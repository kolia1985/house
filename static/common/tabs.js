(function($){  
    $.fn.tabs = function(options){
        var $this = $(this);
        $this.find('.header.closed').next().hide();
        $this.find('.header').click(function() {
            $this = $(this);
            $this.next().toggle();
            $this.toggleClass("closed");
            return false;
        });
    };
})(jQuery);
