// ESTRUCTURA DE DATOS
let numero_orden = [1, 3, 5, 2, 4]; // Array

console.log(numero_orden);
numero_orden.push(6); // Agregar un elemento al final
console.log(numero_orden);
numero_orden.pop(); // Eliminar el último elemento
console.log(numero_orden);
numero_orden.unshift(0); // Agregar un elemento al principio
console.log(numero_orden);
numero_orden.shift(); // Eliminar el primer elemento
console.log(numero_orden[1]);
numero_orden[4] = "Hola"; // Modificar un elemento y actualizar el array
console.log(numero_orden);
numero_orden.sort(); // Ordenar el array
console.log(numero_orden);
numero_orden.reverse(); // Invertir el orden del array
console.log(numero_orden);
numero_orden.splice(2, 1); // Eliminar un elemento en la posición 2
console.log(numero_orden);
numero_orden.splice(2, 0, 5); // Agregar un elemento en la posición 2
console.log(numero_orden);
numero_orden.lastIndexOf(5); // Buscar la última posición de un elemento
console.log(numero_orden);

// Objeto
let persona = {
  nombre: "Juan",
  edad: 25,
  direccion: {
    calle: "Av. Siempre Viva",
    numero: 123,
    ciudad: "Springfield",
  },
};

// Map
let map = new Map().set("nombre", "Juan").set("edad", 25).set("direccion", {
  calle: "Av. Siempre Viva",
  numero: 123,
  ciudad: "Springfield",
});

// Set
let set = new Set().add("Juan").add(25);

set.add("Jose");
set.add(89);
console.log(set);

// Clase
class Persona {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }
}

// Promesa
let output = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Hola mundo");
  }, 2000);
});
