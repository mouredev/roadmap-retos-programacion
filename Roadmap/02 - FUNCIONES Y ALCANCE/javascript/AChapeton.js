// *** TIPOS DE FUNCIONES ***

//Funcion Autoejecutable
(function () {
  console.log("Autoejecutable");
})();

//Funcion por Declaracion
function saludar() {
  return console.log('Hello World!');
}
saludar();

//Funcion por Expresion
var saludo = function saludar2() {
  return console.log('Hola!');
};
saludo();

//Funcion Anonima
var anonima = function () {
  return console.log('Sin nombre');
};
anonima();

//Arrow Function
var arrow = function () {
  return console.log('Arrow function');
};
arrow();

//Callbacks
var funB = function () {
  return console.log('Funcion B ejecutada');
};
var funA = function (callback) {
  callback();
};
funA(funB);


// *** FORMAS DE USO DE FUNCIONES ***

//Sin parametros
var sinParametros = function () {
  return console.log('Sin parametros');
};

//Con uno o varios parametros
var suma = function (a, b) {
  return console.log(a + b);
};
suma(4, 3);

//Sin retorno
var sinReturn = function () {
  console.log('Sin return');
};
sinReturn();

//Con retorno
var conReturn = function () {
  var sum = 4 + 5;
  return sum;
};
conReturn();

//Variable Local y Global
var globalVar = 10;
var funcLocal = function () {
  var localVar = 4;
  globalVar = 2;
  return console.log(localVar + globalVar);
};
//localVar no es accesible fuera de la funcion
//globalVar esta disponible en cualquier lugar de la funcion
funcLocal();


//EJERCICIO EXTRA
var funbun = function (firstText, secondText) {
  var count = 0;
  for (var i = 1; i <= 100; i++) {
      if (i % 3 === 0 && i % 5 === 0) {
          console.log(firstText + secondText);
      }
      else if (i % 3 === 0) {
          console.log(firstText);
      }
      else if (i % 5 === 0) {
          console.log(secondText);
      }
      else {
          count++;
          console.log(i);
      }
  }
  console.log('Numeros impresos: ', count);
  return count;
};
funbun('FUN', 'BUN');
