import 'dart:io';

class Animal {
  late String species;
  late String animalName;
  late String animalSound;
  late int legs;

  Animal({
    required this.species,
    required this.animalSound,
    this.animalName = '',
    this.legs = 0,
  });

  String sound() =>
      'El $species $animalName ${animalSound.isEmpty ? 'No tiene un sonido' : 'emite el sonido: animalSound'}';

  String move() => 'El $species $animalName se mueve';
}

class Cat extends Animal {
  // ! catName no es una propiedad de Cat sino un parametro que permite inicilizar la propiedad animalName de Animal
  // Por eso no requiere ser previamente declarada.
  Cat({String catName = ''})
    : super(species: 'gato', animalSound: '', animalName: catName, legs: 4) {
    animalSound = meow();
    // No es posible acceder a un método de instancia como meow() en la lista de inicializadores
  }

  /* 
    En Dart la lista de inicializadores se define con el signo ":" y precede al cuerpo del constructor.
    * Define los valores de propiedades final o late. antes de ser instanciadas.
    * Evalua expresiones.
    * Llama al constructor de la superclase. 
  */

  String meow() => 'miaaauuuu';

  // Se sobreescribe el método move.
  @override
  move() => 'El gato $animalName corre';
}

class Dog extends Animal {
  Dog({String dogName = ''})
    : super(species: 'perro', animalSound: Dog.barf(), animalName: dogName) {
    // A diferencia de Cat se declara la variable barf como static
    // Lo que hace que el método pertenezca a la clase y no a cada objeto, ya que de lo contrario todavia
    // no esta del todo inicializada, y puede ser asignada como valor en la lista.
    legs = 4;
  }

  static String barf() => 'guaaaau';
  // Un método static no puede usar this ni acceder a campos de instancia como animalName.
}

// //////////////////////// Clases de ej. extra ////////////////////////

class Employee {
  static final Set<int> _usedIds = {};
  // esta variable es privada porque solo tiene finalidad para este archivo en caso de ser importada la clase
  // los ids no pueden accederse ni obtener datos al respecto.

  String job;
  final int id;
  String employeeName;
  List<Employee> inCharge;

  Employee({
    required int id,
    required this.employeeName,
    required this.job,
    List<Employee>? inCharge,
  }) : id = id,
       inCharge = inCharge ?? [] {
    if (!_usedIds.add(id)) {
      // add(id) intenta insertar el nuevo id en el conjunto. Si el id no estaba antes,
      //lo añade y devuelve true. Si ya existía, devuelve false, y entonces el constructor lanza el error.
      throw ArgumentError.value(id, 'id', 'Ya existe un empleado con ese id');
    }
  }

  String isInCharge() => inCharge.isEmpty
      ? 'ninguno'
      : inCharge.map((item) => item.employeeName).join(', ');

  showCredential() => '''\nNombre: $employeeName, id: $id, puesto: $job, 
personal a cargo: ${isInCharge()}''';
  /* 
    Exiten dos opciones:
    * Modificar toString() para que al usar join (que ejecuta toString) devuelva employeeName 
    * o usar map() para que recorra la lista e imprima el Employee.name 
  */

  static String showIds() => _usedIds.join(', ');
}

class Manager extends Employee {
  static const String managerJob = 'gerente';

  Manager({
    int id = 0,
    String name = 'desconocido',
    List<Employee> managerInCharge = const [],
  }) : super(
         id: id,
         employeeName: name,
         job: managerJob,
         inCharge: managerInCharge,
       );

  String evaluatingPerformance([int? value]) {
    if (value == null) return '\nAun no tengo datos sobre tu rendimiento';

    switch (value) {
      case >= 1 && <= 3:
        return '\nDesempeño bajo';
      case >= 4 && <= 6:
        return '\nDesempeño medio';
      case >= 7 && <= 10:
        return '\nDesempeño alto';
      default:
        return '\nIngresa un numero del 1 al 10';
    }
  }
}

class ProjectManager extends Employee {
  static const String projectManagerJob = 'gerente de proyecto';

  String project;

  ProjectManager({
    int id = 0,
    String name = 'desconocido',
    List<Programmer> projectManagerInCharge = const [],
    required this.project,
  }) : super(
         id: id,
         employeeName: name,
         job: projectManagerJob,
         inCharge: projectManagerInCharge,
       );

  @override
  String showCredential() => super.showCredential() + '\nProyecto: $project';

  String meet() =>
      '\nEl $projectManagerJob esta organizando reunión de seguimiento...';

  String manageBudget([int? money]) {
    if (money == null) return '\nNo hay datos sobre el presupuesto';
    if (money > 5000)
      return '\n¡Vamos viento en popa! \u{26F5}... dinero disponible \$$money';
    if (money > 1000)
      return '\nHay menos presupuesto que lo previsto... dinero disponible \$$money';
    if (money <= 1000)
      return '\nEstamos al horno \u{1F4C9}... dinero disponible \$$money';

    return '\nNo hay datos sobre el presupuesto';
  }
}

class Programmer extends Employee {
  static const String programmerJob = 'programador';

  late String language;

  Programmer({int id = 0, String name = 'desconocido', this.language = ''})
    : super(id: id, employeeName: name, job: programmerJob);

  String programming() =>
      '\n$employeeName esta programando en $language \u{1F4BB}...';
}

void main() {
  stdout.write(
    '\n*************** Herencia y polimorfismo *******************************\n',
  );

  Animal carola = Cat(catName: 'Carola');
  print(carola.sound());
  final fluffy = Dog(dogName: 'Fluffy');
  print(fluffy.sound());
  final unknown = Dog();
  print(unknown.sound());

  void countLegs(Animal animal) {
    // Esto es polimorfismo
    if (animal is Cat) {
      print('${animal.animalName} tiene ${animal.legs} patas');
    } else if (animal is Dog) {
      print('${animal.animalName} tiene ${animal.legs} patas');
    }
  }

  countLegs(carola);
  countLegs(fluffy);

  print(carola.move()); // Método sobreescrito de Animal.

  stdout.write('\n******************** Extra **************************\n');

  Programmer programmer1 = Programmer(id: 5, name: 'Ajecs', language: 'Dart');
  print(programmer1.showCredential());

  ProjectManager projectManager1 = ProjectManager(
    id: 3,
    name: 'Carlos Alcaraz',
    project: 'Proyecto principal',
    projectManagerInCharge: [programmer1],
    // Si se asignara un manager o projectManager se generaría error ya que solo acepta la clase Programmer.
  );
  print(projectManager1.showCredential());

  Manager CFO = Manager(
    id: 2,
    name: 'Juan Alfonso',
    managerInCharge: [programmer1, projectManager1],
  );

  print(CFO.showCredential());

  Manager CEO = Manager(
    id: 1,
    name: 'José Martinez',
    managerInCharge: [programmer1, projectManager1, CFO],
  );

  print(CEO.showCredential());

  print(projectManager1.meet());
  print(programmer1.programming());

  print(projectManager1.manageBudget(6000));
  print(CFO.evaluatingPerformance());

  print(Employee.showIds());

  print('');
}
