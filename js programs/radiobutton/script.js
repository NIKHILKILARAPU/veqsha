function submit(){
    var gender = document.getElementsByName('gender');
    var selected=false;
    
    for(var i=0; i<gender.length; i++)
    {
        if(gender[i].checked)
        {
            selected=true;
           const vlue=gender[i].value;
            alert("You selected: " + vlue);
            break;
            
        }
        
    
    }
    if(selected==false)
    {
        alert("select your gender");
    }
}