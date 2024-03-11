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
// clase padre
class Animal{
    constructor(nombre){
       this.nombre=nombre
    }
    emitirSonido() {
        console.log("Este animal hace un sonido");
      }
}
// clase hija
class Perro extends Animal {
    emitirSonido() {
      console.log("Guau guau");
    }
  }
  
  class Gato extends Animal {
    emitirSonido() {
      console.log("Miau miau");
    }
  }

  function imprimirSonido(animal) {
    animal.emitirSonido();
  }
  
  // Prueba
  let perro = new Perro("Firulais");
  let gato = new Gato("Michi");
  imprimirSonido(perro); // Guau guau
  imprimirSonido(gato);  // Miau miau



  class Empleado {
    constructor(id, nombre) {
      this.id = id;
      this.nombre = nombre;
    }
  }

  class Gerente extends Empleado {
    constructor(id, nombre) {
      super(id, nombre);
      this.empleadosACargo = [];
    }
  
    agregarEmpleado(empleado) {
      this.empleadosACargo.push(empleado);
    }
  }

  class GerenteDeProyectos extends Gerente {
    constructor(id,nombre){
        super(id,nombre)
        
    }
  }
  

  class Programador extends Empleado {
    constructor(id, nombre, lenguaje) {
      super(id, nombre);
      this.lenguaje = lenguaje;
    }
  }


let gerente = new Gerente(1, "Ana");
let gerenteProyectos = new GerenteDeProyectos(2, "Carlos");
let programador = new Programador(3, "Luis", "JavaScript");

gerente.agregarEmpleado(gerenteProyectos);
gerente.agregarEmpleado(programador);

