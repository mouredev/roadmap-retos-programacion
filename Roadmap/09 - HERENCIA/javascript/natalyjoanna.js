
// // Superclase

// class Animal {
// 	sonido = "sonido de animal";
	
// 	constructor(nombre) {
// 		console.log("El animal hace: ");
//     this.nombre = nombre;
// 	}
	
// 	sound() {
// 		console.log(`Soy ${this.nombre} y soy un animal que hace el sonido ${this.sonido}`);
// 	}
// }

// // Subclases

// class Perro extends Animal {
// 	sonido = "wof";
	
// 	constructor(nombre) {
// 		super(nombre);
// 	}
// }

// class Gato extends Animal {
// 	sonido = "miau";
	
// 	constructor(nombre) {
// 		super(nombre);
// 	}
// }

// const myDog = new Perro("Pepito");
// myDog.sound();
// const myCat = new Gato("Pepita");
// myCat.sound();

// DIFICULTAD EXTRA

class Empleado {
  constructor(id, nombre) {
    this.id = id;
    this.nombre = nombre;
    this.empleados = []
  }

  add(empleado) {
    this.empleados.push(empleado);
    console.log('Empleado agregado.')
  }

  print() {
    for(let empleado of this.empleados) {
      console.log(empleado.nombre)
    }
  }

}

class Gerente extends Empleado {

  coordinarProyectos() {
    console.log(`${this.nombre} esta coordinando los proyectos de la empresa`)
  }
}

class GerenteDeProyecto extends Empleado {
  constructor(id, nombre, proyecto) {
    super(id, nombre, proyecto);
    this.proyecto = proyecto;
  }

  coordinarProyecto() {
    console.log(`${this.nombre} esta coordinando el proyecto ${this.proyecto}`)
  }
}

class Programador extends Empleado {
  constructor(id, nombre, lenguaje) {
    super(id, nombre, lenguaje);
    this.lenguaje = lenguaje;
  }

  programar() {
    console.log(`${this.nombre} esta programdo en ${this.lenguaje}`)
  }

  add(empleado) {
    console.log(`Un programador no debe de terner empleados a su cargo. ${empleado} no se agregara`)
  }
}

let myManger = new Gerente(1, "Nataly");
let myProjectManager1 = new GerenteDeProyecto(2, "Joanna", "Proyecto 1");
let myProjectManager2 = new GerenteDeProyecto(3, "Marcos", "Proyecto 2");
let myProgramer1 = new Programador(4, "Mar", "Javascript");
let myProgramer2 = new Programador(5, "Joan", "Dart");
let myProgramer3 = new Programador(6, "Nat", "Kotlin");

myManger.add(myProjectManager1)
myManger.add(myProjectManager2)

myProjectManager1.add(myProgramer1)
myProjectManager1.add(myProgramer2)
myProjectManager2.add(myProgramer3)

myProgramer1.add(myProgramer2)

myManger.coordinarProyectos()
myProjectManager1.coordinarProyecto()
myProgramer3.programar()

myManger.print()
myProjectManager1.print()

