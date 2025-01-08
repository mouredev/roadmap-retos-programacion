program("facility", "disk");

function program(word1: string, word2: string): void {

    console.log(isPalindrome(word1) ? `The word ${word1} is a palindrome` : `The word ${word1} is not a palindrome`);
    console.log(isPalindrome(word2) ? `The word ${word2} is a palindrome` : `The word ${word2} is not a palindrome`);

    console.log(areAnagrams(word1, word2) ? `The words ${word1} and ${word2} are anagrams` : `The words ${word1} and ${word2} are not anagrams`);

    console.log(isIsogram(word1) ? `The word ${word1} is an isogram` : `The word ${word1} is not an isogram`);
    console.log(isIsogram(word2) ? `The word ${word2} is an isogram` : `The word ${word2} is not an isogram`);

}

function isPalindrome(word: string): boolean {

    const len = word.length;

    for (let i = 0; i < len / 2; i++) {
        if (word[i] !== word[len - i - 1]) {
            return false;
        }
    }

    return true;

}

function areAnagrams(word1: string, word2: string): boolean {

    if (word1.length !== word2.length) {
        return false;
    }

    const lettersWord1 = word1.split('').sort();
    const lettersWord2 = word2.split('').sort();

    return lettersWord1.join('') === lettersWord2.join('');

}

function isIsogram(word: string): boolean {

    const letters: string[] = [];

    for (const letter of word) {
        if (letters.includes(letter)) {
            return false;
        }
        letters.push(letter);
    }

    return true;

}
