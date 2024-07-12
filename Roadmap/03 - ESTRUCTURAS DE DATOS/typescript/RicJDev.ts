//EJERCICIO
//ARRAYS
const arr1: number[] = [23, 10, 20, 40, 12];

interface Car {
	model: string;
	year: number;
	price: number;
}

const someCarsModels: Car[] = [
	{
		model: 'Honda Civic',
		year: 2012,
		price: 10100,
	},
	{
		model: 'Toyota Corolla',
		year: 2010,
		price: 10200,
	},
	{
		model: 'Nissan Centra',
		year: 2012,
		price: 20300,
	},
];

//Inserción
someCarsModels.push({
	model: 'Chevrolet Aveo',
	year: 2010,
	price: 11300,
});

someCarsModels.unshift({
	model: 'Honda Fit',
	year: 2010,
	price: 14300,
});

let carToSplice: Car = {
	model: 'Peugeot 208',
	year: 2019,
	price: 19800,
};

someCarsModels.splice(2, 0, carToSplice);

//Búsqueda
let includesResult = someCarsModels.includes(carToSplice);
console.log('El elemento existe dentro del array?', includesResult);

let index = someCarsModels.indexOf(carToSplice);
console.log(someCarsModels[index]);

let findResult = someCarsModels.find((car) => {
	return car.model == 'Toyota Corolla';
});
console.log(findResult);

index = someCarsModels.findIndex((car) => {
	return car.model == 'Chevrolet Aveo';
});
console.log(someCarsModels[index]);

//Actualización
someCarsModels[index] = {
	model: 'Toyota Yaris',
	year: 2017,
	price: 18800,
};

console.log(someCarsModels[index]);

//Eliminación
someCarsModels.pop();
someCarsModels.shift();
someCarsModels.splice(2, 1);
someCarsModels.length = 0;

console.log(someCarsModels);

//Otros
arr1.sort((a, b) => {
	return b - a;
});
console.log(arr1);

//OBJETOS
const obj1 = {
	key: 'value',
};

//Inserción
type dinamicKeysValuesObj = { [key: string]: number | object };

const obj2: dinamicKeysValuesObj = {
	id: 102,
};

obj2.user = {
	name: 'Ric',
	age: 21,
};
console.log(obj2);

//Búsqueda
console.log(obj2.user);

//Actualización
obj2.user = {
	name: 'Joshua',
	age: 19,
};
console.log(obj2);

//Eliminación
delete obj2.user;

console.log(obj2);

//SETS
const mySet = new Set(arr1);
console.log(mySet);

//Inserción
mySet.add(22);
console.log(mySet);

//Búsqueda
let names: Set<string> = new Set(['Joe', 'Jill', 'Steve']);

let setHasResult = names.has('Jill');
console.log('El elemento existe dentro del set?', setHasResult);

//Actualización
const namesArr = Array.from(names);
namesArr[1] = 'Juan';

names = new Set(namesArr);

//Eliminación
names.delete('Juan');
mySet.clear();
console.log(mySet, names);

//MAPS
const myMap = new Map([
	['key1', 'value1'],
	['key2', 'value2'],
]);

console.log(myMap);

//Inserción
myMap.set('key3', 'value3');

console.log(myMap);

//Búsqueda
const mapValue = myMap.get('key1');

console.log(mapValue);

//Actualización
myMap.set('key3', 'value3');

//Eliminación
myMap.delete('key2');

console.log(myMap);

//EXTRA
import * as readline from 'readline';

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const contacts = new Map();
const phoneRegex = /(\d{4})\-(\d{7})/;

function addContact() {
	console.log('\nAGREGAR CONTACTO');

	rl.question('Nombre del contacto? ', (name) => {
		if (contacts.has(name)) {
			console.log('El contacto ya ha sido registrado');

			menu();
		} else {
			rl.question('Número de teléfono del contacto? ', (phone) => {
				if (phoneRegex.test(phone)) {
					contacts.set(name, phone);
					console.log('Contacto registrado exitosamente!');
				} else {
					console.log('Formato inválido. Por favor seguir el formato 0000-0000000');
				}

				menu();
			});
		}
	});
}

function updateContact() {
	console.log('\nACTUALIZAR CONTACTO');

	rl.question('Nombre del contacto? ', (name) => {
		if (contacts.has(name)) {
			rl.question('Nuevo número de teléfono del contacto? ', (phone) => {
				if (phoneRegex.test(phone)) {
					contacts.set(name, phone);
					console.log('Contacto actualizado exitosamente!');
				} else {
					console.log('Formato inválido. Por favor seguir el formato 0000-0000000');
				}

				menu();
			});
		} else {
			console.log('No existe ese contacto');

			menu();
		}
	});
}

function searchContact() {
	console.log('\nBUSCAR CONTACTO');

	rl.question('Nombre del contacto? ', (name) => {
		if (contacts.has(name)) {
			let phone = contacts.get(name);
			console.log(`findResultado: ${name}, ${phone}`);
		} else {
			console.log('Contacto no registrado');
		}

		menu();
	});
}

function deleteContact() {
	console.log('\nELIMINAR CONTACTO');

	rl.question('Nombre del contacto? ', (name) => {
		if (contacts.has(name)) {
			contacts.delete(name);
			console.log('Contacto eliminado exitosamente!');
		} else {
			console.log('Contacto no registrado');
		}

		menu();
	});
}

function getContactsList() {
	console.log('\nLISTA DE CONTACTOS:');

	if (contacts.size > 0) {
		contacts.forEach((phone, name) => {
			console.log(`- ${name}: ${phone}`);
		});
	} else {
		console.log('No hay registros');
	}

	menu();
}

function exit() {
	console.log('\nSaliendo de la app...');
	rl.close();
}

function menu() {
	console.log('\nAGENDA DE CONTACTOS');

	const optionMethods = new Map([
		['1', addContact],
		['2', updateContact],
		['3', searchContact],
		['4', deleteContact],
		['5', getContactsList],
		['6', exit],
	]);

	console.log(
		'1. Agregar contacto\n2. Actualizar contacto\n3. Buscar contacto\n4. Eliminar contacto\n5. Listar contactos\n6. Salir'
	);

	rl.question('Elija una opción (1 - 6) ', (option) => {
		const method = optionMethods.get(option) || menu;

		method();
	});
}

menu();
