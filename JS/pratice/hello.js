// Second

function salute() {
    // Alternates between "Hello!" and "Goodbye!" when the button is clicked
    const heading = document.querySelector("h1");

    // Look through the document and find the first element that has the tag "h1"
    if (heading.innerHTML === "Hello!") {
        heading.innerHTML = "Goodbye!";

    } else {
        heading.innerHTML = "Hello!";
    }
}
