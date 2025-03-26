/* #02 FUNCIONES Y ALCANCE
## Ejercicio
 */

// Funciones baseicas 
// ---- Función sin parametro ni retorno ----
function saludoSimple() {
  console.log("Hola, JavaScript");
}
saludoSimple(); 
// ---- Función con parametro  ----

function saludoConParametro(nombre) {
  console.log(`Hola, ${nombre}!`);
}
saludoConParametro("JavaScript"); 
// ---- Función con retorno ----
function SumarNumeros(a,b) {
    return a + b;
} 
console.log(SumarNumeros(3,5))
// Función dentro de una función
function saludoConFuncionDentro(nombre) {
    function saludoInterno() {
        console.log(`Hola, ${nombre}!`);
    }
    saludoInterno();
}
saludoConFuncionDentro("JavaScript");

// Variable global
let global = "Variable global";

function variableGlobal() {
    console.log(`Hola, ${global}!`);
}
variableGlobal();
// Variable local

function variableLocal() {
    let local = "Variable local";
    console.log(`Hola, ${local}!`);
}
variableLocal();

// Arrow funtion
let arrowFuntion = (num) => {  return num % 2 === 0 ? `El numero ${num} es par` : `El numero ${num} es impar`; }

console.log(arrowFuntion(5)); 


function imprimirNumeros(String1, String2) { 
    let contador = 0
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(String1 + String2);
        } else if (i % 5 === 0) {
            console.log(String2);
        } else if (i % 3 === 0) {
            console.log(String1);
        } else {
            console.log(i)
            contador++
            
        }                  
    }return `El total de numeros impresos es ${contador}`
}

console.log(imprimirNumeros("Buzz", "Frizz"))
