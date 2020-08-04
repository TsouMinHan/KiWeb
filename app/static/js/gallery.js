// // timesleep learn from 
// // https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep
// function sleep(ms) {
//     return new Promise(resolve => setTimeout(resolve, ms));
// }

// // When the user clicks on the button, scroll to the top of the document
// async function downFunction() {
//     var end = document.body.scrollHeight;

//     for (distance = 500; distance < end; distance += 1){
//         if (distance%500 === 0){                
//             console.log(distance, end);
//             document.documentElement.scrollTop = distance;
//             document.body.height = distance; 
//             await sleep(1000);
//         }
        
//     }
// }
// -----------------^^^Not Use^^^----------------------


$(function(){
    $('#Done').click(function(){
        var post_data = {
            "mode": 'done'
        }
        $.ajax({
            url: '/data_from_adax',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(post_data),
            success: function(data){
                document.getElementById('canvas').innerHTML="";

                data['img_ls'].forEach(function(img){
                    document.getElementById('canvas').innerHTML += `<div class="col-md-5">
                    <a href="${img}"><img src="${img}" width=100%></a>
                    <br> 
                </div></a></h4>`
                })
            }
        });
    });
});


$(function(){
    $('#DoneBack').click(function(){
        var post_data = {
            "mode": "back"
        }
        $.ajax({
            url: '/data_from_adax',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(post_data),
            success: function(datas){
            },
            complete: function(){
                location.href = '/';
            }
        });
    });
});

function switchDisplay(item) {
    var TargetArea = document.getElementById(item);
    TargetArea.style.display = (TargetArea.style.display == 'block'?'none':'block');   
    if(TargetArea.style.display=="block"){
        document.getElementById("txt1").innerHTML = "▲輸入"; 
    }
    else{
        document.getElementById("txt1").innerHTML = "▼輸入";
    }
  }

$(function () {
    $('#Submit').click(function () {
        var postData = {
            "url": $('#_url').val()
        }

        $.ajax({
            url: "/baha_gallery_ajax",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(postData),
            success: function (data) {
                if (data["status"] =="Failed"){
                    document.getElementById('flash').innerHTML = "duplicate!!";
                }
                else{
                    document.getElementById('flash').innerHTML ="insert success!!";
                }  
            },
            complete: function(){
                    document.getElementById('_url').value = ''
                }
            });
    });
});