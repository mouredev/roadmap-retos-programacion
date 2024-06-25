/* -- exercise */
// -- by value
let a = 5;
let b = a;

b = 10;
console.log(a);
console.log(b);

// by reference
let obj1 = { name: "Alice" };
let obj2 = obj1;

obj2.name = "Bob";
console.log(obj1.name);
console.log(obj2.name);

// Passing Variables to Functions
// by value
function changeValue(x) {
  x = 10;
}

let valueA = 5;
changeValue(valueA);
console.log(valueA);

// by reference
function changeObject(obj) {
  obj.name = "Charlie";
}

let object1 = { name: "Alice" };
changeObject(object1);
console.log(object1.name);

/* -- extra challenge */
function swapByValue(x, y) {
  let temp = x;
  x = y;
  y = temp;
  return [x, y];
}

let value1 = 10;
let value2 = 20;

let [new1, new2] = swapByValue(value1, value2);

console.log("Original values: value1 =", value1, ", valueB =", value2);
console.log("Swapped values: newA =", new1, ", newB =", new2);

function swapByReference(obj1, obj2) {
  let temp = obj1.value;
  obj1.value = obj2.value;
  obj2.value = temp;
  return [obj1, obj2];
}

let objectA = { value: "Hello" };
let objectB = { value: "World" };

let [newObjectA, newObjectB] = swapByReference(objectA, objectB);

console.log("Original values: objectA.value =", objectA.value, ", objectB.value =", objectB.value);
console.log("Swapped values: newObjectA.value =", newObjectA.value, ", newObjectB.value =", newObjectB.value);
