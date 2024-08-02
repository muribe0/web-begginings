# Scroll

## Window
Propiedades:
- `window.innerHeight`: How tall is the window
- `window.innerWidth`: How wide is the window
- `window.scrollX`: How many pixels have been scrolled horizontally
- `window.scrollY`: How many pixels have been scrolled vertically
- `document.body.offsetHeight` is the height of the (whole) content of the page.
- `window.scrollBy(x, y)`: Scroll the window by x pixels horizontally and y pixels vertically

So if the user has scrolled to the bottom of the page:
`window.scrollY + window.innerHeight >== document.body.offsetHeight`

# Animation

```css
@keyframes hide {
    0% {
        opacity: 1;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margin: 10px;
    }

    75% {
        opacity: 0;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margin: 10px;
    }

    100% {
        opacity: 0;
        height: 0;
        padding: 0;
        line-height: 0;
        margin: 0;
    }
}

.post {
    background-color: #77dd11;
    padding: 20px;
    margin: 10px;

    /* for animation */
    animation-name: hide;
    animation-duration: 1s;
    animation-fill-mode: forwards;
    animation-play-state: paused;
}
```

# React

We will use `React`, `ReactDOM`, `Babel` to simplify js code for a big project.

First we add the script with: 



