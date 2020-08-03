$(function () {
    $('#Submit').click(function () {
      var postData = {
        "url": $('#_url').val()
      }
      console.log(postData);
      $.ajax({
        url: "/index_ajax",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(postData),
        success: function (data) {
          console.log(data);
          if (data["flash"]){
            document.getElementById('flash').innerHTML = data["flash"];
          }
          else{
            for (var key in data) {
              document.getElementById('items-list').innerHTML += `<li><a class="" href="${data[key]['url'] }" target="_blank"><img src="${data[key]['favicon']}" height="16px" width="16px">${key}</a></li>
              <br>`
            };
          }
          
        },
        complete: function(){
            document.getElementById('_url').value = ''
        }
      });
    });
  });


function delete_bookmark(key_id) {
  postData = {
    "key_id": key_id
  }
  $.ajax({ 
    url: "/delete_bookmark_ajax", 
    type: "POST", 
    contentType: "application/json", 
    data: JSON.stringify(postData), 
    success: function(data){
      console.log(data)
      document.getElementById("items-list").innerHTML = "";
      for (const key in data){
        document.getElementById("items-list").innerHTML += `<li>
        <a class="" href="${data[key]['url']}" target="_blank">
          <img src="${data[key]['favicon']}$" height="16px" width="16px">${key}
        </a>
        <button type="button" class="pull-right btn-link" id="${key}">X</button>
      </li>
      <br>`;
        
      }
    } 
});
};

function switchDisplay(item) {
  var TargetArea = document.getElementById(item);
  TargetArea.style.display = (TargetArea.style.display == 'block'?'none':'block');   
  
  if(TargetArea.style.display=="block"){
    document.getElementById("bookmark-txt").innerHTML = "▲書籤"; 
  }
  else{
    document.getElementById("bookmark-txt").innerHTML = "▼書籤";
  }
}
