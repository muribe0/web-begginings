function showPage(page) {
    document.querySelectorAll(`div`).forEach(div => {
        div.style.display = 'none';
    })

    document.querySelector(`#${page}`).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
    //

    buttons = document.querySelectorAll('button');
    buttons.forEach( button => {
        button.onclick = function() {
            showPage(this.dataset.page);
        }
    })
});