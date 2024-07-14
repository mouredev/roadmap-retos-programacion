//EJERCICIO
//Acceso a caracteres específicos
const myAlphabet: string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

console.log(myAlphabet[17] + myAlphabet[8] + myAlphabet[2])

const nameChart1: string = myAlphabet.charAt(17)
const nameChart2: string = myAlphabet.charAt(8)
const nameChart3: string = myAlphabet.charAt(2)

console.log(nameChart1, nameChart2, nameChart3)

const rPosition: number = myAlphabet.indexOf('R')

console.log(`La letra R es la número ${rPosition + 1} de nuestro alfabeto`)

//Longitud
const phrase: string = 'Me encantan las papas fritas'

console.log(`\"${phrase}\" tiene ${phrase.length} caracteres`)

//Subcadenas
const phraseSlice: string = phrase.slice(16)

console.log(phraseSlice)

const heroes: string = 'Batman le gana a Superman'
const Batman: string = heroes.substring(0, 6)
const Superman: string = heroes.substring(17)

console.log(Batman)
console.log(Superman)

//Concatenación
let action: string = ' está peleando con '

console.log(Batman.concat(action, Superman))
console.log(Batman + action + Superman)

//Repetición
let ric: string = 'Ric '

console.log(ric.repeat(3))

//Recorrido
for (let i = 0; i < myAlphabet.length; i++) {
	console.log(myAlphabet[i])
}

//Conversión a mayúsculas y minúsculas
const fruits: string[] = ['fresa', 'PARCHITA', 'LiMÓn', 'Mango']

fruits.forEach((fruit) => {
	console.log(fruit.toUpperCase())
})

fruits.forEach((fruit) => {
	console.log(fruit.toLowerCase())
})

//Reemplazo
let musicPlayer = 'Music Player current song: The Pretender - Foo Fighters'
console.log(musicPlayer)

musicPlayer = musicPlayer.replace('The Pretender - Foo Fighters', 'Monster - Skillet')
console.log(musicPlayer)

//División
const companiesString: string = 'Google, Apple, Telegram, Facebook'
const companiesArr = companiesString.split(', ')

console.log(companiesArr)

//Unión
const colorsArray = ['blue', 'red', 'yellow', 'white']
const colorsString = colorsArray.join(', ')

console.log(colorsString)

//Interpolación
console.log(`\n\"TypeScript es JavaScript premium\" \n\n\t\t\t${ric.toUpperCase()}\n`)

//Verificación
const fiveInSpanish: string = 'Cinco'
const fiveCharsRegex = /\b[A-Za-z]{5}\b/g

console.log('Tiene cinco caracteres la palabra "cinco"?', fiveCharsRegex.test(fiveInSpanish))

//Otros
const randomPhrase = 'Pedro estaba bebiendo un jugo de manzana'
const jRegex = /\b[Jj]{1}[A-Za-z]{3}\b/g

let result = randomPhrase.match(jRegex)

console.log(result)

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
