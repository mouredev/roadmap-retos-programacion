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

//Ejemplos de declaración de funciones
//formas de declarar funciones sin parametros ni retorno
function funcion1() {
  if (1 === 1) {
    console.log("1 es efectivamente 1");
  } else {
    console.log("Estamos locos, 1 no es 1");
  }
}

let funcion2 = function () {
  if (1 === 1) {
    console.log("1 es efectivamente 1");
  } else {
    console.log("Estamos locos, 1 no es 1");
  }
};

let arrowFunction = () => {
  console.log("1 es efectivamente 1");
};

//Formas de declarar funciones con parametros pero sin retorno

function funcion3(a) {
  if (a === 1) {
    console.log(a + " es efectivamente 1");
  } else {
    console.log(a + " no es 1");
  }
}

let funcion4 = function (a) {
  if (a === 1) {
    console.log(a + " es efectivamente 1");
  } else {
    console.log(a + " no es 1");
  }
};

let arrowFunction2 = (a) => {
  console.log(a + " es efectivamente " + a);
};

//Formas de declarar funciones con parametros y retorno

function funcion5(a) {
  if (a === 1) {
    return a + " es efectivamente 1";
  } else {
    return a + " no es 1";
  }
}

let funcion6 = function (a) {
  if (a === 1) {
    return a + " es efectivamente 1";
  } else {
    return a + " no es 1";
  }
};

let arrowFunction3 = (a) => {
  return a + " es efectivamente " + a;
};

//Metodo de crear funciones extra. Crear funciones dentro de un obejto
let objeto1 = {
  funcionObjeto() {
    console.log("Soy una función dentro de un objeto");
  },
};

//Crear funcion dentro de otra funcion (con bonus, retornar una funcion como resultado de otra: Función anidada)

function nuevoSaludo(saludo) {
  return function (nombre) {
    console.log(saludo + ", " + nombre);
  };
}

let saludoEspanol = nuevoSaludo("Hola"); //la función nuevoSaludo retorna la función interna y esta se asigna a la variable saludoEspañol
saludoEspanol("Manuel"); //Al llamar a saludoEspañol, se llama a la funcion interna que almacena y recibe el parametro nombre

//Ejercico extra

function impNum(a, b) {
  console.log("Ejercicio FizzBuzz");
  console.log("------------------")
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(a +  b);
    } else if (i % 3 === 0) {
      console.log(a);
    } else if (i % 5 === 0) {
      console.log(b);
    } else {
      console.log(i);
    }
  }
  console.log("------------------")
}
impNum("Fizz", "Buzz");