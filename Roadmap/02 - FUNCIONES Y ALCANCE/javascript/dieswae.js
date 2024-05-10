/* Funcion sin parametros ni retorno */

function helloWorld() {
  console.log('¡Hello World!');
}
helloWorld() //ejecución

/* Funcion con un parametro y sin retorno */

function hiAgain(name) {
  console.log(`Hello, ${name}!`);
}
hiAgain('Diego')

/* Funcion con varios parametros sin retorno */

function SumOfNumbers(a, b) {
  let add = a + b;
  console.log(`La suma de ${a} y ${b} es = ${add}`)
}
addNumbers(34, 35)

/* Funcion sin parametros y con retorno */

function Number() {
  return 7
}
console.log('el numero es', Number());

/* Funcion con parametro y con retorno */

function Name(name){
  return `Hello ${name}!`
}
console.log(Name('Itachi'))

/* Funcion con varios parametros y con retorno */

function nameAndLanguage(name, language) {
  return `¡Hello! my name is ${name}, and my favorite language is ${language}`
}
console.log(nameAndLanguage(Diego, JavaScript));

/* Arrow Functions sin parametros ni retorno */

const Hello = () => console.log('¡Hello! from the console');

/* Arrow Functions con parametros y retorno */

const sayHello = (name) => {
  return `Hello ${name}, from the arrow function`
}
console.log(sayHello('Messi'));

/* función clousure */

function helloClosure () {
  let counter = 0;

  function increment () {
    counter++;
    return counter;
  }
  return increment;
}

const incremento = helloClosure();

console.log(incremento()); // 1
console.log(incremento()); // 2

/* Variable global y local */

const imGLobal = 'soy Global';

function localGlobal () {
  const imLocal = 'soy Local'

  console.log(imGLobal);
  console.log(imLocal);  
}
localGlobal()

/* Funcion Built-in */

let Num = 2
let Text = "Hola"
console.log("variableNumerica: " + typeof(Num) + " variableTexto: " + typeof(Text))

/* EXTRA */

function from1To100 (param1, param2) {
  let count = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(param1 + param2);
    } else if (i % 3 === 0) {
      console.log(param1);
    } else if (i % 5 === 0) {
      console.log(param2);
    } else {
      console.log(i);
      count++
    }
  }
  return count
}

const fizzBuzz = from1To100('Fizz', 'Buzz');
console.log(fizzBuzz);








