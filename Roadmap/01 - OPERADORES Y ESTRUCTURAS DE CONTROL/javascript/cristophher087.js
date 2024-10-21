//Operadores aritmeticos

//Suma (+)

let a = 1;
let b = 2;

console.log("Los operadores logicos son los siguientes:");
console.log(`a + b = ${a + b}     suma`);
console.log(`a - b = ${a - b}     resta`);
console.log(`a * b = ${a * b}     multiplicación`);
console.log(`a / b = ${a / b}     divición`);
console.log(`a % b = ${a % b}     `);
console.log(`a ** b = ${a ** b}   potencia`);
console.log(`a++ = ${a++}       incremento`);
console.log(`b-- = ${b--}       decremento`);

//operadores de asignación

let x = 5; // Asignación simple
x += 3;    // Equivale a x = x + 3
console.log(x); //  8

x -= 2;    // Equivale a x = x - 2
console.log(x); //  6

x *= 4;    // Equivale a x = x * 4
console.log(x); //  24

x /= 6;    // Equivale a x = x / 6
console.log(x); //  4

x %= 3;    // Equivale a x = x % 3
console.log(x); //  1

x **= 3;   // Equivale a x = x ** 3
console.log(x); //  1

//Operadores de asignación [true, false]

let m = 10;     //entero
let n = '10';   //cadena de caracteres

console.log(m == n);  //(compara solo el valor)
console.log(m === n); //(compara valor y tipo)
console.log(m != n);  //false
console.log(m !== n); //true

console.log(m > 5);
console.log(m >= 10);
console.log(m < 15);
console.log(m <= 9);

//Operadores logicos

let p = true;
let q = false;

// Operador AND
console.log(p && q);

// Operador OR
console.log(p || q);

// Operador NOT
console.log(!p);
console.log(!q);

//Operadores de cadena

let saludo = "Hola";
let quienSaluda = "Cristopher";

let mensajeUno = saludo + ", " + quienSaluda + "!";
console.log(mensajeUno);

// Con plantillas literales
let mensajeTemplate = `${saludo}, ${nombre}!`;
console.log(mensajeTemplate);

let r = 5;  // En binario: 0101
let s = 3;  // En binario: 0011

console.log(r & s); //      1   (0001)
console.log(r | s); //      7   (0111)
console.log(r ^ s); //      6   (0110)
console.log(~r);    //      -6  (inverso de 0101 es 1010 en complemento a dos)
console.log(r << 1); //     10  (0101 << 1 = 1010)
console.log(r >> 1); //     2   (0101 >> 1 = 0010)
console.log(r >>> 1); //    2   (0101 >>> 1 = 0010)

/*
Operador ternario
Es una forma abreviada de una declaración if-else. Evalúa una condición y retorna un valor según sea verdadera o falsa.
(condición ? valor_si_verdadero : valor_si_falso)
*/
let edad = 18;

let mensaje = (edad >= 18) ? "Eres mayor de edad." : "Eres menor de edad.";
console.log(mensaje); // Eres mayor de edad.

// Uso con asignación
let acceso = (edad >= 18) ? true : false;
console.log(acceso); //  true

/*
Determinan el tipo de una variable o valor.
-typeof: Retorna una cadena indicando el tipo de una variable.
-instanceof: Verifica si un objeto es una instancia de una determinada clase o constructor.
-new: Crea una instancia de un objeto.
-delete: Elimina una propiedad de un objeto.
*/
let texto = "Hola";
let numero = 42;
let objeto = { nombre: "Juan" };
let arreglo = [1, 2, 3];
let funcion = function () { };

console.log(typeof texto);    //  string
console.log(typeof numero);   //  number
console.log(typeof objeto);   //  object
console.log(typeof arreglo);  //  object
console.log(typeof funcion);  //  function

// Uso de instanceof
console.log(arreglo instanceof Array); //       true
console.log(objeto instanceof Object); //       true
console.log(funcion instanceof Function); //    true

// Uso de delete
delete objeto.nombre;
console.log(objeto); //  {}

/* 
Operador Spread (...)
Expande elementos de un arreglo u objeto en lugares donde se esperan múltiples elementos.
*/
// En arreglos
let frutas = ["manzana", "banana"];
let masFrutas = [...frutas, "naranja"];
console.log(masFrutas); // Output: ["manzana", "banana", "naranja"]

// En objetos
let persona = { nombre: "Ana", edad: 25 };
let nuevaPersona = { ...persona, ciudad: "Madrid" };
console.log(nuevaPersona); // Output: { nombre: "Ana", edad: 25, ciudad: "Madrid" }
/*
Operador Rest (...)
Recopila múltiples elementos y los agrupa en un solo arreglo o objeto.
*/
// En funciones
function sumar(a, b, ...resto) {
    return a + b + resto.reduce((acc, val) => acc + val, 0);
}

console.log(sumar(1, 2, 3, 4, 5)); // Output: 15

// En destructuración de objetos
let { nombre, ...otrosDatos } = persona;
console.log(nombre);      // Output: "Ana"
console.log(otrosDatos);  // Output: { edad: 25 }

/*
Otros operadores
Operador in
Verifica si una propiedad existe en un objeto.
*/
let coche = { marca: "Toyota", modelo: "Corolla" };
console.log("marca" in coche); // Output: true
console.log("color" in coche); // Output: false

/*
Operador ? (Nullish Coalescing Operator ??)
Retorna el valor del operando derecho si el operando izquierdo es null o undefined.
*/
let valor = null;
let resultado = valor ?? "Valor por defecto";
console.log(resultado); // Output: "Valor por defecto"

valor = 0;
resultado = valor ?? "Valor por defecto";
console.log(resultado); // Output: 0

/*
Operador ?. (Optional Chaining Operator)
Permite acceder a propiedades de objetos que podrían ser null o undefined sin causar errores.
*/
let usuario = {
    nombre: "Luis",
    direccion: {
        ciudad: "Barcelona"
    }
};

console.log(usuario.direccion?.ciudad); // Output: "Barcelona"
console.log(usuario.contacto?.telefono); // Output: undefined

/*
Ejercicio extra
*/

let cuenta = 10;

for (let cuenta = 10; cuenta <= 55; cuenta++) {
    if (cuenta % 3 === 0 || cuenta != 16) {
        console.log(`La cuenta es: ${cuenta}`);
    }
    else {
        console.log("---");
    }
}
