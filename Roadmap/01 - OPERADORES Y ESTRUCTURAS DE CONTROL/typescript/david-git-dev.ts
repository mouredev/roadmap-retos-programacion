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
// Operadores Aritméticos
let suma = 5 + 2;        // Suma (+)
console.log(suma);
let resta = 5 - 2;       // Resta (-)
console.log(resta);
let multiplicacion = 5 * 2; // Multiplicación (*)
console.log(multiplicacion);
let division = 5 / 2;    // División (/)
console.log(division);
let modulo = 5 % 2;      // Resto o Módulo (%)
console.log(modulo);
let incremento = 1;    // Incremento (++x o x++)
console.log(incremento++,++incremento);
let decremento = 1;    // Decremento (--x o x--)
console.log(decremento--,--decremento);

// Operadores de Asignación

let x = 5;              // Asignación (=)
console.log(x)
x += 2;                 // Asignación de Suma (+=)
console.log(x)
x -= 2;                 // Asignación de Resta (-=)
console.log(x)
x *= 2;                 // Asignación de Multiplicación (*=)
console.log(x)
x /= 2;                 // Asignación de División (/=)
console.log(x)
x %= 2;                 // Asignación de Módulo (%=)
console.log(x)
x **= 2;                // Asignación de Exponenciación (**=)
console.log(x)
// Operadores de Comparación

let igual = (5 == "5");       // Igualdad Débil (==)
console.log(igual);
let estrictamenteIgual = (5 === "5"); // Igualdad Estricta (===)
console.log(estrictamenteIgual);
let diferente = (5 != "5");    // Desigualdad Débil (!=)
console.log(diferente);
let estrictamenteDiferente = (5 !== "5"); // Desigualdad Estricta (!==)
console.log(estrictamenteDiferente);
let mayor = (5 > 2);           // Mayor que (>)
console.log(mayor);
let menor = (5 < 2);           // Menor que (<)
console.log(menor);
let mayorOIgual = (5 >= 2);    // Mayor o igual que (>=)
console.log(mayorOIgual);
let menorOIgual = (5 <= 2);    // Menor o igual que (<=)
console.log(menorOIgual);
// Operadores Lógicos
let and = (true && false);     // Y Lógico (&&)
console.log(and)
let or = (true || false);      // O Lógico (||)
console.log(or)
let not = !true;               // No Lógico (!)
console.log(not)

// Operadores de Bit a Bit
let bitAnd = (5 & 1);          // AND a nivel de bits (&)
console.log(bitAnd);
let bitOr = (5 | 1);           // OR a nivel de bits (|)
console.log(bitOr);
let bitXor = (5 ^ 1);          // XOR a nivel de bits (^)
console.log(bitXor);
let bitNot = ~5;               // NOT a nivel de bits (~)
console.log(bitNot);
let desplazarIzquierda = (5 << 1);  // Desplazamiento a la izquierda (<<)
console.log(desplazarIzquierda);
let desplazarDerecha = (5 >> 1);    // Desplazamiento a la derecha (>>)
console.log(desplazarDerecha);
let desplazarDerechaConCero = (5 >>> 1); // Desplazamiento a la derecha con relleno de ceros (>>>)
console.log(desplazarDerechaConCero);

// Operadores Ternarios
let ternario = (5 > 2) ? "Mayor" : "Menor"; // Operador Ternario (condicion ? valor1 : valor2)
console.log(ternario)

// Operadores de Tipo
let tipo = typeof 5;        // Operador de Tipo (typeof)
let esInstancia = ({} instanceof Object); // Operador instanceof
const obj ={
    propiedad:{subprop:undefined},
    variable:null
}
// Operador de Encadenamiento Opcional
let valor = obj.propiedad?.subprop;  // Encadenamiento opcional (?.)
console.log(valor)
// Operador Nullish Coalescing
let valorDefinido = obj.variable ?? "Valor por defecto";  // Nullish Coalescing (??)
// Estructuras de Control de Flujo
console.log(valorDefinido);

// if...else
let xx = 10;
if (xx > 5) {
    console.log("x es mayor que 5");
} else if (xx === 5) {
    console.log("x es igual a 5");
} else {
    console.log("x es menor que 5");
}

// switch
let color = "rojo";
switch (color) {
    case "rojo":
        console.log("El color es rojo");
        break;
    case "azul":
        console.log("El color es azul");
        break;
    default:
        console.log("Color no reconocido");
}

// Operador Ternario (condición ? valor1 : valor2)
let edad = 18;
let mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
console.log(mensaje);

// Estructuras de Control de Bucles (Loops)

// for
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// for...of (para iterar sobre iterables como arrays)
let array = [1, 2, 3, 4];
for (let valor of array) {
    console.log(valor);
}

// for...in (para iterar sobre propiedades enumerables de un objeto)
let objeto = { nombre: "Juan", edad: 25 };
for (let propiedad in objeto) {
    console.log(`${propiedad}: ${objeto[propiedad]}`);
}

// while
let contador = 0;
while (contador < 5) {
    console.log(contador);
    contador++;
}

// do...while
let num = 0;
do {
    console.log(num);
    num++;
} while (num < 5);

// Estructura de Control para Excepciones

// try...catch...finally
try {
    let resultado = 10 / 0;  // Posible error
    console.log(resultado);
} catch (error) {
    console.log("Ocurrió un error: " + error.message);
} finally {
    console.log("Esto se ejecuta siempre");
}

// break
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;  // Rompe el bucle si i es igual a 5
    }
    console.log(i);
}

// continue
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        continue;  // Salta el resto del código en la iteración actual si i es igual a 5
    }
    console.log(i);
}

// Estructura de Control asincrónica

// async...await (para manejar promesas de forma síncrona)
async function obtenerDatos() {
    try {
        let respuesta = await fetch('https://api.example.com/datos');
        let datos = await respuesta.json();
        console.log(datos);
    } catch (error) {
        console.log("Error al obtener los datos: " + error.message);
    }
}
//reto extra
/* * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo. */
function numbersTentoFifhtty(){
    const final = 55;
    let start = 10;
    while(start<=55){
        start++;
        console.log(start%2===0&&start!==16&&start%3!==0?start:'');
    }
}
