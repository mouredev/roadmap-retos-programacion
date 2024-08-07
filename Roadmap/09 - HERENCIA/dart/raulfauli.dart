/// #09 HERENCIA

abstract class Animal {
  String nombre;

  Animal(this.nombre);

  void emitirSonido();
}

class Perro extends Animal {
  Perro(String nombre) : super(nombre);

  @override
  void emitirSonido() {
    print('$nombre dice "Guau"');
  }
}

class Gato extends Animal {
  Gato(String nombre) : super(nombre);

  @override
  void emitirSonido() {
    print('$nombre dice "Miau"');
  }
}

// Extra
class Employee {
  int id;
  String nombre;

  Employee(this.id, this.nombre);

  void trabajar() {
    print('$nombre está trabajando');
  }
}

class ProjectManager extends Employee {
  ProjectManager(int id, String nombre) : super(id, nombre);

  void gestionarProyecto() {
    print('$nombre está gestionando un proyecto');
  }
}

class Manager extends ProjectManager {
  Manager(int id, String nombre) : super(id, nombre);

  void gestionar() {
    print('$nombre está gestionando');
  }
}

void main() {
  final perro = Perro('Laica');
  final gato = Gato('Calcetín');

  perro.emitirSonido();
  gato.emitirSonido();

  // Extra
  final empleado = Employee(1, 'Raúl');
  empleado.trabajar();
  final projectManager = ProjectManager(2, 'Alejandro');
  projectManager.trabajar();
  projectManager.gestionarProyecto();
  final manager = Manager(3, 'Rafa');
  manager.trabajar();
  manager.gestionarProyecto();
  manager.gestionar();
}
