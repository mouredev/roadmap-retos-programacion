//EJERCICIO
//ARRAYS
let frutasQueMeGustan = ['mango', 'fresa', 'pera', 'manzana', 'uva', 'durazno'];

//-Iteración de elementos-
for (let i = 0; i < frutasQueMeGustan.length; i++) {
	console.log(frutasQueMeGustan[i]);
}

frutasQueMeGustan.forEach((elemento) => {
	console.log(elemento);
});

frutasQueMeGustan.map((elemento) => {
	console.log(elemento);
});

//-Insercion-
frutasQueMeGustan.push('guanabana');

frutasQueMeGustan.unshift('aguacate');

frutasQueMeGustan.splice(2, 1, 'papaya');

//-Borrado-
frutasQueMeGustan.pop();

frutasQueMeGustan.shift();

frutasQueMeGustan.splice(1, 1);

//-Actualizacion-
frutasQueMeGustan[2] = 'piña';

frutasQueMeGustan.splice(1, 1, 'parchita');

frutasQueMeGustan.fill('tamarindo', 2, 3);

//-Búsqueda-
console.log(frutasQueMeGustan.indexOf('parchita'));

frutasQueMeGustan.push('parchita');
console.log(frutasQueMeGustan.lastIndexOf('parchita'));

console.log(frutasQueMeGustan.includes('parchita'));
console.log(frutasQueMeGustan.includes('naranja'));

console.log(
	frutasQueMeGustan.find((valor) => {
		return valor === 'tamarindo';
	})
);

console.log(
	frutasQueMeGustan.findIndex((valor) => {
		return valor === 'parchita';
	})
);

console.log(
	frutasQueMeGustan.findLast((valor) => {
		return valor === 'parchita';
	})
);

console.log(
	frutasQueMeGustan.findLastIndex((valor) => {
		return valor === 'parchita';
	})
);

//-Ordenado-
let nuevoArray = [12, 10, 34, 25, 82];
console.log(nuevoArray);
nuevoArray.sort((a, b) => a - b);
console.log(nuevoArray);

let nuevoArray2 = [12, 10, 34, 25, 82];
console.log(nuevoArray2);
nuevoArray2.sort((a, b) => b - a);
console.log(nuevoArray2);

//-Concatenación-
console.log(nuevoArray.concat(nuevoArray2));

//-Otros-
console.log(frutasQueMeGustan.join(' '));

let nuevoArray3 = [
	[1, 3],
	[23, 43],
	[21, 67],
	[12, 23],
];

console.log(nuevoArray3.flat());

//SETS
const animales = new Set(['gallina', 'foca', 'lagarto']);
console.log(animales);

//-Insercion-
animales.add('gato');
animales.add('perro');
animales.add('araña');
animales.add('gato'); //no se ejecuta debido a que los sets no admiten duplicados
console.log(animales);

//-Borrado-
animales.delete('lagarto');
animales.delete('perro');
console.log(animales);

//-Ordenado-
// los sets no tienen indice, por lo que no es posible ordenarlos sin antes convertirlos en un array
const miNuevoSet = new Set([12, 23, 45, 87, 43, 67, 12, 87]);
console.log(miNuevoSet);

let arrayDelSet = Array.from(miNuevoSet).sort((a, b) => a - b);
console.log(arrayDelSet);

//-Otros-
console.log(animales.has('foca'));

animales.clear();
console.log(animales);

//MAPS
const miMap = new Map([
	['clave1', 'valor1'],
	['uno', 1],
	['dos', 2],
]);
console.log(miMap);

//-Iteración de elementos-
miMap.forEach((element) => {
	console.log(element);
});

//-Insercion-
miMap.set('nombre', 'Ric');
console.log(miMap);

//-Actualizacion-
miMap.set('nombre', 'Josue'); //se utiliza el mismo metodo
console.log(miMap);

//-Borrado-
miMap.delete('dos'); //elimina una clave-valor existente
console.log(miMap);

//-Otras operaciones-
console.log(miMap.get('nombre')); //obtiene el valor de una clave
console.log(miMap.get('uno'));

console.log(`Mi map contiene la clave 'dos': ${miMap.has('dos')}`); //verfica si el map contiene una clave

console.log(miMap.size); //nos indica la cantidad de claves-valor

//OBJETOS
const persona = {
	nombre: 'Ricardo',
	edad: 21,
	sexo: 'masculino',
	casado: false,
	estatura: 159,
};
console.log(persona);

//-Insercion-
persona.pasatiempos = ['escribir', 'dibujar', 'leer'];
console.log(persona);

//-Borrado-
delete persona.estatura;

//-Actualizacion-
persona.pasatiempos[1] = 'escuchar musica';

