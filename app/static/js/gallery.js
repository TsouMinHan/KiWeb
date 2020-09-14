$(function() {
    $('.Done').click(function() {
        var post_data = {
            "mode": 'done'
        }
        $.ajax({
            url: '/data_from_adax',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(post_data),
            beforeSend: function() {
                $('#loading').show();
                document.getElementById('canvas').innerHTML = "";
            },
            success: function(data) {
                data['img_ls'].forEach(function(img) {
                    document.getElementById('canvas').innerHTML += `<div class="col-md-5">
                    <a href="${img}"><img src="${img}" width=100%></a>
                    <br> 
                </div></a></h4>`
                })
            },
            complete: function() {
                $('#loading').hide();
            }
        });
    });
});

$(function() {
    $('.DoneBack').click(function() {
        var post_data = {
            "mode": "back"
        }
        $.ajax({
            url: '/data_from_adax',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(post_data),
            beforeSend: function() {
                $('#loading').show();
                document.getElementById('canvas').innerHTML = "";
            },
            success: function(datas) {},
            complete: function() {
                location.href = '/';
            }
        });
    });
});

function switchDisplay(item) {
    var TargetArea = document.getElementById(item);
    TargetArea.style.display = (TargetArea.style.display == 'block' ? 'none' : 'block');
    if (TargetArea.style.display == "block") {
        document.getElementById("txt1").innerHTML = "▲輸入";
    } else {
        document.getElementById("txt1").innerHTML = "▼輸入";
    }
}

$(function() {
    $('#Submit').click(function() {
        var postData = {
            "url": $('#_url').val()
        }

        $.ajax({
            url: "/baha_gallery_ajax",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(postData),
            success: function(data) {
                if (data["status"] == "Failed") {
                    document.getElementById('flash').innerHTML = "duplicate!!";
                } else {
                    document.getElementById('flash').innerHTML = "insert success!!";
                }
            },
            complete: function() {
                document.getElementById('_url').value = ''
            }
        });
    });
});