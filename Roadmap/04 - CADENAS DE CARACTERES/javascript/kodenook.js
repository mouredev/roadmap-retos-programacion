
let txt = 'hello, javascript!'

console.log(txt.charAt(4))
console.log(txt.toUpperCase())
console.log(txt.toLowerCase())
console.log(txt.trim())
console.log(txt.repeat(2))
console.log(txt.replace('h', 'j'))
console.log(txt.split(' '))
console.log(txt.endsWith('script!'))
console.log(txt.startsWith('hello'))

/**
 * The function checks if a word is a palindrome, an anagram, or an isogram.
 * @param word - The first parameter "word" is a string that you want to check if it is a palindrome,
 * an anagram, or an isogram.
 * @param word2 - The parameter `word2` is a second word that will be compared to the first word for
 * anagram check.
 */
function typeWord(word, word2) {

    if (word === word.split('').reverse().join('')) {
        console.log('is palindrome')
    }

    if (word.split('').sort().join('') == word2.split('').sort().join('')) {
        console.log('is an anagram')
    }

    if (word.length === new Set(word).size) {
        console.log('is isogram')
    }
}

typeWord('roma', 'amor')