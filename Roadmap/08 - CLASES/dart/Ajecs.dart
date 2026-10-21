import 'dart:io';

class Car {
  late String brand;
  late String model;
  late String color;
  late int price;

  /*
    Si no se declara un constructor, Dart utiliza el constructor predeterminado. 
    El constructor predeterminado es un constructor generativo sin argumentos ni nombre.
  */
  late String engineType; // Propiedad no usada en el constructor.

  // Propiedad no usada en el constructor e inicializada puede ser usada en el constructor.
  late String engineCapacity = '1.0';

  Car(this.brand, this.model, this.color, this.price);

  String start() => 'El motor del $brand $model ha arrancado';
  String quotePrice() =>
      'El valor del $model $engineCapacity de color $color es de $price';
  // ! Sin necesidad de definir la propiedad engineType se usa igual.
}

// ///////////////////////// Clases ej. Extra ///////////////////////////

class Pila<T> {
  // Se define una propiedad de tipo T (generico). Para que al añadir un valor en la pila, no sea necesario definir el tipo de dato.
  // El cual se define al instanciar la clase (int, double, String, dynamic).

  String stackName;
  late List<T> stackItems;

  Pila(String stackName, this.stackItems) : stackName = stackName.toLowerCase();

  String addStackItem(T item) {
    stackItems.add(item);
    return 'Se ha añadido el item $item en la ultima posición: \n${stackItems.reversed.join(' - ')}';
  }

  String removeStackItem() {
    var lastItem = stackItems.removeLast();
    return 'Se ha removido el elemento $lastItem:\n${stackItems.reversed.join(' - ')}\n';
  }

  String itemsLength() => stackItems.length == 0
      ? 'La pila $stackName esta vacia.'
      : 'La pila $stackName contiene ${stackItems.length} elementos\n';

  String printStack() => itemsLength() == 0
      ? 'La pila $stackName esta vacia.'
      : '\nLos items de la pila $stackName son: ${stackItems.reversed.join(' - ')}\n';
}

// ///////////////////////// Cola ///////////////////////////

class Cola<T> {
  late String queueName;
  late List<T> queueItems;

  Cola(String queueName, this.queueItems) : queueName = queueName.toLowerCase();

  String addQueueItem(T item) {
    var oldItem = queueItems[0];
    queueItems[0] = item;
    return 'Se ha reemplazado el item $oldItem por el item $item en la PRIMER posición:\n${queueItems.join(' - ')}';
  }

  String removeQueueItem() {
    if (queueItems.length == 0) return 'La cola $queueName esta vacia.';

    var removedItem = queueItems.removeAt(0);

    if (queueItems.length >= 1) {
      return '\nSe ha eliminado el primer item -> $removedItem:\n${queueItems.join(' - ')}';
    }
    return '''\nSe ha eliminado el primer item -> $removedItem:
${queueItems} No hay más elementos para eliminar.\n''';
  }

  String itemsLength() => queueItems.length == 0
      ? 'La cola $queueName esta vacia.'
      : 'La cola $queueName contiene ${queueItems.length} elementos\n';

  String printQueue() => itemsLength() == 0
      ? 'La cola $queueName esta vacia.'
      : '\nLos items de la cola $queueName son: ${queueItems.join(' - ')}\n';
}

void main() {
  stdout.write('\n****************** Clases ********************\n\n');

  print('<< Ejemplo objeto "Auto" >>\n');

  Car siena = Car('Fiat', 'Siena', 'blanco', 5000);

  print(siena.start());
  print(siena.quotePrice());

  siena.engineType = 'Auto'; // Se modifica el valor de la propiedad.
  siena.color = 'negro'; // Se cambia el valor definido en la instancia.

  print('\nPropiedad no iniciada en el constructor: ${siena.engineType}');
  print('\nValor de la propiedad "color" cambiada: \n${siena.quotePrice()}');

  stdout.write(
    '\n*************************** Extra **************************\n',
  );

  print('<< Pila >>');

  Pila ciudades = Pila('Ciudades', [
    'Tokyo',
    'Nueva York',
    'París',
    'Buenos Aires',
    'Madrid',
  ]);

  print(ciudades.printStack());
  print(ciudades.itemsLength());

  print(ciudades.removeStackItem());
  print(ciudades.addStackItem('Caracas'));

  print('\n<< Cola >>');

  Cola<int> numbers = Cola<int>('Numeros', [2, 3, 4, 5, 6, 7, 8]);
  // Es importante tener en cuenta el uso del tipado al utilizar genéricos.
  // ! Si se obvia el tipado al comienzo de la variable 
  // ! Al ejecutar el metodo addQueueItem() la lista queueItems sera de tipo dynamic. 
  // ! Y por tanto aceptará cualquier tipo .

  print(numbers.printQueue());
  print(numbers.itemsLength());

  print(numbers.addQueueItem(1));
  print(numbers.removeQueueItem());
  print(numbers.removeQueueItem());
  print(numbers.removeQueueItem());
  print(numbers.removeQueueItem());
  print(numbers.removeQueueItem());
  print(numbers.removeQueueItem());
  print(numbers.removeQueueItem());
  print(numbers.removeQueueItem());
}
