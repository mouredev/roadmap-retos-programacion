// Tipos de Funciones en JavaScript
function sinParametrosNiRetorno() {
  console.log("No hay parámetros ni retorno");
}
function conUnParametro(parametro) {
  console.log("El parámetro es: " + parametro);
}
function conVariosParametros(parametro1, parametro2) {
  console.log("Los parámetros son: " + parametro1 + " y " + parametro2);
}
function conRetorno(parametro) {
  return parametro;
}
function conVariosRetornos(parametro) {
  return [parametro, parametro + 1];
}

//Funciones dentro de funciones
function funcionPrincipal() {
  console.log("Función Principal");
  function funcionSecundaria() {
    console.log("Función Secundaria");
  }
  funcionSecundaria();
}

//Ejemplo de función propia de JavaScript
function mostrarAlerta() {
  alert("Alerta");
}

//Ejemplo de variable global y local
var variableGlobal = "Variable Global";
function mostrarVariableGlobal() {
  console.log(variableGlobal);
  var variableLocal = "Variable Local";
  console.log(variableLocal);
}
mostrarVariableGlobal();

//Ejercicio extra
let primerParametro = "Primero";
let segundoParametro = "Segundo";
let array = [];
function retornoParams(param1, param2) {
  for (let i = 1; i < 101; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      array.push(param1 + param2);
    } else if (i % 3 == 0) {
      array.push(param1);
    } else if (i % 5 == 0) {
      array.push(param2);
    } else {
      array.push(i);
    }
  }
  return array;
}
let resultado = retornoParams(primerParametro, segundoParametro);
console.log(resultado);
