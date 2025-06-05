[Home](/) / Perfect Number

<style>@import url("//readme.codeadam.ca/readme.css");</style>

## Perfect umber

**Write a function that determines whether or not the first parameter is a perfect number.**

> [What is a perfect number?](https://en.wikipedia.org/wiki/Perfect_number)

### Function Scaffolding

```javascript
/**
 * Determines whether the given number is a perfect number.
 * A perfect number is a number that is equal to the sum of its proper divisors (excluding itself).
 *
 * @param {number} num - The number to check.
 * @returns {boolean} True if the number is perfect, false otherwise.
 */
function isPerfectNumber(num) {
    // ...
}
```

### Possible Approach

1. Create a function with one parameter. Have the function `console.log()` the input.
2. Define an empty string variable called `reverse` to store the reversed string. 
3. Use a `for` loop to iterate through each character.
4. Append each character to the beginning of the `reverse` variable. 
5. Return the contents of the `reverse` variable.

### Assets

> [Download PDF Slide Desk](/pdfs/perfect-number.pdf)

---

<a href="https://codeadam.ca">
<img src="https://cdn.codeadam.ca/images@1.0.0/codeadam-logo-coloured-horizontal.png" width="100">
</a>






