/*
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
  (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan
  en tu lenguaje:
  Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

//Ejercicio

    //Operadores
    console.log('OPERADORES')

    //Aritméticos
console.log('- Operadores aritméticos');

console.log(`${2 + 2}`);
console.log(`${2 - 1}`);
console.log(`${2 * 3}`);
console.log(`${6 / 2}`);
console.log(`${5 % 2}`);
console.log(`${2 ** 3}`);

    //Lógicos
console.log('- Operadores lógicos');

console.log(`${2 || true || false}`); //or (devuelve el primer true (En este caso 2))
console.log(`${true && false}`); //and
console.log(`${!true}`); //not

    //Comparación
console.log('- Operadores de comparación');

console.log(`${2 < 5}`);
console.log(`${2 <= 5}`);
console.log(`${5 > 3}`);
console.log(`${5 >= 3}`);
console.log(`${2 == '2'}`);
console.log(`${3 === "3"}`);
console.log(`${2 != "2"}`);
console.log(`${3 !== "3"}`);

    //Asignación e identidad
console.log('- Operadores de asignación e identidad');

var a = 2;
var b = 3;
console.log(`${a}`); //a = 2
console.log(`${a += b}`); //2 + 3 = 5 = a
console.log(`${a -= b}`); //5 - 3 = 2 = a
console.log(`${a *= b}`); //2 * 3 = 6 = a
console.log(`${a /= b}`); //6 / 3 = 2 = a
console.log(`${b %= a}`); //3 % 2 = 1 = a
b = 3;
console.log(`${a **= b}`); //2 ** 3 = 8 = a
console.log(`${a === 8}`) // Identidad

    //Cadena
console.log('- Operador de cadena');

console.log('Sergio' + ' ' + 'García');

    //Ternario
console.log('- Operador ternario');

console.log((20 < 10) ? "20 es menor que 10" : "20 no es menor que 10");

    //Pertenencia
console.log('- Operador de pertenencia')

var myArray = [1, 2, 3, 4, 5]
console.log(3 in myArray)

    //Tipos
console.log('- Operadores de tipos');

var myVariable = ["Sergio", "David"];
console.log(typeof myVariable);
console.log(myVariable instanceof Array); //True si un objeto es una instancia de otro objeto

    //Bits
console.log('- Operadores de bits');

console.log(5 & 3); //AND a nivel de bits: 1
console.log(5 | 3); //OR a nivel de bits: 7
console.log(5 ^ 3); //XOR a nivel de bits: 6

//Estructuras de control
console.log('ESTRUCTURAS DE CONTROL');

    //Condicionales
console.log('- Condicionales');

let myName = "Sergio";

if (myName == "Jose") {
    console.log('Me llamo Jose');
} else if (myName == "Sergio") {
    console.log('Me llamo Sergio');
} else {
    console.log('No me llamo Jose ni Sergio');
};

    //Switch
console.log("- Switch");

switch (myName) {
    case "Jose":
        console.log("Me llamo Jose");
    case "Sergio":
        console.log("Me llamo Sergio");
};

    //Bucles For
console.log("- Bucles for");

for (let i = 1; i <= 5; i++) {
    console.log(i);
};

console.log("- Bucles for/of");

for (item of myArray) {
    console.log(item);
};

console.log("- Bucle for/in");
let myPerson = {
    name: "Sergio",
    surname: "García",
    age: 24,
    languages: [
        "Python",
        "JavaScript"
    ]
};

for (item in myPerson) {
    console.log(`${item}: ${myPerson[item]}`);
};

console.log("- Bucle forEach");

myArray.forEach(element => {
    console.log(element);
});

    //Bucles while
console.log("- Bucle while");

let i = 0;
let max = 5;

while (i <= max) {
    console.log(i);
    i += 1;
};

console.log("- Bucle do/while")

let e = 0;

do {
    console.log(e)
    e++;
} while (e <= max);

//Extra
console.log("EXTRA");

for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 & i != 16 & i % 3 != 0) {
        console.log(i);
    }
};