
let txt: string = 'hello, javascript!'

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
 * The function checks if a word is a palindrome, an anagram of another word, or an isogram.
 * @param {string} word - The `word` parameter is a string that represents a word.
 * @param {string} word2 - The parameter `word2` is a string that represents another word that will be
 * compared to `word` to check if they are anagrams.
 */
function typeWord(word: string, word2: string): void {

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