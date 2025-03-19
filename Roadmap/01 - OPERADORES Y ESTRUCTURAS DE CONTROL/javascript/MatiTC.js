//Operadores de Js

//Aritméticos
let a = 7;
let b = 3;
console.log(a + b); //suma. 7 + 3 = 10
console.log(a - b); //resta. 7 - 3 = 4
console.log(a * b); //multiplicación. 7 * 3 = 21
console.log(a / b); //division. 7 / 3 = 2.33333335
console.log(a % b); //modulo. 7 % 3 = 1
console.log(++a); // incremento. 7 + 1 = 8 
console.log(--b); // decremento. 3 - 1 = 2

//Comparación (==)
let x = 10
let y = "10" 
console.log(x == y);  // 10 == "10" true (coerción de tipo)
console.log(x === y); // 10 == "10" false (sin coerción de tipo)
console.log(x != y);  // 10 != "10" false (coerción de tipo)
console.log(x !== y); // 10 != "10" true (sin coerción de tipo)
console.log(x > 5); // true
console.log(y < 5); // false

//Lógicos AND(&&) OR(||) NOT(!)
let p = true;
let q = false;
console.log(p && q); // false (y lógico)
console.log(p || q); // true (o lógico)
console.log(!p);     // false (no lógico)

//Asignación 
let num = 10; //equivalente x = y
num += 5; // equivalente a num = num + 5;
num -= 3; // equivalente a num = num - 3;
num *= 2; // equivalente a num = num * 2;
num /= 4; // equivalente a num = num / 4;
num **= 4; // equivalente a num = num ** 4;
num %= 2; // equivalente a num = num % 2;
console.log(num);

//Identidad
let m = 10;
let n = "10";
console.log(m == n); // true (comparación estricta)
console.log(m != n); // false (comparación estricta)
console.log(m === n); // false (comparación estricta)
console.log(m !== n); // true (comparación estricta)

//Pertenencia
let obj = { prop: "valor" }; //Objeto(Estructura de datos que agrupa propiedades y métodos)
console.log("prop" in obj); // true (verifica si la propiedad está en el objeto)

//Operadores a nivel de bits(Esto si lo copie)
let c = 5;   // Representación binaria: 0101
let d = 3;   // Representación binaria: 0011

console.log(c & d);  // 1 (AND a nivel de bits: 0101 & 0011 = 0001)
console.log(c | d);  // 7 (OR a nivel de bits: 0101 | 0011 = 0111)
console.log(c ^ d);  // 6 (XOR a nivel de bits: 0101 ^ 0011 = 0110)
console.log(~c);     // -6 (NOT a nivel de bits: ~0101 = 1010, considerando el complemento a 2)
console.log(c << 1); // 10 (desplazamiento a la izquierda: 0101 << 1 = 1010)
console.log(d >> 1); // 1  (desplazamiento a la derecha con signo: 0011 >> 1 = 0001)
console.log(d >>> 1);// 1  (desplazamiento a la derecha sin signo: 0011 >>> 1 = 0001)

/* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 * que representen todos los tipos de estructuras de control que existan
 * en tu lenguaje:
*/

console.log(`.........................................`)
//Condicionales (if-else):

let miEdad = 24;
let tuEdad = 31;

if (miEdad > tuEdad){
    console.log(`Si soy mayor ${miEdad}`)
}else{
    console.log(`No, soy soy menor que tu. Tengo ${miEdad}`)
}

if (miEdad > tuEdad){
    console.log(`Si soy mayor ${miEdad}`)
}else if ( miEdad == tuEdad){
    console.log(`Tenemos la misma edad, yo tengo ${miEdad} y tu también tienes ${tuEdad}`);
} else {
    console.log("Entonces yo soy el menor");
}

console.log(`.........................................`)
//Iterativas 
//For clásico. Interactúa 5 veces
for (let i = 0; i < 5; i++) {
    console.log("Iteración " + (i + 1));
}

console.log(`.........................................`)
//For..in
//Utilizado sobre propiedades de un objeto.
const persona = {
    nombre: "Juan",
    edad: 25,
    ciudad: "Ejemplo"
};

for (let propiedad in persona) {
    console.log(propiedad + ": " + persona[propiedad]);
}

console.log(`.........................................`)


//for...of:
//Utilizado para iterar sobre objetos iterables
const numeros = [1, 2, 3, 4, 5];

for (let numero of numeros) {
    console.log(numero);
}
console.log(`.........................................`)

//forEach
//Método específico de los Arrays 
const colores = ["rojo", "verde", "azul"];

colores.forEach(function(color, indice) {
    console.log("Color en posición " + indice + ": " + color);
});

console.log(`.........................................`)
//Iterativas (while) 
//Comprueba la condición lógica y después ejecuta
let contador = 0;

while (contador < 3) {
    console.log("While " + (contador + 1));
    contador++;
}
console.log(`.........................................`)

////Iterativas (while) 
//Ejecuta el algoritmo y después hace la comprobación
let j = 0;

do {
    console.log("Do While " + (j + 1));
    j++;
} while (j < 2);
console.log(`.........................................`)

//Manejo de Excepciones (try-catch):
function dividirNumeros(a, b) {
    try {
        if (b === 0) {
            throw new Error("No se puede dividir por cero.");
        }
        let resultado = a / b;
        console.log("Resultado: " + resultado);
        return resultado;
    } catch (error) {
        console.error("Error: " + error.message);
    }
}
console.log(dividirNumeros(10, 2)) // Resultado: 5
console.log(dividirNumeros(8, 0)) // Error: No se puede dividir por cero.

console.log(`.........................................`)

//Switch 
let diaDeLaSemana = 3;
let mensaje;

switch (diaDeLaSemana) {
    case 1:
        mensaje = "Lunes";
        break;
    case 2:
        mensaje = "Martes";
        break;
    case 3:
        mensaje = "Miércoles";
        break;
    case 4:
        mensaje = "Jueves";
        break;
    case 5:
        mensaje = "Viernes";
        break;
    case 6:
        mensaje = "Sábado";
        break;
    case 7:
        mensaje = "Domingo";
        break;
    default:
        mensaje = "Día no válido";
}

console.log("Hoy es " + mensaje);

/*
 * EJERCICIO:
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

function imprimirNumerosPares(inicio, fin) {
    for (let i = inicio; i <= fin; i++) {
        if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
            console.log(i);
        }
    }
}

imprimirNumerosPares(10, 55);
