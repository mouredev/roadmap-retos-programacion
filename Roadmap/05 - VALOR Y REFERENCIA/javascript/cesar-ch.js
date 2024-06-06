// #05 VALOR Y REFERENCIA

// Asignación de variables por valor
let a = 10;
let b = a;

a = 5;

console.log(a); // 5
console.log(b); // 10

// Asignación de variables por referencia
let x = { a: 10, b: 5 };
let y = x;

x.a = 12;
x.b = 24;

console.log(x); // { a: 12, b: 24 }
console.log(y); // { a: 12, b: 24 }

// Función con parámetro por valor
function cambiarValor(numero) {
    numero = 100;
    console.log(numero); // 100
}

let numero = 5;
cambiarValor(numero);

console.log(numero); // 5

// Función con parámetro por referencia
function cambiarReferencia(objeto) {
    objeto.a = 100;
    console.log(objeto); // { a: 100 }
}

let objeto = { a: 5 };
cambiarReferencia(objeto);

console.log(objeto); // { a: 100 }

// Ejemplo que intercambia los valores de dos variables por valor
function intercambiarValores(c, d) {
    let temp = c;
    c = d;
    d = temp;

    return [c, d];
}

// Ejemplo que intercambia los valores de dos variables por referencia
function intercambiarReferencias(obj1, obj2) {
    let temp = { ...obj1 };
    let temp2 = { ...obj2 }
    let temp3 = temp.value
    temp.value = temp2.value
    temp2.value = temp3
    return [temp, temp2];
}


let c = 10;
let d = 5;
let e = 10;
let objA = { value: 10 };
let objB = { value: 5 };

let [newc, newd] = intercambiarValores(c, d);
console.log("Valores iniciales:", c, d) // 10 5
console.log("Valores por valor:", newc, newd); // 5 10


let [newObjA, newObjB] = intercambiarReferencias(objA, objB);
console.log("Valores iniciales:", objA, objB) // { value: 10 } { value: 5 }
console.log("Valores por referencia:", newObjA, newObjB); // { value: 5 } { value: 10 }
