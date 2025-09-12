/* Concepto de Recursividad */

function imprimirNumerosDescendente(numero) {
  if (numero >= 0) {
    console.log(numero);
    imprimirNumerosDescendente(numero - 1);
  }
}

imprimirNumerosDescendente(100);
