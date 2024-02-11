// #03 ESTRUCTURAS DE DATOS

/**
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */

// 1. Arrays (Coleccion de datos)
const pLanguages = ['javascript', 'python', 'c#'];
// inserción
pLanguages.unshift('java'); // insercion al principio del array
pLanguages.push('kotlin'); // insercion al final del array
pLanguages[5] = 'php'; // insercion en una posicion especificada del array
pLanguages.length; // -> 6
console.log(pLanguages); // -> ['java', 'javascript', 'python', 'c#', 'kotlin', 'php']
// borrado
pLanguages.shift(); // borra el primer elemento del array
pLanguages.pop(); // borra el ultimo elemento del array
pLanguages.length; // -> 4
delete pLanguages[2]; // borra el elemento en una posicion especificada pero mantiene el espacio vacío
pLanguages.length; // -> 4
console.log(pLanguages); // -> ['javascript', 'python', 'empty', 'kotlin']
// actualización
pLanguages[2] = 'c++'; // actualiza el elemento en una posicion especificada
console.log(pLanguages); // -> ['javascript', 'python', 'c++', 'kotlin']
// ordenación
pLanguages.sort(); // ordena el array de menor a mayor por defecto (alfabeticamente)
console.log(pLanguages); // -> ['c++', 'javascript', 'kotlin', 'python']
pLanguages.reverse(); // invierte el orden del array
console.log(pLanguages); // -> ['python', 'kotlin', 'javascript', 'c++']

// 2. Objects (Colecciones de pares clave-valor)
const languages = {
	javascript: '1995',
	python: '1991',
	c: '1972',
};
// inserción y actualización
languages.java = '995';
languages['kotlin'] = '2011';
Object.defineProperty(languages, 'php', {
	value: '1995',
	writable: true,
	enumerable: true,
	configurable: true,
});
console.log(languages); // -> {javascript: '995', python: '1991', c: '1972', java: '1995', kotlin: '2011', php: '1995'}
languages.java = '1995'; // actualiza la propiedad java
console.log(languages); // -> {javascript: '1995', python: '1991', c: '1972', java: '1995', kotlin: '2011', php: '1995'}
// borrado
delete languages.c; // borra la propiedad c y su valor del objeto languages

// 3. Set (Colecciones de valores unicos (no duplicados))
const numbers = new Set([0]);
// inserción
numbers.add(1);
numbers.add(2);
numbers.add(3);
numbers.add(1); // este no ingresa al array por ser duplicado
numbers.size; // -> 4
numbers.has(0); // -> true
numbers.has(5); // -> false
console.log(numbers); // -> {0, 1, 2, 3}
// borrado
numbers.delete(0);
numbers.size; // -> 3
console.log(numbers); // -> {1, 2, 3}

// 4. Map (Coleccion asociativa de datos)
const numbersMap = new Map([['zero', 0]]);
// inserción
numbersMap.set('one', 1);
numbersMap.set('two', 2);
numbersMap.set('three', 3);
numbersMap.size; // -> 4
console.log(numbersMap); // -> {zero: 0, one: 1, two: 2, three: 3}
// actualización
numbersMap.set('zero', 'cero');
numbersMap.set('one', 'uno');
numbersMap.set('two', 'dos');
numbersMap.set('three', 'tres');
console.log(numbersMap); // -> {zero: 'cero', one: 'uno', two: 'dos', three: 'tres'}
// borrado
numbersMap.delete('zero');
numbersMap.size; // -> 3
console.log(numbersMap); // -> {one: 'uno', two: 'dos', three: 'tres'}

/** DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

/**
 * Use el entorno nodejs para poder programar la agenda del
 * ejercicio extra.
 * */
import { createInterface } from 'readline';

const rl = createInterface({
	input: process.stdin,
	output: process.stdout,
});

const contacts = {
	Test: {
		name: 'Test Name',
		phone: '3012456789',
	},
};

const regex = /^[0-9]{10}$/; // 10 digitos - solo numeros

main();

function main() {
	console.log('\nWelcome to Contacts.\n');

	console.log('  0. All Contacts');
	console.log('  1. Search');
	console.log('  2. Add');
	console.log('  3. Update');
	console.log('  4. Delete');
	console.log('  5. Exit');

	rl.question('\nChoose an option: ', (action) => {
		functionSet(action);
	});
}

function backToMain() {
	rl.question('\nPress enter to back to menu', () => {
		console.clear();
		main();
	});
}

function validatePhone(phone) {
	return regex.test(phone);
}

function functionSet(action) {
	if (action === '0') {
		showContacts(contacts);
	} else if (action === '1') {
		console.log('\n==Search Contact==\n');
		rl.question('Enter the contact nick: ', (nick) => {
			searchContact(contacts, nick);
		});
	} else if (action === '2') {
		console.log('\n==Add a Contact==\n');
		rl.question('Enter the contact nick: ', (nick) => {
			rl.question('Enter the contact name: ', (name) => {
				rl.question('Enter the contact phone: ', (phone) => {
					addContact(contacts, nick, name, phone);
				});
			});
		});
	} else if (action === '3') {
		console.log('\n==Update Contact==\n');
		rl.question('Enter the contact nick: ', (nick) => {
			rl.question('Enter the contact name: ', (name) => {
				rl.question('Enter the contact phone: ', (phone) => {
					updateContact(contacts, nick, name, phone);
				});
			});
		});
	} else if (action === '4') {
		console.log('\n==Delete Contact==\n');
		rl.question('Enter the contact nick: ', (nick) => {
			deleteContact(contacts, nick);
		});
	} else if (action === '5') {
		exitContacts();
	} else {
		console.log('Invalid option. Select an option from 0 to 5');
		setTimeout(() => {
			console.clear();
			main();
		}, 2000);
	}
}

function showContacts(obj) {
	console.log('\nHere are your contacts:\n');
	if (Object.keys(obj).length === 0) {
		console.log('No contacts... list is empty.');
	} else {
		for (const contact in obj) {
			console.log(`${contact}: ${obj[contact].name} - ${obj[contact].phone}`);
		}
	}
	backToMain();
}

function searchContact(obj, nick) {
	const search = obj.hasOwnProperty(nick);
	if (search) {
		console.log(`${obj[nick].name} - ${obj[nick].phone}`);
	} else {
		console.log(`Contact ${nick} does not exist`);
	}
	backToMain();
}

function addContact(obj, nick, name, phone) {
	if (obj.hasOwnProperty(nick)) {
		console.log(`Contact ${nick} already exist`);
		backToMain();
	} else if (validatePhone(phone)) {
		obj[nick] = { name, phone };
		console.log(`Contact ${nick} successfully added`);
	} else {
		console.log('Invalid phone number. Phone must have 10 digits');
	}
	backToMain();
}

function updateContact(obj, nick, name, phone) {
	if (obj.hasOwnProperty(nick) && validatePhone(phone)) {
		obj[nick].name = name;
		obj[nick].phone = phone;
		console.log(`Contact ${nick} successfully updated`);
	} else {
		console.log(
			`Contact ${nick} does not exist or you input an invalid phone number. Phone must have 10 digits`
		);
	}
	backToMain();
}

function deleteContact(obj, nick) {
	if (obj.hasOwnProperty(nick)) {
		delete obj[nick];
		console.log(`Contact ${nick} successfully deleted`);
	} else {
		console.log(`Contact ${nick} does not exist`);
	}
	backToMain();
}

function exitContacts() {
	console.log('Exiting Contacts!');
	setTimeout(() => {
		console.clear();
		process.exit();
	}, 1000);
}
