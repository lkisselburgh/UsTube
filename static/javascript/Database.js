function ShowAdd() {
    if (document.getElementById("add_form").style.display == "none") {
        document.getElementById("add_form").style.display = "block";
        document.getElementById("add_button").value = "Cancel";
    } else {
        document.getElementById("add_form").style.display = "none";
        document.getElementById("add_button").value = "Add";

    }
    
}