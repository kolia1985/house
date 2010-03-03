(function($){  
    $.fn.simple_table = function(options){
        var $simple_table = $(this);
        $simple_table.find('tbody tr').live('mouseover', function(){ 
                    $(this).addClass("state-hover"); 
                }).live('mouseout', function(){ 
                    $(this).removeClass("state-hover"); 
                }
            ).live("click", function(){
                var url = $(this).attr("url");
                if(typeof(url)!="undefined") location.href=url;
            });
    };
})(jQuery);
