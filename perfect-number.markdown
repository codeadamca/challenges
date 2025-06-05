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
2. Use a loop to determine all the potential divisors.
3. Place all divisors except the input number in an array.
4. Sum all the numbers in the array.
5. Compare the total with the `input`.
6. Return true or false.

### Assets

> [Download PDF Slide Desk](/pdfs/perfect-number.pdf)

---

<a href="https://codeadam.ca">
<img src="https://cdn.codeadam.ca/images@1.0.0/codeadam-logo-coloured-horizontal.png" width="100">
</a>






