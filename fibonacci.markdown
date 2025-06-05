[Home](/) / Fibonacci Sequence

<style>@import url("//readme.codeadam.ca/readme.css");</style>

## Fibonacci Sequence

**Write a function that will return the nth term in the Fibonacci sequence, where n is the first parameter.**

> [What is the Fibonacci sequence?](https://en.wikipedia.org/wiki/Fibonacci_sequence)

### Function Scaffolding

```javascript
/**
 * Returns the nth term in the Fibonacci sequence.
 *
 * @param {number} n - The position (1-based) in the Fibonacci sequence to retrieve.
 * @returns {number} The nth Fibonacci number.
 */
function getFibonacci(n) {
    // ...
}
```

### Possible Approach

1. Create a function with one parameter. Have the function console.log() the input.
2. If n is 0 or 1 then return n.
3. Create an array that has the first two numbers of the Fibonacci sequence.
4. Write a loop that will iterate n number of times. 
5. In each iteration add the two previous numbers and add it to the array.
6. Return the last number in the array.

### Assets

> [Download PDF Slide Desk](/pdfs/fibonacci.pdf)

---

<a href="https://codeadam.ca">
<img src="https://cdn.codeadam.ca/images@1.0.0/codeadam-logo-coloured-horizontal.png" width="100">
</a>






