// Función sin parámetros ni retorno
function sayHello() {
  console.log("Hola, mundo!");
}

// Función con un parámetro y retorno
function square(number) {
  return number * number;
}

// Función con varios parámetros y retorno
function calculateSum(a, b) {
  return a + b;
}

// Función anidada dentro de otra función
function outerFunction() {
  function innerFunction() {
    console.log("Función interna");
  }

  innerFunction();
}

// Ejemplo de función predefinida en JavaScript
let arr = [1, 2, 3, 4, 5];
let sum = arr.reduce(function (accumulator, currentValue) {
  return accumulator + currentValue;
});

// Variable global
let globalVariable = "Soy una variable global";

// Función que accede a una variable global
function accessGlobalVariable() {
  console.log(globalVariable);
}

sayHello(); // Imprime "Hola, mundo!"
console.log(square(5)); // Imprime 25
console.log(calculateSum(2, 3)); // Imprime 5
outerFunction(); // Imprime "Función interna"
console.log(sum); // Imprime 15
accessGlobalVariable(); // Imprime "Soy una variable global"

// EJERCICIO EXTRA
function printNumbersWithTexts(text1, text2) {
  let count = 0;

  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(text1 + text2);
      count++;
    } else if (i % 3 === 0) {
      console.log(text1);
      count++;
    } else if (i % 5 === 0) {
      console.log(text2);
      count++;
    }
  }

  return count;
}

console.log(printNumbersWithTexts("Fizz", "Buzz"));
