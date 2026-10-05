/*
Valor y referencia
*/

// Tipos de dato por valor

let myIntA = 10
let myIntB = myIntA
myIntB = 20
myIntA = 30

console.log(myIntA)
console.log(myIntB)


// Tipos de dato por referencia

let myListA = [10, 20]
let myListB = myListA
myListB.push(30)
console.log(myListA)
console.log(myListB)

// Funciones con datos por valor

let myIntC = 10

function myIntFunc(myInt) {
    myInt = 20
    console.log(myInt)
}

myIntFunc(myIntC)
console.log(myIntC)

// Funciones con datos por referencia

let myListC = [10, 20]

function myListFunc(myList) {
    let myListE = myList
    myListE.push(30)

    let myListD = myListE
    myListD.push(40)

    console.log(myListE)
    console.log(myListD)
}

myListFunc(myListC)
console.log(myListC)

/*
Extra
*/

//Por valor

function value(valueA, valueB){
    let temp = valueA;
    valueA = valueB;
    valueB = temp;
    return [valueA, valueB];
}

let myIntD = 10;
let myIntE = 20;
const [myIntF, myIntG] = value(myIntD, myIntE);

console.log(`${myIntD}, ${myIntE}`)
console.log(`${myIntF}, ${myIntG}`)

//Por referencia

function ref(valueA, valueB){
    let temp = valueA;
    valueA = valueB;
    valueB = temp;
    return [valueA, valueB];
}

let myListE = [10, 20]
let myListF = [30, 40]
const [myListG, myListH] = ref(myListE, myListF);


console.log(`${myListE}, ${myListF}`)
console.log(`${myListG}, ${myListH}`)