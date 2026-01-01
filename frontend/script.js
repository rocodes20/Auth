const form = document.getElementById("form");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const payload = {
        name:name,
        email:email,
        password:password
    }
    try {    const res = await fetch("http://127.0.0.1:8000/register",{
        method : "POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(payload)
    });
    const data = await res.json();
    alert(data.message)
}
    catch(err){
        console.error(err);
    }

})