//EJERCICIO
//Acceso a caracteres específicos
//Subcadenas
//Longitud
//Concatenación
let myString1: string = 'Hola, '
let myString2: string = 'TypeScript'

let message: string = myString1.concat(myString2)

console.log(message)

//Repetición
//Recorrido
//Conversión a mayúsculas y minúsculas
//Reemplazo
//División
//Unión
//Interpolación
//Verificación
//Otros

//EXTRA
function analyzeTheseWords(word1: string, word2: string) {
	function palindrome(word: string) {
		const reversedWord = word.toLowerCase().split('').reverse().join('')

		if (word.toLowerCase() === reversedWord) {
			console.log(`${word} es un palíndromo`)
		} else {
			console.log(`${word} no es un palíndromo`)
		}
	}

	function anagram(word1: string, word2: string) {
		const arr1 = word1.toLowerCase().split('').sort().join('')
		const arr2 = word2.toLowerCase().split('').sort().join('')

		if (arr1 === arr2) {
			console.log(`${word1} es un anagrama de ${word2}`)
		} else {
			console.log(`${word1} no es un anagrama de ${word2}`)
		}
	}

	function isogram(word: string) {
		const array = word.toLowerCase().split('')
		const set = new Set(array)

		if (array.length === set.size) {
			console.log(`${word} es un isograma`)
		} else {
			console.log(`${word} no es un isograma`)
		}
	}

	palindrome(word1)
	palindrome(word2)

	anagram(word1, word2)

	isogram(word1)
	isogram(word2)
}

analyzeTheseWords('Roma', 'Amor')
analyzeTheseWords('Radar', 'Paloma')
