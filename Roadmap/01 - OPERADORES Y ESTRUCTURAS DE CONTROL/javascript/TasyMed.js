// #01 OPERADORES Y ESTRUCTURAS DE CONTROL

// Numeros usados en las operaciones
let numero1 = 10;
let numero2 = 5;

// Operadores Aritméticos
let suma = numero1 + numero2; // Suma
console.log("Suma:", suma); // 15

let resta = numero1 - numero2; // Resta
console.log("Resta:", resta); // 5

let multiplicacion = numero1 * numero2; // Multiplicación
console.log("Multiplicación:", multiplicacion); // 50

let division = numero1 / numero2; // División
console.log("División:", division); // 2

let modulo = numero1 % numero2; // Módulo - Da el residuo  de una divicion
console.log("Módulo:", modulo); // 0

numero1++; // Incremento
console.log("Incremento de numero1:", numero1); // 11

numero2--; // Decremento
console.log("Decremento de numero2:", numero2); // 4

// Operadores de Asignación

numero1 += numero2; // Suma y asigna
console.log(numero1); // 15

numero1 -= numero2; // Resta y asigna
console.log(numero1); // 10

numero1 *= numero2; // Multiplica y asigna
console.log(numero1); // 50

numero1 /= numero2; // Divide y asigna
console.log(numero1); // 10

numero1 %= numero2; // Módulo y asigna
console.log(numero1); // 0

// Operadores de Comparación

let igual = numero1 == numero2; // Igual a
console.log(igual); // false

let estrictoIgual = numero1 === numero2; // Igual estricto a
console.log(estrictoIgual); // false

let distinto = numero1 != numero2; // Distinto a
console.log(distinto); // true

let estrictoDistinto = numero1 !== numero2; // Distinto estricto a
console.log(estrictoDistinto); // true

let mayor = numero1 > numero2; // Mayor que
console.log(mayor); // false

let menor = numero1 < numero2; // Menor que
console.log(menor); // false

let mayorIgual = numero1 >= numero2; // Mayor o igual que
console.log(mayorIgual); // true

let menorIgual = numero1 <= numero2; // Menor o igual que
console.log(menorIgual); // true

// ---- Operadores ----

/*
Usamos los mismos numeros
let numero1 = 10;
let numero2 = 5;
*/

// 1. Condicionales (if, else if, else)
if (numero1 > numero2) {
    console.log("numero1 es mayor que numero2");
} else if (numero1 < numero2) {
    console.log("numero1 es menor que numero2");
} else {
    console.log("Ambos números son iguales");
}

// 2. Switch-case
let operacion = "+";
switch (operacion) {
    case "+":
        console.log("Suma:", numero1 + numero2);
        break;
    case "-":
        console.log("Resta:", numero1 - numero2);
        break;
    default:
        console.log("Operación no reconocida");
}

// 3. Bucle while
let contador = 0;
while (contador < 3) {
    console.log(contador); //El numero en el que va
    contador++;
}

// 4. Bucle do-while
contador = 0;
do {
    console.log(contador); //El numero en el que va
    contador++;
} while (contador < 3);

// 5. Bucle for
for (let i = 0; i < 3; i++) {
    console.log(i); //El numero en el que va
}

// ---- RETO ----

let NumeroReto1 = 10;
let NumeroReto2 = 55;

for (let x = NumeroReto1; x <= NumeroReto2; x++) {
    if (x % 2 !== 0) {  
        continue;  // Salta los impares
    } else if (x === 16) {  
        continue;  // Salta el 16
    } else if (x % 3 === 0) {  
        continue;  // Salta los múltiplos de 3
    } else {  
        console.log(x);  // Imprime los números que cumplen las condiciones
    }
}