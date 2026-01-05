function submit(){
    var mail=document.getElementById("mail");
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(mail.value.trim()==="")
    {
        alert("enter mail id");
    }
    else if(!pattern.test(mail.value))
    {
        alert("enter valid mail id");
    }
    else{
        alert("mail id submitted successfully")
    }

}