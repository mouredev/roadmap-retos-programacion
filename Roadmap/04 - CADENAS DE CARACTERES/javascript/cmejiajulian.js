/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */

// CREACION DE CADENAS 

let cadena1 = 'Hola Mundo';// Usando comillas simples
let cadena2 = "Hola Mundo";// Usando comillas dobles 
let cadena3 = `Hola Mundo`;// Usando comillas invertidas 


//Concatenacion 

console.log(cadena1 +' '+ cadena2 +' '+ cadena3);


//Propiedades de las cadenas de caracteres 

//lenght - devuelve la longitud de la cadena

let usuario = 'Julian';
console.log(usuario.length) //6

// toUpperCase() - Convierte la cadena a mayusculas 

let videoJuego = ' Assassins creed valhalla '
console.log(videoJuego.toUpperCase());//MODERN WARE


//toLowerCase() convierte la cadena a minusculas 

let videoJuego2 = 'CALL OF DUTY '
console.log(videoJuego2.toLowerCase());// call of duty 

//charAt(index) - devuelve el caracter en la posicion especificada

let saludo= 'Hola';
console.log(saludo.charAt(0));//H

/*indexOf(subcadena) - devuelve el índice de la primera aparición 
 de la subcadena especificada, o -1 si no se encuentra.*/

let music = 'Metal Rock Pop';
console.log ( music.indexOf('Rock'));

//substring(inicio,fin) devuelve la palabra segun la posicion indicada

let mago = 'reconocer';
console.log(mago.substring(9,0));

//split - divide la cadena en un array de subcadenas usando el seperador especificado

let deporte = 'Natacion Ciclismo Futbol';
console.log(deporte.split());//[Natacion Ciclismo Futbol]

/*replace(buscar, reemplazar)  - reemplaza la primera aparicion de la 
subcadena especificada*/

let diosDeLaGuerra = 'Tanos'
console.log(diosDeLaGuerra.replace('Tanos','DIOS'));//DIOS

//trim - elimina los espacios en blanco de la cadena 

let cidadPrincipal = ' New York  '
console.log(cidadPrincipal.trim());

 /* Temple Strings (Plantillas de Cadenas de Texto)
las comillas invertidas``permiten interpolar variables y expreciones
dentro de las cadenas asi 
*/

let firstName = 'Julian';
let lastName = 'Batista';
let fullName = `Nombre completo: ${firstName} ${lastName}!`
 
console.log(fullName);


/*  
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Por favor ingrese la primera palabra: ', (primeraPalabra) => {
    rl.question('Por favor ingrese la segunda palabra: ', (segundaPalabra) => {

        // Palíndroma
        const palabrainvertida = (palabra) => {
            return palabra.split('').reverse().join('');
        };

        // Anagrama
        const anagrama = (palabra) => {
            return palabra.toLowerCase().split('').sort().join('');
        };

        const esAnagrama = (palabra1, palabra2) => {
            return anagrama(palabra1) === anagrama(palabra2);
        };

        // Isograma
        const palabraUnica = (palabra) => {
            palabra = palabra.toLowerCase();
            const letrasUni = new Set();

            for (const letra of palabra) {
                if (letrasUni.has(letra)) {
                    return false;
                }
                letrasUni.add(letra);
            }
            return true;
        };

        // Comparaciones
        if (primeraPalabra.toLowerCase() === palabrainvertida(segundaPalabra.toLowerCase())) {
            console.log('Es palíndroma');
        } else if (esAnagrama(primeraPalabra, segundaPalabra)) {
            console.log('Es anagrama');
        } else if (palabraUnica(primeraPalabra)) {
            console.log('Es isograma');
        } else {
            console.log('No es ninguna');
        }

        rl.close();
    });
});
