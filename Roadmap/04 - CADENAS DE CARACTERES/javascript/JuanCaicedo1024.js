/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 */

//acceso a caracteres
var str = "Hola mundo";

str.charAt(0); // retorna H
str[0]; //retorna H

//Subcadenas

str.slice([0, 2]); // Hol
str.substring(0, 4); //Hola

// Longitud de la cadena
str.length; //10

//concatenacion
let saludo = "Hola";
let destino = "mundo";

console.log(saludo + " " + destino); //Hola mundo
console.log(`${saludo} ${destino}`); // Hola mundo

//repeticion
"JS".repeat(5); // JS JS JS JS JS

//Recorrido de una cadena
for (let i of str) {
  console.log(i);
} // H O L A M U N D O

//Conversión a mayúsculas y minúsculas
str.toUpperCase; // MAYUSCULAS
str.toLowerCase; // minuscula

// Reemplazo de texto

str.replace("mundo", "JavaScript"); // Hola JavaScript

//División de una cadena en un array

let palabras = str.split(" ", 1); //Hola

// Unión de un array en una cadena
console.log(str.split("").join("-")); //el split convierte la string en un array pars que la funcion join les inserte "-"

//Verificación de contenido

str.includes("Hola"); // la variable str incluye Hola? dara como resultado un true
str.startsWith("Mundo"); // la varaibale str no empieza con la palabra Mundo tonces resultado sera false
str.endsWith("Mundo"); // la varaibe str si finaliza con la palabra mundo tonces resultara true

//  Eliminación de espacios en blanco
let strConEspacios = "   Espacios   ";
console.log(strConEspacios.trim()); // "Espacios"
console.log(strConEspacios.trimStart()); // "Espacios   "
console.log(strConEspacios.trimEnd()); // "   Espacios"

//De numero a string
let num1 = 10;
let cadena = num1.toString();

//Conversión de cadena a número
let str = "123";
console.log(parseInt(cadenaNumero)); // 123 entero
console.log(parseFloat("123.45")); // 123.45 decimal

//comparacion

console.log("a" === "A"); //devolvera false

//Reversión de una cadena

console.log(str.split("").reverse().join("")); //o d n u m   a l o H

/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

let palabra1 = "xdssd"
let palabra2 = "xdddd"


function palindromos(){
    let reversa1 = palabra1.toLowerCase().split("").reverse().join("")
    let reversa2 = palabra2.toLowerCase().split("").reverse().join("")
    
    if (reversa1 === palabra1.toLowerCase()){
        console.log(`las palabras ${palabra1} si es palindromos`)
    } 
    
    if(reversa2 === palabra2.toLowerCase()){
        console.log(`la palabra ${palabra2} si es palindromos` )
    }
        else {
        console.log("no es palindromo")
    }
    
    
}

palindromos()


function Anagramas (){
    let Anagramas1 = palabra1.toLowerCase().split("").sort().join("")
    let Anagramas2 = palabra2.toLowerCase().split("").sort().join("")

    if (Anagramas1 === Anagramas2){
        console.log(`las palabras ${palabra1, palabra2} son anagramas`)
    } else {
        console.log("No son anagramas")
    }
}

Anagramas()

function Isogramas() {
    let Isograma1 = palabra1.toLowerCase().split("");
    let letras = new Set();

    for (let letra of Isograma1) {
        if (letras.has(letra)) { 
            return "No es un isograma";
        }
        letras.add(letra); 
    }

    return "Es un isograma"; 
}
