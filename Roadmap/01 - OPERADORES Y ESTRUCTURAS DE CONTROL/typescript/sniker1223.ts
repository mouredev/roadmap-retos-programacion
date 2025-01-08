// Arithmetic Operators
var numberA: number = 100
console.log("Arithmetic Operators")
console.log("+ Addition:", numberA + 50)
console.log("- Subtraction:", numberA - 50)
console.log("* Multiplication:", numberA * 50)
console.log("/ Division:", numberA / 50)
console.log("% Modulus:", numberA % 2)
numberA++
console.log("++ Increment:", numberA)
numberA--
console.log("-- Decrementing:", numberA)

// Assignment Operators
console.log("\nAssignment Operators")
numberA = 50
console.log("= Assignment: numberA = ", numberA)
numberA += 1
console.log("+= Addition assignment: numberA += ", numberA)
numberA -= 1
console.log("-= Substraction Assignment: numberA -= ", numberA)
numberA *= 2
console.log("*= Multiplication Assignment: numberA *= ", numberA)
numberA /= 3
console.log("/= Division Assignment: numberA /= ", numberA)
numberA %= 2
console.log("%= Modulus Assignment: numberA %= ", numberA)

// Comparison Operators
console.log('\nComparision Operators')
console.log('==	Is equal to	10 == 10 = ', 10 == 10)
console.log('=== Identical (equal and of same type) ', 10 === 10)
console.log("!= Not equal to 20 != 20: ", 20 != 20)
console.log("!== Not Identical 20 !== 20", 20 !== 20)
console.log('2 is greater than 1:', 2 > 1)
console.log('2 is greater than or equal to 2', 2 >= 2)
console.log('2 is less than 1: ', 2 < 1)
console.log('2 is less than or equal to 1', 2 <= 1)

// Logical Operators
console.log('\nLogical Operators')
numberA = 6
console.log('&& and operator:', numberA > 1 && numberA < 8)
console.log('|| or operator:', numberA > 1 || numberA > 8)
console.log('! not operator:', !(6 == 6))

// Typescript typeof Operator
console.log('\nTypescript typeof Operator')
console.log('typeof: ', typeof "Hello world");

// CONTROL STRUCTURES
console.log('\nif Statement')
if (7 < 18) {
  console.log("Good day")
}

console.log('\nelse Statement')
if (19 < 18) {
  console.log("Good day")
} else {
  console.log("Good evening")
}

console.log('\nelse if Statement')
let dateTime = new Date().getHours()

if (dateTime < 10) {
  console.log("Good morning")
} else if (dateTime < 20) {
  console.log("Good day")
} else {
  console.log("Good evening")
}

console.log('\nSwitch Statement')
switch (new Date().getDay()) {
  case 0:
    console.log("Sunday")
    break;
  case 1:
    console.log("Monday")
    break;
  case 2:
    console.log("Tuesday")
    break;
  case 3:
    console.log("Wednesday")
    break;
  case 4:
    console.log("Thursday")
    break;
  case 5:
    console.log("Friday")
    break;
  case 6:
    console.log("Saturday")
}

console.log('\nfor loop')
var list: Array<String> = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];
let textList = "";
for (let i = 0; i < list.length; i++) {
  textList += list[i] + "\n";
}
console.log(textList)

console.log('\nfor in loop')
const person = {
  fname: "John",
  lname: "Doe",
  age: 25
}
let textPerson1 = ""

const keys = Object.keys(person);

keys.forEach((key) => {
  console.log(person[key as keyof typeof person]);
});

console.log('\nWhile Loop')
let iterable = 0
while (iterable <= 10) {
  console.log("The number is " + iterable)
  iterable++;
}

console.log('\ntry and finally')

function doIt() {
  try {
    return console.log('1')
  } finally {
    return console.log('2')
  }
}
doIt();

// Challenge. Print numbers between 10 and 55(included), even and odd but not print 16 and multiple of 3.
console.log('\nChallenge')
for (let n = 0; n <= 55; n++) {
  if (n >= 10 && n % 2 == 0 && n != 16 && !(n % 3 == 0) || n == 55) {
    console.log(n)
  }
}

