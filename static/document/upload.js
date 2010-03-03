(function($){  
    $.fn.upload = function(options){
       var opts = $.extend({}, $.fn.upload.defaults, options);
       $.fn.upload.opts = opts;
       
       var container = $(this);
       var fields = $(container).children();
       
       $(this).find('.documents-upload').live("click", function() {
           var form = $('<form enctype="multipart/form-data" />');
           container.append(form);
           form.append(fields);

           var handler = function(data){
               if (data.indexOf("h3") != -1){
                   $(container).html(data);
               } else if (data.length != 0) {
                   $(opts.table).html($(data)[0]);
               } else {
                   alert('error');
               }
           };

           form.ajaxSubmit({
               "clearForm": true, 
               "type": "post", 
               "url": opts.url,
               "success": handler}
           );
           return false;
       });
       
       $(".doc_delete").live("click", function(){
           $.ajax({"url": $(this).attr("href"),
                   "success": function(data){
                       $(opts.table).html($(data)[0]);
                   }
           });
           return false;
       });
    };
    $.fn.upload.defaults = {
        url: '',
        table: ''
    };
})(jQuery);
