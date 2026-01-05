function validate(){
    let username = document.getElementById("name").value;
    let mail = document.getElementById("email").value;
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    let phno = document.getElementById("phone").value;
    let age = document.getElementById("age").value;
    let country=document.getElementById("contry").value;
    let gender=document.getElementsByName("gender");
    let gendersat=false;
    let dob=document.getElementById("date").value;

    if(username.trim()===""){
        document.getElementById("nameeq").innerText="Username cannot be empty";
    }
    if(mail.trim()===""){
        document.getElementById("emaileq").innerText="Email cannot be empty";
    }
    else if(!pattern.test(mail)){
        document.getElementById("emaileq").innerText="Enter valid email";
    }
    if(phno.trim()===""){
        document.getElementById("phoneeq").innerText="Phone number cannot be empty";
    }
    else if(phno.length!=10){
        document.getElementById("phoneeq").innerText="Enter valid phone number";
    }
    if(age.trim()===""){
        document.getElementById("ageeq").innerText="Age cannot be empty";
    }
    if(dob.trim()===""){
        document.getElementById("dateeq").innerText="Date of Birth cannot be empty";
    }
    if(country==="")
    {
        document.getElementById("countryeq").innerText="Select your country";
    }
    

    
}
