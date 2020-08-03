const textarea = document.querySelector("Textarea");

textarea.addEventListener("input", event => {
    const target = event.currentTarget;
    let current_length;

    if (get_blank_checked())
        current_length = target.value.replace(/\s+/g,'').length;
    else
        current_length= target.value.length;
    document.getElementById("result_text").innerHTML=current_length;
});

function get_blank_checked(){
    return document.getElementById("exculde_blank").checked;
};