// ** EJERCICIO

// Por valor

let m = 10;
let n = m; // b es una copia del valor de a

m // 10
n // 10

n = 20;
m // 10 (a no cambia)
n // 20 (b cambia)

function modifyValue(x) {
    x = 20;
    x // 20
}

let y = 10;
modifyValue(y);
y // 10 (y no cambia)

// Por referencia

let o1 = {name: "Alice"};
let o2 = o1; // o2 es una referencia a o1

o1.name // Alice
o2.name // Alice

o2.name = "Bob";
o1.name // Bob (o1 cambia porque o2 es una referencia a o1)
o2.name // Bob

function modifyObject(obj) {
    obj.name = "Charlie";
    obj.name // Charlie
}

let person = {name: "Alice"};
modifyObject(person);
person.name // Charlie (person cambia)

// ** DIFICULTAD EXTRA ** -----------------------------------------------------------------------------------------------------------------------------------------------

// Intercambio por valor
function intercambioPorValor(val1, val2) {
    let temp = val1;
    val1 = val2;
    val2 = temp;
    return [val1, val2];
}

// Intercambio por referencia
function intercambioPorReferencia(ref1, ref2) {
    let temp = {...ref1}; // Clonamos el objeto para evitar modificar los originales
    ref1.name = ref2.name;
    ref2.name = temp.name;
    return [ref1, ref2];
}

// Variables primitivas (por valor)
let a = 5;
let b = 10;

let [newA, newB] = intercambioPorValor(a, b);
console.log(newA, newB); // 10, 5 (intercambiadas)
console.log(a, b); // 5, 10 (se mantienen iguales)

// Objetos (por referencia)
let obj1 = { name: "Alice" };
let obj2 = { name: "Bob" };
console.log(obj1.name, obj2.name); // Alice, Bob

let [newObj1, newObj2] = intercambioPorReferencia({ ...obj1 }, { ...obj2 });
console.log(newObj1.name, newObj2.name); // Bob, Alice
console.log(obj1.name, obj2.name); // Alice, Bob (se mantienen iguales)