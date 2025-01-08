// Por valor (inmutables)
let number = 42;
let string = "Hola mundo!";
let boolean = true;

// Por referencia (mutables)
let myList = [1, 2, 3];
let myDict = { Nombre: "Juan", Apellido: "Herrera" };

// Función con parámetros "por valor"
function elevateValue(value, n) {
    value **= n;
    console.log(value);
}

console.log(number);
elevateValue(number, 2);
console.log(number);

// Función con parámetros "por referencia"
function elevateValues(container, n) {
    for (let index = 0; index < container.length; index++) {
        container[index] = container[index] ** n;
    }
    console.log(container);
}

console.log(myList);
elevateValues(myList, 2);
console.log(myList);

console.log("-----------------------------------------");

/*
 * DIFICULTAD EXTRA (opcional):
 */

function areValuesEqual(original1, original2, new1, new2) {
    return original1 === new1 && original2 === new2;
}

function swapByValue(param1, param2) {
    let temp = param1;
    param1 = param2;
    param2 = temp;
    return [param1, param2];
}

let value1 = "Juan";
let value2 = "David";

console.log(value1, value2);
let [value3, value4] = swapByValue(value1, value2);
console.log(value1, value2);
console.log(value3, value4);
console.log(
    "El valor de las variables originales fue invertido:",
    areValuesEqual(value1, value2, value3, value4)
);
console.log("---------------------------");

function swapByReference(param1, param2) {
    if (param1.length === param2.length) {
        for (let index = 0; index < param1.length; index++) {
            let temp = param1[index];
            param1[index] = param2[index];
            param2[index] = temp;
        }
    }
    return [param1, param2];
}

value5 = ["Juan", "David"];
value6 = ["Herrera", "Parra"];

console.log(value5, value6);
let [value7, value8] = swapByReference(value5, value6);
console.log(value5, value6);
console.log(value7, value8);
console.log(
    "El valor de las variables originales fue invertido:",
    areValuesEqual(value5, value6, value7, value8)
);