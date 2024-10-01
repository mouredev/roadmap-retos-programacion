/*Funciones en Javascript*/

/* Funciones declaradas en JS */
/*Las funciones declaradas son aquellas funciones que se definen con la palabra clave function, seguida del nombre
  al igual que los parámetros opcionales que deseemos utilizar en dicha función y, por último, las llaves que definirán el bloque de
  código que ejecutará dicha función

  Para hacer uso de esta función, se debe hacer un llamado, especificando los argumentos (si así es requerido), de los que hará uso la función
*/

/* Función */
function multiplicarNumeros(a, b) {
  return console.log(`El resulta de multiplicar ${a} * ${b} es: ${a * b}`);
}

/* Llamado a la función */
multiplicarNumeros(7, 9);

/* Funciones expresadas en JS */
/* Las funciones expresadas son aquellas que se pueden guardar en una variable o constante: */
// No es obligatorio que tengan nombre

const saludo = function (nombre) {
  return console.log(`Hola ${nombre}`);
};

saludo(`orlas135`);

/* Funciones flecha */
/* Las funciones flecha son una manera de crear funciones expresadas de una manera más abreviada */
/* Si la sentencia que irá dentro de estas funciones flecha solo lleva una línea, se pueden omitir las llaves
   al igual que también se puede omitir la palabra return, ya que se convierte en algo implícito
*/

const miFuncion = (num1, num2) => num1 + num2;

console.log(`Resultado de la suma: ` + miFuncion(9, 9));

/* Si se le da el nombre a una función expresada, se puede hacer referencia a ella misma dentro de la misma función */
const factorial = function fac(n) {
  return n < 2 ? 1 : n * fac(n - 1);
};

console.log(factorial(7));

/*Las funciones pueden también servir como argumento para otras funciones previamente definidas */

/*Las funciones también pueden ser vistas como métodos de un objeto, por ejemplo: */

const raiz = Math.sqrt(49);
/*El objeto Math tiene un método llamado sqrt, que saca la raíz cuadrada del número enviado como argumento */

/*Función dentro de otra función*/

function operacionesMatematicas(op, num1, num2) {
  if (op == 1) {
    sumar(num1, num2);
  } else if (op == 2) {
    restar(num1, num2);
  } else if (op == 3) {
    multiplicar(num1, num2);
  } else if (op == 4) {
    dividir(num1, num2);
  } else {
    return console.log(`Opción de operación no válida`);
  }

  function sumar(n1, n2) {
    return console.log(`Resultado: ${n1 + n2}`);
  }
  function restar(n1, n2) {
    return console.log(`Resultado: ${n1 - n2}`);
  }

  function multiplicar(n1, n2) {
    return console.log(`Resultado: ${n1 * n2}`);
  }

  function dividir(n1, n2) {
    console.log(`Resultado: ${n1 - n2}`);
  }
}

operacionesMatematicas(4, 4, 9);

/* Variable local vs Variable global */
/* Dependiendo del contexto en el que se definan las variables y/o funciones en el código, estas van a ser de ámbito global o de ámbito local */
/* Dicho esto, las varibales definidas por fuera de un bloque de código van a ser de ámbito global, pero las varibles o funciones definidas dentro de un bloque de código solo van a poder ser accedidas dentro de ese ámbito */

/*Esta variable pordrá ser accedida en cualquier momento dentro de todo el documento */
const global = `Variable global`;

for (let index = 0; index < 3; index++) {}
/* La varaible index solo puede ser utilizada dentro del bloque de código del ciclo FOR */

/*Dificultad extra */

function dificultadExtra(param1, param2) {
  let veces = 0;
  for (i = 0; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(`${param1 + param2}`);
    } else if (i % 3 == 0) {
      console.log(param1);
    } else if (i % 5 == 0) {
      console.log(param2);
    } else {
      console.log(i);
      veces++;
    }
  }

  return console.log(`El número se imprimió un total de ${veces} veces.`);
}

dificultadExtra(`texto1`, `texto2`);
