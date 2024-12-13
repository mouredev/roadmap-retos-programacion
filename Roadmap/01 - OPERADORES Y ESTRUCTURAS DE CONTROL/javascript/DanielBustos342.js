let a = 5;
let b = 2;

//! Operadores aritmeticos: ESTOS OPERADORES REALIZAN OPERACIONES MATEMATICAS SOBRE NUMEROS
console.log(`Operadores aritmeticos:`);
//* suma
let suma = a + b;
console.log(`Operador suma ${a} + ${b} = ${suma}`);
//* resta
let resta = a - b;
console.log(`Operador resta ${a} - ${b} = ${resta}`);
//* multiplicacion
let multiplicacion = a * b;
console.log(`Operador multiplicacion ${a} * ${b} = ${multiplicacion}`);
//* division
let division = a / b;
console.log(`Operador division ${a} / ${b} = ${division}`);
//* modulo
let modulo = a % b;
console.log(`Operador modulo ${a} % ${b} = ${modulo}`);
//* exponente
let exponente = a ** b;
console.log(`Operador exponente ${a} ^ ${b} = ${exponente}`);
//* incremento
let incremento = a;
console.log(`Operador incremento ${a} = ${++incremento}`);
//* decremento
let decremento = a;
console.log(`Operacion decremento ${a} = ${--decremento}`);
//! Operadores de asignacion : ASIGNAN VALORES A LAS VARIABLES
console.log(`Operadores de asignacion:`);
//* asignacion
let c = 10;
console.log(`Asignacion ( = ) ${c}`);
//* asignacion de adicion
c += 3;
console.log(`Asignacion de adicion ( += ) ${c}`);
//* asignacion de resta
let d = 20;
d -= 5;
console.log(`Asignacion de resta ( -= ) ${d}`);
//* asignacion de multiplicacion
d *= 2;
console.log(`Asignacion de multiplicacion ( *= ) ${d}`);
//* asignacion de division
d /= 2;
console.log(`Asignacion de division ( /= ) ${d}`);
//* asignacion de modulo
d %= 2;
console.log(`Asignacion de modulo ( %= ) ${d}`);
//* asignacion de explonente
let e = 5;
e **= 2;
console.log(`Asignacion de exponente ( **= ) ${e}`);
//! Operadores de comparacion: COMPARAN DOS VALORES Y DEVUELVEN UN VALOR BOOLEANO
console.log(`Operadores de comparacion:`);
//* igual
let x = 5;
let y = 5;
let z = 10;
console.log(`Igual ( == ) ${x} == ${y} = ${x == y}`);
//* no igual
console.log(`No igual ( != ) ${x} != ${z} = ${x != z}`);
//* estrictamente igual
console.log(`Estrictamente igual ( === ) ${x} === '5' = ${x === "5"}`);
//* estrictamente no igual
console.log(`Estrictamente no igual ( !== ) ${x} !== '5' = ${x !== "5"}`);
//! Operadores de relacion: COMPARAN DOS VALORES Y DEVUELVEN UN VALOR BOOLEANO
console.log(`Operadores de relacion:`);
//* mayor que
console.log(`Mayor que ( > ) ${x} > ${z} = ${x > z}`);
//* mayor o igual que
console.log(`Mayor o igual que ( >= ) ${x} >= ${z} = ${x >= z}`);
//* menor que
console.log(`Menor que ( < ) ${x} < ${z} = ${x < z}`);
//* menor o igual que
console.log(`Menor o igual que ( <= ) ${x} <= ${z} = ${x <= z}`);
//! Operadores logicos
console.log(`Operadores logicos:`);
//* AND
console.log(`Operador AND ${true} && ${false} = ${true && false}`);
//* OR
console.log(`Operador OR ${true} || ${false} = ${true || false}`);
//* NOT
console.log(`Operador NOT !${true} = ${!true}`);
//! Otros operadores
console.log(`Otros operadores:`);
//* Operador Condicional (ternario) (`? :`) Asigna un valor basado en una condicion
console.log(
  `Operador Condicional (ternario): a=${a} > b=${b} ${
    a > b ? "a es mayor que b" : "a no es mayor que b"
  }`
);
//* Operador tipo: devuelve el tipo de dato de una variable
console.log(`Operador tipo: typeof ${a} = ${typeof a}`);
//* Operador de eliminacion: elimina una propiedad de un objeto
let obj = { name: "Miguel", age: 25 };
console.log(obj);
console.log(`Operador de eliminacion: delete ${obj.name} = ${delete obj.name}`);
console.log(obj);

//! DIFICULTAD EXTRA (opcional): Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3

for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}
