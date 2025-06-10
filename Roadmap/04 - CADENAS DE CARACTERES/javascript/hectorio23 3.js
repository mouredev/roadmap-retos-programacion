"use strict";

const { NOMEM } = require('dns');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

/*
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
  conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
*/


function discoverType(value1, value2) {
    // Se guarda una variable local la cual sera modificada
    // para posteriormente ser comparada con la segunda palabra.
    // Se puede observar que se ordena de manera contraria
    let valueReverse = value1.split('').reverse().join('');

    if (valueReverse === value2) {
        return "\nLas palabras anteriormente insertadas forman en realidad un palíndromo\n\n";
    } else if (isograma(value1) && isograma(value2)) {
        return "\nAmbas palabras son isogramas\n\n";
    } else if (isograma(value1) || isograma(value2)) {
        return "\nUna de las palabras es un isograma\n\n";
    } else if (anagrama(value1, value2)) {
        return "\nEs un anagrama\n\n";
    }

    return "\nLas palabras proporcionadas no cumplen con las condiciones para ser un palíndromo, isograma o anagrama\n";
}

function isograma(palabra) {
    let _tmp_ = "";

    for (let item of palabra) {
        if (_tmp_.includes(item)) {
            return false;
        }
        _tmp_ += item;
    }
    return true;
}

function anagrama(palabra1, palabra2) {
    let palabra1_sorted = palabra1.split('').sort().join('');
    let palabra2_sorted = palabra2.split('').sort().join('');

    if (palabra1.length !== palabra2.length || palabra1_sorted !== palabra2_sorted) {
        return false;
    }
    return true;
}

function main() {
    // Las siguientes variables almacenan las palabras
    // insertadas por el usuario
    let value1;
    let value2;
    rl.question("Inserta la primera palabra: ", (nombre) => { value1 = nombre;})    
    rl.question("Ahora inserta la segunda palabra: ", (nombre) => { value2 = nombre;})    

    let cadena1 = "Hola";
    let cadena2 = "Mundo";

    // Modifican la variable original transformando sus caracteres en minúsculas
    value1 = value1.toLowerCase();
    value2 = value2.toLowerCase();

    // Se llama a la función discoverType, la cual devuelve una cadena dependiendo de
    // si las palabras ingresadas por el usuario forman parte de un palíndromo, anagrama o isograma.
    // Para lograr esto, se invocan otras funciones cuyo único propósito es verificar
    // si las palabras cumplen con las especificaciones dadas.
    console.log(discoverType(value1, value2));

    // Concatenación de dos cadenas
    let concatenacion = cadena1 + " " + cadena2;
    console.log("Concatenación: " + concatenacion);

    // Se elimina cualquier espacio de la cadena de caracteres
    let cadenaPrueba = concatenacion.replace(/\s/g, "");
    console.log("Cadena sin espacios en blanco: " + cadenaPrueba);

    // Obtención de la longitud de dos cadenas
    console.log("Longitud de la cadena 1: " + cadena1.length);
    console.log("Longitud de la cadena 2: " + cadena2.length);

    // Acceso a caracteres individuales
    console.log("Primer caracter de la cadena 1: " + cadena1[0]);
    console.log("Último caracter de la cadena 2: " + cadena2[cadena2.length - 1]);

    // Comparación
    if (cadena1 === cadena2) {
        console.log("Las cadenas son iguales");
    } else {
        console.log("Las cadenas son diferentes");
    }

    // Subcadena
    let subcadena = concatenacion.substring(5, 10); // Extrae "Mundo"
    console.log("Subcadena: " + subcadena);

    // Búsqueda
    let buscar = "Mundo";
    let posicion = concatenacion.indexOf(buscar);
    if (posicion !== -1) {
        console.log("La cadena '" + buscar + "' fue encontrada en la posición " + posicion);
    } else {
        console.log("La cadena '" + buscar + "' no fue encontrada");
    }

    // Modificación
    concatenacion = concatenacion.replace("Mundo", "Universo");
    console.log("Después de reemplazar 'Mundo' por 'Universo': " + concatenacion);
}

main();
