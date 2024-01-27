//at, charAt - Recibe un numero y devuelve el caracter en esa posicion
const sentence: string = 'Mouredev by Brais Moure'
console.log('at', sentence.at(10))
console.log('charAt', sentence.charAt(3))


//concat - Conecta dos strings y devuelve una nueva
const str1: string = 'Hola'
const str2: string = 'Mundo'
console.log('concat con espacio', str1.concat(' ', str2))
console.log('concat con caracter', str1.concat('-', str2))

//startsWith & endsWith - Evalua si el string inicia/termina con los caracteres del string del argumento y devuelve un booleano
console.log('startsWith 1', sentence.endsWith('Mouredeb'))
console.log('startsWith 2', sentence.endsWith('by'))
console.log('endsWith 1', sentence.endsWith('Moure'))
console.log('endsWith 2', sentence.endsWith('dev'))

//fromCharCode - Devuelve un string creada por una secuencia de unidades de UTF-16
console.log('fromCharCode', String.fromCharCode(12, 24, 15, 9))

//includes - Evalua si un substring se encuentra dentro de un string. Devuelve un booleano. Se diferencia entre mayusculas y minusculas
const word1: string = 'by'
const word2: string = 'By'
console.log('includes 1', sentence.includes(word1))
console.log('includes 2', sentence.includes(word2))

//indexOf - Devuelve la posicion en la que un substring inicia dentro de un string. En caso que la substring se repita, devuelve la posicion de la primera encontrada.
//lastIndexOf - Devuelve la posicion en la que un substring inicia dentro de un string. En caso que la substring se repita, devuelve la posicion de la ultima encontrada.
const newSentence: string = 'Hola mundo. Bienvenidos al stream! Adios mundo.'
const word3: string = 'mundo'
console.log('indexOf', newSentence.indexOf(word3))
console.log('lastIndexOf', newSentence.lastIndexOf(word3))

//match - Devuelve los valores que coincidan con el regex
const regex = /[A-Z]/g //Evalua solo mayusculas
console.log('match', sentence.match(regex))

//padStart & padEnd - Agregan un caracter al inicio o al final de la string, segun tantos espacios falten entre el ancho del string, y el ancho del argumento.
console.log('padStart', sentence.padStart(106, '-'))
console.log('padStart', sentence.padStart(102, '.'))
console.log('padEnd', sentence.padEnd(40, '^'))
console.log('padEnd', sentence.padEnd(80, '*'))

//raw - Metodo que funciona con template literals para crear un string, en base a otra que tenga caracteres especiales que no se quieren perder o interpretar de forma inadecuada.
const filePath = String.raw`C:\Development\profile\aboutme.html`
console.log('raw', `Ruta de acceso: ${filePath}`)

//repeat - Devuelve una nueva string que contiene el numero de copias del string del argumento, concatenadas
const strSinSpacio: string = 'Mundo!'
const strConSpacio: string = 'Mundo! '
console.log('repeat 1', `Hola ${strSinSpacio.repeat(3)}`)
console.log('repeat 2', `Hola ${strConSpacio.repeat(5)}`)

//replace - Sustituye uno, varios, o toda un string, con otra string del segundo argumento del metodo.
const ownRegex = /Brais Moure/i
console.log('replace 1', sentence.replace('Brais', 'AChapeton'))
console.log('replace 2', sentence.replace(ownRegex, 'Andres'))

//search - Ejecuta una busqueda en base a un regex para buscar una similitud en un string, y devolver el index de esa primera similitud
const regex2 = /[^\w\s']/g; //Este regex evalua todo lo que NO sea una palabra, espacios en blanco, o comillas
console.log('search', newSentence.search(regex2))

//slice - Extrae una seccion del string y retorna una nueva, si modificar la original
console.log('slice', sentence.slice(7))

//split - Divide el string en base a un patron, y crea un array con las substrings resultantes
console.log('split', sentence.split(' '))

//toLowerCase & toUpperCase - Devuelve un string transformado todo a minusculas/mayusculas
console.log('toLowerCase', sentence.toLowerCase())
console.log('toUpperCase', sentence.toUpperCase())

//trim - Elimina todos los espacios vacios que se encuentren al inicio o al final de un string
//trimStart - Elimina solo los espacios vacion que se encuentra al inicio
//trimEnd - Elimina solo los espacios vacion que se encuentra al final
const whiteSpaces: string = '    Hello World!     '
console.log('trim 1', whiteSpaces)
console.log('trim 2', whiteSpaces.trim())
console.log('trimStart', whiteSpaces.trimStart())
console.log('trimEnd', whiteSpaces.trimEnd())


const esPalindromo = (my_string: string): void => {
  const reverseStr: string = my_string.toLowerCase().split('').reverse().join('')
  if(my_string.toLowerCase() === reverseStr){
    console.log('Es palindroma')
  }else{
    console.log('No es palindroma')
  }
}

esPalindromo('reconocer')
esPalindromo('mundo')

const esAnagrama = (str1: string, str2: string): void => {
  const reverseStr2: string = str2.toLowerCase().split('').reverse().join('')
  if(str1.toLowerCase() === reverseStr2){
    console.log(`La palabra ${str1} es un anagrama`)
  }else{
    console.log(`${str1} no es un anagrama`)
  }
}

esAnagrama('amor', 'roma')

const esIsograma = (my_string: string): void => {
  const letrasArray: String[] = my_string.toLowerCase().split('')
  const letrasSet = new Set(letrasArray)
  if(letrasArray.length === letrasSet.size){
    console.log(`La palabra ${my_string} es un isograma`)
  }else{
    console.log(`${my_string} no es un isograma`)
  }
}

esIsograma('murcielago')
esIsograma('ambiente')

