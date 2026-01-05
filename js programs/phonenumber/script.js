function submit(){
    var ph=document.getElementById("phnumber");
    if(ph.value.trim()==="")
    {
        alert("enter mobile number")
    }
    else if(ph.value.length!=10)
    {
        alert("enter valid mobile number")
    
    }
    else
    {
        alert("success")
    
    }

}