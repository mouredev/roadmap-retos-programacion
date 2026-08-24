// https://www.typescriptlang.org/

// Por valor: tipos primitivos se copian
let x: number = 10;
let y: number = x;
y = 20;
console.log(x); // 10
console.log(y); // 20

// Por referencia: objetos y arrays comparten referencia
const arr1: number[] = [1, 2, 3];
const arr2: number[] = arr1;
arr2.push(4);
console.log(arr1); // [1, 2, 3, 4]
console.log(arr2); // [1, 2, 3, 4]

const obj1: { value: number } = { value: 1 };
const obj2: { value: number } = obj1;
obj2.value = 99;
console.log(obj1.value); // 99
console.log(obj2.value); // 99

// Paso por valor en función
function incrementValue(n: number): number {
  n += 1;
  return n;
}
let num: number = 5;
const newNum: number = incrementValue(num);
console.log(num);    // 5
console.log(newNum); // 6

// Paso por referencia en función
function appendItem(list: number[], item: number): void {
  list.push(item);
}
const original: number[] = [1, 2, 3];
appendItem(original, 4);
console.log(original); // [1, 2, 3, 4]

// Dificultad extra: swap por valor y por referencia

// Swap por valor (primitivos, retorna nuevos valores)
function swapByValue(a: number, b: number): [number, number] {
  return [b, a];
}
let p: number = 1;
let q: number = 2;
const [newP, newQ] = swapByValue(p, q);
console.log(p, q);       // 1 2 (sin cambios)
console.log(newP, newQ); // 2 1

// Swap por referencia (objeto compartido)
type Pair = { a: number; b: number };

function swapByRef(pair: Pair): void {
  const temp = pair.a;
  pair.a = pair.b;
  pair.b = temp;
}
const pair: Pair = { a: 10, b: 20 };
console.log(pair.a, pair.b); // 10 20
swapByRef(pair);
console.log(pair.a, pair.b); // 20 10
