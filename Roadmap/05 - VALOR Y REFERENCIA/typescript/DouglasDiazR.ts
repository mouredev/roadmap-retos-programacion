//Asignación por Valor
let varA = 10;
let varB = varA; // Se asigna el valor de `varA` a `varB`

varB = 20; // Modificamos el valor de `varB`

console.log("varA: ", varA); // Imprime: 10 (el valor de la variable`varA` no cambió)
console.log("varB: ", varB); // Imprime: 20 (el valor de la variable`varB` se modificó)

//Asignación por Referencia
let _obj1 = { name: "Javier" };
let _obj2 = _obj1; //Se asigna el valor de obj1 a obj2

_obj2.name = "Douglas"; // Modificamos la propiedad 'name' del obj2

console.log("obj1: ", _obj1); // Imprime obj1:  { name: 'Douglas' } la modificación afecta a obj1
console.log("obj2: ", _obj2); // imprime obj2:  { name: 'Douglas' }

//Función con parámetros pasados por valor
function incremetarValor(x: number): void {
  x = x + 1; // Se modifica el valor de x
  console.log("x: ", x);
}

let _num = 10;

incremetarValor(_num); //se pasa el valor de _num por valor

console.log("num: ", _num); //el valor de '_num' no fue modificado

//Función con parámetros pasados por referencia
function actualizarNombre(persona: { nombre: string }): void {
  persona.nombre = "Javier"; // Modificamos el nombre en el objeto
  console.log("persona.nombre: ", persona.nombre);
}

let objPersona = { nombre: "Douglas" };

actualizarNombre(objPersona); // Se pasa `objPersona` por referencia

console.log("objPersona: ", objPersona); // Imprime: "Javier" (el objeto fue modificado)

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

let _num1 = 5;
let _num2 = 10;

function porValor(param1: number, param2: number): [number, number] {
  let temporal = param1;
  console.log("temporal", temporal);
  param1 = param2;
  console.log("param1", param1);
  param2 = temporal;
  console.log("param2", param2);
  return [param1, param2];
}

let [_nuevoValor1, _nuevoValor2] = porValor(_num1, _num2);
console.log("valorInicial1", _num1); //5
console.log("ValorInicial2", _num2); //10
console.log("nuevoValor1", _nuevoValor1); //10
console.log("nuevoValor2", _nuevoValor2); //5

let personaObj1 = { nombre: "Javier" };
let personaOBj2 = { nombre: "Ivana" };

function porReferencia(param1: { nombre: string }, param2: { nombre: string }) {
  let temporalObj = param1.nombre;
  console.log("temporal", temporalObj);
  param1.nombre = param2.nombre;
  console.log("param1", param1);
  param2.nombre = temporalObj;
  console.log("param2", param2);
  return [param1, param2];
}

let [nuevoValorObj1, nuevoValorObj2] = porReferencia(personaObj1, personaOBj2);
console.log("valorinIcialObj1", personaObj1); // { nombre: 'Ivana' }
console.log("valorinIcialObj2", personaOBj2); // { nombre: 'Javier' }
console.log("nuevoValorObj1", nuevoValorObj1); // { nombre: 'Ivana' }
console.log("nuevoValorObj2", nuevoValorObj2); // { nombre: 'Javier' }
