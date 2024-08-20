//Assignment operators are used to assign a value to a variable.
let myVariable = 5; 
// Assigns the value 5 to the variable myVariable
//If we don't assign a value to a variable, js will assign the "undefined" value by default
let myVariable2; 
// myVariable2 is undefined by default
//The assignment operator can also be used to assign the result of an expression to a variable

myVariable = 6 //Assigns a diferent value 
console.log(myVariable);
myVariable += 3; // Adds 3 to the value of myVariable and assigns the result to myVariable
console.log(myVariable);
myVariable -= 3; // Subtracts 3 from the value of myVariable and assigns the result to myVariable
console.log(myVariable);
myVariable *= 3; // Multiplies the value of myVariable by 3 and assigns the result to myVariable
console.log(myVariable);
myVariable /= 3; // Divides the value of myVariable by 3 and assigns the result to myVariable

//Arithmetic operators are used to perform mathematical operations on variables and values.
//The arithmetic operators are: 
//Addition: + 
console.log(5 + 7);
//Subtraction: -
console.log(5 - 7);
//Multiplication: *
console.log(5 * 7);
//Division: /
console.log(5 / 7);
//Modulus (remainder): %
console.log(5 % 7);
//Exponentiation: **
console.log(5 ** 7);
//Increment and decrement operators are used to increase or decrease the value of a variable by 1.
//Increment ++ the second sign can be replaced by a number, this number will be the increment
console.log(++myVariable);
console.log(++myVariable);

//For example +5 will increment by 5 every step
console.log(myVariable +5);

//Decrement -- the second sign can be replaced by a number, this number will be the decrement
//For example -5 will decrement by 5 every step

console.log(myVariable -5);

//Extra

for(i=10; i<=55; i++){
    if(i === 16 || i % 3 === 0 || i % 2 != 0){
        continue
    }
    console.log(i);
}




