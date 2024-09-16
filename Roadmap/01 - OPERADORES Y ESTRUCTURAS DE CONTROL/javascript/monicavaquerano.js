// 01 OPERADORES Y ESTRUCTURAS DE CONTROL
// Monica Vaquerano
//  https://monicavaquerano.dev

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


// Assignment
let x = 5;
let y = 10;

// Arithmetic
console.log("suma: 5 + 10 =", x + y);
console.log("resta: 5 - 10 =", x - y);
console.log("multiplicacion: 5 * 10 =", x * y);
console.log("exponencial: 5 ** 10 =", x ** y);
console.log("division: 5 / 10 =", x / y);
console.log("modulo: 10 % 5 =", y % x);

// Assignment Operators
console.log("suma: x += y ", x += y);
console.log("resta: x -= y ", x -= y);
console.log("multiplicacion: x *= y ", x *= y);
console.log("exponencial: x **= y ", x **= y);
console.log("division: x /= y ", x /= y);
console.log("modulo: y /= x ", y %= x);

// Comparison Operators
x = 12;
y = 6;

console.log("x == 12 :", x == 12);
console.log("x === '12' :", x === '12');
console.log("y != 6 :", y != 6);
console.log("y !== '6' :", y !== '6');
console.log("x > y :", x > y);
console.log("x < y :", x < y);
console.log("x >= 12 :", x >= 12);
console.log("x <= 11 :", x <= 11);
console.log("x >= y ? 'x es mayor o igual' : 'x no es mayor o igual' =>", x >= y ? 'x es mayor o igual' : 'x no es mayor o igual');


// Logical Operators
console.log("x > y && x == 12 :", x > y && x == 12);
console.log("x != 12 || y == 6 :", x != 12 || y == 6);
console.log("!(x != 12 && y != 6) :", !(x != 12 && y != 6));

// Type Operators
console.log("typeof x :", typeof x);
console.log("typeof 'Soy una string' :", typeof 'Soy una string');
cadena = new String('Soy una string');
numero = new Number(8);
console.log("numero instanceof Number :", (numero instanceof Number));
console.log("cadena instanceof String :", (cadena instanceof String));

// Shift Assignment Operators
console.log("x <<= y :", x <<= y);
console.log("x >>= y :", x >>= y);
console.log("x >>>= y :", x >>>= y);

// Bitwise Assignment Operators
x = 2, y = 2;
console.log("x &= y :", x &= y);
console.log("x ^= y :", x ^= y);
console.log("x |= y :", x |= y);

// Operadores de Pertenencia

const car = { make: 'Honda', model: 'Accord', year: 1998 };

console.log('make' in car);
// Expected output: true

delete car.make;
if ('make' in car === false) {
    car.make = 'Suzuki';
}

console.log(car.make);
// Expected output: "Suzuki"


// # - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
// # que representen todos los tipos de estructuras de control que existan
// # en tu lenguaje:
// # Condicionales, iterativas, excepciones...
// # Debes hacer print por consola del resultado de todos los ejemplos.

console.log("\nEstructuras de Control Condicional:");

let list = [-3, 0, 1, 6];

// Loop For If
for (let item in list) {
    list[item] *= 2;
    if (list[item] < 0) {
        console.log("Soy un número negativo:", list[item])
    } else if (list[item] == 0) {
        console.log("Soy cero!")
    } else if (0 < list[item] && list[item] < 4) {
        console.log("Soy un número entre 0 y 5:", list[item])
    } else {
        console.log("Soy un número mayor a 5:", list[item])
    }
}

// Loop For Of - parecido más a pyhton
for (let item of list) {
    if (item < 0) {
        console.log(item, "bajo cero")
    } else if (item > 0) {
        console.log(item, "sobre cero")
    } else {
        console.log("Soy ceroooo!")
    }
}

console.log("\nEstructuras de Control Ternario:");

// Loop For
for (let i = 0; i < list.length; i++) {

    // Conditional (ternary) operator / Operador condicional (ternario)
    console.log(list[i] <= 0 ? "Soy un número negativo" : "Soy un número positivo");
}

console.log("\nEstructuras de Control Iterativas:");

// While loop
let counter = 0;
while (counter < 3) {
    console.log("Counter es menor a 3: counter =", counter)
    counter++
}

//Do-While loop
counter = 3;
do {
    console.log("Counter es mayor a 0: counter =", counter)
    counter--
}
while (counter > 0);

// For Loop
for (let i = 10; i >= 0; i--) {
    if (i == 0) {
        console.log("Boom!");
    } else {
        console.log(i);
    }
}

// Switch
let day;
switch (new Date().getDay()) {
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
        break;
    default:
        day = "I don't know";
        break;
}
console.log(day)

// For In loop in Object
let contactos = {
    "Alice": { "telefono": "0123456" },
    "Bob": { "telefono": "0123456" },
    "Charlie": { "telefono": "0123456" },
}
for (let i in contactos) {
    console.log(i, contactos[i])
}

// For Of Loop in Objects

// Loop over keys
for (let key of Object.keys(contactos)) {
    console.log(key)
}

// Loop over values
for (let value of Object.values(contactos)) {
    console.log(value)
}

// Loop over entries
for (let [key, value] of Object.entries(contactos)) {
    console.log(`${key.toUpperCase()}: ${Object.values(value)}`)
}


console.log("\nExcepciones:");
// Try and except
x = 0;
try {
    if (x == 0) {
        throw new Error("Ocurrió una excepción :P");
    }
} catch (error) {
    console.error(error.message);
}

// Muchas excepciones
try {
    if (x == 0) throw "No es cero";
    if (x < 0) throw "Es menor que cero";
    if (x > 0) throw "Es mayor que cero";

} catch (error) {
    console.log("Ocurrió una excepción:", error)
}

// Error: Name of Error and Message
try {
    throw new TypeError("oops");
} catch ({ name, message }) {
    console.log(name); // "TypeError"
    console.log(message); // "oops"
}


// Excepciones Anidadas
try {
    try {
        throw new Error('mi error');
    } catch (err) {
        console.error('interno', err.message);
        throw err;
    } finally {
        console.log('finally interno');
    }
} catch (err) {
    console.error('externo', err.message);
}

// Output:
// interno mi error
// finally interno
// externo mi error


// Excepciones con Finally
try {
    if (x == 0) {
        throw (new Error("ERROR"));
    }
} catch (err) {
    console.error('Catch:', err.message);
} finally {
    console.log("Finally!!!!!");
}


// DIFICULTAD EXTRA (opcional):
// Crea un programa que imprima por consola todos los números comprendidos
// entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3:
// """
console.log("DIFICULTAD EXTRA")

let result = "";
for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && !(i % 3 == 0) && i != 16) {
        result += `${i}, `
    }
}
console.log(result.slice(0, -2));