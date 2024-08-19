const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let cont = 0;

// 17 ITERACIONES - imprimir números del 1 al 10
// #1

while (cont < numeros.length) {
  console.log(numeros[cont])
  cont += 1;
}

// #2
cont = 0;
do {
  console.log(numeros[cont]);
  cont += 1;
} while (cont < numeros.length)

// #3
for (let i = 0; i < numeros.length; i++) {
  console.log(numeros[i])
}

// [Extra]
//
console.log('Extra')
// #1
cont = 0;
while (cont < numeros.length) {
  console.log(numeros[cont])
  cont += 1;
}

// #2

cont = 0;
do {
  console.log(numeros[cont]);
  cont += 1;
} while (cont < numeros.length)

// #3

for (let i = 0; i < numeros.length; i++) {
  console.log(numeros[i])
}

// #4

for (const numero of numeros) {
  console.log(numero);
}

// #5

numeros.forEach((numero) => console.log(numero));

// #6
for (const contIn in numeros) {
  console.log(numeros[contIn]);
}

// #7
numeros.map((numero) => console.log(numero));

// #8
numeros.filter((numero) => console.log(numero))

// #9
numeros.flatMap((numero) => console.log(numero))

// #10
Array.from(numeros, (numero) => console.log(numero));
