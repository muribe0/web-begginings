document.addEventListener('DOMContentLoaded', function() {
    let counter = 0;

    document.querySelector('#increase').onclick = () => {
        counter++;
        document.querySelector('h1').innerHTML = counter;
    }

    document.querySelector('#decrease').onclick = () => {
        counter--;
        document.querySelector('h1').innerHTML = counter;
    }
});