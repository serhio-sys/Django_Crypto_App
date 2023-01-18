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
            var btn = form.parentNode.parentNode
            btn.remove()
        },
        error:function(err){
            console.log(err)
        }
    })
}))