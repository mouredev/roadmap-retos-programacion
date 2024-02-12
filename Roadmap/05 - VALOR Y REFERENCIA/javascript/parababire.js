//Asignación de variables.

/*Asignar valor:
Cuando un valor primitivo (number, boolean, string...) es asignado a 
una variable, este puede ser copiado a otra variable por medio de lo 
que conocemos como asignación por valor.*/

let fruta = "banana";
let fruta2 = fruta;//A la variable fruta2 se le asigna una copia del valor contenido en la variable fruta.
fruta = "mandarina";
console.log(`La ${fruta} es el nuevo valor de la variable fruta. Ésta al contener un valor primitivo, 
la copia de su valor en fruta2, no es alterado y sigue siendo ${fruta2}.`);//

/*Asignar referencia:
De datos tipo Array, Object y Function*/

//Al asignar un objeto a una variable, este es guardado en un espacio de memoria libre (referencia).
let carro = {
  color: "azul",
  puertas: 2,
  ruedas: 4,
}
let carro1 = carro;//El motor de javascript busca la referencia asignada a la variable carro y la copia a carro1.
carro.puertas = 4;//Se modifica la propiedad puertas del objeto guardado en la variable carro.
console.log(`\nComo ambas variables tienen la misma referencia los cambios al objeto se pueden acceder desde sus copias ejem: carro1.puertas = ${carro1.puertas}.`);

//Parámetros asignados por valor.

function sumar(suma) {
  return suma = suma + 1;
}

let suma = 1;
console.log(sumar(suma));
console.log(suma);

//Parámetros asignados por referencia.

function comer(fruto) {
  return fruto.cantidad = fruto.cantidad -1;
}

let fruto = {
  nombre: 'banana',
  cantidad: 4
}

console.log(comer(fruto));
console.log(fruto.cantidad);

//Extra

let bike1 = "azul";
let bike2 = "rojo";

//Función de asignación por valor

/*Cabe aclarar que las funciones solo retornan un valor, pero con el uso de arrays u objetos
podemos simular el retorno de más de un valor.*/
function intercambio(bike1, bike2) {
  let temp = bike1;
  bike1 = bike2;
  bike2 = temp;
  return [bike1, bike2];
}

//El uso de desestructuración permite asignar el resultado de una función a un conjunto de variables.
let [bike3, bike4] = intercambio(bike1, bike2);
console.log(bike1);
console.log(bike2);
console.log(bike3);
console.log(bike4);

//Función de asignación por referencia.

let persona1 = {
  cabello: true,
  nombre: 'angel'
}

let persona2 = {
  cabello: false,
  nombre: 'luis'
}

function asignarPorRefencia(persona1, persona2) {
  let temp = persona1.nombre;
  persona1.nombre = persona2.nombre;
  persona2.nombre = temp;
  return [persona1, persona2];
}

const [persona3, persona4] = asignarPorRefencia(persona1, persona2);
console.log(persona1);
console.log(persona2);
console.log(persona3);
console.log(persona4);