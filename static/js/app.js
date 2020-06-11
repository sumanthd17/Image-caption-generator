var data = []
var token = ""

jQuery(document).ready(function () {
    $('#btn-process').on('click', function () {
        $.ajax({
            url: '/predictions',
            type: "post",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                "input_img": $('#input-img').val(),
            }),
            success: function(resp) {
                $('#text_1').val(resp['pred_1'])
                $('#text_2').val(resp['pred_2'])
                $('#text_3').val(resp['pred_3'])
                $('#text_4').val(resp['pred_4'])
            }
        }).done(function (jsondata, textStatus, jqXHR) {
            console.log('success')
            // console.log(jsondata)
            $('#text_1').val(jsondata['pred_1'])
            $('#text_2').val(jsondata['pred_2'])
            $('#text_3').val(jsondata['pred_3'])
            $('#text_4').val(jsondata['pred_4'])
        }).fail(function (jsondata, textStatus, jqXHR) {
            console.log('Failed')
            // console.log(jsondata)
        });
    })
})