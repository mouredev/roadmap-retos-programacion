/*
 * EJERCICIO:
 * 1- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 *2 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 *3 - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// 1 

//Operadores Aritmeticos

let adicion = 6 + 4;
console.log(adicion);
let sustraccion = 9 - 3;
console.log(sustraccion);
let multiplicacion = 7 * 3;
console.log(multiplicacion);
let division = 4 / 2;
console.log(division);
let modulo = 10 % 3;
console.log(modulo);
let incremento = 10;
incremento++;
console.log(incremento);
let decremento = 10;
decremento--;
console.log(decremento);
let exponenciacion = 3 ** 4;
console.log(exponenciacion);

//Operadores de asignacion 

let asignacion = 12;
console.log(asignacion);
let adicionAsignacion = 30;
adicionAsignacion += 5;
console.log(adicionAsignacion);
let sustraccionAsignacion = 20;
sustraccionAsignacion -= 5;
console.log(sustraccionAsignacion);
let multiplicacionAsignacion = 2;
multiplicacionAsignacion *= 2;
console.log(multiplicacionAsignacion);
let divisionAsignacion = 10;
divisionAsignacion /= 2;
console.log(divisionAsignacion);
let moduloAsignacion = 15;
moduloAsignacion %= 3;
console.log(moduloAsignacion);
let expAsignacion = 2;
expAsignacion **= 8;
console.log(expAsignacion);


//Operadores de comparacion 

let igualdad = 5;
console.log(igualdad == 5);//true

let igualdadExtricto = 10;
console.log(igualdadExtricto === '10')//false
console.log(igualdadExtricto === 10)//true

let desigualdad = 15;
console.log(desigualdad != 15) //false
console.log(desigualdad != 5) //true

let desigualEstricto = 20;
console.log(desigualEstricto !== 20)//false
console.log(desigualEstricto !== '20')//true

let mayorque = 25;
console.log(mayorque > 20)//true
console.log(mayorque > 30)//false

let mayorOigual = 25;
console.log(mayorOigual >= 25)//true
console.log(mayorOigual >= 30)//false

let menorque = 25;
console.log(menorque < 35)//true
console.log(menorque < 15)//false

let menorOigual = 25;
console.log(menorOigual <= 25)//true
console.log(menorOigual <= 15)//false

//Operadoresm logicos 

console.log(true && false); //false   AND logico  &&
console.log(true || false); //true OR logico ||
console.log(!true); //false NOT logico !
let nulo = null ?? 'Es nulo o undefined';
console.log(nulo);// Es nulo o undefined
let NotNull = 200 ?? '200';
console.log(NotNull);// 200


//Operadores bit a bit

let and = 5 & 3; // 1 (0101 & 0011 = 0001)
let or = 5 | 3; // 7 (0101 | 0011 = 0111)
let xor = ~5; // -6 (~0101 = 1010)
let despIzquierda = 5 << 1; // 10 (0101 << 1 = 1010)
let despDerecha = 5 >> 1; // 2 (0101 >> 1 = 0010)
let despDerechaNoSigno = -5 >>> 1; // 2147483645

//Operadores de cadena

//concatenacion +
let nombre = 'Andy ';
let apellido = 'Fernandez ';
let edad = 35;

let concatenacion = nombre + apellido;
console.log(`Mi nombre es ${concatenacion}`);//Mi nombre es Andy Fernandez

//concatenacion de asignacion +=
nombre += apellido;
let nombreCompleto = nombre;
console.log(nombreCompleto);//Andy Fernandez

//Operadores de tipo

//typeof

console.log(typeof edad);//number
console.log(typeof nombre);//string

//instanceof

let miarray = [];
if (miarray instanceof Array) {
    console.log('True');
}

//in

let myObj = { candy: 150 }
console.log("candy" in myObj); //true

//Operador ternario

let age = 35;

let acces = (age <= 17) ? "Eres menor, acceso deneagado" : "Puedes entrar";
console.log(acces); //Puedes entrar 

// operador coma 
let a = 1, b = 2, c = 3;

//Operador de agrupacion ()

let sumaFirst = (5 + 5) * 2;
console.log(sumaFirst);

for (let index = 0; index < array.length; index++) {
    const element = array[index];

}

/* *2 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
*   que representen todos los tipos de estructuras de control que existan
*   en tu lenguaje:
*   Condicionales, iterativas, excepciones...
 */

//Estructuras de control de flujo

//(if,elseif,else)
let access = false;
let pass = 123456;
let keys = 3;

function checkUser() {
    let password = prompt("Introduce el password");
    if (pass == password && password !== "" && keys >= 0) {
        access = true;
        console.log("Puedes acceder");
        alert("Puedes acceder");
    } else if (keys === 0) {
        console.log("Agotado el máximo de intentos, vuelva a intentarlo más tarde");
        return alert("Agotado el máximo de intentos, vuelva a intentarlo más tarde");
    } else {
        alert("Password incorrecto");
        console.log("Acceso denegado, Password incorrecto");
        keys--;
        console.log(keys);
        checkUser();
    }
}

checkUser();


//switch

let fruit = "apple";

switch (fruit) {
    case "banana":
        console.log("Es una banana.");
        break;
    case "apple":
        console.log("Es una manzana.");
        break;
    case "orange":
        console.log("Es una naranja.");
        break;
    default:
        console.log("No es una fruta conocida.");
}

//for
for (let i = 0; i < 5; i++) {
    console.log(i);
}

//while

let count = 0;

while (count < 5) {
    console.log(count);
    count++;
}

//do... wile

do {
    console.log(count);
    count++;
} while (count < 5);

//for in (iterar sobre propiedades)

let person = { name: "John", age: 30, city: "New York" };

for (let key in person) {
    console.log(key + ": " + person[key]);
}

//for of (iterar sobre elementos)
let numbers = [15, 23, 36, 42, 544];
for (let number of numbers) {
    console.log(number);
}


//try, catch, finally 

try {
    let result = noexisto();
  } catch (error) {
    console.log("Se ha producido un error: " + error.message);
  } finally {
    console.log("Esto se ejecuta siempre, haya error o no.");
  }


/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 * */

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i)
    }
}
