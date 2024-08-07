// // HERENCIA
// // SUPERCLASE
// class Animal {
//   constructor(nombre, color) {
//     this.nombre = nombre;
//     this.color = color;
//   }
//   sonido() {}
// }

// // SUBCLASES
// class Perro extends Animal {
//   coloring() {
//     console.log(`${this.nombre} es de color ${this.color}`);
//   }

//   sonido(sonido) {
//     console.log(`${this.nombre} hace ${sonido}`);
//   }
// }

// class Gato extends Animal {
//   coloring() {
//     console.log(`${this.nombre} es de color ${this.color}`);
//   }

//   sonido(sonido) {
//     console.log(`${this.nombre} hace ${sonido}`);
//   }
// }

// let perro = new Perro("Milkshake", "cafe");
// let gato = new Gato("Vaquita", "negro");
// perro.sonido("guau");
// gato.sonido("miau");
// perro.coloring();
// gato.coloring();

// EJERCICIO
class Company {
  constructor(id, nombre) {
    this.id = id;
    this.nombre = nombre;
    this.employees = [];
  }
  add(employee) {
    this.employees.push(employee);
  }
  print_employees() {
    for (let employee of this.employees) {
      console.log(employee.nombre);
    }
  }
}

class Manager extends Company {
  coordinate_projects() {
    console.log(
      `${this.nombre} está coordinando todos los proyectos de la empresa.`
    );
  }
}

class ProjectManager extends Company {
  constructor(id, nombre, proyect) {
    super(id, nombre);
    this.proyect = proyect;
  }
  coordinate_proyect() {
    console.log(`${this.nombre} está coordinando su proyecto.`);
  }
}

class Programmer extends Company {
  constructor(id, nombre, lenguage) {
    super(id, nombre);
    this.lenguage = lenguage;
  }
  code() {
    console.log(`${this.nombre} está programando en ${this.lenguage}`);
  }

  add(employee = Employee) {
    console.log(
      `Un programador no tiene empleados a su cargo. ${employee.nombre} no se añadira.`
    );
  }
}
my_manager = new Manager(1, "Jose");

my_proyectManager = new ProjectManager(2, "Maria", "Proyecto 1");
my_protectManager2 = new ProjectManager(3, "Pedro", "Proyecto 2");

my_programmer = new Programmer(4, "Juan", "JavaScript");
my_programmer2 = new Programmer(5, "Carlos", "Python");
my_programmer3 = new Programmer(6, "Luis", "Java");
my_programmer4 = new Programmer(7, "Rodrigo", "Java");

my_manager.add(my_proyectManager);
my_manager.add(my_protectManager2);

my_proyectManager.add(my_programmer);
my_proyectManager.add(my_programmer2);

my_protectManager2.add(my_programmer3);
my_protectManager2.add(my_programmer4);

my_programmer.add(my_programmer2);

my_programmer.code();
my_proyectManager.coordinate_proyect();
my_manager.coordinate_projects();
my_manager.print_employees();
my_proyectManager.print_employees();
my_programmer.print_employees();
