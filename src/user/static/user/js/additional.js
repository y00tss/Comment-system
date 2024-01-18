// Script to provide additional moving functionality

function showFullInfo() {
    var fullInfoElement = document.getElementById("full-info");
    var button = document.querySelector("#one .button");

    if (fullInfoElement.style.display === "none") {
        fullInfoElement.style.display = "block";
        button.textContent = "Show Less";
    } else {
        fullInfoElement.style.display = "none";
        button.textContent = "Learn More";
    }
}