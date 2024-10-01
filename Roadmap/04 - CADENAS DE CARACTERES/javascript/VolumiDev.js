var cadenaTexto = 'Este es el ejemplo para trabajar con cadenas de texto'
// Mostramos la longitud de la cadena de texto
console.log('La longitud de la cadena de texto es de',cadenaTexto.length, 'caracteres')

// Metodos para acceder a cada uno de los caracteres de la cadena de texto
console.log('Accedemos con el at() al caracter deseado ->', cadenaTexto.at(3))  // Podemos acceder con el at() directamte
console.log('Accedemos con el charAt al caracter deseado ->', cadenaTexto.charAt(3)) 
console.log('Accedemos con el charCodeAt(), que nos retorna el codigo UTF-16 ->', cadenaTexto.charCodeAt(3))
console.log('Accedemos como si fuera un array con los [] ->', cadenaTexto[3])

// Metodos para extraer partes de la cadena de texto
console.log('Utilizamos el metodo Slice() ->', cadenaTexto.slice(8,15))
console.log('Utilizamos el metodo Substring() ->', cadenaTexto.substring(8,15))
console.log('Utilizamos el metodo Substr() ->', cadenaTexto.substr(8,15))

// Transformar con lower upper case
console.log('Utilizamos el toLowerCase() para pasarlo a miniscula ->', cadenaTexto.toLowerCase())
console.log('Utilizamos el toLowerCase() para pasarlo a miniscula ->', cadenaTexto.toUpperCase())

// Concatenar varias cadenas de texto.
var text1 = 'texto 1'
var text2 = 'texto 2'
console.log('Concatenamos las dos cadenas ->', text1.concat(' - ', text2))

// Eliminar los espacios de la cadena de texto
var cadenaEspacio = '     contenido de la cadena       '
console.log('Esta es la variable sin modificar ->', cadenaEspacio)
console.log('Eliminamos los espacio del principio y del final de la cadena de texto ->', cadenaEspacio.trim())
console.log('Eliminamos los espacio del principio  de la cadena de texto ->', cadenaEspacio.trimStart())
console.log('Eliminamos los espacio del del final de la cadena de texto ->', cadenaEspacio.trimEnd())

// Añadimos cadena al principio o al final de la variable una determinada cantidad de veces que le pasemos.
var numero = '5'
console.log('Le añadimos al principio de la cadena de texto tantos 0 como le indiquemos ->', numero.padStart(3,'0'))
console.log('Le añadimos al fianl de la cadena de texto tantos 0 como le indiquemos ->', numero.padEnd(3,'0'))

// Repetimos un cadena de texto tantas veces como le pasasmos por parametro
var rep = 'repetir '
console.log('Vamos a repetir la cadena 4 veces ->', rep.repeat(4))

// Reemplazmos la cadena que le pasamos como parametro por la del siguiente parametro
var txt = 'Hola Diego, Diego'
console.log('Reemplazamos "Diego" por "Juan" ->', txt, '->', txt.replace('Diego','Juan'))
console.log('Reemplazamos "Diego" por "Juan" ->', txt, '->', txt.replace(/DIEGO/i,'Juan'))
console.log('Reemplazamos "Diego" por "Juan" ->', txt, '->', txt.replace(/DIEGO/gi,'Juan'))
var txt = 'Tenemos un perro que se llama Otto. Es un perro de raza Golden'
console.log('Vamos a cambiar todos los "perro" por "gato" ->', txt.replaceAll('perro', 'gato'))

// Convertir una cadena de texto en un array
console.log('Vamos a usar el " " como caracter de spliteo ->', txt.split(' '))

// Comprobar si una cadena contiene una cadena que le pasamos por parametro.
console.log('Vamos a ver si contiene la "a" ->', txt.includes('a'))
console.log('Vamos a ver si contiene la "w" ->', txt.includes('w'))

// Dificultad extra
const readline = require("readline")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

function palindromo(p1){
  let palflag = true
  let arrayP1 = p1.split('')
  let array_sin_espacios = [];
  for(let i=0 ; i < arrayP1.length ; i++){
    if(arrayP1[i] != ' '){
      array_sin_espacios.push(arrayP1[i])
    }
  }

  for (let i = 0; i < arrayP1.length && palflag == true; i++) {
    if(array_sin_espacios[i] != array_sin_espacios.reverse()[i]){
      palflag = false
    }
  }
  if(palflag == true){
    console.log(`${p1}\ Es palindromo`)
  }else{
    console.log(`${p1}\ No es palindromo`)
  }
}

function anagrama(p1 ,p2){
  let ana_p1 = p1.replace(/\s+/g,'').toLowerCase()
  let ana_p2 = p2.replace(/\s+/g,'').toLowerCase()
  ana_p1 = ana_p1.split('').sort()
  ana_p2 = ana_p2.split('').sort()
  if(ana_p1.length != ana_p2.length){
    console.log('No son anagrama')
  }else{
    ana_p1 = ana_p1.join('')
    ana_p2 = ana_p2.join('')
    if(ana_p1 === ana_p2){
      console.log('Son anagrama')
    }
  }
}

function isograma(p1){
  let iso_flag = true
  let isoP1 = p1.replace(/\s+/g,'').toLowerCase()
  isoP1 = isoP1.split('').sort()
  for(let i=1 ; i<isoP1.length && iso_flag == true; i++){
    if(isoP1[i] == isoP1[i-1]){
      iso_flag = false
    }
  }
  if(iso_flag){
    console.log(`${p1} es un isograma`)
  }else{
    console.log(`${p1} no es un isograma`)
  }
}


function inicio(){
  rl.question('Introduce una cadena de caracteres\n', (p1) => {
    rl.question('Introduce la segunda cadena\n', (p2) => {
      p1 = p1.toLowerCase()
      p2 = p2.toLowerCase()
      if (p1 == p2){
        console.log('Ambas palabras tiene que se distintas')
        inicio()
      }else{
        console.log('Palabra 1 =', p1)
        console.log('Palabra 2 =', p2)
        palindromo(p1)
        palindromo(p2)
        anagrama(p1, p2)
        isograma(p1)
        isograma(p2)

        rl.question('Desea cerrar el programa? S/N\n', (resp) => {
          resp = resp.toUpperCase()
          if(resp == 'S'){
            console.log('Saliendo....')
            process.exit(0)
          }else{
            inicio()
          }
        })
      }
    })
  })
  
}

  inicio()
