const url = window.location.href
const form = document.querySelector("#s-form")
const input = document.querySelector("#search-inp")
const results = document.querySelector("#results")

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const sendData = (coin) =>{
    $.ajax({
        type: "POST",
        url: 'find/',
        data:{
            'csrfmiddlewaretoken':csrf,
            'coin':coin
        },
        success:(res)=>{
            const data = res.data
            console.log(res.data)
            results.innerHTML = ""
            if (Array.isArray(data)){
                data.forEach(coin=>{
                    results.innerHTML += `
                    <a href="" class="item">
                        <div class="row mt-2 mb-2">
                            <div class="col-2"><img src="${coin.img}" height="50"></div>
                            <div class="col-10">
                                <h5>${coin.sym}</h5>
                                <p class="text-muted">${coin.name}</p>
                            </div>
                        </div>
                    </a>
                    `
                })
            }
            else{
                if(input.value.length>0){
                    results.innerHTML = `<b>${data}</b>`
                }
                else{
                    results.classList.add("not-visible")
                }
            }
        },
        error:(err)=>{
            console.log(err)
        }
    })
}

input.addEventListener('keyup',(e)=>{
    if (results.classList.contains("not-visible")){
        results.classList.remove("not-visible")
    }
    if (input.value.length>0){

    }
    sendData(e.target.value)
})