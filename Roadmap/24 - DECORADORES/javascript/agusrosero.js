/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 */
class Math {
  add(a, b) {
    return a + b;
  }
}

function decoratorLog(f) {
  let oldValue = f;

  f = function () {
    console.log(`Calling "${f.name}" with`, arguments);
    return oldValue.apply(null, arguments);
  };
}

Math.prototype.add = decoratorLog(Math.prototype.add);

/* DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */

function contadorLlamadas(fn) {
  let contador = 0;

  return function (...args) {
    contador++;
    console.log(`La función ha sido llamada ${contador} veces`);

    return fn.apply(this, args);
  };
}

function saludo(nombre) {
  console.log(`Hola, ${nombre}!`);
}

const saludoConContador = contadorLlamadas(saludo);

saludoConContador("Hernan");
saludoConContador("Agustin");
