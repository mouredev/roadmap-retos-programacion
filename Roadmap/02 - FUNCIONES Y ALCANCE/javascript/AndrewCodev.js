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

//Funcion tradicional
function tradicional() {
  console.log("Función creada de manera tradicional");
}

tradicional();

//funciones de flecha

const sinParamsNiReturns = () => {
  console.log("Esta función no tiene parametros ni retornos");
};

sinParamsNiReturns();

const conParametros = (num1, num2) => {
  console.log(num1 + num2);
};

conParametros(27, 7);

const conRetorno = (num1, num2) => {
  return num1 + num2;
};

conRetorno(9, 8);

//Funciones dentro de funciones?

const miPrimerFuncion = (nombre, apellido, edad) => {
  const persona = [nombre, apellido, edad];

  const miSegundaFuncion = (persona) => {
    console.log(persona);
    return (
      "Mi nombre es : " +
      persona[0] +
      ", mi apellido es: " +
      persona[1] +
      " y mi edad es: " +
      persona[2]
    );
  };

  return miSegundaFuncion(persona);
};

miPrimerFuncion("Andrew", "Codev", 31);

//Variable local y global
let varGlobal = "Soy global";

const localGlobal = (varGlobal) => {
  let varLocal = "Soy Local";
  if (varGlobal === varLocal) {
    return "La variable local y la global son iguales";
  } else {
    return "La variable local y la global son diferentes";
  }
};

localGlobal(varGlobal);

// DIFICULTAD EXTRA
const dificultadExtra = (cad1, cad2) => {
  let contador = 0;

  for (let i = 0; i <= 100; i++) {
    const esMultiploDe3 = i % 3 === 0;
    const esMultiploDe5 = i % 5 === 0;

    if (esMultiploDe3 && esMultiploDe5) {
      console.log(`${cad1} ${cad2}`);
    } else if (esMultiploDe3) {
      console.log(`${cad1}`);
    } else if (esMultiploDe5) {
      console.log(`${cad2}`);
    } else {
      console.log(i);
      contador++;
    }
  }

  return contador;
};

const vecesNumero = dificultadExtra("Hola", "Mundo");
console.log(`Números impresos: ${vecesNumero}`);
