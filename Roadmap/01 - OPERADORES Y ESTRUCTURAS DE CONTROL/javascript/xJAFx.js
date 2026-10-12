// Suma
console.log("Suma 3 + 3 = " + (3 + 3));

// Resta
console.log("Resta 3 - 3 = " + (3 - 3));

// Multiplicación
console.log("Multiplicación 3 * 3 = " + (3 * 3));

// División
console.log("División 3 / 3 = " + (3 / 3));

// Módulo
console.log("Módulo 3 % 3 = " + (3 % 3));

// Potencias
console.log("Potencias 3 ** 3 = " + (3 ** 3));

// Incremento
let incrementVariable = 3;
incrementVariable++;
console.log(incrementVariable);

// Reducción
let decrementVariable = 3;
decrementVariable--;
console.log(decrementVariable);

// Asignación de Valor
let assignValue = 3;
console.log(assignValue);

// Asignación con Adición
let addValue = 0;
addValue += 3;
console.log(addValue);

// Asignación con Resta
let reduceValue = 3;
reduceValue -= 3;
console.log(reduceValue);

// Asignación con Multiplicación
let multiplyValue = 3;
multiplyValue *= 3;
console.log(multiplyValue);

// Asignación con División
let divideValue = 9;
divideValue /= 3;
console.log(divideValue);

// Asignación con Potencia
let testNum = 2;
let exponentNum = 3;
console.log(testNum **= exponentNum);

// Asignación con Módulo
testNum = 9;
let remainderNum = 3;
console.log(testNum %= remainderNum);

// Igualdad. Este operador de comparación sólo chequea si el valor es igual.
let num1 = 3;
let num2 = "3";
console.log(num1 == num2);

// No Igual. Este operador sólo chequea si el valor es diferente.
let num3 = 3;
let num4 = 4;
console.log(num3 != num4);

// Igualdad Estricta. Este operador, a diferencia de la Igualdad, chequea tanto el valor como el tipo de datos, ambos deben ser iguales.
num1 = 3;
num2 = "3";
console.log(num1 === num2);

// No Igual Estricto. Este tipo de operador chequea tanto tipo de datos como el valor.
num3 = "3";
num4 = "4";
console.log(num3 !== num4);

// Menor Que... Compara si el valor de la izquierda es menor que el valor de la derecha
let num5 = 3;
let num6 = 5;
console.log(num5 < num6);

// Mayor Que... Compara si el valor de la izquierda es mayor que el valor de la derecha
num5 = 5;
num6 = 3;
console.log(num5 > num6);

// Menor o Igual Que... Compara si el valor de la izquierda es menor o igual al valor de la derecha
let num7 = 5;
let num8 = 8;
console.log(num7 <= num8);

//Mayor o Igual Que... Compara si el valor de la izquierda es mayor o igual al valor de la derecha
num7 = 4;
num8 = 9;
console.log(num7 >= num8);

// Desplazamiento a la Izquierda
let num9 = 5;
let num10 = 4;
console.log(num9 << num10);

// Desplazamiento a la Izquierda con Asignación
num9 = 5;
num9 <<= 4;
console.log(num9);

// Desplazamiento a la Derecha
let num11 = 8;
let num12 = 2;
console.log(num11 >> num12);

// Desplazamiento a la Derecha con Asignación
num11 = 8;
num11 >>= 2;
console.log(num11);

// Desplazamiento a la Derecha sin Signo. Similar al Desplazamiento a la Derecha, pero éste añade la misma cantidad de ceros a la izquierda como el segundo valor sea, lo que da siempre un número positivo
let num13 = -8;
let num14 = 2;
console.log(num13 >>> num14);

// Desplazamiento a la Derecha sin Signo con Asignación
num13 = -8;
num13 >>>= 2;
console.log(num13);

// Suma Unaria. Intenta Convertir el valor a tipo numérico
let x = "2";
console.log(+x);

// Negación Unaria. Intenta Convertir el valor a tipo numérico y lo invierte
let y = "2";
console.log(-y);

