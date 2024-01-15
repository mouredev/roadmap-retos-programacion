///URL del sitio web oficial: https://dart.dev/

///Formas de crear comentarios:

//Comentario de código en formato línea

///Comentario docuementación en formato línea

/** 
 * Comentario de código y documentación en formato bloque
*/

void main() {

  ///Crea una variable

  var reto = 'reto_00'; //declaración implícita
  String aspectoReto = 'Sintaxis'; //declaración explícita



      ///Variables constantes. 
      ///   final: no se puede cambiar el valor
      ///   const: constante en tiempo de compilación
  

  final nombre = 'Marina'; //declaración constante implícita 
  final String user = 'marina'; //declaración constante explícita

  const mes = 'Enero';
  const int dia = 1;

  ///Tipos de datos primitivos

  int numEntero = 34;
  double numDoble = 56.9;

  String texto = "Reto 00";

  bool estadoTrue = true;
  bool estadoFalse = false;

  List listaValores = ['Sintaxis', 'Variables', 'Tipos', 'Print'];

  Set lenguajes = {'dart', 'java', 'python', 'c++'};
  Set<String> lenguajesPRG = {}; //Conjunto vacío

  Map capitales = {
    'España' : 'Madrid',
    'Alemania' : 'Berlín',
    'Francia' : 'París'
  };

  //Imprimir valores

  print("¡Hola, dart!");
}