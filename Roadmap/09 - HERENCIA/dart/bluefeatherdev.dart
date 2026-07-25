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

/// 1. [Concepto de herencia]:
class Animal {
  void speak() {
    print('...');
  }
}

class Dog extends Animal {
  // Dog hereda métodos de Animal,
  // Dog puede sobrescribírlos:
  @override
  void speak() {
    print('Woof!');
  }
}

class Cat extends Animal {
  // Cat hereda métodos de Animal,
  // Cat puede sobrescribírlos:
  @override
  void speak() {
    print('Meow!');
  }
}

/// 2. [DIFICULTAD EXTRA]:
class Employees {
  // Atributos de todo empleado
  int id;
  String name;
  List employees = [];

  // Constructor de empleados
  Employees(this.id, this.name);

  // Añadir un empleado
  void addEmploy(Employees employ) {
    employees.add(employ);
  }

  // Ver todos los empleados
  void showEmployees() {
    for (var employ in employees) {
      print('id: ${employ.id}, name: ${employ.name}');
    }
  }

  // Método común de todo empleado
  void greet() {
    print('I\'m $name (Cargo: Employ, Id: $id)');
  }
}

class Managers extends Employees {
  // Usar atributos de Empleados
  Managers(super.id, super.name);

  // Sobrescribir el método común
  @override
  void greet() {
    print('I\'m $name (Cargo: Manager, Id: $id)');
  }

  // Método único de Gerentes
  void coordinateProjects() {
    print('$name is coordinating all our projects!');
  }
}

class ProjectManager extends Employees {
  // Atributo único de Gerentes de Proyectos
  String project;

  // Usar atributos de Empleados
  ProjectManager(super.id, super.name, this.project);

  // Sobrescribir el método común
  @override
  void greet() {
    print('I\'m $name (Cargo: Project Manager, Id: $id)');
  }

  // Método único de Gerentes de Proyectos
  void coordinateProjects() {
    print('$name is coordinating only his/her project: $project');
  }
}

class Programmers extends Employees {
  // Atributo único de Programadores
  String language;

  // Usar atributos de Empleados
  Programmers(super.id, super.name, this.language);

  // Sobrescribir el método común
  @override
  void greet() {
    print('I\'m $name (Cargo: Programmer, Id: $id)');
  }

  // Método único de Programadores
  void makeSoftware() {
    print('$name is coding in $language!');
  }
}

void main() {
  /// 1. [Concepto de herencia]:
  final myAnimal = Animal();
  myAnimal.speak(); // ...

  final myDog = Dog();
  myDog.speak(); // Woof!

  final myCat = Cat();
  myCat.speak(); // Meow!

  /// 2. [DIFICULTAD EXTRA]:
  
  // Definir roles de la empresa
  final myManager = Managers(1, 'MoureDev');
  
  final myProjectManager1 = ProjectManager(2, 'KontrolDev', 'hello-ios');
  final myProjectManager2 = ProjectManager(3, 'Roswell468', 'hello-android');
  
  final myProgrammer1 = Programmers(4, 'BlueFeatherDev', 'Dart');
  final myProgrammer2 = Programmers(5, 'MeryDev', 'Swift');
  final myProgrammer3 = Programmers(6, 'SwordDev', 'Java');
  final myProgrammer4 = Programmers(7, 'WingDev', 'Kotlin');

  // Empleados del Gerente
  myManager.addEmploy(myProjectManager1);
  myManager.addEmploy(myProjectManager2);

  // Empleados de Gerentes de Proyectos  
  myProjectManager1.addEmploy(myProgrammer1);
  myProjectManager1.addEmploy(myProgrammer2);

  myProjectManager2.addEmploy(myProgrammer3);
  myProjectManager2.addEmploy(myProgrammer4);

  // Actividad del Gerente + Sus empleados 
  myManager.coordinateProjects();
  myManager.showEmployees();

  // Actividad de los Gerentes de Proyectos + Sus empleados
  myProjectManager1.coordinateProjects();
  myProjectManager1.showEmployees();

  myProjectManager2.coordinateProjects();
  myProjectManager2.showEmployees();

  // Actividades de los Programadores + No tienen empleados
  myProgrammer1.makeSoftware();
  myProgrammer2.makeSoftware();
  myProgrammer3.makeSoftware();
  myProgrammer4.makeSoftware();

  // La empresa entera te saluda
  myManager.greet();
  myProjectManager1.greet();
  myProjectManager2.greet();
  myProgrammer1.greet();
  myProgrammer2.greet();
  myProgrammer3.greet();
  myProgrammer4.greet();
}
