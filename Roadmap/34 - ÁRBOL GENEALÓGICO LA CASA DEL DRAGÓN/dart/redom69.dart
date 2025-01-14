class Person {
  int id;
  String name;
  Person? couple;
  List<Person> children;

  Person({
    required this.id,
    required this.name,
    this.couple,
    List<Person>? children,
  }) : children = children ?? [];

  void addChild(Person child) {
    children.add(child);
  }

  void modifyCouple(Person newCouple) {
    couple = newCouple;
  }

  @override
  String toString() {
    String coupleName = couple != null ? couple!.name : "None";
    return 'Person(id=$id, name=$name, couple=$coupleName, children=${children.length})';
  }
}

class FamilyTree {
  Person root;
  Map<int, Person> people;

  FamilyTree(this.root) : people = {root.id: root};

  void addPerson(Person person) {
    if (!people.containsKey(person.id)) {
      people[person.id] = person;
    } else {
      print('Ya existe');
    }
  }

  void deletePerson(int personId) {
    if (people.containsKey(personId)) {
      people.remove(personId);
    } else {
      print('No existe');
    }
  }

  void editPerson(int id,
      {String? name, Person? couple, List<Person>? children}) {
    if (people.containsKey(id)) {
      Person person = people[id]!;
      if (name != null) person.name = name;
      if (couple != null) person.modifyCouple(couple);
      if (children != null && children.isNotEmpty) person.children = children;
    } else {
      print('No existe');
    }
  }

  void displayTree([Person? person, int level = 0]) {
    person ??= root;

    String indent = ' ' * (level * 4);
    String coupleName =
        person.couple != null ? ' & ${person.couple!.name}' : '';
    print('$indent${person.name}$coupleName');

    for (var child in person.children) {
      displayTree(child, level + 1);
    }
  }
}

void main() {
  Person jaehaerys = Person(id: 1, name: "Jaehaerys I Targaryen");
  Person alysanne = Person(id: 2, name: "Alysanne Targaryen");

  Person baelon = Person(id: 3, name: "Baelon Targaryen");
  Person alyssa = Person(id: 4, name: "Alyssa Targaryen");

  Person viserys = Person(id: 5, name: "Viserys I Targaryen");
  Person aemma = Person(id: 6, name: "Aemma Arryn");

  Person daemon = Person(id: 7, name: "Daemon Targaryen");
  Person rhea = Person(id: 8, name: "Rhea Royce");
  Person laena = Person(id: 9, name: "Laena Velaryon");
  Person rhaenyra = Person(id: 10, name: "Rhaenyra Targaryen");

  Person alicent = Person(id: 11, name: "Alicent Hightower");
  Person aegonII = Person(id: 12, name: "Aegon II Targaryen");
  Person helaena = Person(id: 13, name: "Helaena Targaryen");
  Person aemond = Person(id: 14, name: "Aemond Targaryen");
  Person daeron = Person(id: 15, name: "Daeron Targaryen");

  jaehaerys.modifyCouple(alysanne);
  baelon.modifyCouple(alyssa);
  baelon.children = [viserys, daemon];
  viserys.modifyCouple(aemma);
  viserys.children = [rhaenyra];
  daemon.modifyCouple(rhea);
  daemon.children = [];

  daemon.modifyCouple(laena);
  Person baela = Person(id: 16, name: "Baela Targaryen");
  Person rhaena = Person(id: 17, name: "Rhaena Targaryen");
  daemon.children = [baela, rhaena];

  rhaenyra.modifyCouple(daemon);

  viserys.modifyCouple(alicent);
  viserys.children.addAll([aegonII, helaena, aemond, daeron]);

  FamilyTree familyTree = FamilyTree(viserys);
  familyTree.addPerson(jaehaerys);
  familyTree.addPerson(alysanne);
  familyTree.addPerson(baelon);
  familyTree.addPerson(alyssa);
  familyTree.addPerson(daemon);
  familyTree.addPerson(rhea);
  familyTree.addPerson(laena);
  familyTree.addPerson(rhaenyra);
  familyTree.addPerson(alicent);
  familyTree.addPerson(aegonII);
  familyTree.addPerson(helaena);
  familyTree.addPerson(aemond);
  familyTree.addPerson(daeron);
  familyTree.addPerson(baela);
  familyTree.addPerson(rhaena);

  familyTree.displayTree();
}
