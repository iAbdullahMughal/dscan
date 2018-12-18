
$(function() {
    $('#upload-file-btn').click(function() {
        jQuery('#uploading_sample').showLoading();
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                  jQuery('#uploading_sample').hideLoading();

                if (data['return_code'])
                {
                    window.location = '/process?sample=' + data['return_value'] + '.json';
                }
                else{
                    $('#failed').modal('show');
                }

            },
        });
    });
});