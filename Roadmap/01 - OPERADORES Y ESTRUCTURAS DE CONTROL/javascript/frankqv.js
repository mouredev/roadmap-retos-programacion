// #01 Javasript  
// 🌐 EJEMPLO DE OPERADORES Y ESTRUCTURAS DE CONTROL EN JAVASCRIPT

console.log("🌐 OPERADORES Y ESTRUCTURAS DE CONTROL EN JAVASCRIPT\n")

// 🌟 Operadores
/*
 * - Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits.
 */
// 1. Operadores Aritméticos
console.log("\n1. Operadores aritméticos")
let a = 19, b= 37;
console.log(`
Suma:            ${a} + ${b} = ${a + b}
Resta:           ${a} - ${b} = ${a - b}
Multiplicacion:  ${a} * ${b} = ${a * b}
División:        ${a} / ${b} = ${a / b}
Módulo(residuo): ${a} % ${b} = ${a % b}
Exponente:       ${a} ^ ${b} = ${a ** b}
`);


// 2. Operadores Lógicos
console.log("\n2. Operadores Lógicos:");
let x = true, y = false;
console.log("x = true, y = false;");
console.log(`AND (&&):  ${x} AND ${y} =`, x && y);   // false, porque uno de los valores es false
console.log(`OR (||):   ${x} OR ${y} =`, x || y);    // true, porque al menos uno de los valores es true
console.log(`NOT (!):  NOT ${x} =`, !x);        // false, invierte el valor de x


// 3. Operadores de Comparación
console.log("\n4. Operadores de Comparación:");
console.log(`Igual a (==): ${a} == ${b}=`, a == b);   // Igualdad
console.log(`Diferente a (!=): ${a} != ${b}`, a != b); // Desigualdad
console.log(`Mayor que (>): ${a} > ${b}`, a > b);    // Mayor que
console.log(`Menor que (<): ${a} < ${b}`, a < b);    // Menor que
console.log(`Mayor o igual que (>=): ${a} >= ${b}`, a >= b); // Mayor o igual
console.log(`Menor o igual que (<=): ${a} <= ${b}`, a <= b); // Menor o igual


// 4. Operadores de Asignación Aritméticos
console.log("\n 4. Operadores de Asignación Aritméticos:");
let z = 7; 
z += 3; console.log("z += 3:", z); // z = 10
z -= 2; console.log("z -= 2:", z); // z = 8
z *= 2; console.log("z *= 2:", z); // z = 16
z /= 4; console.log("z /= 4:", z); // z = 4
z %= 3; console.log("z %= 3:", z); // z = 1
z **= 3; console.log("z **= 3:", z); // z = 1


// Operadores bit a bit y asignación
console.log("\nOperadores bit a bit y asignación:");
let bitX = 5; // 5 en binario: 0101
bitX &= 6; console.log("bitX &= 6:", bitX); // AND
/* 6 en binario es 0110
 * Operación AND bit a bit: 0101 & 0110 = 0100 (en decimal, 4) */
bitX = 4; bitX |= 2; console.log("bitX |= 2:", bitX); // OR
/* 4 en binario es 0100
 * 2 en binario es 0010
 * Operación OR bit a bit: 0100 | 0010 = 0110 (en decimal, 6) */
bitX = 6; bitX ^= 3; console.log("bitX ^= 3:", bitX); // XOR
/* 6 en binario es 0110
 * 3 en binario es 0011
 * Operación XOR bit a bit: 0110 ^ 0011 = 0101 (en decimal, 5) */
bitX = 5; bitX <<= 2; console.log("bitX <<= 2:", bitX); // Shift Left
/* 5 en binario es 0101
 * Desplanumber_Xar 2 posiciones a la inumber_Xquierda: 0101 << 2 = 10100 (en decimal, 20) */
bitX = 20; bitX >>= 2; console.log("bitX >>= 2:", bitX); // Shift Right
/* 20 en binario es 10100
 * Desplanumber_Xar 2 posiciones a la derecha: 10100 >> 2 = 0101 (en decimal, 5) */
bitX = -20; bitX >>>= 2; console.log("bitX >>>= 2:", bitX); // Shift Right sin signo
/* En binario (32 bits), -20 es representado como 11111111111111111111111111101100
 * Desplanumber_Xar 2 posiciones a la derecha sin signo: 00111111111111111111111111111011 (en decimal, 1073741819) */



// 5. Operadores de Identidad
console.log("\n 5. Operadores de Identidad:");
let obj1 = {a: 1};
let obj2 = {a: 1};

// Verifica si tienen el mismo valor
console.log(`Igualdad (==): obj1 == obj2 = `, obj1 == obj2);     // false, también porque son dos objetos distintos

// Verifica si son el mismo objeto
console.log(`Identidad (===): obj1 === obj2 =`, obj1 === obj2);  // false, porque son dos objetos distintos




//6. Operadores de Pertenencia
let obj = {a: 1};
// Verifica si una propiedad existe en un objeto
console.log("'a' in obj:", "a" in obj);  // true, porque la propiedad 'a' existe en obj

