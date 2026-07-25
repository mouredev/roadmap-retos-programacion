// Ejemplo de asignación "por valor"
let a = 10;
let b = a; // Se copia el valor de 'a' en 'b'
b = 20; // Cambiar 'b' no afecta a 'a'

console.log("Por valor:");
console.log("a:", a); // 10
console.log("b:", b); // 20

// Ejemplo de asignación "por referencia"
let obj1 = { value: 10 };
let obj2 = obj1; // Se copia la referencia de 'obj1' en 'obj2'
obj2.value = 20; // Cambiar 'obj2.value' afecta a 'obj1.value'

console.log("\nPor referencia:");
console.log("obj1:", obj1); // { value: 20 }
console.log("obj2:", obj2); // { value: 20 }


// Función con parámetros pasados "por valor"
function modifyValue(x) {
  x = x * 2; // Esto no afecta a la variable original
  console.log("Dentro de modifyValue:", x);
}

let num = 5;
modifyValue(num);
console.log("Después de modifyValue:", num); // 5

// Función con parámetros pasados "por referencia"
function modifyReference(obj) {
  obj.value = obj.value * 2; // Esto modifica el objeto original
  console.log("Dentro de modifyReference:", obj);
}

let myObj = { value: 5 };
modifyReference(myObj);
console.log("Después de modifyReference:", myObj); // { value: 10 }

/// Dificultad extra
function swapByValues (a,b) {
 return [b, a]
}

function swapByreference (a, b) {
    let temp = a.value
    a.value = b.value
    b.value = temp
}

let value1 = 5; let value2 = 10

let [newValue1, newValue2] = swapByValues(value1, value2)
console.log (`\nVariables por valor:`)
console.log (`valores orginales: ${value1}, ${value2}`)
console.log (`Nuevos valores: ${newValue1}, ${newValue2}`)

let myObj1 = {value: 5}; let myObj2 = {value: 10}
console.log (`\nVariables por referencia:`)
console.log (`referencias originales: ${myObj1.value}, ${myObj2.value}`)
swapByreference (myObj1, myObj2)
console.log (`referencias cambiadas: ${myObj1.value}, ${myObj2.value}`)

