document.getElementById('file-browse').addEventListener('click', function() {
	document.getElementById('files-input-upload').click();
});

document.getElementById('files-input-upload').addEventListener('change', function() {
	document.getElementById('file-input').value = this.value;

	document.getElementById('upload-file-btn').removeAttribute('disabled');
});

$(function() {
    $('#upload-file-btn').click(function() {
        jQuery('#page-body').showLoading();
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload_sample',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                  jQuery('#page-body').hideLoading();

                  window.location = '/analysis_report?sample=' + data.return_value;


            },
            error: function (xhr, ajaxOptions, thrownError) {
                jQuery('#page-body').hideLoading();
            }
        });
    });

});