let arr = [1, 2, 3];
console.log("arr.includes(2):", arr.includes(2)); // true, porque 2 está en el arreglo


//7. Operadores de Bits
let p = 5, q = 3; // 5 es 0101 en binario, 3 es 0011
console.log("AND (&):", p & q); // 0101 & 0011 = 0001 (1 en decimal)
console.log("OR (|):", p | q);  // 0101 | 0011 = 0111 (7 en decimal)
console.log("XOR (^):", p ^ q); // 0101 ^ 0011 = 0110 (6 en decimal)


// 8. Operador Ternario (forma corta de un if-else)
let edad = 18;
let resultado = edad >= 18 ? "Mayor de edad" : "Menor de edad";
console.log(resultado);  // "Mayor de edad"





// 🌟 Estructuras de Control
/*
 * - Condicionales (if, else if, else), Condicional con operadores lógicos, 
 *   Switch, Bucles (for, while), Excepciones (try, catch, throw)
 */

// 1. Condicionales (if, else if, else)
console.log("\nEstructuras Condicionales (if, else if, else) - Tu Destino Numerado:");
let numero = Math.floor(Math.random() * 5) + 1; // Asigna un número aleatorio entre 1 y 5.
console.log(`Tu número del destino es: ${numero}`);
if (numero === 1) {
    console.log("✨ Has recibido la bendición de un sabio. Tu camino está iluminado por estrellas eternas.");
} else if (numero === 2) {
    console.log("⚔️ Encontraste una espada antigua enterrada en la roca. Ahora eres el elegido para liderar una guerra legendaria.");
} else if (numero === 3) {
    console.log("🌊 Un barco pirata aparece y te invita a una aventura en alta mar. ¡Cuidado con los tiburones!");
} else if (numero === 4) {
    console.log("🔥 El suelo tiembla y un volcán emerge frente a ti. Solo el más valiente puede cruzarlo.");
} else if (numero === 5) {
    console.log("🌌 Una puerta dimensional se abre ante ti. ¿Te atreverás a entrar y explorar lo desconocido?");
} else {
    console.log("🤔 Parece que tu destino es incierto. El universo espera que tomes una decisión pronto.");
}


// 2. Estructura de control condicional (switch)
console.log("\nEestructura de control condicional Switch - Tu día de la semana:");
let dia = Math.floor(Math.random() * 7) + 1; // Asigna un número aleatorio entre 1 y 7 para simular los días de la semana.
switch(dia) {
    case 1: console.log("☀️ Hoy es Lunes. El inicio de una nueva semana llena de oportunidades.");
        break;
    case 2: console.log("🌱 Hoy es Martes. El día perfecto para sembrar las semillas de tus sueños.");
        break;
    case 3: console.log("🌞 Hoy es Miércoles. La mitad de la semana, sigue avanzando.");
        break;
    case 4: console.log("🌟 Hoy es Jueves. El día ideal para planear la última parte de la semana.");
        break;
    case 5: console.log(`🎉 Hoy es Viernes. El cuerpo lo sabe, no lo sabe hay que decirle que el cuerpo no se manda solo 💅🏻 Jajaja`);
        break;
    case 6: console.log("🌙 Hoy es Sábado. El día perfecto para descansar y recargar energías.");
        break;
    case 7: console.log("🌌 Hoy es Domingo. Un día para reflexionar y prepararse para la semana que viene.");
        break;
    default:
        console.log("❗ Error: Día inválido.");
}


// 3. Iterativas (for, while, do-while)
console.log("\nEstructuras Iterativas:");
// Bucle FOR
for (let i = 0; i < 5; i++) {
    console.log("Iteración con FOR:", i);
}

// Bucle WHILE
let contador = 0;
while (contador < 3) {
    console.log("Iteración con WHILE:", contador);
    contador++;
}

// Bucle DO-WHILE
let num = 0;
do {
    console.log("Iteración con DO-WHILE:", num);
    num++;
} while (num < 2);

// 4. Manejo de excepciones
console.log("\nManejo de Excepciones:");
console.log("\nExcepciones:");
try {
    let resultado = 10 / 0; // Aunque no genera error, podemos lanzar uno manual
    if (!isFinite(resultado)) {
        throw new Error("¡No se puede dividir por cero!");
    }
} catch (error) {
    console.error("Error capturado:", error.message);
} finally {
    console.log("Esto siempre se ejecuta.");
}




 // 🌟 DIFICULTAD EXTRA: Imprimir números entre 10 y 55 (incluidos), pares, que no sean 16 ni múltiplos de 3
console.log(`\nDIFICULTAD EXTRA: Imprimir números entre 10 y 55 (incluidos), pares, que no sean 16 ni múltiplos de 3
Números entre 10 y 55 (pares, excluyendo el 16 y múltiplos de 3):
`);
for (let num = 10; num <= 55; num++) {
    if (num % 2 === 0 && num !== 16 && num % 3 !== 0) {
        console.log(num);
    }
}


