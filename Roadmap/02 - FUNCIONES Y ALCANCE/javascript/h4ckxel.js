/* EJERCICIO:

  * Crea ejemplos de funciones básicas que representen las diferentes
    * posibilidades del lenguaje:
 * Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * Comprueba si puedes crear funciones dentro de funciones.
 * Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * Debes hacer print por consola del resultado de todos los ejemplos.
 * (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

*/

// Funciones sin parámetros ni retorno

function saludar() {
    console.log("Hola");
  }
  
  saludar();// se invoca la función
  
  // Funciones con parámetros y retorno
  
  function sumar(dato1, dato2) {
    return dato1 + dato2;
  }
  
  console.log(sumar(2, 3)); // se invoca la función y se imprime el resultado
  
  // Funciones con parámetros y sin retorno
  
  function restar(dato1, dato2) {
    console.log(dato1 - dato2);
  } 
  
  restar(5, 3); // se invoca la función
  
  
  // Funciones con parámetros y retorno
  
  function multiplicar(dato1, dato2) {
    return dato1 * dato2;
  } 
  
  console.log(multiplicar(5, 3)); // se invoca la función y se imprime el resultado
  
  // Funcion dentro de una función
  
  function dividir(dato1, dato2) {
    function sumar(dato1, dato2) {
      return dato1 + dato2;
    }
    return sumar(dato1, dato2) / 2;
  }
  
  console.log(dividir(10, 2)); // se invoca la función y se imprime el resultado
  
  
  // Funciones ya creadas en el lenguaje
  
  // Función parseInt() - Convierte una cadena a un número entero
  let cadena = "123";
  let numero = parseInt(cadena);
  console.log(numero);  // Imprime: 123
  
  // Función parseFloat() - Convierte una cadena a un número de punto flotante
  let cadenaFlotante = "123.45";
  let numeroFlotante = parseFloat(cadenaFlotante);
  console.log(numeroFlotante);  // Imprime: 123.45
  
  // Función isNaN() - Comprueba si un valor es NaN
  let valorInvalido = "abc" / 10;  // Esto resultará en NaN
  console.log(isNaN(valorInvalido));  // Imprime: true
  
  // Función Math.random() - Genera un número aleatorio entre 0 (inclusive) y 1 (exclusivo)
  let aleatorio = Math.random();
  console.log(aleatorio);
  
  // Función Array.isArray() - Comprueba si un valor es un array
  let array = [1, 2, 3];
  console.log(Array.isArray(array));  // Imprime: true
  
  // Función Date.now() - Devuelve el número de milisegundos transcurridos desde el 1 de enero de 1970 hasta la fecha/hora actual
  let fecha = Date.now();
  
  console.log(fecha);
  
  // Crear un nuevo objeto Date que representa la fecha y hora actuales
  let fecha2 = new Date();
  
  // Obtener el día, mes y año
  let dia = fecha2.getDate();  // Devuelve el día del mes (de 1 a 31)
  let mes = fecha2.getMonth() + 1;  // Devuelve el mes (de 0 a 11, por eso se suma 1)
  let año = fecha2.getFullYear();  // Devuelve el año
  
  console.log("Hoy es " + dia + "/" + mes + "/" + año);
  
  // Variable local y global
  
  let variableGlobal = "Soy una variable global";
  
  function mostrarVariableGlobal() {
    console.log(variableGlobal);
  }
  
  mostrarVariableGlobal(); // Imprime: Soy una variable global
  
  function mostrarVariableLocal() {
    let variableLocal = "Soy una variable local";
    console.log(variableLocal);
  }
  
  mostrarVariableLocal(); // Imprime: Soy una variable local
  
  // console.log(variableLocal); // Imprime: Uncaught ReferenceError: variableLocal is not defined
  
  // Función anónima se usa para asignar una función a una variable o constante
  
  let funcionAnonima = function () {
    console.log("Soy una función anónima");
  }
  
  funcionAnonima(); // Imprime: Soy una función anónima
  
  // Función flecha se usa para asignar una función a una variable o constante
  
  let funcionFlecha = () => {
    console.log("Soy una función flecha");
  }
  
  funcionFlecha(); // Imprime: Soy una función flecha
  
  let objeto = {
    valor: 'Hola',
    funcion: function () {
      console.log(this.valor); // Imprime: Hola
    },
    funcionFlecha: () => {
      console.log(this.valor); // Imprime: undefined
    }
  }
  objeto.funcion();
  objeto.funcionFlecha();
  
  /*
  DIFICULTAD EXTRA (opcional):
    Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    La función retorna el número de veces que se ha impreso el número en lugar de los textos 
    Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
    Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
  */

var writtenNumber = require('written-number'); // Se instala el paquete written-number para convertir números a letras se usa el comando: npm install written-number

function imprimirNumeros(cadena1, cadena2) { 
contador = 0;
numeroaletras1 = 0;
for (let i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
    numeroaletras1 = i;
    palabras1 = writtenNumber(numeroaletras1, { lang: 'es' });
    console.log(palabras1);
    //console.log(cadena1 + cadena2);
    } else if (i % 3 == 0) {
    numeroaletras1 = i;
    palabras1 = writtenNumber(numeroaletras1, { lang: 'es' });
    console.log(palabras1);
    //console.log(cadena1);
    } else if (i % 5 == 0) {
    numeroaletras1 = i;
    palabras1 = writtenNumber(numeroaletras1, { lang: 'es' });
    console.log(palabras1);
    //console.log(cadena2);
    } else {
    console.log(i);
    contador++;
    }
}
return contador;
}
resultado = imprimirNumeros("Fizz", "Buzz");
console.log("Número de veces que se ha impreso el número en lugar de los textos: ", resultado);
