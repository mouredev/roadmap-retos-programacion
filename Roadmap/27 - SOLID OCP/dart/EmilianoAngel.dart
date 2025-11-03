// Incorrecto
// class Form {

//   void drawSquare() {
//     print('Dibujar un cuadrado');
//   }

//   void drawCircle() {
//     print('Dibujar un círculo');
//   }
// }

// Correcto
abstract class Form {
  void draw();
}

class Square implements Form {
  @override
  void draw() {
    print('Dibujar un cuadrado');
  }
}

class Circle implements Form {
  @override
  void draw() {
    print('Dibujar un círculo');
  }
}

class Triangle implements Form {
  @override
  void draw() {
    print('Dibujar un triángulo');
  }
}

// Ejercicio de calculadora

abstract class Operation {
  double execute(double a, double b) {
    return 0;
  }
}

class Addition implements Operation {
  @override
  double execute(double a, double b) {
    return a + b;
  }
}

class Subtraction implements Operation {
  @override
  double execute(double a, double b) {
    return a - b;
  }
}

class Multiplication implements Operation {
  @override
  double execute(double a, double b) {
    return a * b;
  }
}

class Division implements Operation {
  @override
  double execute(double a, double b) {
    if (b == 0) {
      throw Exception('Division by zero is not allowed.');
    }
    return a / b;
  }
}

class Power implements Operation {
  @override
  double execute(double a, double b) {
    double result = 1;
    for(int i = 0; i < b; i++) {
      result *= a;
    }
    return result;
  }
}

class Calculator {
  final Map<String, dynamic> _operations = {};

  void addOperation(String name, Operation operation) {
    _operations[name] = operation;
  }
  double calculate(String name, double a, double b) {
    final operation = _operations[name];
    if (operation == null) {
      throw ArgumentError('Operation $name not supported.');
    }
    return operation.execute(a,b);
  }
}

void main () {
  Calculator calculator = Calculator();

  calculator.addOperation('addition', Addition());
  calculator.addOperation('substraction', Subtraction());
  calculator.addOperation('multiplication', Multiplication());
  calculator.addOperation('division', Division());
  calculator.addOperation('power', Power());

  print(calculator.calculate('addition', 5, 3));
  print(calculator.calculate('substraction', 6, 3));
  print(calculator.calculate('multiplication', 5, 2));
  print(calculator.calculate('division', 12, 6));
  print(calculator.calculate('power', 2, 3));
 
}
