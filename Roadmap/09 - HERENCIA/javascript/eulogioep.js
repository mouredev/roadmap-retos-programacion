// Ejemplo de implementación del concepto de herencia en JavaScript

// Definición de la clase base (superclase) Animal
class Animal {
    constructor(especie, sonido) {
      this.especie = especie;
      this.sonido = sonido;
    }
  
    // Método que muestra el sonido que hace el animal
    hacerSonido() {
      return `El ${this.especie} hace: ${this.sonido}`;
    }
  }
  
  // Definición de la subclase Perro
  class Perro extends Animal {
    constructor(nombre, especie, sonido) {
      super(especie, sonido); // Llamada al constructor de la superclase
      this.nombre = nombre;
    }
  
    // Método exclusivo de la subclase Perro
    ladrar() {
      return `${this.nombre} lanza un ladrido`;
    }
  }
  
  // Definición de la subclase Gato
  class Gato extends Animal {
    constructor(nombre, especie, sonido) {
      super(especie, sonido); // Llamada al constructor de la superclase
      this.nombre = nombre;
    }
  
    // Método exclusivo de la subclase Gato
    maullar() {
      return `${this.nombre} emite un maullido`;
    }
  }
  
  // Ejemplo de implementación adicional (dificultad extra)
  // Definición de la clase base (superclase) Empleado
  class Empleado {
    constructor(id, nombre) {
      this.id = id;
      this.nombre = nombre;
    }
  }
  
  // Definición de la subclase Gerente que hereda de Empleado
  class Gerente extends Empleado {
    constructor(id, nombre, subordinados) {
      super(id, nombre);
      this.subordinados = subordinados;
    }
  
    // Método exclusivo de la subclase Gerente
    informarSobreSubordinados() {
      let informacion = `El gerente ${this.nombre} tiene a los siguientes subordinados: \n`;
      this.subordinados.forEach((subordinado) => {
        informacion += ` - ${subordinado.nombre}\n`;
      });
      return informacion;
    }
  }
  
  // Definición de la subclase GerenteDeProyectos que hereda de Empleado
  class GerenteDeProyectos extends Empleado {
    constructor(id, nombre, proyectos) {
      super(id, nombre);
      this.proyectos = proyectos;
    }
  
    // Método exclusivo de la subclase GerenteDeProyectos
    informarSobreProyectos() {
      let informacion = `El gerente de proyectos ${this.nombre} tiene los siguientes proyectos: \n`;
      this.proyectos.forEach((proyecto) => {
        informacion += ` - ${proyecto}\n`;
      });
      return informacion;
    }
  }
  
  // Definición de la subclase Programador que hereda de Empleado
  class Programador extends Empleado {
    constructor(id, nombre, lenguajes) {
      super(id, nombre);
      this.lenguajes = lenguajes;
    }
  
    // Método exclusivo de la subclase Programador
    informarSobreLenguajes() {
      let informacion = `El programador ${this.nombre} domina los siguientes lenguajes: \n`;
      this.lenguajes.forEach((lenguaje) => {
        informacion += ` - ${lenguaje}\n`;
      });
      return informacion;
    }
  }
  
  // Ejemplo de uso
  let perro = new Perro("Lucky", "Perro", "Gua");
  console.log(perro.hacerSonido()); // El Perro hace: Gua
  console.log(perro.ladrar()); // Lucky lanza un ladrido
  
  let gato = new Gato("Whiskers", "Gato", "Miau");
  console.log(gato.hacerSonido()); // El Gato hace: Miau
  console.log(gato.maullar()); // Whiskers emite un maullido
  
  let gerente = new Gerente(1, "Juan Perez", [new Programador(2, "Maria Rodriguez", ["JavaScript", "Python"])]);
  console.log(gerente.informarSobreSubordinados());
  
  let gerenteProyectos = new GerenteDeProyectos(3, "Luis Martinez", ["Proyecto A", "Proyecto B"]);
  console.log(gerenteProyectos.informarSobreProyectos());
  
  let programador = new Programador(4, "Karla Sanchez", ["JavaScript", "Python"]);
  console.log(programador.informarSobreLenguajes());