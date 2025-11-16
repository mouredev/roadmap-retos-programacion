// Icorrecto
// class Bird {
//   String fly() {
//     return 'Flying';
//   }
// }

// class Chicken extends Bird {
//   fly() {
//     throw Exception('Los pollos no vuela');  
//   }
// }

// Correcto

class Bird {
  String move() {
    return 'Moving';
  }
}

class Chicken extends Bird {
  String move() {
    return 'Walking';
  }
}

// Ejercicio de jerarquia de vehiculos

class Vehicle {
  int speed = 0;

  void accelerate(int increment) {
    speed += increment;
    print('Velocidad = $speed');
  }

  void brake(int decrement) {
    speed -= decrement;
    print('Velocidad = $speed');
  }
}

class Car extends Vehicle {
  @override
  void accelerate(int increment) {
    print('El coche esta acelerando');
    super.accelerate(increment);
  }

  @override
  void brake(int decrement) {
    print('El coche esta frendando');
    super.brake(decrement);
  }
}

class Bycicle extends Vehicle {
  @override
  void accelerate(int increment) {
    print('La bici esta acelerando');
    super.accelerate(increment);
  }

  @override
  void brake(int decrement) {
    print('La bici esta frendando');
    super.brake(decrement);
  }
}

class Motorcycle extends Vehicle {
  @override
  void accelerate(int increment) {
    print('La moto esta acelerando');
    super.accelerate(increment);
  }

  @override
  void brake(int decrement) {
    print('La moto esta frendando');
    super.brake(decrement);
  }
}

void testVehicle(Vehicle vehicle) {
  vehicle.accelerate(5);
  vehicle.brake(3);
}

void main() {

  Bird bird = Bird();
  print(bird.move());
  Chicken chicken = Chicken();
  print(chicken.move());
  
  bird = Chicken();
  print(bird.move());

  // Ejercicio de jerarquia de vehiculos

  Car car = Car();
  Motorcycle motorcycle = Motorcycle();
  Bycicle bycile = Bycicle();

  testVehicle(car);
  testVehicle(motorcycle);
  testVehicle(bycile);

}

