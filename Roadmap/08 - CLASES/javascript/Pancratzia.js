/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 *
 */

class Perro {
  constructor(nombre = "Tiffany", raza = "Poodle", edad = 8) {
    this._nombre = nombre;
    this._raza = raza;
    this._edad = edad;
  }

  get nombre() {
    return this._nombre;
  }

  set nombre(nombre) {
    this._nombre = nombre;
  }

  get raza() {
    return this._raza;
  }

  set raza(raza) {
    this._raza = raza;
  }

  get edad() {
    return this._edad;
  }

  set edad(edad) {
    this._edad = edad;
  }

  toString() {
    return `Nombre: ${this._nombre}
    Raza: ${this._raza}
    Edad: ${this._edad}`;
  }
}

const perro = new Perro();
console.log(perro.toString());

console.log("Pero espera... ¡ES EL CUMPLEAÑOS DE TIFFANY!")
perro.edad = 9;
console.log(perro.toString());
