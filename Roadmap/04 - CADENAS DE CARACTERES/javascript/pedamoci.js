let lorem = new String('Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum, eum! Ipsam odit repellendus dolorem dolor ut sequi beatae, odio earum dignissimos aut consequuntur quibusdam, ad voluptas unde atque, sapiente inventore!')
let hello = 'Hello'
let world = 'world'

// ----------------------- OPERACIONES DE CADENAS -----------------------
  // at() --> busca un caracter o elemento por posición empenzando desde el 0, con números negativos va de atras hacia delante empezando por -1
    console.log(lorem.at(25)) // --> devuelve la 'e' de amet
    console.log(lorem.at(-32)) // --> devuelve ' ' el espacio entre voluptas y unde

  // charAt() --> busca un caracter por posición empenzando desde el 0, no acepta números negativos y no devuelve espacios, saltos de linea, etc.
    console.log(lorem.charAt(45)) // --> devuelve la 's' de adipisicing
    console.log(lorem.charAt(64)) // --> devuelve la '' ya que es el espacio entre Earum y eum

  // charCodeAt() --> devuelve el codigo (valor del 0 al 65523 del codigo UTF-16) de un caracter o elemento buscado por posición empenzando desde el 0, no acepta números negativos y si el caracter es un emoji, símbolo matemático o caracter de un idoma raro el valor devuelto es incorrecto
    console.log(lorem.charCodeAt(45)) // --> devuelve 115 del codigo en UTF-16 de la 's' de adipisicing
    console.log(lorem.charCodeAt(64)) // --> devuelve 32 del codigo en UTF-16 ya que es el espacio entre Earum y eum

  // charCodeAt() --> devuelve el codigo (valor del 0 al 65523 que puede contener letras del codigo UTF-16) de cualquier caracter buscado por posición empenzando desde el 0, no acepta números negativos
    console.log(lorem.codePointAt(45)) // --> devuelve 115 del codigo en UTF-16 de la 's' de adipisicing
    console.log(lorem.codePointAt(64)) // --> devuelve 32 del codigo en UTF-16 ya que es el espacio entre Earum y eum

  // concant() --> concatena 
    console.log(hello.concat(' ', world, ', mensaje número ', 1)); // --> devuelve 'Hello world, mensaje número 1'

  // endsWith() --> devuelve true | false comparando el string ingresado con el final de la cadena
    console.log(lorem.endsWith('!')); // --> true
    console.log(lorem.endsWith('inventore!')); // --> true
    console.log(lorem.endsWith('Lore', 4)); // --> true ya que compara el string con como termina la cadena hasta (sin incluir el caracter) la posición indicada 
    console.log(lorem.endsWith('Lorem', 4)); // --> false 

  // includes() --> devuelve true | false revisando si el string ingresado esta en la cadena, es case sensitive (distingue entre mayúsculas y minúsculas)
    console.log(lorem.includes('!')); // --> true
    console.log(lorem.includes('inventore!')); // --> true
    console.log(lorem.endsWith('lorem')); // --> true ya que dentro de la palabra dolorem se encuaantra 'lorem'
    console.log(lorem.endsWith('Amet')); // --> false 

  // indexOf() --> busca una coincidencia en la cadena con el string ingresado y devuelve la posicion del primer caracter de la primera coincidencia
    console.log(lorem.indexOf('dolor')); // --> devuelve 13 (ignora la posición 93 y 101 que también lo cumplen)
    console.log(lorem.indexOf(' ')); // --> devuelve 5

  // isWellFormed() --> devuelve true | false si el string tiene un codigo UTF-16 completo
    const correctUTF16 = "\uD83D\uDE00"; // el '😄' al ser una simbolo complejo esta formado por dos partes 
    const incorrectUTF16 = "\uD83D"; // Una parte del codigo UTF-16 de '😄'
    console.log(correctUTF16.isWellFormed()); // --> devuelve true
    console.log(incorrectUTF16.isWellFormed()); // --> devuelve false

  // lastIndexOf() --> busca una coincidencia en la cadena con el string ingresado y devuelve la posicion del primer caracter de la última coincidencia
    console.log(lorem.indexOf('dolor')); // --> devuelve 101 (ignora la posición 13 y 93 que también lo cumplen)
    console.log(lorem.indexOf(' ')); // --> devuelve 207

  // localCompare() --> compara la cadena de la derecha con la de la izquerda, si la de la deracha va antes en orden alfabetico devuelve -1, si va despues 1 y 0 si son iguales según llas reglas de comparación 
    console.log("manzana".localeCompare("banana")); // --> 1 
    console.log("banana".localeCompare("manzana")); // --> -1
    console.log("pera".localeCompare("pera")); // --> 0 
    console.log("réservé".localeCompare("RESERVE", 'es', { sensitivity: "base"})) // --> 0 ya que ignora el acento y las mayúsculas
    console.log("ä".localeCompare("z", "es")); // --> -1 ya que 'ä' en el español se la considera como una variante de 'a'
    console.log("ä".localeCompare("z", "sv")); // --> 1 ya que 'ä' es parte del alfabeto sueco y va despues de la 'z'

  // match() --> busca a través de una expreción regular (https://regex101.com) los caracteres o las cadenas que coincidan
    console.log(lorem.match(/[A-Z]/g)); // --> L, E, I ya que devuelve las letras mayúsculas desde la 'A' a la 'Z'
    console.log(lorem.match(/\b\w*um\w*\b/g)); // --> ipsum, Earum, eum, earum ya que devuelve las palabras que contengan 'um'

  // matchAll() --> busca a través de una expreción regular (https://regex101.com) los caracteres o las cadenas que coincidan y la devuelve incluyendo los grupos capturables
    const array = [...lorem.matchAll(/s(a)\w*(ie)\w*(e)/g)]
    console.log(array[0]) // --> sapiente, a, ie, e primero devuelve sapiente ya que busca una palabra 's'-'a'-cualquier caracter-'ie'-cualquier caracter-'e' y despues devuelve cada grupo 'a', 'ie', 'e' 

  // normalize() --> transforma el código dado a uno normalizado
    const name1 = "\u0041\u006d\u00e9\u006c\u0069\u0065" // --> Amélie, el codigo de 'é' esta dado por \u00e9
    const name2 = "\u0041\u006d\u0065\u0301\u006c\u0069\u0065" // --> Amélie, el codigo de 'é' esta dado por \u0065\u0301 el primero correspode a 'e' y el segundo al acento
    console.log(name1 === name2) // --> False
    console.log(name1.normalize('NFC') === name2.normalize('NFC')); // --> True

  // padEnd() --> agrega el caracter/string que quieras al final de un string hasta llegar a la longitud ingresada, empieza desde 1 (siempre devuelve como mínimo el string original)
    console.log(hello.padEnd(6, ',').padEnd(7, ' ') + world) // --> Hello, world

  // padStart() --> agrega el caracter/string que quieras al inicio de un string hasta llegar a la longitud ingresada, empieza desde 1 (siempre devuelve como mínimo el string original)
    console.log('9725'.padStart(10, '*')) // --> ******9725

  // repeat() --> repite el string la cantidad de veces ingresadas
    console.log(`I feel ${'Happy! '.repeat(3)}`) // --> I feel Happy! Happy! Happy!

  // replace() --> remplaza la primer coincidencia de lo indicado a través de una expreción regular o por un string por el string ingresado
    console.log(lorem.replace('dolor', 'DOLOR')) // --> remplaza el primer string 'dolor' (indice 13) por 'DOLOR', ignorando los de indice 93 y 101

  // replaceAll() --> remplaza todas las coincidencia de lo indicado a través de una expreción regular o por un string por el string ingresado
    console.log(lorem.replaceAll('dolor', 'DOLOR')) // --> remplaza todos los string 'dolor' (indice 13, 93, 101) por 'DOLOR'

  // search() --> busca la primer coincidencia de lo indicado a través de una expreción regular o por un string
    console.log(lorem.search('Ipsam')) // --> 70 ya que es el indice donde empieza el strin 'Ipsam'

  // slice() --> devuelve la parte indicada de un string, acepta números negativos
    console.log(lorem.slice(-99,-63)) // --> tae, odio earum dignissimos aut cons
    console.log(lorem.slice(151)) // --> consequuntur quibusdam, ad voluptas unde atque, sapiente inventore!

  // split() --> divede la cadena de texto por el string o la expreción regular ingresada
    console.log(lorem.split(' ')) // --> divide el texto en palabras
    console.log(lorem.split('')) // --> divide el texto en caracteres

  // startWith() --> verifica si en una posición hay un string que empiece como el string ingresado (NO acepta expresiones regelures)
    console.log(lorem.startsWith('Lor')) // --> True el texto comienza com Lorem...
    console.log(lorem.startsWith('lor', 15)) // --> True en el indice 15 inicia un string 'lor' (palabra original 'dolor' indice 13)

  // substring() --> devuelve la parte indicada -1 de un string, los números negativos los interpreta como 0 y no importa el orden en el que ingreses los datos
    console.log(lorem.substring(99,55)) // --> t. Earum, eum! Ipsam odit repellendus dolore ya que invierte los valores al ser el de la izquierda mas grande y el caracter de indice 99 no lo devuelve

  // toLocalLowerCase() --> devuelve el string ingresado en la minúscula del idioma ingresado
    console.log("İstanbul".toLocaleLowerCase("en-US") === "İstanbul".toLocaleLowerCase("tr")) // --> False ya que la 'İ' en minúscula en "en-US" es ditinta a la de "tr"

  // toLocalUpperCase() --> devuelve el string ingresado en la minúscula del idioma ingresado
    console.log("istanbul".toLocaleUpperCase("en-US") === "istanbul".toLocaleUpperCase("tr")) // --> False ya que la 'i' en minúscula en "en-US" es ditinta a la de "tr"

  // toLowerCase() --> devuelve el string en minúscula
    console.log("İstanbul".toLowerCase("en-US") === "İstanbul".toLowerCase("tr")) // --> True ya que vuelve el string insensible a la configuración regional

  // toString() --> devuelve un string de lo ingresado
    const num = 123
    console.log(num.toString());

  // toUpperCase() --> devuelve el string en mayúcula
    console.log("istanbul".toUpperCase("en-US") === "istanbul".toUpperCase("tr")) // --> True ya que vuelve el string insensible a la configuración regional

  // toWellFormed() --> transforma el codigo UTF-16 a un caracter legible
    console.log('ab\uD83D\uDE04c'.toWellFormed()) // --> ab😄c transformo '\uD83D\uDE04' en 😄

  // trim() --> quita los espacios en blanco del comienzo y final de un string (NO quita los saltos de linea)
    console.log(`                  ${hello}, ${world}!                      `.trim()) // --> 'Hello, world!'

  // trimEnd() --> quita los espacios en blanco del final de un string (NO quita los saltos de linea)
  console.log(`                  ${hello}, ${world}!                      `.trimEnd()) // --> '                  Hello, world!'

  // trimStart() --> quita los espacios en blanco del comienzo de un string (NO quita los saltos de linea)
  console.log(`                  ${hello}, ${world}!                      `.trimStart()) // --> 'Hello, world!                      '

  // valueOf() --> devuelve el valor de un objeto string
    const stringObj = new String("foo")
    console.log(stringObj) // --> [String: 'foo']
    console.log(stringObj.valueOf()) // --> 'foo'
    console.log('Hello, world!'.valueOf()) // --> 'Hello, world!'

  // [Symbol.iterator]() --> devuelde cada simbolo de un string (se usa si tenes codigo UTF-16 para separar por caracter)
    const str = "A\uD835\uDC68B\uD835\uDC69C\uD835\uDC6A";
    const strIter = str[Symbol.iterator]();
    console.log(strIter.next().value)
    console.log(strIter.next().value)
    console.log(strIter.next().value)
    console.log(strIter.next().value)
    console.log(strIter.next().value)
    console.log(strIter.next().value)

  // length --> devuelve la cantidad de caracteres que tiene un string
  console.log(lorem.length) // --> 218

