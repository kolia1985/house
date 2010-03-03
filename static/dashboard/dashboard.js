(function($) {
    $.fn.work_queue = function(options) {
        var opts = $.extend({}, $.fn.work_queue.defaults, options);
        $.fn.work_queue.opts = opts;

        var $form = $(this);
        var hid_is_modified = $form.find("#is_modified");
        var $filter_form = $(opts.filter_by_status_selector);
        var $table_form = $(opts.table_form_selector);
        var url = $form.attr("action");
        $form.sortedtable({
            "url": url,
            "extend_form_selector": opts.filter_by_status_selector,
            "can_change_page": ask_for_changes
        });

        $form.find('input').change(function(){
            hid_is_modified.val(1);
        });

        $filter_form.find('#id_status').change(function(){
            var can_filter = ask_for_changes();
            if (can_filter) {
                var wq_form_qs = $form.formSerialize();
                var table_form_qs = $table_form.formSerialize();
                var filter_form_qs = $filter_form.formSerialize();
                $.post(url, wq_form_qs + "&" + table_form_qs + '&' + filter_form_qs,
                    function(data) {
                        var $data = $(data);
                        $form.html($data[0]);
                        $('.paging').html($data[2])
                    });
            }
        });

        var $forwarddialog = $('#forward-div');
        $('#forward-div').dialog({
            bgiframe: true,
            autoOpen: false,
            height: 180,
            width: 300,
            modal: true,
            title: 'Forward',
            buttons: {
                'Ok': function() {
                    var wq_form_qs = $form.formSerialize();
                    var table_form_qs = $table_form.formSerialize();
                    var filter_form_qs = $filter_form.formSerialize();
                    var forward_qs = $('#forward-user-form').formSerialize();
                    $.post(url, wq_form_qs + '&' + table_form_qs + '&' + filter_form_qs + '&'+ forward_qs + "&forward-task=1",
                        function(data) {
                            var $data = $(data);
                            var $errors = $data.find('.errorlist');
                            if ($errors.length == 0) {
                                $form.html($data[0]);
                                $('.paging').html($data[2]);
                                $forwarddialog.dialog('close');
                            }
                            else {
                                $forwarddialog.html($data[4]);
                            }
                        });
                },
                Cancel: function() {
                    $forwarddialog.dialog('close');
                }
            }
        });

        $(opts.action_selector).change(function(){
            var action = $(this).val();
            var checked_boxes = $form.find('input[type="checkbox"]:checked');
            if ((checked_boxes.length == 0) && (action != 0)) {
                alert('Please choose tasks.');
                return
            }
            if (action == 1) {
                // Remove from Work Queue
                $(this).confirmation({
                    title: "Remove from the work queue",
                    data: "Do you really want remove specified tasks from Work Queue?",
                    auto_open: true,
                    delete_click: function(){
                        var wq_form_qs = $form.formSerialize();
                        var table_form_qs = $table_form.formSerialize();
                        var filter_form_qs = $filter_form.formSerialize();
                        $.post(url, wq_form_qs + '&' + table_form_qs + '&' + filter_form_qs + "&complete-task=1",
                            function(data) {
                                var $data = $(data);
                                $form.html($data[0]);
                                $('.paging').html($data[2])
                            });
                    }});
            }
            if (action == 2) {
                // Forward
                $.get(opts.forward_user_form_url,
                    function(data) {
                        $forwarddialog.html(data);
                        $forwarddialog.dialog('open');
                    });
            }
        });
        
        $(opts.save_selector).live("click", function(){
            var wq_form_qs = $form.formSerialize();
            var table_form_qs = $table_form.formSerialize();
            var filter_form_qs = $filter_form.formSerialize();
            $.post(url, wq_form_qs + "&" + table_form_qs + '&' + filter_form_qs + "&save-wq=1",
                function(data) {
                    $form.html($(data)[0]);
                });
        });
        
        window.onbeforeunload=leaving;

    };

    function is_changed(){
        return ($("#is_modified").val() == 1);
    }
    
    function ask_for_changes(){
        if (is_changed()) {
            return confirm($.fn.work_queue.opts.ask_about_changes_text);
        }
        return true;
    }

    function leaving(e) {
        if (is_changed())
           return $.fn.work_queue.opts.ask_about_changes_text;
        return;
    }


    $.fn.work_queue.defaults = {
        action_selector: '#id_action',
        filter_by_status_selector: "#filter-form",
        save_selector: "#wq-submit",
        table_form_selector: '#table-form',
        ask_about_changes_text: "Are you sure to lost you changes?",
        forward_user_form_url: ''
    };
})(jQuery);
