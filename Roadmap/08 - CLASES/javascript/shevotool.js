/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 */

class automovil {
  constructor(marca, modelo, color) {
    this.marca = marca;
    this.modelo = modelo;
    this.color = color;
  }

  imprimirAtributos() {
    return `Marca:${this.marca} Modelo:${this.modelo} Color:${this.color}`;
  }
}

const ford = new automovil("Ford", "Focus", "Azul");
const toyota = new automovil("Toyota", "Land Cruiser", "Blanco");

console.log(ford.imprimirAtributos());
console.log(toyota.imprimirAtributos());

toyota.color = "gris";
console.log(toyota.color);
console.log(toyota);
