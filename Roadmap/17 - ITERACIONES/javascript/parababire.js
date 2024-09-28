// 1. For loop

for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// 2. Do While loop

let num = 1;
do {
  console.log(num);
  num++;
} while (num <= 10);

// 3. For of

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (const num of numbers) {
  console.log(num);
}

// Extra

// 4. While

let i = 1;

while (i <= 10) {
  console.log(i);
  i++;
}

// 5. For in

for (const num in numbers) {
  console.log(numbers[num]);
}

// 6. For each

function impresora(item) {
  console.log(item);
}

numbers.forEach(element => {
  impresora(element);
});

// 7. Map

numbers.map(impresora);

// 8. Flatmap

numbers.flatMap(impresora);

