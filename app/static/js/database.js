document.getElementById("defaultOpen").click();

function openCity(evt, tab) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tab).style.display = "block";
    evt.currentTarget.className += " active";
  }

$('#page').keypress(function(event) {  
  if (event.keyCode == 13) {
    
    if (document.getElementById("page").value > parseInt(document.getElementById("max_page").innerHTML)){
      alert("超出頁數了");
    }
    else{ 
      const index = window.location.href.search("page") - 1;

      window.location.href = window.location.href.substr(0, index) + "?page=" + document.getElementById("page").value;
    }
    
  }
});

$(".update").click(function(id){

});