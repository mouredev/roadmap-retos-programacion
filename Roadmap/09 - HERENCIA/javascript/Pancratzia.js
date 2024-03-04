/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

/*******************PARTE 1*******************/

/* Definición de la superclase Animal */

class Animal {
  constructor(sound) {
    this._sound = sound;
  }

  makeSound() {
    console.log(this._sound);
  }
}

/* Definición de las subclases Perro*/
class Dog extends Animal {
  constructor(breed) {
    super("Guaugau");
    this._breed = breed;
  }

  makeSound() {
    console.log(`Hi! I'm a dog. My breed is ${this._breed}. And my sound is: `);
    super.makeSound();
  }
}

/* Definición de las subclases Gato */
class Cat extends Animal {
  constructor(favFood) {
    super("Miau");
    this._favFood = favFood;
  }

  makeSound() {
    console.log(`Hi! I'm a cat. My favorite food is ${this._favFood}. And my sound is: `);
    super.makeSound();
  }
}

// Objetos de perro y gato
const dog = new Dog("Boxer");
dog.makeSound();

const cat = new Cat("Tuna");
cat.makeSound();
