// Conjuntos de datos en JavaScript

let myArray = ["Perro","Gato","Ciervo","Rinoceronte"] // conjunto de datos array.

myArray.push ("Cabra"); // añade elemento al final del array.
console.log(myArray);

myArray.unshift ("Cebra"); // añade elemento al principio del array.
console.log(myArray);

myArray.push ("Gamo","Vaca","Toro"); // añade varios elementos en bloque al final.
console.log(myArray);

myArray.splice (2,0,"Gacela","Cerdo"); // añade varios elementos en la posicion dada.
console.log(myArray);

delete (myArray[3]) // elimina elemento de array , en este caso posicion 3.
console.log(myArray);

myArray[0] = 'Cerdo' // acutaliza elemento [0] del array , lo actualiza a nombre de animal 'Cerdo'.
console.log(myArray);

console.log('--------------')
console.log (myArray.includes('Cerdo')) // busca el elemento 'Cerdo' dentro de myArray.

myArray = [] // Elimina todo el contenido del arrau
console.log(myArray);

