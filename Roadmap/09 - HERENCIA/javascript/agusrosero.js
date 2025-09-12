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

// EJERCICIO:
class Animal {
  constructor() {
    console.log("Clase Animal");
  }
}

const a1 = new Animal();

class Perro extends Animal {
  sonido() {
    console.log("Wuau! Wuau!");
  }
}

const b1 = new Perro();
b1.sonido();

class Gato extends Animal {
  sonido() {
    console.log("Miau, Miau!");
  }
}

const c1 = new Gato();
c1.sonido();
