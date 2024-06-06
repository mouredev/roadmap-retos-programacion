/// URL del sitio web oficial: https://dart.dev/

import 'dart:io';

void main() {
  /// El paso por valor consiste en que se pasa una copia del valor original al parámetro de la función.
  /// Cualquier modificación no afecta a la variable original
  int valor = 304;
  modificarNumero(valor);
  print(valor);
  
  //// El paso por referencia conciste en que cuando se le pasa un objeto a una función, en este caso
  /// lo que se le pasa es la referencia al objeto original
  /// Si se modifica el contenido del objeto dentro de la función, esos cambios se reflejan
  /// fuera de la función ya que ambas referencias apuntan al mismo objeto

  List<int> lista = [2, 4, 5];
  modificarLista(lista);
  print(lista);

  /// Dificultad extra
  
  var resultadoPaso = pasoParametros(palabra1, palabra2);
  String palabraMod1 = resultadoPaso[0];
  String palabraMod2 = resultadoPaso[1];

  print("$palabra1, $palabra2, $palabraMod1, $palabraMod2");

  var resultadoRef = pasoReferencia(lista1, lista2);
  List<String> listaMod1 = resultadoRef[0];
  List<String> listaMod2 = resultadoRef[1];

  print("$lista1, $lista2, $listaMod1, $listaMod2");

}

void modificarNumero(int valor) {
  valor = 244;
}

void modificarLista(List<int> valores) {
  valores[2] = 7;
}

/// Dificultad extra
  String palabra1 = "dart";
  String palabra2 = "reto";

pasoParametros(palabraPaso1, palabraPaso2) {
  String auxValor;
  auxValor = palabraPaso1;
  palabraPaso1 = palabraPaso2;
  palabraPaso2 = auxValor;
  return [palabra1, palabra2];
}

List<String> lista1 = ["python", "java", "typescript"];
List<String> lista2 = ["c++", "dart", "haskell"];

pasoReferencia(List<String> listaRef1, List<String> listaRef2) {
  List<String> auxRef;
  auxRef = listaRef1;
  listaRef1 = listaRef2;
  listaRef2 = auxRef;
  return [lista1, lista2];
}
