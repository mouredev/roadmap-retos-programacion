//! Variables usadas */
const apples = true
const bananas = false;
// ---
const number = 10;
const number2 = "10";
const number3 = "10";
let owner = "Juan"
let employee = "David"

//? 1. Tipos de operadores

/* Aritmeticos */
const sum = 5 + 5;
const susb = 10 - 4;
const mult = 25 * 1;
const div = 5 / 2;
const exp = 5 ** 2;

/* Logicos */
if (apples && bananas) { // And
    console.log("We have bananas and apples");
} else if (apples || bananas) { // Or
    console.log('We only have one of the two fruits');

} else if (!apples) { // Not
    console.log('We only have bananas');

}

/* Comparacion */
const comp = number != number2 // Diferente a (No estricto)
const comp2 = number !== number3 // Diferente a (Estricto)
const comp3 = number == number2 // Igual a (No estricto)
const comp4 = number === number3 // Igual a (Estricto)
const greaterThan = number > number2 // Mayor a
const lowerThan = number < number2 // Menor a
const lowerOrEqualThan = number <= number2 // Menor o igual a

/* Asignacion */
owner = employee // Owner is assinged employee value
console.log(owner); // David
console.log(employee);

//? 2. Estructuras de control
const numbers = [1, 4, 5, 2, 24, 10, 12]

/* for */
for (let i = 0; i < numbers.length; i++) {
    const number = numbers[i];

    if (number % 2 === 0) {
        console.log(number);
        continue;
    } else {
        continue;
    }
}
/* switch */
const month = 10;
switch (true) {
    case (month > 0 && month <= 4):
        console.log('Its Spring');
        break;
    case (month > 4 && month <= 6):
        console.log('Its Summer');
        break;
    case (month > 6 && month <= 10):
        console.log('Its Autum');
        break;
    case (month > 10 && month <= 12):
        console.log('Its Winter');
        break;
    default:
        console.log("Its not a month")
}
/* if */
const age = 18
const password = "1524"
if (age >= 18 && password === "1524") {
    console.log('You can pass');
} else {
    console.log('You cant pass');
}

/* While */
let result = 1;
let counter = 0;
while (counter < 10) {
    result = result * 2
    counter += 1
}
console.log(result);

/* Do while */
let letter;
do {
     letter = prompt("Enter the letter A")
} while(letter != 'A') {
    alert('Congratulations');
}

let evenOrOdd;
do {    
    evenOrOdd = Number(prompt("Insert a number"))
    if(evenOrOdd < 0 || evenOrOdd > 100) {
        alert('The number must be between 0 and 100')
        
    }

} while (evenOrOdd < 0 || evenOrOdd > 100 || (evenOrOdd % 2 === 0));
if (evenOrOdd % 2 !== 0) {
    alert("It's an odd number");
}

//? Ejercicio Extra
const limit = 10
const limit2 = 55;
const isMultOf3 = (number) => {
    let sum = 0;
    const numberString = number.toString();
    for (let digit in numberString) {
        sum += parseInt(numberString[digit])
    }
    if(sum % 3 === 0) {
        return true
    } else {
        return false
    }
}

for(let i = limit; i <= limit2; i++) {
    if(i % 2 === 0 && (isMultOf3(i) && i !== 16)) {
        console.log(i);
    } else {
        continue;
    }
}
