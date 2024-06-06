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

// Superclase Animal
class Animal {
  nombre: string;

  constructor(nombre: string) {
    this.nombre = nombre;
  }

  // Método para imprimir el sonido del animal
  hacerSonido(): void {
    console.log('El animal hace un sonido');
  }
}

// Subclase Perro que hereda de Animal
class Perro extends Animal {
  constructor(nombre: string) {
    super(nombre);
  }

  // Método para imprimir el ladrido del perro
  hacerSonido(): void {
    console.log(`El perro ${this.nombre} hace guau`);
  }
}

// Subclase Gato que hereda de Animal
class Gato extends Animal {
  constructor(nombre: string) {
    super(nombre);
  }

  // Método para imprimir el maullido del gato
  hacerSonido(): void {
    console.log(`El gato ${this.nombre} hace miau`);
  }
}

// Crear instancias de Perro y Gato
const miPerro: Perro = new Perro('Bobby');
const miGato: Gato = new Gato('Whiskers');

// Llamar al método para hacer sonido de cada animal
miPerro.hacerSonido(); // Imprime: El perro Bobby hace guau
miGato.hacerSonido(); // Imprime: El gato Whiskers hace miau

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
