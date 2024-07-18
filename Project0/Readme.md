# Day 1

1. First I stablished the search bar in the center by using
    ```css
    body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    ```

which centers the search bar using flexbox. Here:
* `display: flex;` makes the body a flex container.
* `align-items: center;` centers the items vertically.
* `justify-content: center;` centers the items horizontally.
* `height: 100vh;` makes the body take the full height of the viewport.
This last one is to ensure that te search bar is always in the center of the screen due to `justify-content: center`. 

2. Then, I added some padding for `form` for the search bar. Since it is the parent element of the search bar and I wanted for it to have certain space around it.
    
3. Next, I added some styles to the search bar itself. I added a border, border-radius, padding, and width. I also added a box-shadow to make it look like it is floating. Some padding, margin between the bar and the button and a change of font. Also, a `min-width` of `400px` to ensure that the search bar does not get too small.
    Also, a `min-width` of `400px` to ensure that the search bar does not get too small.
    Both have this style:
    ```css
    input[type="text"] {
    padding: 8px 0px;
    margin-right: 8px;
    /*border: 1px solid #dfe1e5;*/
    border-radius: 24px;
    box-shadow: none;
    font-size: 16px;
    min-width: 450px;
   }
   ```
4. After that, I added some styles to the button. I added a background color, border, border-radius, padding, and margin. I also added a hover effect to the button to make it more interactive.
    ```css
    input[type="submit"] {
    padding: 8px 16px;
    /*border: none;*/
    border-radius: 4px;
    background-color: #f8f8f8;
    color: #3c4043;
    cursor: pointer;
    font-size: 14px;
    }
    
    input:hover {
    box-shadow: grey 1px 1px 2px;
    border-color: #c0c0c0;
    }
   ```
5. Added some details for the nav bar in the upper right corner. I added some padding, margin, font-size, text-decoration, color, and font-family.
    ```css
    .up {
    display: flex;
    align-items: center;
    justify-content: right;
    }

    .up > a {
    padding: 8px 8px;
    margin: 8px;
    font-size: 18px;
    text-decoration: none;
    color: black;
    font-family: Montserrat sans-serif;
    }
    ```
   
6. Finally, I added some considerations for a responsive page:
   ```css
    @media (max-width: 600px) {
        .search {
            width: 80%;
        }
    }
   ```

Entire `index.css` at dat 1:
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    border: red 1px solid;
}

body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

form {
    padding: 20px;
}


input[type="text"] {
    padding: 8px 0px;
    margin-right: 8px;
    /*border: 1px solid #dfe1e5;*/
    border-radius: 24px;
    box-shadow: none;
    font-size: 16px;
    min-width: 450px;
}

input[type="submit"] {
    padding: 8px 16px;
    /*border: none;*/
    border-radius: 4px;
    background-color: #f8f8f8;
    color: #3c4043;
    cursor: pointer;
    font-size: 14px;
}

input:hover {
    box-shadow: grey 1px 1px 2px;
    border-color: #c0c0c0;
}

.up {
    display: flex;
    align-items: center;
    justify-content: right;
}

.up > a {
    padding: 8px 8px;
    margin: 8px;
    font-size: 18px;
    text-decoration: none;
    color: black;
    font-family: Montserrat sans-serif;
}

/* Responsive Design */
@media (max-width: 600px) {
    .search {
        width: 80%;
    }
}
```

That is all for day 1.
Next: Find out how to put the image search and advanced search in the upper right corner of the screen in the most efficient way.

# Day 2

1. Modifying the nav bar for the button to be beneath the search bar:
   The CSS property `flex-direction: column`; applied to a container makes its children (flex items) stack vertically. This means the main axis runs from top to bottom, and the cross axis runs from left to right. As a result, flex items are laid out in a column, one on top of the other, within their container. 
    ```css
    form {
    display: flex;
    flex-direction: column;
    align-items: center; /* Center align the items for better aesthetics */
    gap: 10px; /* Adjust the gap as needed */
    }
    ```
2. Changed some text formating to be more google-like. `font: 13px/27px Roboto,Arial,sans-serif;` . Made some modifications to the search bar. Specified in the css doc.
3. Several changes towards improvement of the advanced search
    - First, the advanced search is now a `div` element with the class `advanced-search`. This is to make it easier to style the advanced search.
    - The class `filter` is added to the `div` element that contains the advanced search filters. This is to make it easier to style the filters.
    - The class `filter-row` is a `div` element that represents each row of search. 
    - The css aims to use a lot of elements configs as opposed to classes.
    - Css:
      - The `form-section` contains all the rows ant titles.
      - Each div inside of it, has a margin to the left, so it does not stick to the leftmost side of the screen.
      - The `filter` class serves as a flex container for each `filter-row`. Inside each `filter-row` there is a `p` element and `input` element. The `p` element is the title of the filter and the `input` element is the input text field for the filter.

The css looks like this:
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font: 13px/27px Roboto, Arial, sans-serif;
    /*border: red 1px solid;*/
}

.up {
    display: flex;
    justify-content: right;
    align-items: center;
}

.up > a {
    margin: 8px;
    padding: 8px 8px;
    color: black;
    text-decoration: none;
}

.up > a:hover {
    text-decoration: underline;
}

.down {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.down > img {
    margin-bottom: 16px;
}

.down > .search {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
}

input[name="q"], input[type="submit"] {
    border-radius: 24px;
    padding: 8px 24px;
    font-size: 16px;
    border: 1px solid #dfe1e5;
    box-shadow: none;
}

input[name="q"] {
    margin-right: 8px;
    min-width: 450px;
}

input[type="submit"] {
    min-width: 120px;
    border: none;
    background-color: #f8f8f8;
    color: #3c4043;
    cursor: pointer;
    font-size: 14px;
    border-radius: 4px;
    margin: 0 8px;
}

input[name="q"]:hover {
    box-shadow: grey 1px 1px 2px;
    border-color: #c0c0c0;
    background-color: #f0f0f0;
}

hr {
    border: none;
    height: 1px;
    background-color: #000; /* Change the color to suit your design */
    margin: 10px 0 20px 0; /* Add some vertical space around the line */
}

/* top right bottom left*/
.form-section {
    margin: 0 0 0 48px;
}

.form-section > div {
    margin: 10px 0 0 0;
}

.form-section h1 {
    font-size: 22px;
    color: darkred;
}

.form-section h2 {
    font-size: 16px;
}

.filter {
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.filter-row {
    margin: 8px 0;
    display: flex;
    align-items: center;
    flex-direction: row;
}

.filter-row > p {
    min-width: 200px;
}

.filter-row > input {
    padding: 0 0 0 16px;
    margin-right: 16px;
    min-width: 100vh;
}

.explanation {
    font-size: 11px;
    overflow: hidden;
    white-space: nowrap;
    @media (max-width: 1100px) {
        display: none;
        width: 0;
    }
}

.filter-row > label {
    min-width: 100vh;
    padding: 0;
    display: flex;
}

.filter-row > label > input {

    background-color: dodgerblue;
    color: white;
    padding: 4px 16px;
    margin: 0 0 0 auto;
    font-size: 12px;
}


@media (max-width: 800px) {
    .search {
        width: 80%;
    }
    .filter-row > input, .filter-row > label {
        min-width: 50%; /* Adjust min-width to be more responsive */
        width: auto; /* Allows the input to adjust its width according to the screen size */
    }
}
```