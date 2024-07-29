// Thrid

let counter = 0;

function increase() {
    counter++;
    document.querySelector("h1").innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`The counter is ${counter}`);
    }
}

function decrease() {
    counter--;
    document.querySelector("h1").innerHTML = counter;
}

function reset() {
    counter = 0;
    document.querySelector("h1").innerHTML = counter;
}

document.addEventListener("DOMContentLoaded", function() { // When the page is loaded, do the following...
    // This is added so that the code will not run until the page is loaded. Otherwise, the code will run before
    // the HTML is loaded, and the querySelector will not find the element since the body is not loaded yet.

    document.querySelector("#increase").onclick = increase; // When the button with the id "increase" is clicked, call the function "increase"
    document.querySelector("#decrease").onclick = decrease;
});
