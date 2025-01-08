/**
 * palindromo = 'oso' 'ana'
 * anagrama = 'amor' 'roma'
 * isograma = "brújula", "examen", "zebra"
 */

const word1 = 'brujula'
const word2 = 'zebra'

const checkWords = (word1: string, word2: string) => {
    type TResult = {
        word1: string
        word2: string
        areAnagrama: boolean
        areIsograma: boolean
    }
    const result: TResult = {
        word1: '',
        word2: '',
        areAnagrama: false,
        areIsograma: false,
    }

    const isPalindromo = (word) => {
        const reverseWord = word.split('').reverse().join('').replaceAll(' ', '')
        return !!(word.replaceAll(' ', '') === reverseWord)
    }

    const areAnagrama = (word1, word2) => {
        const arrWord1 = word1.replaceAll(' ', '').split('')
        const arrWord2 = word2.replaceAll(' ', '').split('')

        if(arrWord1.length !== arrWord2.length) return false
        for( let i of arrWord1) {
            if(!arrWord2.includes(i)) return false
        }
        return true
    }

    const areIsograma = (word1, word2) => {
        const arrWord1 = word1.replaceAll(' ', '').split('')
        const arrWord2 = word2.replaceAll(' ', '').split('')

        for( let i of arrWord1) {
            if(arrWord2.includes(i)) return false
        }
        return true

    }

    result.word1 = `Palindromo ${isPalindromo(word1)}`
    result.word2 = `Palindromo ${isPalindromo(word2)}`
    result.areAnagrama = areAnagrama(word1, word2)
    result.areIsograma = areIsograma(word1, word2)

    return result
}

console.log(checkWords(word1, word2))

