/* -- exercise */
// -- by value
let a: number = 5;
let b: number = a;

b = 10;
console.log(a);
console.log(b);

// by reference
interface Person {
  name: string;
}

let obj1: Person = { name: "Alice" };
let obj2: Person = obj1;

obj2.name = "Bob";
console.log(obj1.name);
console.log(obj2.name);

// Passing Variables to Functions
// by value
function changeValue(x: number): void {
  x = 10;
}

let valueA: number = 5;
changeValue(valueA);
console.log(valueA);

// by reference
function changeObject(obj: Person): void {
  obj.name = "Charlie";
}

let object1: Person = { name: "Alice" };
changeObject(object1);
console.log(object1.name);

/* -- extra challenge */
function swapByValue(x: number, y: number): [number, number] {
  let temp: number = x;
  x = y;
  y = temp;
  return [x, y];
}

let value1: number = 10;
let value2: number = 20;

let [new1, new2] = swapByValue(value1, value2);

console.log("Original values: value1 =", value1, ", valueB =", value2);
console.log("Swapped values: newA =", new1, ", newB =", new2);

interface ValueContainer {
  value: string;
}

function swapByReference(obj1: ValueContainer, obj2: ValueContainer): [ValueContainer, ValueContainer] {
  let temp: string = obj1.value;
  obj1.value = obj2.value;
  obj2.value = temp;
  return [obj1, obj2];
}

let objectA: ValueContainer = { value: "Hello" };
let objectB: ValueContainer = { value: "World" };

let [newObjectA, newObjectB] = swapByReference(objectA, objectB);

console.log("Original values: objectA.value =", objectA.value, ", objectB.value =", objectB.value);
console.log("Swapped values: newObjectA.value =", newObjectA.value, ", newObjectB.value =", newObjectB.value);
