// #03 ESTRUCTURAS DE DATOS
// Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */

console.log('=== ESTRUCTURAS DE DATOS EN JAVASCRIPT ===');

// 1. ARRAY (Arreglo)
console.log('\n1. ARRAY:');

// Creación
let frutas = ['manzana', 'banana', 'naranja'];
console.log('Array creado:', frutas);

// Inserción
frutas.push('uva'); // Al final
frutas.unshift('pera'); // Al inicio
frutas.splice(2, 0, 'mango'); // En posición específica
console.log('Después de inserciones:', frutas);

// Actualización
frutas[1] = 'kiwi';
console.log('Después de actualizar:', frutas);

// Borrado
frutas.pop(); // Elimina el último
frutas.shift(); // Elimina el primero
frutas.splice(1, 1); // Elimina en posición específica
console.log('Después de borrados:', frutas);

// Ordenación
frutas.sort();
console.log('Ordenado alfabéticamente:', frutas);
frutas.reverse();
console.log('Ordenado inverso:', frutas);

// 2. OBJECT (Objeto)
console.log('\n2. OBJECT:');

// Creación
let persona = {
	nombre: 'Juan',
	edad: 30,
	ciudad: 'Madrid',
};
console.log('Objeto creado:', persona);

// Inserción
persona.profesion = 'Desarrollador';
persona['email'] = 'juan@email.com';
console.log('Después de inserciones:', persona);

// Actualización
persona.edad = 31;
persona['ciudad'] = 'Barcelona';
console.log('Después de actualizaciones:', persona);

// Borrado
delete persona.email;
console.log('Después de borrados:', persona);

// 3. SET (Conjunto)
console.log('\n3. SET:');

// Creación
let numeros = new Set([1, 2, 3, 3, 4]); // Los duplicados se eliminan
console.log('Set creado:', numeros);

// Inserción
numeros.add(5);
numeros.add(6);
console.log('Después de inserciones:', numeros);

// Borrado
numeros.delete(3);
console.log('Después de borrados:', numeros);

// Verificación
console.log('¿Contiene el 4?', numeros.has(4));

// 4. MAP (Mapa)
console.log('\n4. MAP:');

// Creación
let usuarios = new Map();
usuarios.set('user1', { nombre: 'Ana', edad: 25 });
usuarios.set('user2', { nombre: 'Carlos', edad: 30 });
console.log('Map creado:', Array.from(usuarios));

// Inserción
usuarios.set('user3', { nombre: 'Maria', edad: 28 });
console.log('Después de inserciones:', Array.from(usuarios));

// Actualización
usuarios.set('user2', { nombre: 'Carlos', edad: 31 });
console.log('Después de actualizaciones:', Array.from(usuarios));

// Borrado
usuarios.delete('user1');
console.log('Después de borrados:', Array.from(usuarios));

// 5. WEAKMAP y WEAKSET
console.log('\n5. WEAKMAP y WEAKSET:');

// WeakMap (solo acepta objetos como keys)
let weakMap = new WeakMap();
let obj1 = {};
weakMap.set(obj1, 'valor1');
console.log('WeakMap:', weakMap.get(obj1));

// WeakSet (solo almacena objetos)
let weakSet = new WeakSet();
weakSet.add(obj1);
console.log('WeakSet contiene obj1:', weakSet.has(obj1));

// 6. TYPED ARRAYS
console.log('\n6. TYPED ARRAYS:');

// Int32Array
let intArray = new Int32Array([10, 20, 30, 40]);
console.log('Int32Array:', intArray);

// Float64Array
let floatArray = new Float64Array([1.1, 2.2, 3.3]);
console.log('Float64Array:', floatArray);

// 7. ARRAYBUFFER
console.log('\n7. ARRAYBUFFER:');
let buffer = new ArrayBuffer(16);
let view = new Int32Array(buffer);
view[0] = 42;
console.log('ArrayBuffer:', view[0]);

/*
 * DIFICULTAD EXTRA (opcional):
 * Agenda de contactos por terminal
 */

console.log('\n=== AGENDA DE CONTACTOS ===');

// Simulamos entrada de terminal con prompts (en navegador)
// Para Node.js necesitaríamos el módulo 'readline'

class AgendaContactos {
	constructor() {
		this.contactos = new Map();
	}

	validarTelefono(telefono) {
		const regex = /^\d{1,11}$/; // Máximo 11 dígitos numéricos
		return regex.test(telefono);
	}

	agregarContacto(nombre, telefono) {
		if (!this.validarTelefono(telefono)) {
			return '❌ Teléfono inválido. Debe contener solo números y máximo 11 dígitos.';
		}

		if (this.contactos.has(nombre)) {
			return '❌ El contacto ya existe.';
		}

		this.contactos.set(nombre, telefono);
		return '✅ Contacto agregado correctamente.';
	}

	buscarContacto(nombre) {
		if (this.contactos.has(nombre)) {
			return `📞 ${nombre}: ${this.contactos.get(nombre)}`;
		}
		return '❌ Contacto no encontrado.';
	}

	actualizarContacto(nombre, nuevoTelefono) {
		if (!this.validarTelefono(nuevoTelefono)) {
			return '❌ Teléfono inválido.';
		}

		if (this.contactos.has(nombre)) {
			this.contactos.set(nombre, nuevoTelefono);
			return '✅ Contacto actualizado correctamente.';
		}
		return '❌ Contacto no encontrado.';
	}

	eliminarContacto(nombre) {
		if (this.contactos.has(nombre)) {
			this.contactos.delete(nombre);
			return '✅ Contacto eliminado correctamente.';
		}
		return '❌ Contacto no encontrado.';
	}

	listarContactos() {
		if (this.contactos.size === 0) {
			return '📋 La agenda está vacía.';
		}

		let lista = '📋 Lista de contactos:\n';
		for (let [nombre, telefono] of this.contactos) {
			lista += `  ${nombre}: ${telefono}\n`;
		}
		return lista;
	}
}

// Simulación de la interfaz de terminal
function simularAgenda() {
	const agenda = new AgendaContactos();

	console.log('\n--- SIMULACIÓN DE AGENDA ---');

	// Operaciones de ejemplo
	console.log(agenda.agregarContacto('Ana', '1234567890'));
	console.log(agenda.agregarContacto('Carlos', '0987654321'));
	console.log(agenda.agregarContacto('Maria', '5551234567'));

	console.log(agenda.buscarContacto('Ana'));
	console.log(agenda.buscarContacto('Pedro')); // No existe

	console.log(agenda.actualizarContacto('Carlos', '999888777'));
	console.log(agenda.actualizarContacto('Pedro', '111222333')); // No existe

	console.log(agenda.eliminarContacto('Maria'));
	console.log(agenda.eliminarContacto('Luis')); // No existe

	console.log(agenda.listarContactos());

	// Prueba de validación
	console.log(agenda.agregarContacto('Test', 'abc123')); // Inválido
	console.log(agenda.agregarContacto('Test', '123456789012')); // Demasiados dígitos
}

// Ejecutar la simulación
simularAgenda();

// Fin de la simulación
