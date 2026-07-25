console.log("for");
for (i = 1; i <= 10; i++) {
    console.log(i);
}

console.log("while");
let n = 1;
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

// Extra Exercise //
console.log("for of");
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (number of numbers) {
    console.log(number);
}

console.log("for in");
for (number in numbers) {
    console.log(numbers[number]);
}

console.log("forEach");
numbers.forEach((number) => {
    console.log(number);
});

console.log("map");
numbers.map((number) => {
    console.log(number);
});

console.log("Array.from");
Array.from({ length: 10 }, (_, i) => console.log(i + 1));

console.log("reduce");
numbers.reduce((_, number) => {
    console.log(number);
    return number;
}, 0);

console.log("Recursion");
function printNumbers(n) {
    if (n > 10) return;
    console.log(n);
    printNumbers(n + 1);
}

printNumbers(1);