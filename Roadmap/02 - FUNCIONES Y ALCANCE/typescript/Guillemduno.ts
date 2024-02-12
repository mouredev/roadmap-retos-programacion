/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// Función sin parámetros ni retorno.
function imprimeMensaje(): void {
    console.log("Mensaje");
  }
  
  imprimeMensaje();
  
  // Función con um parámetro que no retorna nada.
  function imprimeEsteMensaje(mensaje: string): void {
    console.log(mensaje);
  }
  
  imprimeEsteMensaje("Hola mundo!");
  
  //Función con más de un parámetro de entrada. Devuelve un número como resultatdo.
  function sumaDosNumeros(num1: number, num2: number): number {
    return num1 + num2;
  }
  let resultado = sumaDosNumeros(2, 4);
  console.log(resultado);
  
  // Función dentro de otra función
  function imprimeMensajeConFuncion(): void {
    imprimeEsteMensaje("Función dentro de otra función.");
  }
  imprimeMensajeConFuncion();
  
  /**
   * FUNCIONES CREADAS POR EL LENGUAJE:
   */
  
  // Números
  const numeroRedondeado = Math.round(2.3);
  console.log("Número redondeado: " + numeroRedondeado);
  
  let numeroCadena = 3; // Tipo number
  console.log("Número cadena: " + numeroCadena.toString() + " tipo: " + typeof numeroCadena.toString());
  
  const miNumero = 2.0;
  console.log(miNumero.toExponential());
  
  // Cadenas
  let miNombre = "guillem";
  console.log(miNombre.toUpperCase()); // GUILLEM
  
  const numeroLetras = miNombre.length;
  console.log(`El número de letras de la palabar ${miNombre} es de ${numeroLetras}`);
  
  // Fechas
  const fecha = Date();
  console.log("Fecha: " + fecha);
  
  // Arrays
  
  const misCoches = ["Opel", "Ford"];
  const susCoches = ["Renault", "Seat"];
  console.log(misCoches.concat(susCoches)); // Concatena los dos array en uno.
  
  const misNotas = [2, 4, 6];
  const misNotasMas1 = misNotas.map((x) => x + 1); // Suma uno a cada numero del array.
  console.log(misNotasMas1);
  
  /**
   * Variable LOCAL i GLOBAL
   *  */
  
  // Si se declara la variable num fuera de la funcion esta será global y la
  // función tendrá accesso a ella.
  let num = 10; //variable global
  
  function muestraNumero() {
    console.log("dentro muestra número: " + num);
  }
  muestraNumero();
  
  // Si se declar la variable dentro de la función, solo sera accesible dentro de
  // la función.
  function muestraOtroNumero() {
    let otroNum = 10;
    console.log("desde muestra otro número: " + otroNum);
  }
  
  muestraOtroNumero();
  
  //console.log(otroNum); // Muestra error porque detecta que esta variable no esta definida.
  
  console.log(num);
  
  /**
   * EJERCICIO EXTRA
   */
  
  function imprimeMultiplos(str1: string, str2: string) {
    let count: number = 0;
    for (let index = 1; index <= 100; index++) {
      let esMultiplo3 = index % 3 === 0;
      let esMultiplo5 = index % 5 === 0;
  
      if (esMultiplo3 && esMultiplo5) {
        console.log(index + " " + str1 + " y " + str2);
      } else if (esMultiplo3) {
        console.log(index + " " + str1);
      } else if (esMultiplo5) {
        console.log(index + " " + str2);
      } else {
        console.log(index);
        count++;
      }
    }
    console.log("veces que se ha impreso el número: " + count);
  }
  
  imprimeMultiplos("multiplo de 3", "multiplo de 5");
  