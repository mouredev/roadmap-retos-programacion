

let cuentaRegresiva = numero => {
  //Base case: donde finaliza la función de llamarse así misma.
  if (numero === 0) {
    return;
  }
  console.log(numero);
  return cuentaRegresiva(numero - 1);
}
//console.log(cuentaRegresiva(100));

let parImpar = numero => {
  if (numero === 0) {
    return "Par";
  } else if (numero === 1) {
    return "Impar";
  } else {
    return parImpar(numero - 2)
  }
}
//console.log(parImpar(7));

//Extra

let factorial = n => {
  if (n < 0) {
    return -1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(5));