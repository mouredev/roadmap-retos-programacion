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

//Superclase Animal y subclases Perro y Gato:
class Animal {
    constructor(nombre) {
      this.nombre = nombre;
    }
  
    hablar() {
      console.log("**Sonido genérico de animal**");
    }
  }
  
  class Perro extends Animal {
    constructor(nombre, raza) {
      super(nombre);
      this.raza = raza;
    }
  
    hablar() {
      console.log("**Woof!**");
    }
  }
  
  class Gato extends Animal {
    constructor(nombre, raza) {
      super(nombre);
      this.raza = raza;
    }
  
    hablar() {
      console.log("**Meow!**");
    }
  }
  
  // Ejemplo de uso
  const perro1 = new Perro("Toby", "Labrador");
  perro1.hablar();
  
  const gato1 = new Gato("Luna", "Siamés");
  gato1.hablar();

  //Dificultad Extra: Jerarquía de Empresa de Desarrollo
  class Empleado {
    constructor(id, nombre) {
      this.id = id;
      this.nombre = nombre;
      this.empleadosACargo = [];
    }
  
    getInfo() {
      console.log(`ID: ${this.id}`);
      console.log(`Nombre: ${this.nombre}`);
    }
  }
  
  //Clase Gerente:
  class Gerente extends Empleado {
    constructor(id, nombre, departamento) {
      super(id, nombre);
      this.departamento = departamento;
    }
  
    getInfo() {
      super.getInfo();
      console.log(`Departamento: ${this.departamento}`);
    }
  }
  
  //Clase Gerente de Proyectos:
  class GerenteProyecto extends Gerente {
    constructor(id, nombre, departamento, proyectos) {
      super(id, nombre, departamento);
      this.proyectos = proyectos;
    }
  
    getInfo() {
      super.getInfo();
      console.log(`Proyectos: ${this.proyectos.join(", ")}`);
    }
  }
  
  //Clase Programador:
  class Programador extends Empleado {
    constructor(id, nombre, lenguajes) {
      super(id, nombre);
      this.lenguajes = lenguajes;
    }
  
    getInfo() {
      super.getInfo();
      console.log(`Lenguajes de programación: ${this.lenguajes.join(", ")}`);
    }
  }
  
  // Ejemplo de uso
  const gerente1 = new Gerente(1, "Ana", "Ventas");
  gerente1.getInfo();
  
  const gerenteProyecto1 = new GerenteProyecto(2, "Pedro", "Desarrollo", ["Proyecto X", "Proyecto Y"]);
  gerenteProyecto1.getInfo();
  
  const programador1 = new Programador(3, "María", ["JavaScript", "Python"]);
  programador1.getInfo();
  
  // Asignación de empleados a cargo
  gerente1.empleadosACargo.push(programador1);
  gerenteProyecto1.empleadosACargo.push(programador1);
  
  // Mostrar la información de los empleados a cargo del gerente
  console.log("Empleados a cargo del gerente:");
  for (const empleado of gerente1.empleadosACargo) {
    empleado.getInfo();
  }
  
  // Mostrar la información de los empleados a cargo del gerente de proyecto
  console.log("Empleados a cargo del gerente de proyecto:");
  for (const empleado of gerenteProyecto1.empleadosACargo) {
    empleado.getInfo();
  }