/* -- exercise */
let str: string = "Hello";
console.log(str[0]);

str = "Hello World";
console.log(str.substring(0, 5));
console.log(str.slice(-5));

str = "JavaScript";
console.log(str.length);

let str1: string = "Hello";
let str2: string = "World";
console.log(str1 + " " + str2);
str = "abc";
console.log(str.repeat(3));

str = "JavaScript";
for (let char of str) {
  console.log(char);
}

str = "Hello";
console.log(str.toUpperCase());
console.log(str.toLowerCase());

str = "Hello World";
console.log(str.replace("World", "JavaScript"));

str = "Apple, Banana, Cherry";
console.log(str.split(", "));
let arr: string[] = ["Apple", "Banana", "Cherry"];
console.log(arr.join(", "));

let nameA: string = "Alice";
console.log(`Hello, ${nameA}!`);

str = "JavaScript is awesome";
console.log(str.includes("Java"));
console.log(str.startsWith("Java"));
console.log(str.endsWith("awesome"));

/* -- extra challenge */
const isPalindrome = (word: string): boolean => {
  let reversed: string = word.split("").reverse().join("");
  return word.toLowerCase() === reversed.toLowerCase();
};

const isAnagram = (word1: string, word2: string): boolean => {
  let sorted1: string = word1.toLowerCase().split("").sort().join("");
  let sorted2: string = word2.toLowerCase().split("").sort().join("");
  return sorted1 === sorted2;
};

const isIsogram = (word: string): boolean => {
  let charMap: { [key: string]: boolean } = {};
  for (let char of word.toLowerCase()) {
    if (charMap[char]) return false;
    charMap[char] = true;
  }
  return true;
};

let word1: string = "Madam";
let word2: string = "Adam";

console.log(`"${word1}" is a palindrome:`, isPalindrome(word1));
console.log(`"${word2}" is an anagram of "${word1}":`, isAnagram(word1, word2));
console.log(`"${word1}" is an isogram:`, isIsogram(word1));
