(function($){  
    $.fn.days_past_due = function(options){
        var $this = $(this);
        $("#id_info-client_invoice_date, #id_info-client_payment_received").live("change", function() {
            var required_info_qs = $('#required-info-form').formSerialize();
            $.post(options.url, required_info_qs,
                function(data) {
                     $this.text(data.past_due);
                 }, "json");
        });
    };
})(jQuery);