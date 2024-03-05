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


/* Soluciones */


class Animal {
  constructor(nombre, raza, color, sonido) {
    this.nombre = nombre;
    this.raza = raza;
    this.color = color;
    this._sonido = sonido; // Prefijo _ para indicar que es un atributo protegido
  }

  // Método para imprimir los atributos
  informacion() {
    let informacion = `
    Nombre: ${this.nombre}
    Raza: ${this.raza}
    Color: ${this.color}
    `;
    if (this.clase) {
      informacion += `Clase: ${this.clase}`;
    }
    return informacion;
  }

  // Getter para obtener el sonido que hace el animal
    get sonido() {
    return `
      ${this._sonido}
    `;
  }
}

class Perro extends Animal {
  constructor(nombre, raza, color, sonido) {
    super(nombre, raza, color, sonido);
    this.clase = "Perro\n";
  }
}

class Gato extends Animal {
  constructor(nombre, raza, color, sonido) {
    super(nombre, raza, color, sonido);
    this.clase = "Gato\n";
  }
}

const vaca = new Animal("Clementina", "Holstein", "Blanco y Negro", "Muuuu!!");
console.log(vaca.informacion());

const perro = new Perro("Rex", "Pastor Alemán", "Negro", "Woof Woof!!");
console.log(perro.sonido);

const gato = new Gato("Chimuelo", "Siamés", "Amarillo", "Meoww!!");
console.log(gato.informacion());



/* Extra - Opcional */



class Empleado {
  constructor(nombre, identificador) {
    this.nombre = nombre;
    this.identificador = identificador;
  }

  presentacion() {
    return `Me llamo ${this.nombre}, mi rol en la empresa es ser ${this.identificador}.\n`;
  }
}

class Gerente extends Empleado {
  constructor(nombre, empleados = []) {
    super(nombre, "Gerente");
    this.empleados = empleados;
  }

  presentacion() {
    let info = super.presentacion();
    if (this.empleados.length > 0) {
      info += `Además, tengo ${this.empleados.length === 1 ? 'a un empleado' : `a ${this.empleados.length} empleados`} a mi cargo: ${this.empleados.map(empleado => empleado.nombre).join(', ')}.\n`;
    }
    return info;
  }

  dirigir(empleado) {
    return `No me cierran los números muchachos, lo siento ${empleado.nombre} voy a tener que hacer recortes.\n`;
  }
}

class SupervisorProyectos extends Gerente {
  constructor(nombre, empleados) {
    super(nombre, empleados);
    this.identificador = "Supervisor de Proyectos";
  }

  supervisar() {
    return `Falta una semana para el plazo del proyecto, por favor no se demoren, ${this.nombre} supervisando.\n`;
  }
}

class Programador extends Empleado {
  constructor(nombre) {
    super(nombre, "Programador");
  }

  programar() {
    return `Creando programa, no sea impaciente y espere, ${this.nombre} trabajando.\n`;
  }
}

const jefe = new Gerente("Martín", [new Empleado("Geronimo", "Empleado"), new Empleado("Juan", "Empleado")]);
console.log(jefe.presentacion());
console.log(jefe.dirigir(new Empleado("Geronimo", "Empleado")));

const supervisor = new SupervisorProyectos("Geronimo", [new Empleado("Juan", "Empleado")]);
console.log(supervisor.presentacion());
console.log(supervisor.supervisar());

const empleado = new Programador("Juan");
console.log(empleado.presentacion());
console.log(empleado.programar());
