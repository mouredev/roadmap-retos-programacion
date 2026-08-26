/*
Funciones
*/


// Simple

function greet(){
    console.log("Hola, JavaScript")
}

greet()


// Con retorno 

function returnGreet(){
    return "Hola, JavaScript";
}

console.log(returnGreet())

// Con parametro

function greet(name){
    console.log(`Hola, ${name}`)
}

greet("Sandra")

// Con parametros

function fullName(firstName, lastName){
    console.log(`Hola ${firstName} ${lastName}!`)
}

fullName("Emanuel", "Aristizabal")

// Con un parametro predeterminado

function greet(name = "David"){
    console.log(`Hola, ${name}`)
}

greet()

// Anonimas

const multiply = function(a, b) {
  return a * b;
};

multiply(5, 10)

// Arrow Functions 

const sum = (a, b) => a + b

sum(5, 10)

// Anidadas

function firstName() {
    console.log("Juan")
    function lastName(){
        console.log("Montaño")
    }
    lastName()
}

firstName()

/*
Funciones del lenguaje
*/

console.log(parseInt("5Efs"))
console.log(parseFloat(5.0))
console.log(isNaN("5"))

let str = "Emanuel"
console.log(str.includes("o"))

/*
Variables locales y globales
*/

let secondName = "David"

function name2() {
        let name1 = "Emanuel"
        console.log(`¿Cual es tu primer y segundo nombre? ${name1}, ${secondName}`)
} 

console.log(secondName)
// console.log(name1) No se puede acceder a una variable interna 
name2();

/*
Extra
*/

function printNumbers(text1, text2 ) {
    let count = 0
    for (let i = 1; i <= 100; i++){
        if( i % 3 == 0 && i % 5 == 0){
            console.log(text1 + text2)
        } else if(i % 3 == 0){
            console.log(text1)
        } else if( i % 5 == 0){
            console.log(text2)
        } else {
            console.log(i)
            count += 1
        } 
    } return count
}

console.log(printNumbers("Fizz", "Buzz"))