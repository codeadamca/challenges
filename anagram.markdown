[Home](/) / Anagram

<style>@import url("//readme.codeadam.ca/readme.css");</style>

## Anagram

**Write a function that determines if the first and second parameter are an anagram of each other or not.**

### Function Scaffolding

```javascript
/**
 * Determines if two values are anagrams of each other.
 * An anagram is formed by rearranging the letters of one word to create another.
 *
 * @param {string} str1 - The first string to compare.
 * @param {string} str2 - The second string to compare.
 * @returns {boolean} True if the strings are anagrams, false otherwise.
 */
function areAnagrams(str1, str2) {
    // ...
}
```

### Possible Approach

1. Create a function with one parameter. Have the function `console.log()` the input.
2. Check the length of each string. If they are not equal, return false. 
3. Convert each string to an array of letters.
4. Loop through one of the arrays and compare each letter form the first string with each letter from the second string. 
5. If any letters are different, return false. Otherwise, return true.

### Assets

> [Download PDF Slide Desk](/pdfs/anagram.pdf)

---

<a href="https://codeadam.ca">
<img src="https://cdn.codeadam.ca/images@1.0.0/codeadam-logo-coloured-horizontal.png" width="100">
</a>






