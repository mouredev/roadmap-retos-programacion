//EJERCICIO
//ARRAYS
let frutasQueMeGustan = ['mango', 'fresa', 'pera', 'manzana', 'uva', 'durazno'];
console.log(frutasQueMeGustan);

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
frutasQueMeGustan.push('guanabana'); //inserta un elemento al final
console.log(frutasQueMeGustan);

frutasQueMeGustan.unshift('aguacate'); //inserta un elemento al incio
console.log(frutasQueMeGustan);

frutasQueMeGustan.splice(2, 1, 'papaya'); //inserta un elemento en una ubicación específica
console.log(frutasQueMeGustan);

//-Borrado-
frutasQueMeGustan.pop(); //borra un elemento al final
console.log(frutasQueMeGustan);

frutasQueMeGustan.shift(); //borra un elemento al incio
console.log(frutasQueMeGustan);

frutasQueMeGustan.splice(1, 1); //borra un elemento en una ubicación específica
console.log(frutasQueMeGustan);

//-Actualizacion-
frutasQueMeGustan[2] = 'piña'; //reasigna el valor del elemento array[índice]
console.log(frutasQueMeGustan);

frutasQueMeGustan.splice(1, 1, 'parchita'); //reasigna el valor en una ubicación específica
console.log(frutasQueMeGustan);

frutasQueMeGustan.fill('tamarindo', 2, 3); //reasigna el valor en una ubicación específica
console.log(frutasQueMeGustan);

//-Ordenado-
let nuevoArray = [12, 10, 34, 25, 82];
console.log(nuevoArray);
nuevoArray.sort((a, b) => a - b); //ordena los numeros de menor a mayor
console.log(nuevoArray);

let nuevoArray2 = [12, 10, 34, 25, 82];
console.log(nuevoArray2);
nuevoArray2.sort((a, b) => b - a); //ordena los numeros de mayor a menor
console.log(nuevoArray2);

console.log(frutasQueMeGustan.indexOf('parchita'));

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

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
console.clear();

const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const contactos = [];

function insertaContacto() {
	/**
	 * La funcion debe agregar el contaco al array y luego crear un map a partir de él para asegurar que no se repitan los contactos
	 * Cada contacto será un objeto con las claves nombre y número
	 * Se debe comprobar el formato del numero ingresado. Usar RegEx
	 */

	rl.question('\nIngrese el nombre del contacto\n', (answer) => {
		contactos.push({ nombre: answer });
		rl.question('\nIngrese el número del contacto\n', (answer) => {
			contactos[contactos.length - 1].numeroTelefonico = answer;
			muestraOpciones();
		});
	});
}

function buscaContacto() {
	console.log('\nFuncion para buscar contacto');
	muestraOpciones();
}

function actualizaContacto() {
	/**
	 * Debe haber una manera e reutilizar la función de búsqueda para actualizar un contacto
	 */
	console.log('\nFuncion para actualizar contacto');
	muestraOpciones();
}

function mostrarLista() {
	console.log('\nLISTA DE CONTACTOS');

	contactos.sort((a, b) => {
		a.nombre - b.nombre;
	});

	contactos.forEach((element) => {
		console.log(`- ${element.nombre}: ${element.numeroTelefonico}`);
	});
	muestraOpciones();
}

function eliminaContato() {
	/**
	 * Lo mismo para esta función
	 */
	console.log('\nFuncion para eliminar contacto');
	muestraOpciones();
}

function muestraOpciones() {
	rl.question(
		'\nElige una opcion:\n1.Insertar contacto (i)\n2.Buscar contacto (b)\n3.Actualiar contacto (a)\n4.Eliminar contacto (e)\n5.Mostrar lista de contactos (m)\n6.Salir (s)\n',
		(answer) => {
			answer = answer.toLowerCase();

			if (answer === '1' || answer === 'i' || answer === 'insertar') {
				insertaContacto();
			} else if (answer === '2' || answer === 'b' || answer === 'buscar') {
				buscaContacto();
			} else if (answer === '3' || answer === 'a' || answer === 'actualizar') {
				actualizaContacto();
			} else if (answer === '4' || answer === 'e' || answer === 'eliminar') {
				eliminaContato();
			} else if (answer === '5' || answer === 'm' || answer === 'mostrar') {
				mostrarLista();
			} else if (answer === '6' || answer === 's' || answer === 'salir') {
				console.log('\nSaliendo de la aplicación');
				rl.close();
			} else {
				console.log('\nIngrese un valor válido');
				muestraOpciones();
			}
		}
	);
}

muestraOpciones();
