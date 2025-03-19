
// Operadores Aritméticos
let suma: number = 2 + 4;
let resta: number = 2 - 4;
let multiplicar: number = 2 * 4;
let division: number = 2 / 4;

console.log("Operadores Aritméticos");
console.log("Resultado de la suma ", suma);
console.log("Resultado de  la resta ", resta);
console.log("Resultado de  la multiplicación ", multiplicar);
console.log("Resultado de  la división ", division);

console.log("---------------------------------------------------------------------")

// Operadores Lógicos
const logicoY: boolean = false && true;
const logicoO: boolean = false || true;
const logicoNot: boolean = !false;

console.log("Operadores Lógicos");
console.log("Resultado && ", logicoY);
console.log("Resultado || ", logicoO);
console.log("Resultado Not ", logicoNot);

console.log("---------------------------------------------------------------------")

// Operadores de comparación
// El operador < y <= devuelve true cuando el 1 valor es menor al 2 valor. valor: 1 - valor: 2.
let comparacionMenor: boolean = 1 < 2;
let comparacionMenorIgual: boolean = 1 <= 2;

// El operador < y <= devuelve true cuando el 1 valor es mayor al 2 valor. valor: 3 - valor: 2.
let comparacionMayor: boolean = 3 > 2;
let comparacionMayorIgual: boolean = 3 >= 2;

// El operador ==  devuelve true cuando el 1 valor es igual al 2 valor. valor: 4 - valor: 4.
let comparacionIgual: boolean = 4 == 4;

// El operador ===  devuelve true cuando el 1 valor es estrictamente igual al 2 valor. valor: 5 - valor: 5.
let comparacionIgualIgual: boolean = '5' === '5';

console.log("Operadores Comparaciones");
console.log("Operador < ", comparacionMenor);
console.log("Operador <= ", comparacionMenorIgual);
console.log("Operador > ", comparacionMayor);
console.log("Operador >= ", comparacionMayorIgual);
console.log("Operador == ", comparacionIgual);
console.log("Operador === ", comparacionIgualIgual);

console.log("---------------------------------------------------------------------");

// Operadores de asignación
let asignarTexto: string = '';
console.log("Variable Texto", asignarTexto);

asignarTexto = "Aprendiendo TS.";
console.log(`Asignando texto a la variable vacia ${asignarTexto}`)

console.log("---------------------------------------------------------------------");

// Operadores de Identidad
// No tengo conocimiento si estos existe en TS.

// Estructuras de control

// Condicionales
let numeroUno: number = 2;
let numeroDos: number = 3;
if (2 > 4) {
    console.log(`El valor ${numeroUno} es mayor al valor ${numeroDos}`)
} else {
    console.log(`El valor ${numeroUno} es menor al valor ${numeroDos}`)
}

// Iterativas
for (let ite = 0; ite < numeroDos; ite++) {
    console.log("Iterando :", ite)
}

console.log("---------------------------------------------------------------------");

// Reto Opcional
// Crear un programa que imprima por consola todos los números comprendidos - entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
console.log("Dificulta Extra")
for (let numeros = 10; numeros <= 55; numeros++) {
    if (numeros % 2 === 0 && numeros !== 16 && numeros % 3 !== 0) {
        console.log(numeros)
    }
}