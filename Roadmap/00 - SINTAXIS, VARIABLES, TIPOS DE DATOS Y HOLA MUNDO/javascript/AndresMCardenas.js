// web oficial: https://developer.mozilla.org/es/docs/Web/JavaScript

// asi se comenta en javascript en una sola linea

/*
Esta es la forma de comentar en 
javascript en 
varias lineas
*/

// esta es una variable
// las variables se declaran con la palabra reservada var es de forma global
var nombre1 = "Andres";
// las variables se declaran con la palabra reservada let es de forma local
let nombre2 = "Mauricio";
// las variables se declaran con la palabra reservada const es de forma local y no se puede cambiar su valor
const apellido = "Cardenas";

// tipos de datos primitivos

// string es un tipo de dato que se usa para guardar cadenas de texto
let usuarioTwitch = "Xamael123";
// number 
let edad = 37;
// boolean  es un tipo de dato que solo puede tener dos valores true o false
let casado = false;
// null es un tipo de dato que se usa para inicializar una variable
let carro = null;
// undefined es un tipo de dato que se usa para inicializar una variable
let casa;
// symbol es un tipo de dato que se usa para crear identificadores unicos para objetos inmutables
let simbolo = Symbol("mi simbolo");

// tipos de datos estructurados

// object es un tipo de dato que se usa para guardar objetos
let persona = {
  nombre: "Andres",
  edad: 37,
  casado: false
};
// array es un tipo de dato que se usa para guardar arreglos

let nombreCompleto = ["Andres", "Mauricio", "Cardenas"];

// asi se imprime en consola
console.log("Hola mundo!!!" , "Javascript");