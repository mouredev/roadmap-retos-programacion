const obj = {
	nombre: "Facundo",
	apellido: "Muoio",
	phoneNumber: 4546521,
	address: "Avenida Siempre Viva 200",
	age: 27,
	married: false,
	favoriteMovies: [
		"The wolf of wall street",
		"The prestige",
		"The hateful eight",
		"Goodfellas",
	],
};

//actualizacion de propiedad
obj.nombre = "Daniel";
//eliminacion de propieda
delete obj.married;
//insercion de propiedad
obj.favoriteSport = "Futbol";

// Arreglos
const numbers = [2, 3, 6, 8, 9, 10, 1, 4, 7, 5];

//insertar un elemento en un arreglo
numbers.push(11);
numbers.unshift(0);

//acutualizar un elemento en un arreglo
numbers[numbers.length - 1] = 12;

//eliminar elementos de un arreglo
numbers.pop();
numbers.shift();

//eliminar e insertar elementos de un arreglo
numbers.splice(3, 1, 4);

//ordernar los elmentos del arreglo de menor a mayor
numbers.sort((a, b) => a - b);
//ordenar de mayor a menor
numbers.sort((a, b) => b - a);

////cambiar todos los elementos de un array
numbers.fill(3);

//Sets
const set = new Set();

//Añadir elementos
set.add(1);
set.add(2);
set.add(3);

//Eliminar un elemnto
set.delete(2);
//Eliminar todos los elementos
set.clear();

console.log(set[0]);

//Maps
const map = new Map();

//Añadir elementos
map.set("A", "10");
map.set("B", "8");
map.set("C", "6");
map.set("F", "4");

//Actualizar elemento
map.set("A", "9");

//Eliminar elementos
map.delete("F");
