

void main(){


/* Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
 Debes hacer print por consola del resultado de todos los ejemplos.
 (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)



- Sin parámetros ni retorno, con uno o varios parámetros, con retorno... */

void functionOne (){
  print('Hola');
}

void printName(String name) {
  print(name);
}

int sum(int num1, int num2){
  return num1 + num2;
}

/*- Comprueba si puedes crear funciones dentro de funciones.*/
void outerFunction() {
  print("This is the outer function.");

  void innerFunction() {
    print("This is the inner function.");
  }

 
  innerFunction();
}

outerFunction();
printName('Evelyn');
sum(1,2);


//- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.


 //- Pon a prueba el concepto de variable LOCAL y GLOBAL.

int globalVariable = 10; // Variable global

void functionTwo() {
  int localVariable = 5; // Variable local 

  print("Global variable: $globalVariable");
  print("Local variable: $localVariable");

  void innerFunction() {
    int localVariable = 20; // Variable local en innerFunction
    print("Global variable inside innerFunction: $globalVariable");
    print("Local variable inside innerFunction: $localVariable");
  }

  innerFunction();
}

functionTwo();

 


 



/*DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que: 
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 
Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
int printNumbers(String value1, String value2) {
  int counter = 0;

  for (var i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      print(value1 + value2);
    } else if (i % 3 == 0) {
      print(value1);
    } else if (i % 5 == 0) {
      print(value2);
    } else {
      print(i);
      counter++;  
    }
  }

  return counter;  
}
}