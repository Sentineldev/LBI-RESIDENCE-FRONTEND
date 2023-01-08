
const open_nav_btn = document.querySelector("#open-nav")
const nav = document.querySelector("#nav")
const nav_background = document.querySelector("#nav-background")
const logout_link = document.querySelector("#logout")

logout_link.addEventListener("click", async  (e) =>{
    e.preventDefault()
    const target = e.target.href
    await fetch(target)
    localStorage.removeItem("user")
    window.location.replace("/auth/login")
})

nav_background.addEventListener("click",()=>{

    nav_background.style.display = ""
    nav.style.display = ""

})

open_nav_btn.addEventListener("click",()=>{
    nav.style.display = "flex"
    nav_background.style.display = "block"
})





