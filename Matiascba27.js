// Reto numero 1: Operadores
// 1. Operadores aritmeticos
let a = 10;
let b = 5;
console.log(`Suma: ${a} + ${b} = ${a + b}`);
console.log(`Resta: ${a} - ${b} = ${a - b}`);
console.log(`Multiplicacion: ${a} * ${b} = ${a * b}`);
console.log(`Division: ${a} / ${b} = ${a / b}`);
console.log(`Modulo: ${a} % ${b} = ${a % b}`);
console.log(`Exponensiacion: ${a} ** ${b} = ${a ** b}`);
console.log(`Incremento: ${a}++ = ${++a}`);
console.log(`Decremento: ${b}-- = ${--b}`);

// 2. Operadores de Asignacion
let c = 10;
c += 2;  console.log("+=:", c);
c -= 5;  console.log("-=:", c);
c *= 10;  console.log("*=:", c);
c /= 4;  console.log("/=:", c);
c %= 8;  console.log("%=:", c);
c **= 12; console.log("**=:", c);

// 3. Operadores de Comparacion
console.log("Igual valor: ", 5 == "5");
console.log("Igual valor y tipo: ", 5 === "5");
console.log("No igual: ", 5 != "6");
console.log("No igual valor o tipo: ", 5 !== "5");
console.log("Mayor que: ", 7 > 3);
console.log("Menor que: ", 3 < 7);
console.log("Mayor o igual: ", 7 >= 7);
console.log("Menor o igual: ", 5 <= 7);

// 4. Operadores logicos
console.log("AND:", true && false);
console.log("OR:", true || false);
console.log("NOT:", !true); 

// 5. Operadores de cadena
console.log("Concatenacion:", "Hola" + " " + "Mundo");

// 6. Opreador condicional (Ternario)
let edad = 20;
let mensaje = (edad >= 18) ? 'Adulto' : 'Menor';
console.log("Ternario:", mensaje);

// 7. Operador de tipo
console.log("Tipo de dato: ", typeof 10);
console.log("Tipo de dato: ", typeof "Hola");
console.log("Tipo de dato: ", typeof true);
console.log("Tipo de dato: ", typeof null);
console.log("Tipo de dato: ", typeof undefined);
console.log("Tipo de dato: ", typeof [1, 2, 3]);
console.log("Tipo de dato: ", typeof function() {});
console.log("Tipo de dato: ", typeof Symbol('id'));

// 8. Operador de propagacion (Spread)
let array1 = [1, 2, 3];
let array2 = [...array1, 4, 5, 6];
console.log("Spread:", array2);

// Reto numero 2: Estructuras de control

// 1. Estructura condicionales

// if-else
let edad1 = 18;
if (edad >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");
}

// if-else if-else
let nota = 75;
if (nota >= 90) {
    console.log("Sobresaliente");
} else if (nota >= 70) {
    console.log("Notable");
} else if (nota >= 50) {
    console.log("Aprobado");
} else {
    console.log("Reprobado");    
}

// Switch
let dia = "Lunes";
switch (dia) {
    case "Lunes":
        console.log("Inicio de semana");
        break;
    case "Viernes":
        console.log("Fin de semana laboral");
        break;
    case "Sabado":
        console.log("Fin de semana");
        break;
    default:
        console.log("Dia entre semana");
}

// 2. Estructuras Iterativas
// for
for (let i = 0; i < 10; i++) {
    console.log("Iteracion for:", i);
}

// while
let contador = 0;
while (contador < 10) {
    console.log("Iteracion while:", contador);
    contador++;
}

// do while
let contador2 = 0;
do {
    console.log("Iteracion do while:", contador2);
    contador2++;
} while (contador2 < 10);

// for...of (Ietarar sobre arreglos)
let frutas = ["Manzana", "Pera", "Naranja"];
for (let fruta of frutas) {
    console.log("Fruta:", fruta);
}

// for...in (Ietarar sobre objetos)
let persona = {
    nombre : "Juan",
    edad : 30,
    ciudad : "Barcelona"
};
for (let propiedad in persona) {
    console.log(propiedad + ": " + persona[propiedad]);
}

// 3. Manejo de excepciones
try {
    // Código que puede fallar
    let resultado = 10 / 0;
    console.log("Resultado:", resultado);

    // Forzar un error
    throw new Error("Este es un error forzado");
} catch (error) {
    // Capturar y manejar la excepcion
    console.log("Se produjo un error:", error.message);
} finally {
    // Código que se ejecutara siempre haya error o no
    console.log("Esto se ejecuta siempre");
}

// DIFICULTAD EXTRA
console.log("------- Dificultad Extra-------- \n");

// Solucion 1: Usando un bucle for y condicionales
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}

// Solucion 2: Usando un bucle while
let num = 10;
while ( num <= 55) {
    if (num % 2 === 0 && num !== 16 && num % 3 !== 0) {
        console.log(num);
    }
    num++;
}