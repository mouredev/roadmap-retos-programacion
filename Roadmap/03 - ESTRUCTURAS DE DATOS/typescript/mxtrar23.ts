// Estructuras

// Array
const listaFrutas = ['Manzana','Pera','Kiwi','Fresa'];
console.log(listaFrutas);

listaFrutas.push('Melocotón') // Insercion
listaFrutas.push('Piña')
console.log(listaFrutas);

listaFrutas.push('Fresa') // Eliminación
console.log(listaFrutas);

console.log(listaFrutas[2]); // Acceso


listaFrutas[1]='Cereza' // Actualizacion
console.log(listaFrutas);

listaFrutas.sort(); // Ordenamiento
console.log(listaFrutas);


//Map

let edades = new Map()

edades.set('Jorge',35) // Insercion
edades.set('Carlos',28)
edades.set('Emilio',15)
console.log(edades);
console.log(edades.size); // Tamaño


console.log(edades.get('Jorge')); // Acceso

edades.set('Emilio',19)// Actualización
console.log(edades);

edades.delete('Carlos') // Eliminación
console.log(edades);


//set

const notebook = new Set()

notebook.add(1);// Inssercion
notebook.add('Hola');
notebook.add(['Fresa','Naranja']);
notebook.add({dia:'mañana',hora:'9:00am'});

console.log(notebook);

console.log(notebook.size); // Tamaño

console.log(notebook.has('Hola')); // Comprueba

notebook.delete(1) // Eliminación
console.log(notebook);



























