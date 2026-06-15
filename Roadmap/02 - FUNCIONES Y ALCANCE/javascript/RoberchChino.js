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

// funcion sin retorno

const saludar = () => {
  console.log("Hola mundo");
};
saludar();

// funcion dentro de funcion

const funcionExterna = () => {
  console.log("Soy la función de afuera");

  const funcionInterna = () => {
    console.log("Soy la función de adentro");
  };

  funcionInterna();
};

funcionExterna();

const calcularArea = (base, altura) => {
  return base * altura;
};
console.log(calcularArea(5, 5));

const esMayorDeEdad = (edad) => {
  if (edad >= 18) {
    return true;
  } else {
    return false;
  }
};
console.log(esMayorDeEdad(15));
console.log(esMayorDeEdad(18));
console.log(esMayorDeEdad(19));
console.log(Math.max(10, 20, 5));

let planeta = "Tierra";

const localizacion = () => {
  let pais = "Mexico";
  console.log(planeta);
  console.log(pais);
};

localizacion();
console.log(planeta);
// console.log(pais) // // ERROR: pais no existe fuera de la función

const fizzBuzz = (palabra1, palabra2) => {
  let contador = 0;

  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(palabra1 + palabra2);
    } else if (i % 3 === 0) {
      console.log(palabra1);
    } else if (i % 5 === 0) {
      console.log(palabra2);
    } else {
        console.log(i)
        contador++
    }
  }

  return contador;
};

console.log(fizzBuzz("Dia", "Noche"));
