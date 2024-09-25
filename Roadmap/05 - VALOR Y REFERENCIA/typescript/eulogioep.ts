// Función para imprimir resultados
function print(message: string): void {
    console.log(message);
}

// Ejemplos de asignación por valor (tipos primitivos)
let a: number = 5;
let b: number = a; // b es una copia del valor de a
b = 10; // Cambiar b no afecta a a
print(`Asignación por valor: a: ${a}, b: ${b}`); // a: 5, b: 10

// Ejemplos de asignación por referencia (objetos y arrays)
let arr1: number[] = [1, 2, 3];
let arr2: number[] = arr1; // arr2 apunta al mismo array que arr1
arr2[0] = 100; // Cambiar arr2 afecta a arr1
print(`Asignación por referencia: arr1[0]: ${arr1[0]}, arr2[0]: ${arr2[0]}`); // arr1[0]: 100, arr2[0]: 100

// Función con parámetro por valor
function modificarValor(n: number): void {
    n = 100; // Este cambio no afecta a la variable original
}

let x: number = 5;
modificarValor(x);
print(`x después de modificarValor: ${x}`); // x no cambia

// Función con parámetro por referencia
function modificarReferencia(arr: number[]): void {
    arr[0] = 100; // Este cambio afecta al array original
}

let array: number[] = [1, 2, 3];
modificarReferencia(array);
print(`array[0] después de modificarReferencia: ${array[0]}`); // array[0] cambia

// DIFICULTAD EXTRA
// Función para intercambio por valor
function intercambioPorValor(a: number, b: number): [number, number] {
    let temp: number = a;
    a = b;
    b = temp;
    return [a, b];
}

// Interfaz para el objeto de intercambio por referencia
interface IntercambioObj {
    a: number;
    b: number;
}

// Función para intercambio por referencia
function intercambioPorReferencia(obj: IntercambioObj): IntercambioObj {
    let temp: number = obj.a;
    obj.a = obj.b;
    obj.b = temp;
    return { a: obj.a, b: obj.b };
}

// Programa 1: Intercambio por valor
let num1: number = 10, num2: number = 20;
print(`Antes del intercambio por valor: num1 = ${num1}, num2 = ${num2}`);
let [nuevoNum1, nuevoNum2] = intercambioPorValor(num1, num2);
print("Después del intercambio por valor:");
print(`Variables originales: num1 = ${num1}, num2 = ${num2}`);
print(`Nuevas variables: nuevoNum1 = ${nuevoNum1}, nuevoNum2 = ${nuevoNum2}`);

// Programa 2: Intercambio por referencia
let obj: IntercambioObj = { a: 30, b: 40 };
print(`\nAntes del intercambio por referencia: obj.a = ${obj.a}, obj.b = ${obj.b}`);
let nuevoObj: IntercambioObj = intercambioPorReferencia(obj);
print("Después del intercambio por referencia:");
print(`Objeto original: obj.a = ${obj.a}, obj.b = ${obj.b}`);
print(`Nuevo objeto: nuevoObj.a = ${nuevoObj.a}, nuevoObj.b = ${nuevoObj.b}`);