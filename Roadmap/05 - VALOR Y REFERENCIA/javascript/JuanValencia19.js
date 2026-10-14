// DATOS QUE SE PASAN POR VALOR(Primitivos)

// Números
let a = 10;
let b = a;        // b recibe una COPIA del valor de a
b = 20;           // Cambiamos b
console.log(a);   // 10 (✅ a NO cambió)
console.log(b);   // 20

// Strings
let nombre1 = "Ana";
let nombre2 = nombre1;   // Copia
nombre2 = "Carlos";      // Cambiamos la copia
console.log(nombre1);    // "Ana" (✅ original intacto)
console.log(nombre2);    // "Carlos"

//DATOS QUE SE PASAN POR REFERENCIA(objects/arrays)

// Objetos
const persona1 = { nombre: "Ana", edad: 25 };
const persona2 = persona1;   // persona2 APUNTA al mismo objeto (no copia)

persona2.nombre = "Carlos";  // Modificamos a través de persona2
console.log(persona1.nombre); // "Carlos" (⚠️ persona1 también cambió)

// Arrays
const frutas1 = ["manzana", "pera"];
const frutas2 = frutas1;     // frutas2 apunta al MISMO array

frutas2.push("uva");         // Añadimos a través de frutas2
console.log(frutas1);        // ["manzana", "pera", "uva"] (⚠️ frutas1 cambió)

// const no hace que una estructura de datos sea inmutable solo no permita que sea reasigando

const obj1 = { nombre: "Ana" };
const obj2 = obj1;   // ❌ Esto NO crea una copia, solo otra referencia

obj2.nombre = "Carlos";
console.log(obj1.nombre); // "Carlos" (¡cambió el original!)

//Para copiar de verdad una estructura se debe utilizar el spread (...)

// Copia superficial de array
const arr1 = [1, 2, 3];
const arr2 = [...arr1];  // Spread operator crea copia
arr2.push(4);
console.log(arr1); // [1, 2, 3] (✅ original intacto)
console.log(arr2); // [1, 2, 3, 4]

// Copia superficial de objeto
const obj3 = { nombre: "Ana" };
const obj4 = { ...obj3 };  // Spread crea copia
obj4.nombre = "Carlos";
console.log(obj3.nombre); // "Ana" (✅ original intacto)

//Funciones pasando valores primitivos

function cambiarNumero(num) {
    num = 999;  // Solo cambia la COPIA local
    console.log("Dentro de la función:", num); // 999
}

let miNumero = 10;
cambiarNumero(miNumero);
console.log("Fuera de la función:", miNumero); // 10 (✅ no cambió)

// Funciones pasando valores de array/objects

function cambiarObjeto(objeto) {
    objeto.nombre = "Carlos";  // Modifica el objeto ORIGINAL
    console.log("Dentro:", objeto.nombre); // "Carlos"
}

const persona = { nombre: "Ana" };
cambiarObjeto(persona);
console.log("Fuera:", persona.nombre); // "Carlos" (⚠️ ¡cambió!)

//Dificultad extra

//1. Se intercambia los valores primitivos (=)
// Programa 1: Por valor
let valor1 = 10;
let valor2 = 20;

function intercambiarPorValor(a, b) {
    const temp = a;
    a = b;
    b = temp;
    return [a, b];
}

const [nuevoA, nuevoB] = intercambiarPorValor(valor1, valor2);
console.log("Originales:", valor1, valor2);  // 10, 20 (sin cambios)
console.log("Nuevos:", nuevoA, nuevoB);      // 20, 10 (intercambiados)

// Programa 2: Por referencia
const ref1 = { valor: "A" };
const ref2 = { valor: "B" };

function intercambiarPorReferencia(obj1, obj2) {
    const temp = obj1.valor;
    obj1.valor = obj2.valor;
    obj2.valor = temp;
}

intercambiarPorReferencia(ref1, ref2);
console.log("ref1:", ref1.valor); // "B" (cambió)
console.log("ref2:", ref2.valor); // "A" (cambió)