
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */




// SOLUCION:



/////////////////////////////// Metodos de Cadena (String Methods) ///////////////////////////

// Cadenas de Caracteres:
let cadena1 = 'Gracias, MoureDev'
let cadena2 = 'Gracias por todo'
let cadena3 = 'Adios a todos'

// Longitud String: .length
const longitud = cadena1.length
console.log(longitud)


// Acceso a caracteres especificos:   [], .charAt(), .at()
//                                      Acceso por Indice con corchetes
console.log(cadena2[0])
console.log(cadena2[-1])

//                                      Acceso con metodo .charAt(index)
console.log(cadena2.charAt(0))
console.log(cadena2.charAt(-1))

//                                      Acceso con metodo .at(index)
console.log(cadena2.at(0))
console.log(cadena2.at(-1))


// SUBCADENAS:      .slice(), .substring()
//
console.log(cadena3.substring('0, 4'))
console.log(cadena3.slice(5))
console.log(cadena3.slice(-2))


// CONCATENACION:   +, .concat()

console.log(cadena1 + " " + cadena2)
console.log(cadena1.concat(" ", cadena2))


//  REPETICION:  .repeat()
console.log('JS'.repeat(6))

// RECORRIDO DE CARACTERES: for...of
for (let x of cadena1) {
    console.log(x)
}


console.warn('\n-------- CONVERSION MAYUSCULAS Y MINUSCULAS .toUpperCase(), .toLowerCase() --------\n')

// CONVERSION A MAYISCULAS Y MINUSCULAS:    .toUpperCase(), .toLowerCase()
console.log(cadena1.toUpperCase())
console.log(cadena1.toLowerCase())

console.warn('\n---------------------------- REEMPLAZO ---------------------\n')

// REEMPLAZO:   .replace(), .replaceAll()
console.log(cadena3.replace('Adios', 'Gracias'))
console.log(cadena3.replaceAll('o', '0'))
console.log(cadena3.replace(/o/g, 'Y'))

console.warn('\n----------------------- DIVISION EN PARTES .split(), .join() ---------------------\n')
// DIVISION EN PARTES: .split(), .join()
console.warn('\n   \n')

console.log(cadena1.split(" "))
console.log('1,2,3'.split(','))

console.warn('\n---------------------------- UNION ---------------------\n')
// UNION:
let arrCadenas = [cadena1, cadena2]
console.log(arrCadenas.join(' '))

console.warn('\n---------------------------- INTERPOLACION ---------------------\n')
// INTERPOLACION: `${var}`
let nombre = 'Imanol'
console.log(`Hola, mi nombre es ${nombre} y solo quiero decir... ${cadena1} `)

console.warn('\n---------------------------- VERIFICACION ---------------------\n')
// VERIFICACION:    .includes(), .startsWith(), .endsWith()
cadena1.includes('MoureDev')
cadena1.startsWith('a')
cadena1.endsWith('v')
cadena1.indexOf('Gracias')
cadena1.lastIndexOf('o')


console.warn('\n---------------------------- ELIMINACION DE ESPACIOS ---------------------\n')
// ELIMINACION DE ESPACIOS: .trim(), .trimStart(), .trimEnd()
let cadenaConEspacios = '   Benvenidos  '
console.log(cadenaConEspacios.trim())
console.log(cadenaConEspacios.trimStart())
console.log(cadenaConEspacios.trimEnd())


console.warn('\n---------------------------- COMPARACION DE CADENAS ---------------------\n')
// COMPARACION DE CADENAS:  ===, <, >
console.log('1' === 1)
console.log(2 < 5)


console.warn('\n---------------------------- REEMPLAZO ---------------------\n')
// REEMPLAZO:
let texto = 'Imanol Aguer'
let nuevoTexto = texto.slice(0, 5) + 'Maximiliano'
console.log(`Texto ORIGINAL: ${texto}        Texto Nuevo: ${nuevoTexto}`)

console.warn('\n---------------------------- CONVERTIR ---------------------\n')
// CONVERTIR:
let cadena4 = '1'
let cadena5 = 5
console.log(Number(cadena4))
console.log(String(cadena5))
console.log((157).toString())

console.warn('\n---------------------------- REPETICION ---------------------\n')
// REPETICION:
console.log('Imanol '.padStart(3, 'Aguer'))
console.log('Imanol '.padEnd(3, 'I'))

