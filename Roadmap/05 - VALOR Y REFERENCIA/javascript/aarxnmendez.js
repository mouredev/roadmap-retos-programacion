// Ejemplo de asignación por valor
let numeroA = 10;
let numeroB = numeroA; // numeroB es una copia del valor de numeroA
numeroB = 20;
console.log(numeroA); // 10
console.log(numeroB); // 20

// Ejemplo de asignación por referencia
let objeto1 = { nombre: "Alicia" };
let objeto2 = objeto1; // objeto2 es una referencia a objeto1
objeto2.nombre = "Roberto";
console.log(objeto1.nombre); // "Roberto"
console.log(objeto2.nombre); // "Roberto"

// Función con parámetro por valor
function modificarValor(x) {
    x = 20;
    console.log("Dentro de la función:", x); // 20
}

let numero = 10;
modificarValor(numero);
console.log("Fuera de la función:", numero); // 10

// Función con parámetro por referencia
function modificarObjeto(obj) {
    obj.nombre = "Carlos";
    console.log("Dentro de la función:", obj.nombre); // "Carlos"
}

let persona = { nombre: "Alicia" };
modificarObjeto(persona);
console.log("Fuera de la función:", persona.nombre); // "Carlos"

// Ejercicio Extra: Intercambio por valor
function intercambiarPorValor(x, y) {
    let temp = x;
    x = y;
    y = temp;
    return [x, y];
}

let valor1 = 1;
let valor2 = 2;
let [nuevoValor1, nuevoValor2] = intercambiarPorValor(valor1, valor2);
console.log("Valores originales:", valor1, valor2); // 1, 2
console.log("Valores intercambiados:", nuevoValor1, nuevoValor2); // 2, 1

// Ejercicio Extra: Intercambio por referencia
function intercambiarPorReferencia(obj1, obj2) {
    let temp = obj1.valor;
    obj1.valor = obj2.valor;
    obj2.valor = temp;
}

let referencia1 = { valor: 1 };
let referencia2 = { valor: 2 };
intercambiarPorReferencia(referencia1, referencia2);
console.log("Valores originales:", referencia1.valor, referencia2.valor); // 2, 1