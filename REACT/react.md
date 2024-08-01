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

