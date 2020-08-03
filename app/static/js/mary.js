function check_money(postData){
    var s = 0;
    console.log(postData);
    for(var key in postData){

        if (postData[key]=='undefined'){
            postData[key] = 0;
        }
        postData[key] = parseInt(postData[key])
        s = s + postData[key];
        
    }
    postData.total_bet = s - postData.money
    // console.log(s, postData.money);
    return postData.money - postData.total_bet
}

$(function () {
    $('#Run').click(function () {
        var postData = {
            "apple": $('#apple_bet').val(),
            "cherry": $('#cherry_bet').val(),
            "orange": $('#orange_bet').val(),
            "watermelon": $('#watermelon_bet').val(),
            "banana": $('#banana_bet').val(),
            "pineapple": $('#pineapple_bet').val(),
            "grape": $('#grape_bet').val(),
            "seven": $('#seven_bet').val(),
            "money": $('#money').val(),
        };
        var checked_money = check_money(postData);
        console.log(checked_money);
        if (postData.total_bet==0){
            alert("沒下注要怎麼玩啊");
        }
        else if (checked_money<0){
            alert("死窮鬼還敢玩啊");
        }
        else{
            $.ajax({
                url: "/mary_ajax",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify(postData),
                success: function (data) {
                    console.log((data));
                    document.getElementById('money').value = data.money;
                    document.getElementById("jackpot").src = data.jackpot_path;
                    document.getElementById("earn").innerHTML = `獲得${data.earn}元`;
                    $('#jackpot').show();
                }
            });
        }     
    });
});

$(function () {
    $('#Set').click(function () {
        var num = $('#set_money').val();
        $('.set_number').val(num);
    });
});