// Asignación por valor
let var1 = 5;
let var2 = var1;
var2 = 10;
console.log(var1); // Output: 5
console.log(var2); // Output: 10

// Asignación por referencia (objetos)
let obj1 = {name: "John"};
let obj2 = obj1;
obj2.name = "Jane";
console.log(obj1.name); // Output: Jane
console.log(obj2.name); // Output: Jane

// Asignación por referencia (arrays)
let arr1 = [1, 2, 3];
let arr2 = arr1;
arr2.push(4);
console.log(arr1); // Output: [1, 2, 3, 4]
console.log(arr2); // Output: [1, 2, 3, 4]

// Funciones con paso por valor
function increment(num) {
  num++;
  return num;
}

let x = 5;
let y = increment(x);
console.log(x); // Output: 5
console.log(y); // Output: 6

// Funciones con paso por referencia
function changeName(obj) {
  obj.name = "Alice";
}

let person = {name: "Bob"};
changeName(person);
console.log(person.name); // Output: Alice

/*Dificultad Extra
En JavaScript, todos los parámetros se pasan por valor. Sin embargo, si pasas un objeto (incluyendo arrays y funciones), lo que se pasa es la referencia al objeto. Esto significa que si modificas las propiedades del objeto dentro de la función, esos cambios se reflejarán fuera de la función:
*/

// Programa 1: Pasando parámetros primitivos (por valor)
function swapValues(val1, val2) {
  let temp = val1;
  val1 = val2;
  val2 = temp;
  return [val1, val2];
}

let a = 5;
let b = 10;
console.log(`Original a: ${a}, b: ${b}`); // Original a: 5, b: 10

let [newA, newB] = swapValues(a, b);
console.log(`Swapped a: ${newA}, b: ${newB}`); // Swapped a: 10, b: 5
console.log(`After swap a: ${a}, b: ${b}`); // After swap a: 5, b: 10

// Programa 2: Pasando objetos (por referencia)
function swapObjectValues(obj) {
  let temp = obj.val1;
  obj.val1 = obj.val2;
  obj.val2 = temp;
  return {val1: obj.val1, val2: obj.val2};
}

let obj = {val1: 5, val2: 10};
console.log(`Original obj.val1: ${obj.val1}, obj.val2: ${obj.val2}`); // Original obj.val1: 5, obj.val2: 10

let newObj = swapObjectValues(obj);
console.log(`Swapped obj.val1: ${newObj.val1}, obj.val2: ${newObj.val2}`); // Swapped obj.val1: 10, obj.val2: 5
console.log(`After swap obj.val1: ${obj.val1}, obj.val2: ${obj.val2}`); // After swap obj.val1: 10, obj.val2: 5
