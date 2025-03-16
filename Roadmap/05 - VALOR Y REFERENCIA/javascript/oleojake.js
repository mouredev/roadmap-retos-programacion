/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 */

// Asignación por Valor en tipos PRIMITIVOS
let nombre = "Pablo";
let nombre1 = nombre;
nombre += " Marzal";
console.log(nombre); // Pablo Marzal
console.log(nombre1); // Pablo

let edad = 25;
let edad1 = edad;
edad = edad + 5;
console.log(edad); // 30
console.log(edad1); // 25

// Asignación por Referencia en Arrays y Objetos. Hacen referencia al mismo espacio de memoria

let myArray = [1, 2];
let myArray2 = myArray;

myArray.push(3);
console.log(myArray); // [1, 2, 3]
console.log(myArray2); // [1, 2, 3]

let myObject = {
    nombre: "Pablo",
    edad: 25
};
let myObject1 = myObject;

myObject.edad = 30;
console.log(myObject); // {nombre: 'Pablo', edad: 30 }
console.log(myObject1); // {nombre: 'Pablo', edad: 30 }

// Función variable por VALOR

function multiplicar(number) {
    number = number * 2;
    return number;
}

let original = 10;
let resultado = multiplicar(original);

console.log(original); // --> 10 El valor original no cambia
console.log(resultado); // 20

// Función variable por REFERENCIA

// Los arrays se comportan como objetos

let myPerson = {
    nombre: "Pablo",
    edad: 25
};

function cumpleaños (persona){
    persona.edad = persona.edad + 1;
}
console.log(myPerson.edad); // Inicialmente es 25
cumpleaños(myPerson); // Llamamos a la funcion pasando un objeto (por referencia)
console.log(myPerson.edad); // --> 26 cambia la edad en el objeto original, fuera de la función aunque no la hayamos mencionado

/* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */



//EXTRA
// Por Valor
let fruta1 = "Melocotón";
let fruta2 = "Uva";

function cambioValor (param1, param2){
    let temp = param1;
    param1 = param2;
    param2 = temp;
    return [param1, param2];
}

let newFruta1 = cambioValor(fruta1, fruta2)[0];
let newFruta2 = cambioValor(fruta1, fruta2)[1];

console.log(fruta1); // Melocotón. El original no ha cambiado
console.log(fruta2); // Uva. El original no ha cambiado
console.log(newFruta1); // Uva. Aquí sí que se han invertido porque es una nueva variable
console.log(newFruta2); // Melocotón. Aquí también

// Por Referencia

let fruta1Object = {
    nombre: 'Melocotón',
}

let fruta2Object= {
    nombre: 'Uva',
}

function cambioReferencia (obj1, obj2){
    let aux = obj1.nombre ;
    obj1.nombre = obj2.nombre;
    obj2.nombre = aux;
    return [obj1, obj2];
}

console.log(fruta1Object);
console.log(fruta2Object);
let newFrutas = cambioReferencia (fruta1Object, fruta2Object);
console.log(newFrutas[0]);
console.log(newFrutas[1]);
// Los originales cambian de orden también porque se modifica el espacio en memoria no el valor
console.log(fruta1Object);
console.log(fruta2Object);