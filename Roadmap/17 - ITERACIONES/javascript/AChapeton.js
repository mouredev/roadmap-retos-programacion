// FOR
console.log('FOR');
for (let i = 0; i <= 10; i++) {
    console.log(i);
}
// FOREACH
console.log('FOREACH');
let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
numbers.forEach(function (i) {
    console.log(i);
});
// FOR IN
console.log('FOR IN');
for (let i in numbers) {
    console.log(numbers[i]);
}
// FOR OF
console.log('FOR OF');
for (let _i = 0, numbers_1 = numbers; _i < numbers_1.length; _i++) {
    let i = numbers_1[_i];
    console.log(i);
}
// WHILE
console.log('WHILE');
let w = 0;
while (w < 11) {
    console.log(w);
    w++;
}
// DO-WHILE
console.log('DO-WHILE');
let d = 0;
do {
    console.log(d);
    d++;
} while (d < 11);
