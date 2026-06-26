// https://www.typescriptlang.org/

// Función sin parámetros ni retorno
function greet(): void {
  console.log("hola");
}
greet();

// Función con un parámetro
function double(n: number): number {
  return n * 2;
}
console.log(double(5));

// Función con varios parámetros
function add(a: number, b: number): number {
  return a + b;
}
console.log(add(3, 4));

// Función con retorno
function square(n: number): number {
  return n * n;
}
console.log(square(6));

// Función anidada
function outer(): void {
  const x: number = 10;

  function inner(): void {
    console.log(x);
  }

  inner();
}
outer();

// Función de la librería estándar
console.log(Math.sqrt(16));
console.log("hello".toUpperCase());

// Variable local vs global
let global: string = "global";

function checkScope(): void {
  let local: string = "local";
  console.log(global);
  console.log(local);
}
checkScope();
console.log(global);

// Dificultad extra: FizzBuzz con parámetros
function fizzBuzz(fizz: string, buzz: string): number {
  let count: number = 0;
  for (let i: number = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(fizz + buzz);
    } else if (i % 3 === 0) {
      console.log(fizz);
    } else if (i % 5 === 0) {
      console.log(buzz);
    } else {
      console.log(i);
      count++;
    }
  }
  return count;
}

const printed: number = fizzBuzz("Fizz", "Buzz");
console.log(`Números impresos: ${printed}`);
