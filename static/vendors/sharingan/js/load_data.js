$(document).ready(function() {
    $('#main_table').DataTable({
            "scrollX": true,
            "ajax": {
                "url": "/load_reports",
                "dataType": "json",
                "dataSrc": "data"
            },
            "columns": [
                {"data": "sample_name"},
                {"data": "sample_extension"},
                {"data": "sample_size"},
                {
                "mData": "md5sum",
                "mRender": function (data, type, row) {
                    return '<a class="btn btn-sm btn-outline-success" href=analysis_report?sample='+  data  + '>  <i class="fa fa-share-square-o"> View </i>  </a>'
                }
                }
            ]
        });

} );