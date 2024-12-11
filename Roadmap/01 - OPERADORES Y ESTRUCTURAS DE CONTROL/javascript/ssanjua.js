const dato = 5;
let a = 2;
let b = 10;
let algo = null;

// Operadores aritmeticos
console.log({ suma: 2 + 2 });
console.log({ resta: 2 - 1 });
console.log({ multiplicacion: 2 * 2 });
console.log({ division: 6 / 3 });
console.log({ modulo: 10 % 2 });

// Operadores logicos
console.log({ or: 2 || 4 });
console.log({ and: true && (dato <= 2) });
console.log({ not: !false });

// Operadores de asignacion
console.log((a += b)); // 12
console.log((a -= b)); // 2
console.log((a *= b)); // 20
console.log((a /= b)); // 2
console.log((a %= b)); // 2
console.log((a &= b)); // 2
console.log((a ^= b)); // 8
console.log((a |= b));  //10
console.log((a &&= b)); // 10
console.log((a ||= b)); // 10
console.log((a ??= b)); // 10

// Operadores de comparacion
console.log({ igual: 2 == 2 })
console.log({ estrictamenteIgual: 2 === '2' });
console.log({ desigual: 2 != '2' });
console.log({ estrictamenteDesigual: 2 !== 4 });
console.log({ mayorQue: 10 > 4 });
console.log({ menorQue: 5 < 9 });
console.log({ mayorOIgual: 10 <= 5 });
console.log({ menorOIgual: 7 <= 9 });

// Operadores de tipo
console.log("typeof a :", typeof a);
console.log("typeof 'name' :", typeof 'name');
let text = new String('Hello');
let num = new Number(28);
console.log("instanceof Number :", (num instanceof Number));
console.log("instanceof String :", (text instanceof String));

// Operador ternario
const age = (a + b) >= 18 ? 'yes' : 'no';
console.log(age);

// Operador de propagacion
const array = [2, 29, 99, 103];
const newArr = [...array, 1000, 2999];
console.log(newArr);

// Falsy
console.log(algo ?? "nada");


// Extra
function extra() {
  for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
      console.log(i);
    }
  }
};

extra();

