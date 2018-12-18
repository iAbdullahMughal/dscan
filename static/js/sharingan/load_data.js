
$(document).ready(function() {
    $('#main_table').DataTable({
            "ajax": {
                "url": "/load_data",
                "dataType": "json",
                "dataSrc": "data"
            },

            "columns": [
                {"data": "file_name"},

                { "mData": "extension",
                "mRender": function (data, type, row) {
                        html_content = '';
                        var extension_list = data;
                        var listLength = extension_list.length;
                        for (var i = 0; i < listLength; i++) {
//                            alert(extension_list[i]);
                               html_content = html_content + "<span class=\"badge badge-dark\">" + extension_list[i] + "</span> ";

                            }
                            return html_content;


                }
                },

                { "mData": "has_macro",
                "mRender": function (data, type, row) {
                    if (data){
                        return "<span class=\"badge badge-danger\">Contains Macro</span>";
                    }
                    else{
                        return "<span class=\"badge badge-success\">No Macro</span>";
                    }

                }
                },
                {
                "mData": "md5sum",
                "mRender": function (data, type, row) {
                    return '<a class="btn btn-success" href=process?sample='+  data  + '.json>  <i class="fa fa-share-square-o"></i>  </a>'
                }
            }
            ]
        });

} );
