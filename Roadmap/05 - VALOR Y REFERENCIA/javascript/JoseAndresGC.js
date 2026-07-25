// Tipos de datos por valor

let a = 100;
let b = 200;
let c = b;

// Tipos de datos por referencia

let array1 = [1, 2, 3];
let array2 = array1;
array2.push(4);
let perro = {nombre: "Felipe", raza: "Pitbull"};

// ejemplo por valor

let numero = 10;

function duplicar(valor) {
    valor = 20;    
}

duplicar(numero); // numero sigue siendo 10
console.log(numero); // 10


// ejemplo por referencia

let persona = {nombre : "María"};

function cambiarNombre(persona) {
    persona.nombre = "José";
}

cambiarNombre(persona); // Ahora el nombre es "José"
console.log(persona.nombre); // "José"

// DIFICULTAD EXTRA:

let param1 = 10;
let param2 = 20;

// intercambio de valores por valor
function programa1(param1, param2) {
    let aux = param1;
    param1 = param2;
    param2 = aux;
    console.log(param1, param2);
    
}
programa1(param1, param2);
console.log(param1, param2); // [10, 20]

// intercambio de valores por referencia

let param3 = [1, 2, 3];
let param4 = [10, 20, 30];

function programa2(param3, param4) {
    let aux = param3;
    param3 = param4;
    param4 = aux;
    console.log(param3, param4);
}
programa2(param3, param4);
console.log(param3, param4); // [30, 40]