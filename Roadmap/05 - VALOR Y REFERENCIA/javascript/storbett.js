// Tipos de datos por valor

let myIntA = 10;
let myIntB = myIntA;
myIntA = 30;
console.log(myIntA); // 30
console.log(myIntB); // 10

// Tipos de datos por referencia

let myListA = [10, 20];
let myListB = myListA;
myListB.push(30);
console.log(myListA); // [10, 20, 30]
console.log(myListB); // [10, 20, 30]

// Funciones por datos por valor
let myIntC = 10;

function myIntFunc(myInt) {
    myInt = 20;
    console.log(myInt); // 20
}

myIntFunc(myIntC);
console.log(myIntC); // 10

// Funciones de datos por referencia

function myListFunc(myList) {
    let myListE = myList;
    myList.push(30);
    let myListD = myListE;
    myListD.push(40);

    console.log(myList); // [10, 20, 30, 40]
    console.log(myListD); // [10, 20, 30, 40]
}

let myListC = [10, 20];
myListFunc(myListC);
console.log(myListC); // [10, 20, 30, 40]

// Buscar mecanismo de copiado

// EXTRA

function value(valueA, valueB) {
    let temp = valueA;
    valueA = valueB;
    valueB = temp;
    return [valueA, valueB];
}

let myIntD = 10;
let myIntE = 20;
let [myIntF, myIntG] = value(myIntD, myIntE);

console.log(`${myIntD}, ${myIntE}`); // 10, 20
console.log(`${myIntF}, ${myIntG}`); // 20, 10

// Referencia

function ref(valueA, valueB) {
    let temp = valueA;
    valueA = valueB;
    valueB = temp;
    return [valueA, valueB];
}

let myListE = [10, 20];
let myListF = [30, 40];
let [myListG, myListH] = ref(myListE, myListF);

console.log(`${myListE}, ${myListF}`); // [10, 20], [30, 40]
console.log(`${myListG}, ${myListH}`); // [30, 40], [10, 20]
