console.log("for");
for (let i: number = 1; i <= 10; i++) {
    console.log(i);
}

console.log("while");
let n: number = 1;
while (n <= 10) {
    console.log(n);
    n++;
}

console.log("do while");
n = 1;
do {
    console.log(n);
    n++;
} while (n <= 10);

// ** Extra Exercise ** //
console.log("for of");
const numbers: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (const number of numbers) {
    console.log(number);
}

console.log("for in");
for (const index in numbers) {
    console.log(numbers[index]);
}

console.log("forEach");
numbers.forEach((number: number) => {
    console.log(number);
});

console.log("map");
numbers.map((number: number) => {
    console.log(number);
});

console.log("Array.from");
Array.from({ length: 10 }, (_, i: number) => console.log(i + 1));

console.log("reduce");
numbers.reduce((_, number: number) => {
    console.log(number);
    return number;
}, 0);

console.log("Recursion");
function printNumbers(n: number): void {
    if (n > 10) return;
    console.log(n);
    printNumbers(n + 1);
}

printNumbers(1);
