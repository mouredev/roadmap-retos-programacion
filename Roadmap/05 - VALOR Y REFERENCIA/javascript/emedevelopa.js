// Valor y referencia

//Primitivos

let nombre = "León";
let nombre1 = nombre;
nombre += " Pérez";
console.log(nombre);
console.log(nombre1);

let edad = 13;
let edad1 = edad;
edad += " años";
console.log(edad);
console.log(edad1);

//Objetos y Arrays

let myArray = [1, 2, 3];
let myArray2 = myArray;

myArray.push(4);
console.log(myArray);
console.log(myArray2);

let myObject = {nombre: "Marea", edad: 9};
let myObject1 = myObject;

myObject.edad = 12;
console.log(myObject);
console.log(myObject1);

//EXTRA

//Por valor
let comida = "Macarrones";
let comida1 = "Lentejas";

function cambio (param1, param2) {
    let temp = param1;
    param1 = param2;
    param2 = temp;

    return {param1, param2};
}

let resultado = cambio (comida, comida1);
let {param1: nuevoValor1, param2: nuevoValor2} = resultado;

console.log(comida);
console.log(comida1);
console.log(nuevoValor1);
console.log(nuevoValor2);

//Por referencia
let niña1 = { nombre: "Ana", color: "rosa" };
let niña2 = { nombre: "Lucia", color: "Verde" };


function intercambio2(param1, param2) {
    let temp1 = param1;
    param1 = param2;
    param2 = temp1;
    
    return { param1, param2 };
}

let resultado1 = intercambio2(niña1, niña2);

let { param1: nuevoValor3, param2: nuevoValor4 } = resultado1;

    console.log(niña1); 
    console.log(niña2); 
    console.log(nuevoValor3); 
    console.log(nuevoValor4); 