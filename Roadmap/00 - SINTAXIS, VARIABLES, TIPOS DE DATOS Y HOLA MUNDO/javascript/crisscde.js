/* 
  * Documentación de JS
  JS tiene 2 documentaciones oficiales:
    - MDN JavaScript => https://developer.mozilla.org/es/docs/Web/JavaScript
    - ECMAScript => https://ecma-international.org/publications-and-standards/standards/ecma-262/
*/


// * Formas de crear comentarios

// Comentarío de una sola linea

/* 
  Comentario 
  multilínea
*/

// * Formas de crear variables
/* 
  Antes de ECMAScript 6
    Antes solo se podían crear variables con var, estas variables tienen:
      - 2 ámbitos (global y función)
      - Puede ser re-asignadas y re-declaradas
      - Puede ser declarada sin inicializar 
      - Al momento de ser elevadas al inicio de su scope (Hoisting). Las variables creadas con var
        son inicializadas con undefined
*/
var variable1 = "Antes de ECMAScript 6 se usaba esta forma de declarar variables";

/*
  Despues de ECMAScript 6
    
    - Let -> Sirve para crear variables al igual que var, las diferencias son las siguientes>
      - Su ámbito es de bloque
      - Solo puede ser re-asignada
      - Puede ser declara sin inicializar
      - Al momento de ser elevadas al inicio de su scope (Hoisting). Las variables creadas con let
        no son inicializadas
    - const -> Sirve para crear constantes, estas toma todas las caracteristicas de var, la unica
                diferencia es que no pueden ser re-asignadas, por lo mismo, al momento de
                declararlas, se deben de inicializar
*/
let variable2 = "El cambio es el scope, var tiene un scope global y let tiene un scope local"
const constante = "Forma de crear constantes";

// * Tipos de datos primitivos
const string = "Cadena de texto"; // => String
const number = 6; // => Number (integer or float)
const boolean = true; // => Boolean
const nulo = null; // => Null;
const undefinido = undefined; // => undefined
const simbolo = Symbol("Único e inmutable"); // => Symbol
const bigInt = 7893160947916243814n; // => BigInt

// * Mostrando información en la consola
console.log("Hola, JavaScript");