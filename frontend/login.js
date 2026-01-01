const loginform = document.getElementById("loginform");

loginform.addEventListener("submit",async(e)=>{
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const payload = {
        email:email,
        password:password
    }

    const res  = await fetch("http://127.0.0.1:8000/login",{
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body:JSON.stringify(payload)
    })
    const data = await res.json()
    alert(data.message)

})