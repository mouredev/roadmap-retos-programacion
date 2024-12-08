// Ejercicio //

// Accessing specific characters
let str = "Hello World";
console.log(str[0]);
console.log(str.charAt(6));

// Substrings
console.log(str.substring(0, 5));
console.log(str.slice(6));
console.log(str.slice(-5));

// Length
console.log(str.length);

// Concatenation
let str1 = "Hello";
let str2 = "World"; 
console.log(str1 + " " + str2);
console.log(str1.concat(" ", + str2));

// Repetition
console.log(str.repeat(3));

// Iteration
for (let char of str) {
    console.log(char);
}

// Conversion to uppercase and lowercase
console.log(str.toUpperCase());
console.log(str.toLowerCase());

// Replacement
console.log(str.replace("World", "Everyone"));

// Splitting
let words = str.split(" ");
console.log(words);

// Joining
let joinedStr = words.join(" ");
console.log(joinedStr);

// Interpolation
let _name = "Isaac";
let greeting = `Hello ${_name}!`;
console.log(greeting);

// Checking substrings
console.log(str.includes("World"));
console.log(str.startsWith("Hello"));
console.log(str.endsWith("World"));

// Trimming
let paddedStr = "   Hello World     ";
console.log(paddedStr.trim());
console.log(paddedStr.trimStart());
console.log(paddedStr.trimEnd());

// Converting to array of characters
console.log(Array.from(str));

// Finding character of substring position
console.log(str.indexOf("o"));
console.log(str.lastIndexOf("o"));

// Extra Exercise //

function checkPalindrome(word) {
    let inverted = word.split('').reverse().join('');
    return word === inverted;
}

function checkAnagram(word1, word2) {
    let ordered1 = word1.split('').sort().join('');
    let ordered2 = word2.split('').sort().join('');
    return ordered1 === ordered2;
}

function checkIsogram(word) {
    let letters = new Set([]);
    for (char of word) {
        if (letters.has(char)) {
            return false;
        } 
        letters.add(char);
    }
    return true;
}

function checkWords(word1, word2) {
    return {
        word1ItsPalindrome: checkPalindrome(word1),
        word2ItsPalindrome: checkPalindrome(word2),
        theyAreAnagrams: checkAnagram(word1, word2),
        word1ItsIsogram: checkIsogram(word1),
        word2ItsIsogram: checkIsogram(word2),
    };
}

let word1 = "civic";
let word2 = "radar";

console.log(checkWords(word1, word2));
