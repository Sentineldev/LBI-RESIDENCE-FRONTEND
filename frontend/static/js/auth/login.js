const form = document.querySelector("#login-form")
const message_container = document.querySelector("#message-container")
const message = document.querySelector("#message")

const loader_container = document.querySelector("#loader-spinner")

async function HandleSubmit(e){

    e.preventDefault()

    const data = new URLSearchParams(new FormData(form))

    loader_container.style.display = "flex"

    let request = await fetch(location.href,{
        method:"POST",
        body:data
    })

    
    if(request.status == 200){
        let response = await request.json()
        localStorage.setItem("user",JSON.stringify(response))

        window.location.replace("/user/dashboard")
    }
    else{
        let response = await request.json()
        message_container.style.display = "inherit"
        message.innerText = response.message
    }

    loader_container.style.display = ""
    

}




form.onsubmit = HandleSubmit

