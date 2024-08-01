window.onpopstate = function(event) { // When I pop something out of history (when go back in history)
    if (event.state) {
        console.log(event.state.section);
        showSection(event.state.section);
    }
}

function showSection(section) {
    fetch(`/section/${section}`)
        .then(response => response.text())
        .then(text => {
            document.querySelector('#content').innerHTML = text;
        })
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            const section = this.dataset.section;
            history.pushState({section: section}, '', `/section${section}`); // Add event to browsing history
            showSection(this.dataset.section);
        }
    })
    // default section
    // showSection(1);
});