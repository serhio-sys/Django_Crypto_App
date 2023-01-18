const forms = document.querySelectorAll(".work")

forms.forEach((form)=>form.addEventListener("submit",(e)=>{
    e.preventDefault()
    var action_url = form.getAttribute("action")
    $.ajax({
        type: "GET",
        url: action_url,
        contentType: false,
        processData: false,
        success: function(){
            var btn = form.querySelector(".btn")
            if (btn.classList.contains("btn-danger")){
                btn.classList.remove("btn-danger")
                btn.classList.add("btn-success")
                btn.innerHTML="Add"
            }
            else{
                btn.classList.remove("btn-success")
                btn.classList.add("btn-danger")
                btn.innerHTML="Remove"
            }
        },
        error:function(err){
            console.log(err)
        }
    })
}))