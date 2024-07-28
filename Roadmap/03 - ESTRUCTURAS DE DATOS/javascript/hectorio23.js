const readline = require('readline');

// Creación de la interfaz de entrada/salida
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para descubrir el tipo de relación entre dos palabras
function discoverType(value1, value2) {
    // Invertir la primera palabra
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

// Función para verificar si una palabra es un isograma
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

// Función para verificar si dos palabras son anagramas
function anagrama(palabra1, palabra2) {
    let palabra1_sorted = palabra1.split('').sort().join('');
    let palabra2_sorted = palabra2.split('').sort().join('');

    if (palabra1.length !== palabra2.length || palabra1_sorted !== palabra2_sorted) {
        return false;
    }
    return true;
}

// Función principal
function main() {
    rl.question("Inserta la primera palabra: ", function(value1) {
        if (!value1) {
            console.log("Entrada inválida. Por favor, inserta una palabra.");
            rl.close();
            return;
        
        }
        rl.question("Ahora inserta la segunda palabra: ", function(value2) {

            let cadena1 = "Hola";
            let cadena2 = "Mundo";

            if (!value1 || !value2) {
                return ;
            }
            // Convertir las palabras ingresadas a minúsculas
            value1 = value1.toLowerCase();
            value2 = value2.toLowerCase();

            // Mostrar el tipo de relación entre las palabras ingresadas
            console.log(discoverType(value1, value2));

            // Ejemplos de operaciones con cadenas
            let concatenacion = cadena1 + " " + cadena2;
            console.log("Concatenación: " + concatenacion);

            let cadenaPrueba = concatenacion.replace(/\s/g, "");
            console.log("Cadena sin espacios en blanco: " + cadenaPrueba);

            console.log("Longitud de la cadena 1: " + cadena1.length);
            console.log("Longitud de la cadena 2: " + cadena2.length);

            console.log("Primer caracter de la cadena 1: " + cadena1[0]);
            console.log("Último caracter de la cadena 2: " + cadena2[cadena2.length - 1]);

            if (cadena1 === cadena2) {
                console.log("Las cadenas son iguales");
            } else {
                console.log("Las cadenas son diferentes");
            }

            let subcadena = concatenacion.substring(5, 10); // Extrae "Mundo"
            console.log("Subcadena: " + subcadena);

            let buscar = "Mundo";
            let posicion = concatenacion.indexOf(buscar);
            if (posicion !== -1) {
                console.log("La cadena '" + buscar + "' fue encontrada en la posición " + posicion);
            } else {
                console.log("La cadena '" + buscar + "' no fue encontrada");
            }

            concatenacion = concatenacion.replace("Mundo", "Universo");
            console.log("Después de reemplazar 'Mundo' por 'Universo': " + concatenacion);

            // Cerrar la interfaz readline
            rl.close();
        });
    });
}

// Ejecutar la función principal
main();
