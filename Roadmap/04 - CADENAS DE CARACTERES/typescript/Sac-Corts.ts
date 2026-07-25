// Define a character string
let text: string = "TypeScript is a typed language";

// 1. Access to specific characters
let firstCharacter: string = text[0];
let lastCharacter: string = text[text.length - 1];

// 2. String length
let _length: number = text.length; 

// 3. Substrings
let substring: string = text.substring(0, 10);
let substringSlice: string = text.slice(11, 13);

// 4. String concatenation
let additionalText: string = " with type support";
let concatenated: string = text.concat(additionalText);
let concatenationWithOperator: string = text + additionalText;

// 5. Repetition
let repeat: string = "Hi! ".repeat(3);

// 6. Iterate a string
for (let char of text) {
    console.log(char);
}

// 7. Conversion to upper and lower case
let uppercase: string = text.toUpperCase();
let lowercase: string = text.toLowerCase();

// 8. Character or substring replacement
let replacement: string = text.replace("typed", "modern");

// 9. Divison of strings in array
let _words: string[] = text.split(" ");

// 10. Union of an array of strings
let united: string = _words.join("-");

// 11. String interpolation
let version: number = 4;
let interpolation: string = `The current version of TypeScript is ${version}`;

// 12. Checking if one string contains another
let contains: boolean = text.includes("language");
let startsWith: boolean = text.startsWith("Type");
let endsWith: boolean = text.endsWith("language");

// 13. Substring or character indexes
let indexWord: number = text.indexOf("typed");
let lastIndexLetter: number = text.lastIndexOf("e");

// 14. Remove whitespace
let textWithSpace: string = "   TypeScript   ";
let noSpace: string = textWithSpace.trim();
let noStartSpace: string = textWithSpace.trimStart();
let noEndSpace: string = textWithSpace.trimEnd();

// 15. Compare strings
let isEqual: boolean = text === "TypeScript is a typed language";
let isEqualIgnoreCase: boolean = text.toLowerCase() === "typescript is a typed language";

// 16. Type conversions to string
let number: number = 42;
let numberAsString: string = number.toString();

// 17. Find a pattern with regular expressions
let regex: RegExp = /typed/i;
let coincidence: boolean = regex.test(text);

// 18. Get matches of a regular expression
let coincidences: RegExpMatchArray | null = text.match(/e/g);

// *** Extra Exercise *** //
function checkPalindromeTypeScript(word: string): boolean {
    let inverted: string = word.split('').reverse().join('').toLowerCase();
    return word === inverted;
}

function checkAnagramTypeScript(word1: string, word2: string): boolean {
    let ordered1: string = word1.toLowerCase().split('').sort().join('');
    let ordered2: string = word2.toLowerCase().split('').sort().join('');
    return ordered1 === ordered2;
}

function checkIsogramTypeScript(word: string): boolean {
    let isogram = new Set<string>();
    for (let char of word) {
        if (isogram.has(char)) {
            return false;
        }
        isogram.add(char);
    }
    return true;
}

function checkWordsTypeScript(word1: string, word2: string) {
    return {
        word1ItsPalindrome: checkPalindromeTypeScript(word1),
        word2ItsPalindrome: checkPalindromeTypeScript(word2), 
        theyAreAnagram: checkAnagramTypeScript(word1, word2),
        word1ItsIsogram: checkIsogramTypeScript(word1),
        word2ItsIsogram: checkIsogramTypeScript(word2)
    };
}

let _word1: string = "Roma";
let _word2: string = "Amor";

console.log(checkWordsTypeScript(_word1, _word2));