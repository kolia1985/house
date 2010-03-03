function bind_datapicker(id){
    $(id).datepicker({
        showOn: 'button',
        dateFormat:"yy-mm-dd",
        buttonImage: '/media/common/img/calendar.png',
        buttonImageOnly: true
    }); 
}

function bind_datapicker_to_span(name){
    $('#id_' + name).datepicker({
        showOn: 'button',
        buttonImage: '/media/common/img/calendar.png',
        buttonImageOnly: true,
        dateFormat:"yy-mm-dd",
        onSelect: function() {
            var date = $(this).datepicker('getDate');
            var month = date.getMonth() + 1;
            var year = date.getFullYear();
            var day = date.getDate();
            if(day < 10) day = '0' + day;
            if(month < 10) month = '0' + month;
            $('#span_' + name).text(year + '-' + month + '-' + day);
            $('#id_' + name).trigger('change');

            // Hack - trigger for hidden fields, doesn't triggered after getting data by ajax.
            $("#is_modified").val(1);
        }
    }
    );
}