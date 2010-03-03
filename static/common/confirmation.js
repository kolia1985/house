(function($){
    $.fn.confirmation = function(options) { 
        var opts = $.extend({}, $.fn.confirmation.defaults, options);
        var link = $(this);
        opts.url = link.attr('href')

        $.fn.confirmation.opts = opts;
        var $dialog = get_dialog('#' + opts.dialog_id);
        $dialog.html(opts.data);
        
        if (opts.auto_open) {
            $dialog.dialog('open');
        }
        else {
            $(this).click(function() {
                $dialog.dialog('open');
                return false;
            }).hover(
                function(){ 
                    $(this).addClass("ui-state-hover"); 
                },
                function(){ 
                    $(this).removeClass("ui-state-hover"); 
                }
            )
        }

        
        $dialog.dialog({
            bgiframe: true,
            resizable: false,
            autoOpen: $.fn.confirmation.opts.auto_open,
            title: opts.title,
            height: $.fn.confirmation.opts.height,
            width: $.fn.confirmation.opts.width,
            modal: true,
            overlay: {
                backgroundColor: '#000',
                opacity: 0.5
            },
            buttons: {
                'OK': function() {
                    $.get($.fn.confirmation.opts.url, {}, function(data){
                        $.fn.confirmation.opts.delete_click();
                        $dialog.dialog('close');
                    });
                },
                Cancel: function() {
                    $(this).dialog('close');
                }
            }
        });
        
    };

    function get_dialog(dialog_selector){
        var $dialog = $(dialog_selector);
        if ($dialog.length == 0) {
            $('body').append('<div id="'+ $.fn.confirmation.opts.dialog_id +'">Loading...</div>');
            $dialog = $(dialog_selector);
        }
        return $dialog;
    }

    $.fn.confirmation.defaults = {
        dialog_id: "confirmation",
        height: 140,
        width: 500,
        title: 'ROA',
        auto_open: false,
        data: 'Really want to delete?',
        delete_click: function() {
            
        }
    };
})(jQuery);  