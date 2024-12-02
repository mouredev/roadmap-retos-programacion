
// Operadores Aritméticos

let a = 10;
let b = 5;

console.log("Suma:", a + b);         // 15
console.log("Resta:", a - b);        // 5
console.log("Multiplicación:", a * b); // 50
console.log("División:", a / b);     // 2
console.log("Módulo:", a % b);       // 0
console.log("Exponenciación:", a ** b); // 100000







// Operadores Lógicos

let x = true;
let y = false;

console.log("AND lógico:", x && y); // false
console.log("OR lógico:", x || y);  // true
console.log("NOT lógico:", !x);     // false






// Operadores de Comparación
let p = 10;
let q = 20;

console.log("Igual a:", p == q);        // false
console.log("No igual a:", p != q);     // true
console.log("Mayor que:", p > q);       // false
console.log("Menor que:", p < q);       // true
console.log("Mayor o igual que:", p >= q); // false
console.log("Menor o igual que:", p <= q); // true







// Operadores de Asignación
let n = 5;

n += 3; // n = n + 3
console.log("Asignación de suma:", n); // 8

n -= 2; // n = n - 2
console.log("Asignación de resta:", n); // 6

n *= 4; // n = n * 4
console.log("Asignación de multiplicación:", n); // 24

n /= 3; // n = n / 3
console.log("Asignación de división:", n); // 8

n %= 2; // n = n % 2
console.log("Asignación de módulo:", n); // 0








// Operadores de Identidad

let r = 5;
let s = "5";

console.log("Identidad (igual):", r === s); // false
console.log("Identidad (no igual):", r !== s); // true









// Operadores de Pertenencia

let arr = [1, 2, 3, 4, 5];

console.log("Pertenencia (en array):", arr.includes(3)); // true
console.log("Pertenencia (no en array):", arr.includes(6)); // false







// Operadores de Bits

let m = 5;  // 0101 en binario
let ñ = 3;  // 0011 en binario

console.log("AND bit a bit:", m & ñ); // 1 (0001 en binario)
console.log("OR bit a bit:", m | ñ);  // 7 (0111 en binario)
console.log("XOR bit a bit:", m ^ ñ); // 6 (0110 en binario)
console.log("Complemento bit a bit:", ~m); // -6 (invertido en binario)
console.log("Desplazamiento a la izquierda:", m << 1); // 10 (1010 en binario)
console.log("Desplazamiento a la derecha:", m >> 1); // 2 (0010 en binario)
















// Condicionales

let age = 20;

if (age < 18) {
    console.log("Eres menor de edad.");
} else if (age >= 18 && age < 65) {
    console.log("Eres adulto.");
} else {
    console.log("Eres mayor de edad.");
}





// Iterativas


// Bucle for
for (let i = 0; i < 5; i++) {
    console.log("Bucle for, iteración:", i);
}

// Bucle while
let j = 0;
while (j < 5) {
    console.log("Bucle while, iteración:", j);
    j++;
}

// Bucle do-while
let k = 0;
do {
    console.log("Bucle do-while, iteración:", k);
    k++;
} while (k < 5);





// Excepciones

try {
    let result = 10 / 0;
    if (!isFinite(result)) {
        throw new Error("División por cero");
    }
    console.log("Resultado:", result);
} catch (error) {
    console.log("Error capturado:", error.message);
} finally {
    console.log("Bloque finally ejecutado.");
}









// * DIFICULTAD EXTRA (opcional):
//   * Crea un programa que imprima por consola todos los números comprendidos
//   * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//   *
//   * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

    
function imprimir_numeros(){
    for ( let x = 10; x < 56; x++){
        if (x >= 10 && x <=55 && x % 2 === 0 && x != 16 && x % 3 != 0) {
            console.log(x)
        }
    }
    
}
imprimir_numeros()

