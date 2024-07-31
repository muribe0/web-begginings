document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('form').onsubmit = function() {

        // Get me the value of the input field with the id 'name'
        const name = document.querySelector('#name').value;
        alert(`Hello, ${name}!`);
        // Prevent the form from submitting
        return false;
    };
});