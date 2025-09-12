/*
 * #01 - Operadores y estructruas de control
 * https://dart.dev/language/operators
*/

void main() {
  print('Arithmetic Operations\n');
  arithmeticOperators();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Increment/Decrement Operations\n');
  incrementDecrementOperators();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Equality And Relational Operations\n');
  equalityAndRelationalOperators();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Type Operators\n');
  typesOperators();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Logic Operators\n');
  logicalOperators();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Conditional Expressions\n');
  conditionalExpressions();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Cascade Notation\n');
  cascadeNotation();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Conditional Structures\n');
  conditionalStructures();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Loops\n');
  loops();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Switch\n');
  switchFn();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Specific Control Loops\n');
  specificControlLoops();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');

  print('Dificultad Extra (Optional)\n');
  dificultadExtra();
  print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n');
}

void arithmeticOperators() {
  assert(5 + 5 == 10);
  print('Assert ( + ) passed successfully: 5 + 5 = ${5 + 5}');
  assert(5 - 5 == 0);
  print('Assert ( - ) passed successfully: 5 - 5 = ${5 - 5}');
  assert(2 - 5 == -3);
  print('Assert ( -expr ) passed successfully: 2 - 5 = ${2 - 5}');
  assert(5 * 5 == 25);
  print('Assert ( * ) passed successfully: 5 * 5 = ${5 * 5}');
  assert(25 / 5 == 5);
  print('Assert ( / ) passed successfully: 25 / 5 = ${25 / 5}');
  assert(5 ~/ 5 == 1);
  print('Assert ( ~/ ) passed successfully: 5 ~/ 5 = ${5 ~/ 5}');
  assert(5 % 5 == 0);
  print('Assert ( % ) passed successfully: 5 % 5 = ${5 % 5}');
}

void incrementDecrementOperators() {
  int a = 0;
  print('a = 0');
  ++a;
  assert(a == 1);
  print('Increment Operator ( ++var ) passed successfully: a = ${a}');
  a++;
  assert(a == 2);
  print('Increment Operator ( var++ ) passed successfully: a = ${a}');
  --a;
  assert(a == 1);
  print('Decrement Operator ( --var ) passed successfully: a = ${a}');
  a--;
  assert(a == 0);
  print('Decrement Operator ( var-- ) passed successfully: a = ${a}');
}

void equalityAndRelationalOperators() {
  assert(2 == 2);
  print('Assert ( == ) passed successfully: 2 == 2 = ${2 == 2}');
  assert(2 != 3);
  print('Assert ( != ) passed successfully: 2 != 2 = ${2 != 3}');
  assert(3 > 2);
  print('Assert ( > ) passed successfully: 2 > 2 = ${3 > 2}');
  assert(2 < 3);
  print('Assert ( < ) passed successfully: 2 < 2 = ${2 < 3}');
  assert(3 >= 3);
  print('Assert ( >= ) passed successfully: 2 == 2 = ${3 >= 3}');
  assert(2 <= 3);
  print('Assert ( <= ) passed successfully: 2 == 2 = ${2 <= 3}');
}

void typesOperators() {
  print(
      '1) Create instances of different animal types: animal1, animal2, animal3');
  Animal animal1 = Cat();
  Animal animal2 = Dog();
  Animal animal3 = Animal();

  // Using 'as' for type conversion
  print('2) Use "as" for type conversion');
  Cat cat = animal1 as Cat;
  Dog dog = animal2 as Dog;

  print('3) Use "is" to check type');
  // ignore: unnecessary_type_check
  if (animal1 is Cat) {
    print('animal1 is a Cat');
  }

  print("4) Using 'is!' to check that it's not of a specific type");
  if (animal3 is! Dog) {
    print('animal3 is not an Animal');
  }

  print("5) Invoking methods specific to subtypes");
  cat.meow();
  dog.bark();
}

void logicalOperators() {
  print("Create 'a' variable with value is 0");
  int a = 0;
  if (!(a == 1)) {
    int b = 0;
    print("A is different from 0 using logical operator ( !expr )");
    a++;

    if ((a == 1) || (a == 2)) {
      print("A is 1 or 2 using logical operator ( || )");
      a++;
    }

    if (b == 0 && a == 2) {
      print("A is 2 and b is 0 using logical operator ( && )");
    }
  }
}

void conditionalExpressions() {
  print("Create variable isPublic as bool false");
  bool isPublic = false;
  // ignore: dead_code
  print("Create variable visibility as String");
  String visibility = '';
  print("Executing conditional expression using ? and :");
  // ignore: dead_code
  visibility = isPublic ? "public" : "private";
  print("visibility is $visibility");
}

void cascadeNotation() {
  print(
      "Create a new variable 'paint' of type 'Paint' with properties (color, height, width, backgroundColor, strokeWidth)");
  Paint paint = Paint()
    ..color = 'blue'
    ..height = 5
    ..width = 5
    ..backgroundColor = 'black'
    ..strokeWidth = 1;

  print("Assigning values to the 'paint' object using cascade notation");
  print(
      "$paint = Color: ${paint.color}, Height: ${paint.height}, Width: ${paint.width}, BackgroundColor: ${paint.backgroundColor}, StrokeWidth: ${paint.strokeWidth}");
}

void conditionalStructures() {
  bool condition = true;
  print("Executes a block of code if a condition is true");
  if (condition) {
    print("Condition is true");
    // ignore: dead_code
  } else {
    print("Executes a block of code when the condition is not true");
    print("Condition is false");
  }

  print("Evaluates multiple conditions in sequence");
  int number = 42;
  if (number > 50) {
    print("Number is greater than 50");
  } else if (number > 30) {
    print("Number is greater than 30");
  } else {
    print("Number is less than or equal to 30");
  }
}

void loops() {
  print("Iterates over a range of values or a specific sequence.");
  for (int i = 0; i < 5; i++) {
    print("Iteration $i");
  }

  print("while: Executes a block of code while a condition is true.");
  int count = 0;
  while (count < 3) {
    print("Count is $count");
    count++;
  }

  print(
      "do-while: Similar to while but guarantees at least one execution before checking the condition.");
  int value = 0;
  do {
    print("Value is $value");
    value++;
  } while (value < 3);
}

void switchFn() {
  print(
      "Switch: Directs the execution of code based on the value of an expression. Parameter is 'Monday'");
  String day = "Monday";
  switch (day) {
    case "Monday":
      print("It's the start of the week");
      break;
    case "Friday":
      print("It's almost the weekend");
      break;
    default:
      print("It's a regular day");
  }
}

void specificControlLoops() {
  print("break: Exits a loop or a control structure.");
  for (int i = 0; i < 5; i++) {
    if (i == 3) {
      break;
    }
    print("Breaking at $i");
  }

  print("continue: Skips to the next iteration of a loop.");
  for (int i = 0; i < 5; i++) {
    if (i == 2) {
      continue;
    }
    print("Iteration $i");
  }
}

void dificultadExtra() {
  print(
      "Program that prints even numbers between 10 and 55 (inclusive), excluding 16 and multiples of 3:");
  for (int number = 10; number <= 55; number++) {
    if (number % 2 == 0 && number != 16 && number % 3 != 0) {
      print(number);
    }
  }
}

class Animal {
  void makeSound() {
    print('Generic sound');
  }
}

class Cat extends Animal {
  void meow() {
    print('Meow!');
  }
}

class Dog extends Animal {
  void bark() {
    print('Woof!');
  }
}

class Paint {
  String color = '';
  int height = 0;
  int width = 0;
  String backgroundColor = '';
  double strokeWidth = 0;
}
