/* 
  * - Crea ejemplos de funciones básicas que representen las diferentes
  *   posibilidades del lenguaje:
  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
*/

//Funciones sin parametros y sin retorno
  const funcion = function(){
    //"Estoy en una función sin parámetros y sin retorno"
  }
  console.log(funcion);

//Funciones con un parametro
  const funcionConUnParametro = function(greeting) {
    console.log(`${greeting}, soy un programa`);
  }
  funcionConUnParametro("Hola");

//funciones con varios parametros
  const funcionConVariosParametros = function(a, b){
    console.log(a + b);
  }
  funcionConVariosParametros(5,10);

//Funciones con retorno
  const sumarDosNumeros = function (x, y) {
    return x + y;
  }
  console.log(sumarDosNumeros(3,4));

//Funciones flecha(es una expresion compacta de lo que es una funcion tradicional)
  /*
    Diferencias y limitaciones:
    No tiene sus propios enlaces a this o super y no se debe usar como métodos.
    No tiene argumentos o palabras clave new.target.
    No apta para los métodos call, apply y bind, que generalmente se basan en establecer un ámbito o alcance
    No se puede utilizar como constructor.
    No se puede utilizar yield dentro de su cuerpo.
  */

  const dividirNumeros = (x, y) => x / y;
  console.log(dividirNumeros(6,2));

/*
   * - Comprueba si puedes crear funciones dentro de funciones.
*/
  const saludar = function(a) {
    const hablar = () => console.log(`Hola ${a}`);
    hablar()
  }

  saludar('JavaScript');

/*
   * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
*/
//En este caso se utiliza la funcion de tiempo 'setTimeout' la cual ejecuta una funcion despues de determinado tiempo
  setTimeout(() => console.log('Hola despues de 2000 ms'), 2000)

/*
  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
*/
// Esta es una variable global, la cual puede ser accedida en cualquier lugar del documento.
let variableGlobal = 'Variable global';

/**
 * Esta es una función llamada miFuncion.
 * Dentro de esta función, se declara una variable local llamada variableLocal.
 * Solo podemos acceder a variableLocal dentro de la función.
 */
function miFuncion() {
  let variableLocal = 'Variable local';
  // Aquí podríamos realizar operaciones con la variableLocal.
}

// Ejemplo de uso de la variable global
console.log(variableGlobal);

// Intentar acceder a la variable local fuera de la función resultaría en un error.
// console.log(variableLocal); // Esto generaría un error porque variableLocal no está definida aquí.

/*
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

const imprimirNumeros = function(a, b) {
  let contadorNumeros = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(`${a} ${b}`);
    } else if (i % 3 === 0) {
      console.log(a);
    } else if (i % 5 === 0) {
      console.log(b);
    } else {
      contadorNumeros++
    }
  }
  return contadorNumeros
}

console.log(`La cantidad de veces en que se imprimio un numero es de: ${imprimirNumeros('Hola', 'JavaScript')}`)