// Negación Bit a Bit. Invierte el valor de cada bit
let z = 3;
console.log(~z);

// Negación Lógica
let a = false;
console.log(!a);

// Tipo
let b = "Texto";
console.log(typeof(b));

// Eliminación
const person = {
    name: "John",
    age : 30
};
delete person.age;
console.log(person);

// Vacío
let c = 2;
console.log(void c);

// Instancia De...
const person2 = {
    name: "John",
    age: 30
}
console.log(person2 instanceof Object);

// Pertenencia
const person3 = {
    name : "Jane",
    age : 30
}
console.log("name" in person3);

// Y a nivel de Bits. Compara dos valores a nivel de bits, y regresa el valor en que ambos valores posean bits con valor en 1
let d = 6;
let e = 3;
console.log(d & e);

// Y a Nivel de Bits con Asignación
d = 6;
d &= 3;
console.log(d);

// O a nivel de Bits. Compara dos valores a nivel de bits y regresa el valor en que cualquiera de los dos valores posea bits con valor en 1
d = 6;
e = 3;
console.log(d | e);

// O a nivel de Bits con asignación
d = 6;
d |= 3;
console.log(d);

// O Exclusivo a nivel de Bits. Compara dos valores a nivel de bits y regresa el valor, en cuya posición cualquiera de los dos valores (pero no ambos) posean bits con valor en 1
d = 6;
e = 3;
console.log(d ^ e);

// O Exclusivo a nivel de Bits con asignación
d = 6;
d ^= 3;
console.log(d);

// Lógico Y... Compara dos valores, dando respuesta verdadera si ambos son correctos
let f = 3;
let g = 1 + 2;
console.log(f && g === 3);

// Lógico Y... con Asignación. Asigna el valor a la derecha sólo si el valor de la izquierda es "Truthy"
f = 3;
f &&= 1+2;
console.log(f);

// Lógico O... Compara dos valores, dando respuesta verdadera si cualquiera de los dos es correcto
f = 3;
g = 2;
console.log(f === 2 || g === 2);

// Lógico O... con Asignación. Asigna el valor de la derecha al valor de la izquierda sólo si el valor de la izquierda es "Falsy"
f = 0;
f ||= 40;
console.log(f);

// Coalescencia Nula. Regresa el valor de la derecha si el valor de la izquierda es nulo o indefinido. De lo contrario regresa el valor de la izquierda
let h = null;
let i = 10;
console.log(h ?? i);

// Coalescencia Nula con Asignación. Asigna el valor de la derecha al valor de la izquierda sólo si éste es nulo o indefinido
h = null;
h ??= 30;
console.log(h);

// Condicional Ternario. Comparamos dos valores contra un primer valor para regresar una respuesta. Si la condición (el primer valor) se cumple, la respuesta entregada es el segundo valor, de lo contrario, la respuesta a entregar es el tercer valor
let j = 8;
console.log(j >= 8 ? "cat" : "dog");

let test = Math.floor(Math.random() * (10 - 1 + 1));
console.log(test);

if (test === 10) {
    console.log("Perfect Score");
} else if (test >= 5 && test < 10) {
    console.log("Good Score")
} else if (test >= 3 && test < 5) {
    console.log("Bad Score")
} else {
    console.log("Very Bad Score");
}

let strayCats = 10;
while(strayCats > 0) {
    console.log(strayCats);
    strayCats--;
}
if (strayCats === 0) {
    console.log("Every stray cat has been adopted!");
}

let count = 0;
for(let i = 0; i < 10; i++) {
    count++;
    console.log(count);
}


switch("Cat") {
    case "Dog":
        console.log("Dog");
        break;
    case "Lion":
        console.log("Lion");
        break;
    case "Cat":
        console.log("Cat");
        break;
    case "Mouse":
        console.log("Mouse");
        break;
}


// Ejercicio Extra

for(let i = 10; i < 55; i += 2) {
    if (i === 16 || i % 3 === 0) {
    } else {
        console.log(i);
    }
}