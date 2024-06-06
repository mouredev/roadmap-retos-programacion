//Cuenta regresiva por recursión

let cuentaRegresiva = numero => {
  //Base case: donde finaliza la función de llamarse así misma.
  if (numero >= 0) {
    console.log(numero);
    cuentaRegresiva(numero - 1);
  }
}
cuentaRegresiva(100);

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
  if (n <= 0) {
    return "Posición no valida";
  } else if (n === 1) {
    return 0;
  } else if (n === 2) {
    return 1;
  } else {
    return fibNum(n - 1) + fibNum(n - 2);
  }
}
console.log(fibNum(7));