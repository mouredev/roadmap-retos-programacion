/** OPERADORES ****************************************************************/

// Operadores Aritméticos (+,-,*,/,%)
let num1 = 15;
let num2 = 5;

let suma = num1 + num2;
let resta = num1 - num2;
let multiplicacion = num1 * num2;
let division = num1 / num2;
let resto = num1 % num2;
let exponencial = num1 ** num2;

// Operadores Lógicos (||, &&, !)
/*
 * Operadores Lógicos (||, &&, !)
 * || → OR → Si al menos una de las condiciones es verdadera, el resultado es verdadero.
 * && → AND → Si todas las condiciones son verdaderas, el resultado es verdadero.
 * ! → NOT → Invierte el valor lógico de una expresión. Si la expresión es verdadera, se vuelve falsa, y viceversa.
 */

let x = true;
let y = false;
let z = true;

let logico1 = x && y && z;
let logico2 = x || y || z;
let logico3 = ((x || !y) && z) || (!x && z);


// Operadores de Comparación (<, <=, >=, >, ==, ===, !=, !==)
let n1 = 16;
let n2 = 8;
let n3 = "16";

let comparacion1 = n1 > n2;
let comparacion2 = n1 < n2;
let comparacion3 = n1 >= n2;
let comparacion4 = n1 <= n2;
let comparacion5 = n1 == n3;
let comparacion6 = n1 != n3;
let comparacion7 = n1 === n3;
let comparacion8 = n1 !== n3;

// Operadores de Asignación (=, +=, -=, *=, /=, %=, **=)
let a = 10;
a += 5; // a = a + 5 → a = 10 + 5 → a = 15
a -= 3; // a = a - 3 → a = 15 - 3 → a = 12
a *= 2; // a = a * 2 → a = 12 * 2 → a = 24
a /= 4; // a = a / 4 → a = 24 / 4 → a = 6
a %= 4; // a = a % 4 → a = 6 % 4 → a = 2
a **= 3; // a = a ** 3 → a = 2 ** 3 → a = 8

--a; // a = a - 1 → a = 8 - 1 → a = 7
a--; // a = a - 1 → a = 7 - 1 → a = 6
++a; // a = a + 1 → a = 6 + 1 → a = 7
a++; // a = a + 1 → a = 7 + 1 → a = 8

// Operadores bit a bit
let var1 = 10; // 1010
let var2 = 3; // 0011

let opeacionBit1 = var1 & var2; // 0010 - Si ambos son 1
let opeacionBit2 = var1 | var2; // 1011 - Si almenos 1 es 1
let opeacionBit3 = var1 ^ var2; // 1001 -  Si los bits son diferentes 0 si son iguales 1
let opeacionBit4 = ~var1; // 0101 -  Invierte el valor bit a bit
let opeacionBit5 = var1 >> 2; // 1010 → 0101 → 0010
let opeacionBit6 = var1 << 2; // 1010 → 101000

/** ESTRUCTURAS DE CONTROL ****************************************************/

// Condicionales
const MAYORIA_EDAD = 18;
let edad_persona = 23;

if (edad_persona < 0 || edad_persona > 120) {
    console.log(`Edad inexistene, ingrese un valor correcto`);

} else if (edad_persona < MAYORIA_EDAD) {
    console.log(`Con ${edad_persona} años sos menor de edad`);

} else {
    console.log(`Con ${edad_persona} años sos mayor de edad`);
}

//Switch

let opcion = 2;

switch (opcion) {
    case 1:
        console.log("Opción 1");
        break;

    case 2:
        console.log("Opción 2");
        break;

    case 3:
        console.log("Opción 3");
        break;

    default:
        console.log("Debes ingresar una de las 3 opciones");
        break;
}

//Bucle For

for (let i = 0; i < 10; i++) {
    console.log(`i = ${i}`);
}

//Bucle While

let j = 10;
while (j-- > 5) {
    console.log(`j = ${j}`);
}

//Bucle Do-while
let tiene_permiso = false;

do {
    console.log("No tienes permiso");

    //Usando variables anteriormente creadas
    if (edad_persona > MAYORIA_EDAD) {
        tiene_permiso = true;
        console.log("Ahora si tienes permiso");
    }

} while ((tiene_permiso = false));

// DIFICULTAD EXTRA
for (let i = 10; i <= 55; i++) {
    if (!(i&1) && i != 16 && i % 3 !== 0) {
        console.log(i);
    }
}

// > Autor: Fravelz
