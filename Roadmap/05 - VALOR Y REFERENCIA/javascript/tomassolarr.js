/*
  ASIGNACIÓN POR VALOR
*/

let numero1 = 10;
let numero2 = 20;

let copiaNumero1 = numero1;
let copiaNumero2 = numero2;

copiaNumero1 = 50;

console.log(numero1);
console.log(copiaNumero1);

/*
  ASIGNACIÓN POR REFERENCIA
*/

let objeto1 = { nombre: "Tomas" };
let objeto2 = objeto1;

objeto2.nombre = "Juan";

console.log(objeto1.nombre);
console.log(objeto2.nombre);

/*
  FUNCIÓN POR VALOR
*/

function cambiarValor(valor) {
  valor = 100;
  return valor;
}

let dato = 30;
let nuevoDato = cambiarValor(dato);

console.log(dato);
console.log(nuevoDato);

/*
  FUNCIÓN POR REFERENCIA
*/

function cambiarReferencia(persona) {
  persona.nombre = "Pedro";
  return persona;
}

let usuario = { nombre: "Diego" };
let nuevoUsuario = cambiarReferencia(usuario);

console.log(usuario);
console.log(nuevoUsuario);

/*
  EJERCICIO EXTRA - INTERCAMBIO POR VALOR
*/

function intercambiarValor(a, b) {
  let temp = a;
  a = b;
  b = temp;
  return [a, b];
}

let x = 1;
let y = 2;

let [nuevoX, nuevoY] = intercambiarValor(x, y);

console.log(x);
console.log(y);
console.log(nuevoX);
console.log(nuevoY);

/*
  EJERCICIO EXTRA - INTERCAMBIO POR REFERENCIA
*/

function intercambiarReferencia(obj1, obj2) {
  let temp = obj1.valor;
  obj1.valor = obj2.valor;
  obj2.valor = temp;
  return [obj1, obj2];
}

let objetoA = { valor: 10 };
let objetoB = { valor: 20 };

let [nuevoA, nuevoB] = intercambiarReferencia(objetoA, objetoB);

console.log(objetoA);
console.log(objetoB);
console.log(nuevoA);
console.log(nuevoB);