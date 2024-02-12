// Comparación de caracteres
///////////////////////////////
const a = "a"
const b = "B"
console.log(a < b)
// Las minúsculas son "mayores" que las mayúsculas
console.log(a > b)

// Cambio de case
///////////////////////////////
console.log(a.toUpperCase())
console.log(b.toLowerCase())

// Longitud
///////////////////////////////
const str = "Hola mundo"
console.log(str.length)

// Acceso a caracteres
///////////////////////////////
console.log(str.charAt(0))
console.log(str[0])
console.log(str.at(0))
// Valores negativos cuentan desde el final
console.log(str.at(-2))

// Concatenación de strings
///////////////////////////////
console.log(str.concat(" ", str))

// Palabras contenidas, inicios y finales
///////////////////////////////
console.log(str.includes("mundo"))
console.log(str.endsWith("mundo"))
console.log(str.endsWith("o"))
console.log(str.startsWith("Hola"))
console.log(str.startsWith("H"))

// Index de un carácter o palabra
///////////////////////////////
const sentence = "Mi perro es mayor que tu perro"
console.log(sentence.indexOf("perro"))
console.log(sentence.indexOf("gato"))

// Último index de un carácter o palabra
///////////////////////////////
console.log(sentence.lastIndexOf("perro"))
console.log(sentence.lastIndexOf("gato"))

// Pads
///////////////////////////////
console.log(str.padEnd(20, "."))
console.log(str.padStart(15, ">"))

// Repetición
///////////////////////////////
console.log(a.repeat(10))

// Reemplazo
///////////////////////////////
console.log(sentence.replace("perro", "gato"))
console.log(sentence.replaceAll("perro", "gato"))

// Búsqueda
///////////////////////////////
console.log(sentence.search("perro"))
console.log(sentence[sentence.search("perro")])

// Slice
///////////////////////////////
console.log(sentence.slice(25))
console.log(sentence.slice(20, 30))
console.log(sentence.slice(-8))

// Split
///////////////////////////////
console.log(sentence.split(" "))

// Trim
///////////////////////////////
const str2 = "   Hola   "
console.log(str2.trim())
console.log(str2.trimEnd())
console.log(str2.trimStart())

// Convertir a string
///////////////////////////////
const number = 92
console.log(typeof number.toString())

///////////////////////////////
// Dificultad extra
///////////////////////////////

const isPalindrome = (word) => {
  let validation

  for(let i = 0; i < (word.length / 2) - 1; i++) {
    if(word[i] !== word[word.length - 1 - i]) { return false }
    else { return true }
  }

  return validation
}


const isAnagram = (word1, word2) => {
  let arr1 = word1.normalize("NFD").replace(/[\u0300-\u036f]/g, "").split("").sort()
  let arr2 = word2.normalize("NFD").replace(/[\u0300-\u036f]/g, "").split("").sort()

  if(arr1.length !== arr2.length) {
    return false
  } else {
    if(arr1.length !== arr2.length) {
      return false
    } else {
      return true
    }
  }
}

const isIsogram = (word) => {
  let arr = word.normalize("NFD").replace(/[\u0300-\u036f]/g, "").split("").sort()

  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] == arr[i + 1]) {
      return false
    } else {
      return true
    }
  }
}

console.log(isPalindrome("arenera"))
console.log(isPalindrome("hola"))
console.log(isAnagram("álvaro", "valora"))
console.log(isAnagram("hola", "mundo"))
console.log(isIsogram("murciélago"))
console.log(isIsogram("arena"))
