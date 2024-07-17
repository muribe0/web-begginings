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
