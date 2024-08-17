
// Asignar valores primitivos (por valor)
let a = 'hola';
let b = a;
a += '!';
console.log(a) // el valor de a cambia despues de la modificacion
console.log(b) // b imprime el valor original de a que se le asigno

// Asignar valores complejos (por referencia)
const c = [1,2,3];
const d = c; // en este caso se asigna una refenrecia
d.push(4);
console.log(c) // Se modifica el valor original
console.log(d)

// Pasar valores primitivos (por valor) a una funcion
const greet1 = 'Hello'
const greetings = (greet) => {
  greet = 'Hola javascript';
  return greet;
};
console.log(greetings(greet1)) 
console.log(greet1) // El valor de greet1 no se modifica ni se reasigna fuera de la funcion

// Pasar valores complejos a una funcion
let arreglo = [1,2,3]
function referencia(arr) {
  arr.push(4);
  console.log('Dentro de la funcion ', arr) 
}

referencia(arreglo)
console.log('Fuera de la funcion: ', arreglo) // Se modifica el valor original

// Pasar valores complejos a una funcion y que no se modifiquen
let arreglo2 = [1,2,3]
function copia(arr) {
  const copy = arr.slice(0) // copia del arreglo original
  copy.push(4);
  console.log('Dentro de la funcion ', copy) 
}

copia(arreglo2)
console.log('Fuera de la funcion: ', arreglo2) 

// DIFICULTAD EXTRA
let num1 = 10
let num2 = 20

function porValor(n1, n2) {
  let temp = n1
  n1=n2
  n2=temp
  return [n1, n2]
}

let [num1_f, num2_f] = porValor(num1, num2)
console.log(`Valores que la funcion retorna: ${num1_f} , ${num2_f}`)
console.log(`Valores originales: ${num1} , ${num2}`)

let valores1 = [1,2,3]
let valores2 = [10, 20, 30]

function porReferencia(v1, v2) {
  let temp = v1
  v1=v2
  v2=temp
  return [v1, v2]
}

let [valores1_f, valores2_f] = porReferencia(valores1, valores2)
console.log(`Valores que la funcion retorna: ${valores1_f} y ${valores2_f}`)
console.log(`Valores originales: ${valores1} y ${valores2}`)