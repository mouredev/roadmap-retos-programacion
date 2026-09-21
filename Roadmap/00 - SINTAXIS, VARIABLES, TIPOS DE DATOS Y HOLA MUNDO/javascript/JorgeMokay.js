// WEB OFICIAL JAVASCRIPT
// https://developer.mozilla.org/es/docs/Web/JavaScript

/*
formas de encerrar un comentario en mas lienas
es de esta forma
*/ 

let variable1 = "22";
const constante1 = "55";

console.log(variable1);
console.log(constante1);



// 1. String (Cadena de texto)
let texto = "Hola JavaScript";

// 2. Number (Número entero o decimal)
let numero = 2026;

// 3. BigInt (Números enteros de gran precisión, se añade una 'n' al final)
let numeroGrande = 9007199254740991n;

// 4. Boolean (Verdadero o falso)
let booleano = true;

// 5. Undefined (Variable declarada pero sin valor asignado)
let indefinido;

// 6. Null (Ausencia intencional de valor)
let nulo = null;

// 7. Symbol (Identificador único e inmutable)
let simbolo = Symbol("id");

// Imprimir todos los tipos en consola
console.log(texto);        // "string"
console.log(numero);       // "number"
console.log(numeroGrande); // "bigint"
console.log(booleano);     // "boolean"
console.log(indefinido);   // "undefined"
console.log(nulo);         // "object" (es un comportamiento histórico de JS)
console.log(simbolo);      // "symbol"

