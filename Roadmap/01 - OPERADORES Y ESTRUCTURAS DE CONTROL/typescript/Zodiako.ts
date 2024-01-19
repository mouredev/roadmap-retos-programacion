// Aritmetic
console.log(2 + 2);
console.log(2 - 2);
console.log(2 * 2);
console.log(2 / 2);
console.log(2 % 2);
console.log(2 ** 2);

// Incremental
let a: number = 1;
console.log(a++);

// Decremental
let b: number = 1;
console.log(b--);

// Comparison
console.log(2 > 2);
console.log(2 >= 2);
console.log(2 < 2);
console.log(2 <= 2);
console.log(2 == 2);
console.log(2 === 2);
console.log(2 != 2);
console.log(2 !== 2);

// Logical
console.log(true && true);
console.log(true || false);
console.log(!true);

// Conditional
let age: number = 25;
let adult: boolean = age >= 18 ? true : false;
console.log(adult);

// If
let myNumber: number = 10;
if (myNumber > 5) {
  console.log("My number is greater than 5");
} else {
  console.log("My number is less than 5");
}

// Switch
let color: string = "red";
switch (color) {
  case "red":
    console.log("My color is red");
    break;
  case "blue":
    console.log("My color is blue");
    break;
  default:
    console.log("My color is not red or blue");
    break;
}


