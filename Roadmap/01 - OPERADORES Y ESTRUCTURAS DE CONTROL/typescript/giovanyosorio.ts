/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

//TYPESCRIPT

//Operadores aritmeticos
console.log("Operadores aritmeticos");
let a : number= 5;
let b :number = 2;
let c : number= 3;

console.log("Suma: " + (a + b));
console.log("Resta: " + (a - b));
console.log("Multiplicacion: " + (a * b));
console.log("Division: " + (a / b));
console.log("Modulo: " + (a % b));
console.log("Incremento: " + (++a));
console.log("Decremento: " + (--a));

//Operadores de comparacion
console.log("Operadores de comparacion");
console.log("Igualdad: " + (a == b));
console.log("Desigualdad: " + (a != b));
console.log("Mayor que: " + (a > b));
console.log("Menor que: " + (a < b));
console.log("Mayor o igual que: " + (a >= b));
console.log("Menor o igual que: " + (a <= b));

//Operadores logicos
console.log("Operadores logicos");
console.log("AND: " + (a > b && b > c));
console.log("OR: " + (a > b || b > c));
console.log("NOT: " + !(a > b));

//Operadores de asignacion
console.log("Operadores de asignacion");
console.log("Asignacion: " + (a = b));
console.log("Suma y asignacion: " + (a += b));
console.log("Resta y asignacion: " + (a -= b));
console.log("Multiplicacion y asignacion: " + (a *= b));
console.log("Division y asignacion: " + (a /= b));
console.log("Modulo y asignacion: " + (a %= b));

//Operadores de identidad
console.log("Operadores de identidad");
console.log("Identidad: " + (a === b));
console.log("No identidad: " + (a !== b));

//Operadores de pertenencia
console.log("Operadores de pertenencia");
let d : string = "Hola mundo";
console.log("Incluye: " + d.includes("Hola"));
console.log("Empieza con: " + d.startsWith("Hola"));
console.log("Termina con: " + d.endsWith("mundo"));

//Operadores de bits
console.log("Operadores de bits");
console.log("AND: " + (a & b));
console.log("OR: " + (a | b));
console.log("XOR: " + (a ^ b));
console.log("Desplazamiento a la izquierda: " + (a << b));
console.log("Desplazamiento a la derecha: " + (a >> b));
console.log("Desplazamiento a la derecha sin signo: " + (a >>> b));
console.log("Negacion: " + (~a));

//Estructuras de control
console.log("Estructuras de control");
//Condicionales
console.log("Condicionales");
if(a > b){
    console.log("a es mayor que b");
} else if(a < b){
    console.log("a es menor que b");
}

//Iterativas
console.log("Iterativas");
let i : number = 0;
while(i < 10){
    console.log(i);
    i++;
}

for(let j = 0; j < 10; j++){
    console.log(j);
}

//Excepciones
console.log("Excepciones");
try{
    throw "Error";
} catch(e){
    console.log(e);
}

//Dificultad extra
console.log("Dificultad extra");
for(let k = 10; k <= 55; k++){
    if(k % 2 == 0 && k != 16 && k % 3 != 0){
        console.log(k);
    }
}