// -------------------------- DIFICULTAD EXTRA --------------------------
function palindromos(word) {
  let i = 0
  let j = word.length - 1
  while (i <= word.length/2) {
    // recorre la palabra hasta la mitad ya que más seria redundate debido
    // a que va comparando los caracteres del inicio con los del final 
    if (word[i].toLowerCase !== word[j].toLowerCase) {
      return false
    } else if (i === j) {
      return true
    }
    i++
    j--
  }
}

function anagramas(word1, word2) {
  let i = 0
  while (word2.includes(word1[i]) && word1.length === word2.length) {
    // recorre la primer palabra verificando que la segunda contenga el caracter y remplaza a este por un guion 
    // para matener la igual de length y evitar que verifique con el mismo caracter dos veces
    if (i === word1.length - 1) return true
    word2 = word2.replace(word1[i], '-')
    i++
  } return false
}

function isogramas(word) {
  let i = 0
  do {
    // recorre la palabra guardando letra por letra y cuando quita una,
    //  la remplaza por un guion y verifica que no esta repetida
    if (i === word.length - 1) return true
    letter = word[i]
    word = word.replace(word[i], '-')
    i++
  } while (!word.includes(letter));
  return false
}

function startProgram() {
  // ingresa la/s palabra/s a la función pertinente, esta devuelve true | false y tiene una frase especifica para cada valor
  let operation = prompt('Que deseas verificar si es/son palindromos, anagramas o isogramas?')
  let word = 'y'
  if (operation.toLowerCase() === 'palindromos' || operation.toLowerCase() === 'palindromo') {
    while (word.toLowerCase() !== 'n') {
      if (word.toLowerCase() === 'y'|| word.toLowerCase() === 's') {
        word = prompt('Ingrese la palabra')
        word = prompt(`La palabra ${word} ${palindromos(word) ? 'es un palíndromo' : 'no es un palíndromo'}` + "\n".repeat(2) + 
                    `Desea comprobar si otra palabra es un palíndromo? Y/N`)
      } else {
        word = prompt('Desea comprobar si otra palabra es un palíndromo? Y/N')
      }
    }
  } else if (operation.toLowerCase() === 'anagramas' || operation.toLowerCase() === 'anagrama') {
    while (word.toLowerCase() !== 'n') {
      if (word.toLowerCase() === 'y'|| word.toLowerCase() === 's') {
        word = prompt('Ingrese la primer palabra')
        let word2 = prompt('Ingrese la segunda palabra')
        word = prompt(`Las palabras ${word} y ${word2} ${anagramas(word, word2) ? 'son anagramas' : 'no son anagramas'}` + "\n".repeat(2) + 
                      `Desea comprobar si otras palabras son anagramas? Y/N`)
      } else {
        word = prompt('Desea comprobar si otras palabras son anagramas? Y/N')
      }
    }
  } else if (operation.toLowerCase() === 'isogramas' || operation.toLowerCase() === 'isograma') {
    while (word.toLowerCase() !== 'n') {
      if (word.toLowerCase() === 'y'|| word.toLowerCase() === 's') {
        word = prompt('Ingrese la palabra')
        word = prompt(`La palabra ${word} ${isogramas(word) ? 'es un isograma' : 'no es un isograma'}` + "\n".repeat(2) + 
                      `Desea comprobar si otra palabra es un isograma? Y/N`)
      } else {
        word = prompt('Desea comprobar si otra palabra es un isograma? Y/N')
      }
    }
  }
  do {
    // bucle para saber si el usuario quiere hacer otra operacion (si no ingresa 's', 'y' o 'n') se repite hasta que ingrese un valor aceptado
    operation = prompt('Deseas hacer otra operación? Y/N')
    if (operation.toLowerCase() === 'y'|| operation.toLowerCase() === 's') startProgram()
  } while (operation.toLowerCase() !== 'n')
}
startProgram()