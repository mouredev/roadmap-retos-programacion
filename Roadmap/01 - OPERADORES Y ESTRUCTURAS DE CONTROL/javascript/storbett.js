// Operadores aritméticos
console.log(`suma: 10 + 3 = ${10 + 3}`);
console.log(`resta: 10 - 3 = ${10 - 3}`);
console.log(`multiplicación: 10 * 3 = ${10 * 3}`);
console.log(`división: 10 / 3 = ${10 / 3}`);
console.log(`módulo: 10 % 3 = ${10 % 3}`);
console.log(`exponente: 10 ** 3 = ${10 ** 3}`);
console.log(`división entera: Math.floor(10 / 3) = ${Math.floor(10 / 3)}`);

// Operadores de comparación
console.log(`igualdad 10 == 3 es ${10 == 3}`);
console.log(`desigualdad 10 != 3 es ${10 != 3}`);
console.log(`mayor que 10 > 3 es ${10 > 3}`);
console.log(`menor que 10 < 3 es ${10 < 3}`);
console.log(`mayor o igual que 10 >= 3 es ${10 >= 3}`);
console.log(`menor o igual que 10 <= 3 es ${10 <= 3}`);

// Operadores lógicos
console.log(`AND &&: 10 + 3 == 13 && 5 - 1 == 4 es ${10 + 3 == 13 && 5 - 1 == 4}`);
console.log(`OR: 10 + 3 == 13 || 5 - 1 == 4 es ${10 + 3 == 13 || 5 - 1 == 4}`);
console.log(`NOT !: !(10 + 3 == 14) es ${!(10 + 3 == 14)}`);

// Operadores de asignación
let myNumber = 11; // asignación
console.log(myNumber);
myNumber += 1;
console.log(myNumber);
myNumber -= 1;
console.log(myNumber);
myNumber *= 2;
console.log(myNumber);
myNumber /= 2;
console.log(myNumber);
myNumber %= 2;
console.log(myNumber);
myNumber **= 1;
console.log(myNumber);
myNumber = Math.floor(myNumber / 1);
console.log(myNumber);

// Operadores de identidad
let myNewNumber = myNumber;
console.log(`myNumber === myNewNumber es ${myNumber === myNewNumber}`);
console.log(`myNumber !== myNewNumber es ${myNumber !== myNewNumber}`);

// Operadores de pertenencia
console.log(`'o' in 'Simon' = ${'Simon'.includes('o')}`);
console.log(`'h' not in 'Simon' = ${!('Simon'.includes('h'))}`);

// Operadores de bit
let a = 10; // 1010
let b = 3; // 0011
console.log(`AND: 10 & 3 = ${10 & 3}`);
console.log(`OR: 10 | 3 = ${10 | 3}`);
console.log(`XOR: 10 ^ 3 = ${10 ^ 3}`);
console.log(`NOT: ~10 = ${~10}`);
console.log(`desplazamiento a la derecha : 10 >> 2 = ${10 >> 2}`);
console.log(`desplazamiento a la izquierda : 10 << 2 = ${10 << 2}`);

// Estructuras de control

// Condicionales
let myString = "simons";
if (myString === "simons") {
    console.log("myString es 'simons'");
} else if (myString === "Brais") {
    console.log("myString es 'Brais'");
} else {
    console.log("myString no es 'simons' ni 'Brais'");
}

// Iterativas

for (let i = 0; i <= 10; i++) {
    console.log(i);
}

let i = 0;
while (i <= 10) {
    console.log(i);
    i++;
}

// Manejo de excepciones
try {
    console.log(10 / 0);
} catch (error) {
    console.log("se ha producido un error");
} finally {
    console.log("ha finalizado el manejo de excepciones");
}

// Extra
for (let number = 10; number < 56; number++) {
    if (number % 2 === 0 && number !== 16 && number % 3 !== 0) {
        console.log(number);
    }
}
