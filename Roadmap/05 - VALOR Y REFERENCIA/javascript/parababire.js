const prompt = require('prompt-sync')();
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
Los datos tipo Array, Object y Function*/

//Al asignar un objeto a una variable, este es guardado en un espacio de memoria libre (referencia).
let carro = {
  color: "azul",
  puertas: 2,
  ruedas: 4,
}
let carro1 = carro;//JS busca la referencia asiganada a la variable carro y la copia a carro1.
carro.puertas = 4;//Se modifica la propiedad puertas del objeto guardado en la variable carro.
console.log(`\nComo ambas variables tienen la misma referencia los cambios al objeto se pueden acceder desde sus copias ejem: carro1.puertas = ${carro1.puertas}.`);

//Parámetros asignados por valor

function sumar(suma) {
  return suma = suma + 1;
}

let suma = 1;
console.log(sumar(suma));
console.log(suma);

//Parámetros asignados por referencia

function comer(fruto) {
  return fruto.cantidad = fruto.cantidad -1;
}

let fruto = {
  nombre: 'banana',
  cantidad: 4
}

console.log(comer(fruto));
console.log(fruto.cantidad);