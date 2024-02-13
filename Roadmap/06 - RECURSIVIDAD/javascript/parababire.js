//Cuenta regresiva por recursión

let cuentaRegresiva = numero => {
  //Base case: donde finaliza la función de llamarse así misma.
  if (numero === 0) {
    return;
  }
  console.log(numero);
  return cuentaRegresiva(numero - 1);
}
console.log(cuentaRegresiva(100));

//Extra

/*Número factorial*/
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

/*Fibonachi*/
let fibNum = n => {
  if (n <= 1) {
    return n;
  } else {
    return fibNum(n - 1) + fibNum(n - 2);
  }
}
console.log(fibNum(8));