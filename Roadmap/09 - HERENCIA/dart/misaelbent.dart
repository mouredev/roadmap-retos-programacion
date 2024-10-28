void main(List<String> arguments) {
  Dog cereza = Dog('Cereza');
  Cat pandora = Cat('Pandora');

  pandora.makeSound();
  cereza.makeSound();

  //Extra!!
  //Empleados de la empresa
  //Programadores
  Programmer luis = Programmer('01', 'Luis Perez', ['Pizza deliver', 'Twiter']);
  Programmer carlos =
      Programmer('02', 'Caros Zuluaga', ['Tintoreria', 'Pizza deliver']);
  Programmer angela =
      Programmer('03', 'Angela Bustos', ['Tintoreria', 'Twiter']);
  Programmer camila =
      Programmer('04', 'Camila Suarez', ['Pizza deliver', 'Twiter']);
  List<Employee> programmers = [luis, camila, angela, carlos];
  //Proyects Manager
  ProyectManager cesar =
      ProyectManager('05', 'Cesar Guerrero', 'Pizza deliver', programmers);
  ProyectManager veronica =
      ProyectManager('06', 'Veronica Castro', 'Twiter', programmers);
  ProyectManager julian =
      ProyectManager('07', 'Julian Acevedo', 'Tintoreria', programmers);
  List<Employee> proyectManayers = [cesar, veronica, julian];

  //Manager
  Manager andres = Manager('08', 'Andres Cepeda', proyectManayers);

//lista de todos los empleados
  List<Employee> employees = proyectManayers + programmers;
  employees.add(andres);

  for (var employee in employees) {
    employee.doYourJob();
  }
}

class Animal {
  String name;

  Animal(this.name);

  void makeSound() => print('');
}

class Dog extends Animal {
  Dog(String name) : super(name);

  @override
  void makeSound() {
    print('Guau, guau');
  }
}

class Cat extends Animal {
  Cat(String name) : super(name);

  @override
  void makeSound() {
    print('Miau, miau');
  }
}

abstract class Employee {
  String id;
  String name;

  doYourJob();

  Employee(this.id, this.name);
}

class Programmer implements Employee {
  @override
  String name;

  @override
  String id;

  List<String> assignedProjects;

  Programmer(this.id, this.name, this.assignedProjects);

  @override
  void doYourJob() {
    print('$name, esta trabajando en:');
    for (var proyect in assignedProjects) {
      print(proyect);
    }
  }
}

class ProyectManager implements Employee {
  @override
  String name;

  @override
  String id;

  String proyect;

  List<Employee> programmers;

  ProyectManager(this.id, this.name, this.proyect, this.programmers);

  List<Employee> _team = [];

  void _getTeam(programmers) {
    List<Employee> myTeam = programmers
        .where((programmer) => _filterByProyects(programmer, proyect))
        .toList();
    _team = myTeam;
  }

  bool _filterByProyects(Programmer programmer, String proyect) =>
      programmer.assignedProjects.contains(proyect);

  @override
  void doYourJob() {
    _getTeam(programmers);
    print('$name, esta supervisando el trabajo de:');
    for (var empoyee in _team) {
      print(empoyee.name);
    }
  }
}

class Manager implements Employee {
  @override
  String name;

  @override
  String id;

  List<Employee> team;

  Manager(this.id, this.name, this.team);

  @override
  void doYourJob() {
    print('$name, esta supervisando el trabajo de:');
    for (var empoyee in team) {
      print(empoyee.name);
    }
  }
}
