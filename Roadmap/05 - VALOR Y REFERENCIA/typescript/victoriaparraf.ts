//Asignacion por valor
let a: number = 5;
let b: number = a; // Asignación por valor
console.log(a); // 5
console.log(b); // 5
b = 10;
console.log(a); // 5 (no cambia)
console.log(b); // 10

let str1: string = "Hola";
let str2: string = str1; // Asignación por valor
console.log(str1); // "Hola"
console.log(str2); // "Hola"
str2 = "Adiós";
console.log(str1); // "Hola" (no cambia)
console.log(str2); // "Adiós"

//Asignacion por referencia
let obj1 = { nombre: "Alice" };
let obj2 = obj1; // Asignación por referencia
console.log(obj1); // { nombre: "Alice" }
console.log(obj2); // { nombre: "Alice" }
obj2.nombre = "Bob";
console.log(obj1); // { nombre: "Bob" } (cambia también)
console.log(obj2); // { nombre: "Bob" }

let arr1: number[] = [1, 2, 3];
let arr2: number[] = arr1; // Asignación por referencia
console.log(arr1); // [1, 2, 3]
console.log(arr2); // [1, 2, 3]
arr2.push(4);
console.log(arr1); // [1, 2, 3, 4] (cambia también)
console.log(arr2); // [1, 2, 3, 4]

//Paso de parametros por valor
function incrementarPorValor(x: number): void {
    x += 1;
    console.log(`Dentro de la función: x = ${x}`);
}
let aa: number = 10;
console.log(`Antes de la función: a = ${aa}`); // 10
incrementarPorValor(aa); // Dentro de la función: x = 11
console.log(`Después de la función: a = ${aa}`); // 10

function cambiarCadena(cadena: string): void {
    cadena = "Nueva cadena";
    console.log(`Dentro de la función: cadena = ${cadena}`);
}
let saludo: string = "Hola";
console.log(`Antes de la función: saludo = ${saludo}`); // "Hola"
cambiarCadena(saludo); // Dentro de la función: cadena = "Nueva cadena"
console.log(`Después de la función: saludo = ${saludo}`); // "Hola"

//Paso de parametros por referencia
function cambiarObjeto(obj: { valor: number }): void {
    obj.valor += 10;
    console.log(`Dentro de la función: obj.valor = ${obj.valor}`);
}
let miObjeto = { valor: 20 };
console.log(`Antes de la función: miObjeto.valor = ${miObjeto.valor}`); // 20
cambiarObjeto(miObjeto); // Dentro de la función: obj.valor = 30
console.log(`Después de la función: miObjeto.valor = ${miObjeto.valor}`); // 30

function agregarElemento(arr: number[]): void {
    arr.push(4);
    console.log(`Dentro de la función: arr = ${arr}`);
}
let miArray: number[] = [1, 2, 3];
console.log(`Antes de la función: miArray = ${miArray}`); // [1, 2, 3]
agregarElemento(miArray); // Dentro de la función: arr = [1, 2, 3, 4]
console.log(`Después de la función: miArray = ${miArray}`); // [1, 2, 3, 4]


