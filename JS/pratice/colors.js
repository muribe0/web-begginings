// Fifth
function update_color(selector, color) {
    document.querySelector(selector).style.color = color;
}


document.addEventListener('DOMContentLoaded', function() {

    // document.querySelector("#red").onclick = function () {
    //     update_color("#hello", "red");
    // };

    const buttons = document.querySelectorAll("button");
    buttons.forEach(function(button) {
        // For all buttons->for each of them, when clicked->update color
        button.onclick = function() {
            update_color("#hello", button.dataset.color);
        };
    });

    // Choose a color

    document.querySelector("select").onchange = function () {
        update_color("#hello", this.value); // this.value is the value of the selected option
    }

    document.querySelector("#hello").onmouseover = function () {
        this.style.color = "green";
    };
});