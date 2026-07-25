// Función sin parámetros ni retorno
function sayHello() {
  console.log("Hello!");
}

sayHello();

// Función con un parámetro y retorno
function myNameIs(name) {
  return "My name is " + name;
}

console.log(myNameIs("Raquel Tejada"));

// Función con múltiples parámetros y retorno
function sayFullName(name, surname) {
  return name + " " + surname;
}

console.log(sayFullName("Raquel", "Tejada"));

// Función expresión
const myAge = function (age) {
  return "this is my age" + age;
};

// Función flecha
const arrowFunction = () => console.log("this is arrow function");

// Función anidada
function parent(parentName) {
  return function child(childName) {
    return `${parentName} is the father of ${childName}`;
  };
}

// Variable global y variable local
const globalVariable = "Esto es una variable global";

function localVariable() {
  const localVariable = "Esto es una variable local";
  console.log(globalVariable);
  console.log(localVariable);
}

localVariable();

// Dificultad extra
function numbers(chainNumber1, chainNumber2) {
  for (let i = 1; i <= 100; i++) {
    i % 3 === 0 && i % 5 === 0
      ? console.log(chainNumber1 + chainNumber2)
      : i % 3 === 0
      ? console.log(chainNumber1)
      : i % 5 === 0
      ? console.log(chainNumber2)
      : console.log(i);
  }
}
numbers("trying", "extra mile");
