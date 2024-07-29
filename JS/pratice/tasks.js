document.addEventListener('DOMContentLoaded', function() {
    document.querySelector("#submit").disabled = true;

    document.querySelector("#task").onkeyup = () => {
        if (document.querySelector("#task").value.length > 0) {
            document.querySelector("#submit").disabled = false;
        }
    };

    document.querySelector('form').onsubmit = () => { // similar to using funciont()

       const task = document.querySelector('#task').value;
       console.log(task);

       const li = document.createElement('li');
       li.innerHTML = task;
       document.querySelector('#tasks').append(li);
       document.querySelector('#task').value = '';

       document.querySelector("#submit").disabled = true;

       return false; // to prevent the form from submitting
   }
});