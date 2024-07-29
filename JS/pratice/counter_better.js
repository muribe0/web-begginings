// 3rd & 6th

if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function increase() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector("h1").innerHTML = counter;
    localStorage.setItem('counter', counter);
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

    document.querySelector("h1").innerHTML = localStorage.getItem('counter'); // Set the innerHTML of the h1 element to the value of the counter variable

    document.querySelector("#increase").onclick = increase; // When the button with the id "increase" is clicked, call the function "increase"

    // setInterval(increase, 1000); // Call the function "increase" every 1000 milliseconds (1 second)
    localStorage.setItem('counter', counter);
});
