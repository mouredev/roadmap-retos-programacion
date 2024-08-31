/**
 * EJERCICIO
 */

// Datos por valor
let valueX = 5;
let valueY = valueX;
valueY += 15;

console.log(valueX);
console.log(valueY);

// Datos por referencia
let objectA = {
  valueX: 8,
  valueY: 2
}

let objectB = objectA;

objectA.valueX = 20;
objectA.valueY = 15;

console.table(objectA);
console.table(objectB);

// Función con dato por valor
function modifyValue(valueA) {
  valueA = 'Valor modificado';
  console.log(valueA);
}

let valueB = 'Valor inicial';
console.log(valueB);
modifyValue(valueB);
console.log(valueB);

// Función con dato por referencia
function modifyReference(objectA) {
  objectA.dato = 'dato modificado';
  console.log(objectA);
}

let objectX = {
  dato: 'dato inicial',
}

console.log(objectX);
modifyReference(objectX);
console.log(objectX);

/**
 * EXTRA
 */

// Valor

function replaceValue(valueX, valueY) {
  let aux = valueX;
  valueX = valueY;
  valueY = aux;
  return [valueX, valueY]
}

let name = "César";
let surname = "Carmona";
let [nameRep, surnameRep] = replaceValue(name, surname);

console.log(`Nombre: ${name}, Apellido: ${surname}`);
console.log(`Nombre reemplazado: ${nameRep}, Apellido reemplazado: ${surnameRep}`);

// Referencia

function replaceReference(referenceX, referenceY) {
  let aux = referenceX;
  referenceX = referenceY;
  referenceY = aux;
  return [referenceX, referenceY];
}

let fruits = ['apple', 'orange', 'banana', 'grape'];
let vegetables = ['tomato', 'carrot', 'onion', 'radish'];

let [fruitsRep, vegetablesRep] = replaceReference(fruits, vegetables);
console.log(`Vegetales: ${vegetables}`);
console.log(`Frutas: ${fruits}`);
console.log(`Vegetales reemplazados: ${vegetablesRep}`);
console.log(`Frutas reemplazados: ${fruitsRep}`);