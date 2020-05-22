function ShowAdd() {
    if (document.getElementById("add_form").style.display == "none") {
        document.getElementById("add_form").style.display = "block";
        document.getElementById("add_button").value = "Cancel";
    } else {
        document.getElementById("add_form").style.display = "none";
        document.getElementById("add_button").value = "Add";
    }
}

function ShowEdit() {
    
    if (document.getElementById("editing_form").style.display == "none") {
        document.getElementById("editing_form").style.display = "block";
        document.getElementById("edit_btn").value = "Cancel";
    } else {
        document.getElementById("editing_form").style.display = "none";
        document.getElementById("edit_btn").value = "Edit";
    }
}