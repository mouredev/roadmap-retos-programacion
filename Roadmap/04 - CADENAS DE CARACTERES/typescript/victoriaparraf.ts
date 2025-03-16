//Acceso a caracteres especificos
let cadena: string = "Hola, mundo";
console.log(cadena[0]); // "H"
console.log(cadena.charAt(1)); // "o"

//Longitud
let longitud: number = cadena.length;
console.log(longitud); // 11

//Concatenacion
let cadena1: string = "Hola, ";
let cadena2: string = "mundo";
let concatenado: string = cadena1 + cadena2;
console.log(concatenado); // "Hola, mundo"

let concatenado2: string = cadena1.concat(cadena2);
console.log(concatenado2); // "Hola, mundo"

//Subcadenas
let subcadena1: string = cadena.slice(0, 4);
console.log(subcadena1); // "Hola"

let subcadena2: string = cadena.substring(5, 10);
console.log(subcadena2); // "mundo"

let subcadena3: string = cadena.substr(5, 5);
console.log(subcadena3); // "mundo"

//Repeticion
let repetida: string = "abc".repeat(3);
console.log(repetida); // "abcabcabc"

//Conversión a Mayúsculas y Minúsculas
let mayusculas: string = cadena.toUpperCase();
console.log(mayusculas); // "HOLA, MUNDO"

let minusculas: string = cadena.toLowerCase();
console.log(minusculas); // "hola, mundo"

//Reemplazo
let reemplazada: string = cadena.replace("mundo", "TypeScript");
console.log(reemplazada); // "Hola, TypeScript"

//Division
let partes: string[] = cadena.split(", ");
console.log(partes); // ["Hola", "mundo"]

//Union
let unidas: string = partes.join(" - ");
console.log(unidas); // "Hola - mundo"

//Interpolacion
let nombre: string = "Victoria";
let edad: number = 23;
let saludo: string = `Hola, mi nombre es ${nombre} y tengo ${edad} años`;
console.log(saludo);

//Verificacion de subcadena
let contiene: boolean = cadena.includes("mundo");
console.log(contiene); // true

let empieza: boolean = cadena.startsWith("Hola");
console.log(empieza); // true

let termina: boolean = cadena.endsWith("mundo");
console.log(termina); // true


/***********************************************/
/*EXTRA */

//Funcion para saber si es palindromo
function esPalindromo(palabra: string): boolean {
    let palabraInvertida = palabra.split('').reverse().join('');
    return palabra === palabraInvertida;
}
//Funcion para saber si es una anagrama
function sonAnagramas(palabra1: string, palabra2: string): boolean {
    let ordenarPalabra = (palabra: string) => palabra.toLowerCase().split('').sort().join('');
    return ordenarPalabra(palabra1) === ordenarPalabra(palabra2);
}
//Funcion para comprobar si es isograma
function esIsograma(palabra: string): boolean {
    let letras = new Set();
    for (let letra of palabra.toLowerCase()) {
        if (letras.has(letra)) {
            return false;
        }
        letras.add(letra);
    }
    return true;
}
//Funcion principal

function analizarPalabras(palabra1: string, palabra2: string): void {
    console.log(`Palabra 1: ${palabra1}`);
    console.log(`Palabra 2: ${palabra2}`);
    
    console.log(`"${palabra1}" es palíndromo: ${esPalindromo(palabra1)}`);
    console.log(`"${palabra2}" es palíndromo: ${esPalindromo(palabra2)}`);
    
    console.log(`"${palabra1}" y "${palabra2}" son anagramas: ${sonAnagramas(palabra1, palabra2)}`);
    
    console.log(`"${palabra1}" es isograma: ${esIsograma(palabra1)}`);
    console.log(`"${palabra2}" es isograma: ${esIsograma(palabra2)}`);
}

// Ejemplo de uso
let palabra1 = "amor";
let palabra2 = "roma";
analizarPalabras(palabra1, palabra2);