console.warn('\n---------------------------- REGULAR EXPRESSIONS ---------------------\n')
// EXPRESIONES REGULARES:
console.log('ima123'.match('/\d+/'))
console.log('ima123'.replace('/\d+/', ''))


console.warn('\n---------------------------- INVERTIR UNA CADENA ---------------------\n')
// INVERTIR UNA CADENA:
console.log(cadena1.split('').reverse().join(''))




//  DIFICULTAD EXTRA(opcional):
//  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
//     * para descubrir si son:
//     * - Palíndromos
//     * - Anagramas
//     * - Isogramas


const readline = require('readline')
const { stdin: input, stdout: output } = require('node:process')

const rl = readline.createInterface({ input, output })


function programa() {
    console.warn('\n\n\n---------------------------- BIENVENIDO A TU PROGRAMA ---------------------\n')
    console.log(`
        Bienvenido al Programa: 
        (0) - Verificacion Total
        (1) - Verificacin de Palindromos
        (2) - Verificacin de Anagramas
        (3) - Verificacin de Isogramas
        `)


    var todo = 1
    const returnToMenu = () => {
        const clear = () => console.clear()
        if (todo == 1 || todo == 2 || todo == 3) {
            rl.question('Desea continuar con el programa o cerrarlo: (y/n):  ', (respuesta) => {
                if (respuesta === 'y') {
                    clear()
                    programa()
                } else {
                    clear()
                    rl.close()
                }
            })
        } else {
            rl.close()
        }
    }

    rl.question('Eliga un (numero) para avanxar: ', (optionMethod) => {
        switch (optionMethod) {
            case '1':
                todo = 1
                rl.question('Ingrese la Plabra 1: ', (palabraUno) => {
                    rl.question('Ingrese la Palabra 2: ', (palabraDos) => {
                        checkForPalindromo(palabraUno, palabraDos)
                    })
                })
                break
            case '2':
                todo = 2
                rl.question('Ingrese la Plabra 1: ', (palabraUno) => {
                    rl.question('Ingrese la Palabra 2: ', (palabraDos) => {
                        checkForAnagrama(palabraUno, palabraDos)
                    })
                })
                break
            case '3':
                todo = 3
                rl.question('Ingrese la Plabra 1: ', (palabraUno) => {
                    rl.question('Ingrese la Palabra 2: ', (palabraDos) => {
                        checkForIsograma(palabraUno, palabraDos)
                    })
                })
                break
            case '0':
                rl.question('Ingrese la Plabra 1: ', (palabraUno) => {
                    rl.question('Ingrese la Palabra 2: ', (palabraDos) => {
                        checkForPalindromo(palabraUno, palabraDos)
                        checkForAnagrama(palabraUno, palabraDos)
                        checkForIsograma(palabraUno, palabraDos)
                        todo = 1
                    })
                })
                break;
        }
    })



    const checkForPalindromo = (palabraUno, palabraDos) => {
        console.log('\n\n ----- Resultado Palindromo -----')

        const palabra1 = palabraUno.toLowerCase().split('').reverse().join('')
        const palabra2 = palabraDos.toLowerCase().split('').reverse().join('')
        console.log('Palabra numero 1 a testear --> ', palabra1)
        console.log('Palabra numero 2 a testear --> ', palabra2)

        let db = [palabra1, palabra2]


        for (let i = 0; i < db.length; i++) {
            if (db[i] === palabraUno || db[i] === palabraDos) {
                console.log(`${db[i]} es un Palindromo Completamente`)
            } else {
                console.log(`${db[i]} no es un Palindromo`)
            }
        }

        returnToMenu()
    }


    const checkForAnagrama = (palabraUno, palabraDos) => {
        console.log('\n\n ----- Resultado Anagrama -----')

        const palabra1 = palabraUno.split('').sort().join(0)
        const palabra2 = palabraDos.split('').sort().join(0)


        if (palabra1 === palabra2) {
            console.log(` SI ${palabraUno} y ${palabraDos} son Anagramas.`)
        } else {
            console.log(`NO ${palabraUno} y ${palabraDos} no son Anagramas.`)
        }

        returnToMenu()
    }

    const checkForIsograma = (palabraUno, palabraDos) => {
        console.log('\n\n ----- Resultado Isograma -----')
        console.log('Not available at the Moment!')
        returnToMenu()
    }

}

programa()



