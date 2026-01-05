function submit(){
    var con=document.getElementById("country").value;
    if(con===""){
        alert("Please select a country");
    }else{
        alert("You have selected: " + con);
    }
}