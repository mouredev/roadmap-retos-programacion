void main(List<String> arguments) async {
  sayHi();
  getAge(54);
  getSizeAndWeigth(190, 88);
  getMeasures(size: 190, weigth: 88);
  printMeasures(190, 88);
  multiFunction();
  printer('Ejemplo 7: Funcion tipo flecha');
  await getSorprise();
  printIterable();
  getNumbers('es multiplo de 3', 'es multiplo de 5');
}

// Funcion simple sin argumento ni retorno
void sayHi() {
  print('Ejemplo 1: Funcion simple');
  print('Hola');
}

//Funcion con un parametro y retorno
int getAge(int age) {
  print('Ejemplo 2: Funcion simple con parametro y retorno');
  print(age);
  return age;
}

//Funcion con parametros posicionales y retorno
String getSizeAndWeigth(int size, int weigth) {
  print('Ejemplo 3: Funcion con parametros posicionales');
  print('Su peso es: $weigth y su talla es $size');
  return 'Su peso es: $weigth y su talla es $size';
}

//Funcion con parametros nombrados y retorno
String getMeasures({required int size, required int weigth}) {
  print('Ejemplo 4: Funcion con parametros nombrados');
  print('Su peso es: $weigth y su talla es $size');
  return 'Su peso es: $weigth y su talla es $size';
}

//Funcion con parametros posicionales y uno opcional
void printMeasures(int size, int weigth, [int hipMeasure = 100]) {
  print('Ejemplo 5: Funcion con parametro posicional y opcional');
  print('$size, $weigth, $hipMeasure');
}

// Funcion que llama funciones del sistema
void multiFunction() {
  print('Ejemplo 6: algunos funciones del sistema');
  int number = int.parse('24');
  print('$number es un numero parceado');
  String name = 'Misael';
  print('${name.toUpperCase()} nombre colocado en mayuscula sostenida');
}

//Funcion tipo flecha
int getNewAge(int age) => age;
printer(String p) => print(p);

//Funcion de orden superior con una funcion como parametro
void printSayHi(String Function(String) getString, String partOfDay) {
  print('Ejemplo 7: Funcion de orden superior');
  print('Hola, feliz ${getString(partOfDay)}');
} //revisar antes de enviar

//Funcion asincrona (async)
Future<void> getSorprise() async {
  print('Ejemplo 8: Funcion asincrona');
  for (var i = 1; i <= 3; i++) {
    print('$i...');
    await Future.delayed(Duration(seconds: 2));
  }
  print('SORPRESA!!!');
}

//Funcion generadora
Iterable<int> getNumberList(int cant) sync* {
  for (int i = 1; i <= cant; i++) {
    yield i;
  }
}

void printIterable() {
  print('Ejemplo 9: Funcion generadora');
  print(getNumberList(5));
}

//EXTRA!!!
void getNumbers(String text1, String text2) {
  print('Ejercicio EXTRA!!!');
  int cant = 0;
  for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      print('$i $text1 y $text2');
    } else if (i % 3 == 0) {
      print('$i $text1');
    } else if (i % 5 == 0) {
      print('$i $text2');
    } else {
      cant++;
      print(i);
    }
  }
  print('Numeros que no son multiplos de 3 ni 5: $cant');
}