persona.edad = 22;

console.log(persona);

console.log(Object.keys(persona)); //devuelve un array con las claves del objeto

console.log(Object.values(persona)); //devuelve un array con los valores del objeto

const copiaDePersona = Object.assign({}, persona);
copiaDePersona.nombre = 'Luis';

console.log(copiaDePersona);

//EXTRA
//Se ejecuta en Node js
console.log('\nAGENDA DE CONTACTOS');

const { resolve } = require('path');
const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const contactos = [
	/*
	{
		nombre: 'Pedro',
		telefono: '0412-5248215',
	},
	{
		nombre: 'Julia',
		telefono: '0424-3333333',
	},
	{
		nombre: 'Juan',
		telefono: '0212-3434345',
	},
	*/
];

function funcionDeBusqueda(nombre) {
	let result = undefined;

	contactos.find((contacto) => {
		if (contacto.nombre === nombre) {
			result = contacto;
		}
	});

	return result;
}

let telefonoRegEx = /(\d{4})\-(\d{7})/;

function insertaContacto() {
	let nuevoContacto = {
		nombre: '',
		telefono: '',
	};

	rl.question('\nIngrese el nombre del contacto: ', (nombre) => {
		nuevoContacto.nombre = nombre;

		rl.question('\nIngrese el número de telefono del contacto: ', (telefono) => {
			if (telefonoRegEx.test(telefono)) {
				nuevoContacto.telefono = telefono;
				contactos.push(nuevoContacto);

				console.log('\nContacto agregado con exito!');
			} else {
				console.log('\nFormato inválido. Por favor seguir el formato 0000-0000000');
			}

			agendaDeContactos();
		});
	});
}

function buscaContacto() {
	if (contactos.length > 0) {
		rl.question('\nIngrese el nombre del contacto: ', (nombre) => {
			let contacto = funcionDeBusqueda(nombre);

			if (contacto === undefined) {
				console.log('\nNo existe');
			} else {
				console.log(`\n${contacto.nombre}: ${contacto.telefono}`);
			}

			agendaDeContactos();
		});
	} else {
		console.log('\nNo hay registros');
		agendaDeContactos();
	}
}

function actualizaContacto() {
	if (contactos.length > 0) {
		rl.question('\nIngrese el nombre del contacto: ', (nombre) => {
			let contacto = funcionDeBusqueda(nombre);

			if (contacto === undefined) {
				console.log('\nNo existe');

				agendaDeContactos();
			}

			rl.question('\nIngrese el nuevo número de teléfono del contacto: ', (nuevoTelefono) => {
				if (telefonoRegEx.test(nuevoTelefono)) {
					contacto.telefono = nuevoTelefono;

					console.log('\nEl contacto ha sido actualizado!');
				} else {
					console.log('\nFormato inválido. Por favor seguir el formato 0000-0000000');
				}

				agendaDeContactos();
			});
		});
	} else {
		console.log('\nNo hay registros');
		agendaDeContactos();
	}
}

function eliminaContacto() {
	if (contactos.length > 0) {
		rl.question('\nIngrese el nombre del contacto: ', (nombre) => {
			let contacto = funcionDeBusqueda(nombre);

			if (contacto === undefined) {
				console.log('\nNo existe');
			} else {
				contactos.splice(contactos.indexOf(contacto), 1);

				console.log('\nContacto eliminado exitosamente!');
			}

			agendaDeContactos();
		});
	} else {
		console.log('\nNo hay registros');
		agendaDeContactos();
	}
}

function mostrarLista() {
	if (contactos.length > 0) {
		console.log('\nLISTA DE CONTACTOS\n');

		contactos.forEach((elemento) => {
			console.log(`- ${elemento.nombre}: ${elemento.telefono}`);
		});
	} else {
		console.log('\nNo hay registros');
	}

	agendaDeContactos();
}

function agendaDeContactos() {
	console.log(
		'\n1. Insertar contacto\n2. Buscar contacto\n3. Actualizar contacto\n4. Eliminar contacto\n5. Mostrar lista de contactos\n6. Salir'
	);

	rl.question('\nSeleccione una opción: ', (opcion) => {
		if (opcion === '1') {
			insertaContacto();
		} else if (opcion === '2') {
			buscaContacto();
		} else if (opcion === '3') {
			actualizaContacto();
		} else if (opcion === '4') {
			eliminaContacto();
		} else if (opcion === '5') {
			mostrarLista();
		} else if (opcion === '6') {
			console.log('\nSaliendo de la aplicación...');
			rl.close();
		} else {
			console.log('\nOpción inválida. Introduzca un número del 1 al 6 para ejecutar una acción');
			agendaDeContactos();
		}
	});
}

agendaDeContactos();
