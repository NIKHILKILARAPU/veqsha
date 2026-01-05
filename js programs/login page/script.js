function validate() {
    var name = document.getElementById("username");
    var pass = document.getElementById("password");
    const correctpass = "nikhil6789";

    if (name.value.trim() === "") {
        alert("Please enter username");
    } 
    else if (pass.value.trim() === "") {
        alert("Please enter password");
    } 
    else if (pass.value !== correctpass) {
        alert("Please enter correct password");
    } 
    else {
        alert("Login successful");
    }
}
