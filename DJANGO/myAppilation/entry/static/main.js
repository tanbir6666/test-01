




function deletes(element){
   let html_Id = element.id;
    if (confirm("Do you want to Delete ID : " + html_Id)){
        location.href = "delete/" + html_Id + "/";

    }else{

    }
    
}
if (document.getElementById("delete_undo")){
    const undo_btn = document.getElementById("delete_undo")

    undo_btn.addEventListener("click", function ()
    {
        location.href = "undo/"
    })
}


if (log_out = document.getElementById("logOut")){
    const log_out = document.getElementById("logOut")

    log_out.addEventListener("click", function ()
    {
        location.href = "log_out/"
    })
}

if (document.getElementById("show_error")){
    console.log("Starting")
    let error_view = document.getElementById("show_error").value

   
    
        if (error_view == "0")
        {
            document.querySelector("#name").style.border = "2px solid red"
        } else if (error_view == "1")
        {
            document.querySelector("#age").style.border = "2px solid red"
        } else if (error_view == "2")
        {
            document.querySelector("#Gender").style.border = "2px solid red"
        }else{
            console.log("NO ERROR FOUND")
        }
    
}else{
   console.log(document.getElementById("show_error")+'not found')
}
console.log(document.getElementById("show_error") + 'not found')
