[Home](/) / Decode an Image

<style>@import url("//readme.codeadam.ca/readme.css");</style>

## Decode

**Write a function that will decode a cryptic image from a web page.**

The function will be provided a URL like the following:

[https://challenges.codeadam.ca/decode-an-image-sample-1](decode-an-image-sample-1)

The table in the example URL includes a list of colours, x, and y coordinates. When the colours are placed in a grid using the x and y coordinates they will create a small image.

For example, the above URL will create the following image:

[Sample Grid](images/decode-an-image-grid.png)

Once your code is complete, test your function with the following URLs:

1. [https://challenges.codeadam.ca/decode-an-image-sample-2](decode-an-image-sample-2)
2. [https://challenges.codeadam.ca/decode-an-image-sample-3](decode-an-image-sample-3)

### Function Scaffolding

```javascript
/**
 * Reverses the value of the input.
 *
 * @param {string|url} url - The URL of the grid to decode.
 * @returns {void} 
 */
function decode(url) {
    // ...
}
```

### Possible Approach

1. Create a function with one parameter. Have the function `console.log()` the input.
2. Scape the url input into a variable named `html`. 
3. Extract the `table` from the `html` variable.
4. Convert the tabular data into a array called `grid`.
5. Loop through the `grid` array and generate an image using a `table`, a set of `divs`, or unicode characters.

### Assets

> [Download PDF Slide Desk](/pdfs/decode-an-image.pdf)

---

<a href="https://codeadam.ca">
<img src="https://cdn.codeadam.ca/images@1.0.0/codeadam-logo-coloured-horizontal.png" width="100">
</a>






