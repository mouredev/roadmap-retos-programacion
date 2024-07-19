/*
  EJERCICIO:
  Explora el concepto de "decorador" y muestra cómo crearlo
  con un ejemplo genérico.
*/

console.log("+++++++++ EJEMPLO DE DECORADOR +++++++++");

function decoratorMyName(callback) {
  return function(myName) {
    callback(myName);
  };
}

function sayHello(name) {
  console.log(`¡Hola, me llamo ${name}!`);
}

const decoratedSayHello = decoratorMyName(sayHello);

decoratedSayHello("Samus Aran");

/*
  DIFICULTAD EXTRA (opcional):
  Crea un decorador que sea capaz de contabilizar cuántas veces
  se ha llamado a una función y aplícalo a una función de tu elección.
*/

console.log("\n+++++++++ CONTADOR DE LLAMADAS EN FUNCIONES +++++++++");

function decoratorCounter(callback) {
  let counter = 0;

  return function() {
    counter++;

    console.log(`La cantidad de veces que la funcion "${callback.name}" se ha llamado es de: ${counter}`);
  }
}

function metroid() {
  return;
}

function residentEvil() {
  return;
}

const decoratedMetroid = decoratorCounter(metroid);
const decoratedResidentEvil = decoratorCounter(residentEvil);

decoratedMetroid();
decoratedResidentEvil();
decoratedMetroid();
decoratedMetroid();
decoratedMetroid();
decoratedResidentEvil();
decoratedResidentEvil();
decoratedMetroid();
