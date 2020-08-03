// ajax function
function WhichButton(event) {
    if (event.button ==1 || event.button ==0){
        console.log(event.target.className);
        var c = event.target.className;
        var postData = {
            "id": c
        }
        $.ajax({ 
            url: "/goClick", 
            type: "POST", 
            contentType: "application/json", 
            data: JSON.stringify(postData), 
            success: function(data){
                console.log(data);
            } 
        });
    }
    
};