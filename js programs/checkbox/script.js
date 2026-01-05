function submit(){
    var hobby=document.getElementsByName("hobby");
    var selected=false;
    var hb="";
    for(var i=0;i<hobby.length;i++){
        if(hobby[i].checked){
            selected=true;
            hb+=hobby[i].value+" ";
        }
    }
    if(selected==true){
        alert("You selected: " + hb);
    }   
    else{
        alert("Please select at least one hobby.");
    }   
}