

let cadena = "Hola soy una Cadena primitiva!"
let cadena_obj = new String(cadena) // Objeto String
console.log(typeof cadena)
console.log(typeof cadena_obj) //

let animal = "cat"
let pet = "DOG"

// Acceder a un caracter especifico
console.log(animal.charAt(1))
console.log(animal[2])

// Comparar cadenas
let a = "a"
let b = "b"
if (a<b) {
  console.log(`${a} es menor que ${b}`)
} else if (a>b) {
  console.log(`${a} es mayor que ${b}`)
} else {
  console.log(`${a} y ${b} son iguales`)
}

// Concatenacion
console.log(a + ", " + b)
console.log(animal.concat(' ', pet))

// Cadenas literales largas

let cadenaLarga = 
"Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
 It has survived not only five centuries, but also the leap into electronic typesetting,"
console.log(cadenaLarga)

// Longitud
console.log(cadenaLarga.length)

// Repeticion
console.log(animal.repeat(3))

// Porcion
console.log(cadena.slice(0,4))
console.log(cadena.substring(15,19))

// Busqueda
const regex = /[^\w\s']/g
console.log(cadena.search(regex))
console.log(cadena[cadena.search(regex)])
console.log(cadena.indexOf("primitiva"))
console.log(cadena.match(/[A-Z]/g)) // Busca caracteres que coincidan
 
// Busqueda | Termina en...
console.log(cadena.endsWith("!"))
console.log(cadena.endsWith("?"))

// Busqueda | Empieza en...
console.log(cadena.startsWith("Hola"))
console.log(cadena.startsWith("Adios"))

// Busqueda | buscar palabra en cadena
const word = "primitiva"
console.log( `La palabra "${word}" ${
  cadena.includes(word) ? "esta" : "no esta"
} en la oracion` )

// Dividir y buscar palabras
const palabra = cadena.split(' ')
console.log(palabra[3])

// Reemplazar
console.log(cadena.replace("una", "la"))
let cadena2 = "Un perro y otro perro"
console.log(cadena2.replaceAll('perro', 'caballo'))

// mayusculas y minusculas
console.log(animal.toUpperCase())
console.log(pet.toLowerCase())


console.log(String.fromCodePoint(9731, 9733, 9842, 0x2f804));

// Aumentar el largo al final de la cadena
console.log(cadena.padEnd(35, '.'))

// Aumentar el largo al principio de la cadena
let num = '5'
console.log(num.padStart(2, '0'))
let longnum = '0000000000114'
const cutNum = longnum.slice(-3)
console.log(cutNum.padStart(longnum.length, "*"))

// Iteracion
const iterator = cadena[Symbol.iterator]()
let char = iterator.next()
while (!char.done && char.value !==' ') {
  console.log(char.value)
  char = iterator.next()
}

// Eliminacion de espacios principio y final
console.log("    Hello    ".trimStart())
console.log("    Hello    ".trimEnd())
console.log("    Hello    ".trim())

// Retornar un valor string
console.log(cadena_obj)
console.log(cadena_obj.valueOf())

// DIFICULTAD EXTRA

const readLine = require('readline');
const rl = readLine.createInterface({
  input: process.stdin,
  output: process.stdout
})

function menuPalabras() {
  rl.question('Introduce una palabra: ', (palabra1) => {
    rl.question('Introduce otra palabra: ', (palabra2) => {
      if (palabra1 && palabra2) {
        menu(String(palabra1), String(palabra2))
      } else {
        console.log('Debes introducir las dos palabras');
        menuPalabras();
      }
    })
  })
}

function menu(p1, p2) {
  p1 = p1.toLowerCase();
  p2 = p2.toLowerCase();

  let palabra1 = p1.split('')
  let palabra2 = p2.split('')

  console.log('\n1. Son palindromos?')
  console.log('2. Son anagramas?')
  console.log('3. Son isogramas?')
  console.log('4. Volver a introducir las palabras')
  console.log('5. Salir')

  rl.question('\nElige una opcion: ', (opcion) => {
    switch (opcion) {
      case '1':
        if(isPalindromo(palabra1, palabra2)) {
          console.log('Son palindromos')
          menu(p1, p2)
        } else {
          console.log('No son palindromos')
          menu(p1, p2)
        }
        break;
      case '2':
        if(isAnagrama(palabra1, palabra2)) {
          console.log('Son anagramas')
        } else {
          console.log('No son anagramas')
        }
        menu(p1, p2)
        break;
      case '3':
        if(isIsograma(palabra1) && isIsograma(palabra2)) {
          console.log('Son isogramas')
        } else if (isIsograma(palabra1)) {
          console.log(`La palabra ${palabra1} es isograma pero la ${palabra2} no lo es`)
        } else if (isIsograma(palabra2)) {
          console.log(`La palabra ${palabra2} es isograma pero la ${palabra1} no lo es`)
        } else {
          console.log('No son isogramas')
        }
        menu(p1, p2)
        break;
      case '4':
        menuPalabras()
        break;
      case '5':
        console.log('Saliendo...')
        rl.close()
        break;
      default:
        console.log('elige una de las opciones')
        menu(p1, p2)
    }
  })
}

function isPalindromo(palabra1, palabra2) {
  let i = 0
  let j = palabra2.length-1
  while (i <= palabra1.length-1 && j>=0) {
    if(palabra1[i] !== palabra2[j]) return false
    i++
    j--
  }
  return true
}

function isAnagrama(palabra1, palabra2) {

  let i=0

  while (i<=palabra1.length-1) {
    let j=0
    while(j<=palabra2.length-1) {
      if(palabra1[i] === palabra2[j]){
        palabra2.splice(j,1)
        console.log(palabra2)
        j--
      }
      j++ 
    }
    i++
  }

  if(palabra2.length === 0) {
    return true
  } else {
    return false
  }
}

function isIsograma(palabra) {
  let i=0

  while(i<=palabra.length-1) {
    let j= i+1
    while(j<=palabra.length-1) {
      if(palabra[i]===palabra[j]) {
        return false
      } else {
        j++
      }
    }
    i++
  }
  return true
}

menuPalabras()