/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

//
// Asignar por valor
//

let a = 8
let b = 10

console.log(a)
console.log(b)

//
// Por Referencia 
//

b = 20
let obj1 = { name: "Gian", age: 20}
let obj2 = obj1

obj2.name = "David"

console.log(b)
console.log(obj1)
console.log(obj2)

//
// Cambiar valor por medio de una Funcion 
//

function changeValor(num){
    return num + 4
}

console.log(changeValor(4))

//
// Cambiar un valor por referencia por medio de una funcion 
//

function changeName(obj,name){
    obj.name = name
    return obj 
}

console.log(changeName(obj2,"Jean"))

//
// EXTRA
//

let num1 = 4
let num2 = 8

function invertPos (num1, num2){
    tem1 = num2
    tem2 = num1
    return [tem1,tem2]
}

let [num3, num4] = invertPos(num1,num2)

console.log(`Originales: num1 = ${num1}, num2 = ${num2}`);
console.log(`Nuevos: num3 = ${num3}, num4 = ${num4}`);

let per1 = { name: "Juan", age: 26 };
let per2 = { name: "Fran", age: 26 };

function invertName(obj1, obj2) {
    let temObj1 = { ...obj1 };
    let temObj2 = { ...obj2 };

    let tem = temObj1.name;
    temObj1.name = temObj2.name;
    temObj2.name = tem;

    return [temObj1, temObj2];
}

let [per3, per4] = invertName(per1, per2);

console.log(`Originales: per1 = ${per1.name}, per2 = ${per2.name}`);
console.log(`Nuevos: per3 = ${per3.name}, per4 = ${per4.name}`);