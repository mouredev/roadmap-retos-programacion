let a: number = 3;
let b: number = 4;

let sum: number = a + b;
console.log("a + b = " + sum);

let sub: number = a - b;
console.log("a - b = " + sub);

let mul: number = a * b;
console.log("a * b = " + mul);

let div: number = a / b;
console.log("a / b = " + div);

let res: number = a % b;
console.log("a % b = " + res);

let pow: number = a ** b;
console.log("a ** b = " + pow);

let inc: number = a++;
console.log("a++ = " + inc);

let dec: number = a--;
console.log("a-- = " + dec);

a += b;
console.log("a += b\tNumber A: " + a);

a -= b;
console.log("a -= b\tNumber A: " + a);

a *= b;
console.log("a *= b\tNumber A: " + a);

a /= b;
console.log("a /= b\tNumber A: " + a);

a = b;
console.log("a = b\tNumber A: " + a);

a %= b;
console.log("a %= b\tNumber A: " + a);

a **= b;
console.log("a **= b\tNumber A: " + a);

if (a == b) {
    console.log("Number A is equal to number B");
}

if (a === b) {
    console.log("The number A and its type is equal to the number B");
} else if (a > b) {
    console.log("The number A is greater than the number B");
} else {
    console.log("Number A is neither greater than nor equal to number B");
}

if (a >= b) {
    console.log("Number A is greater than or equal to number B");
} else {
    console.log("The number A is less than the number B");
}

console.log(a != b ? "The number A is different from the number B" : "The number A is the same as the number B");
console.log(a !== b ? "Number A is different from number B in both value and type" : "The number A is the same as the number B");

switch(b) {
    case 1:
        console.log("The number B is equal to 1");
        break;
    case 2:
        console.log("The number B is equal to 2");
        break;
    case 3:
        console.log("The number B is equal to 3");
        break;
    case 4:
        console.log("The number B is equal to 4");
        break;
    default:
        console.log("The number B is not 1, 2, 3, 4");
}

while (a < b) {
    console.log("Loop while\t Number A: " + a);
    a++;
}

a = 1;

do {
    console.log("Loop do while\t Number A: " + a)
    a++;
} while (a <= b);

for (let i = 0; i < 3; i++) {
    console.log("Loop for " + i);
}

let array: number[] = [1, 2, 3, 4];

for (var i of array) {
    console.log("Loop of " + i);
}

for (var e in array) {
    console.log("Loop in " + e);
}

try {
    throw new Error('Error caught');
} catch(e) {
    console.log(e);
}

program()

function program(): void {
    for (let i = 10; i <= 55; i++) {
        if (i % 2 == 0 && i != 16 && i % 3 != 0) {
            console.log("\n" + i);
        }
    }
}
