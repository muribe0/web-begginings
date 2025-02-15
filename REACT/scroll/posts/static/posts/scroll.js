// start with first post
let counter = 1;

// loads 20 posts at a time
const quantity = 20;

document.addEventListener('DOMContentLoaded', load);

window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
}

document.addEventListener('click', event => {
    const element = event.target;
    if (element.className === 'hide') {
        // If the element clicked is a button with class hide, remove the parent div
        element.parentElement.style.animationPlayState = 'running';

        element.parentElement.addEventListener('animationend', () => {
            element.parentElement.remove();
        })
    }
});

function load() {
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    fetch(`/posts?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            data.posts.forEach(add_post);
        });
}

function add_post(contents) {
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = `${contents} <button class="hide">Hide</button>`;

    // Add post to DOM
    document.querySelector('#posts').append(post);
}