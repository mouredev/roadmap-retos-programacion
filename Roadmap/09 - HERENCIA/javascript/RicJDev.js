console.log('\n---HERENCIA--');
class Animal {
	constructor(nombre, sonido) {
		this.nombre = nombre;
		this.sonido = sonido;
	}
	emiteSonido() {
		if (this.sonido != null) {
			console.log(this.sonido);
		}
	}
}

class Gato extends Animal {
	constructor(nombre, sonido) {
		super(nombre, sonido);
		this.sonido = 'Miau!';
	}
}

class Perro extends Animal {
	constructor(nombre, sonido) {
		super(nombre, sonido);
		this.sonido = 'Guau!';
	}
}

let = habla = (Animal) => {
	Animal.emiteSonido();
};

console.log('\nA partir de una clase creamos un animal');
let miAnimal = new Animal('Ter');
console.log(miAnimal);

miAnimal.emiteSonido();

console.log('\nHeredando sus propiedades creamos un perro');
let miPerro = new Perro('Ferr');
console.log(miPerro);

console.log('\nHeredando las propiedades de animal también creamos un gato');
let miGato = new Gato('Fran');
console.log(miGato);

console.log(
	'\nEn la clase animal almacenamos un método para que el animal emita sonido, el cual es heredado a perro y gato'
);
miPerro.emiteSonido();
miGato.emiteSonido();

console.log(
	'\nTambién creamos una función que le dice a los animales que "hablen", es decir, que emitan su sonido'
);
habla(miPerro);
habla(miGato);

console.log('\n---DIFICULTAD EXTRA---');
class Empleado {
	constructor(cargo, nombre, id, aSuCargo = []) {
		this.cargo = cargo;
		this.nombre = nombre;
		this.id = id;
		this.aSuCargo = aSuCargo;
	}

	trabaja() {
		console.log(`\n${this.nombre} está trabajando...`);
	}

	verCredencial() {
		console.log(
			`\n${this.nombre} posee la credencial: #${this.id}\nCargo: ${this.cargo}`
		);
	}

	verCargaDeEmpleados() {
		if (this.aSuCargo.length > 0) {
			console.log(
				`\n${this.nombre} tiene ${this.aSuCargo.length} empleado(s) a su cargo:`
			);
			for (let i = 0; i < this.aSuCargo.length; i++) {
				console.log(`-${this.aSuCargo[i]}`);
			}
		} else {
			console.log(`\n${this.nombre} no tiene empleados a su cargo`);
		}
	}
}

class Gerente extends Empleado {
	constructor(nombre, id, aSuCargo, cargo) {
		super(cargo, nombre, id, aSuCargo);
		this.cargo = 'Gerente';
	}

	asignarProyecto(Empleado, proyecto) {
		console.log(
			`\n${this.nombre} le asignó el proyecto \"${proyecto}\" a ${Empleado.nombre}`
		);
		Empleado.proyectoActual = proyecto;
		this.aSuCargo.push(Empleado.nombre);
		this.aSuCargo = new Set(this.aSuCargo);
		this.aSuCargo = Array.from(this.aSuCargo);
	}

	cancelarProyecto(Empleado) {
		if (Empleado.proyectoActual != null) {
			console.log(
				`\n${this.nombre} ha cancelado el proyecto \"${Empleado.proyectoActual}\" asignado a ${Empleado.nombre}`
			);
			Empleado.proyectoActual = null;
			this.aSuCargo.splice(this.aSuCargo.indexOf(Empleado.nombre), 1);
		} else {
			console.log(`\n${Empleado.nombre} no tiene ningún proyecto asignado`);
		}
	}
}

class GerenteDeProyecto extends Empleado {
	constructor(nombre, id, proyectoActual, aSuCargo, cargo) {
		super(cargo, nombre, id, aSuCargo);
		this.cargo = 'Gerente de proyecto';
		this.proyectoActual = proyectoActual;
	}

	sumarAlEquipo(Empleado) {
		console.log(
			`\n${this.nombre} ha pedido a ${Empleado.nombre} que se una a su equipo de desarrollo`
		);
		this.aSuCargo.push(Empleado.nombre);
		this.aSuCargo = new Set(this.aSuCargo);
		this.aSuCargo = Array.from(this.aSuCargo);
	}

	retirarDelEquipo(Empleado) {
		if (this.aSuCargo.includes(Empleado.nombre)) {
			console.log(
				`\n${this.nombre} ha pedido a ${Empleado.nombre} que se retire de su equipo de desarrollo`
			);
			this.aSuCargo.splice(this.aSuCargo.indexOf(Empleado.nombre), 1);
		} else {
			console.log(
				`\n${Empleado.nombre} no está en la carga de epleados de ${this.nombre}`
			);
		}
	}

	asignarTareas(Empleado, tarea) {
		if (this.aSuCargo.includes(Empleado.nombre)) {
			if (this.proyectoActual != null) {
				console.log(
					`\n${this.nombre} le encomendó ${tarea} a ${Empleado.nombre} para su proyecto \"${this.proyectoActual}\"`
				);
				Empleado.tareaActual = tarea;
			} else {
				console.log(
					`\n${this.nombre} no puede asignar tareas si no está trabajando en ningún proyecto`
				);
			}
		} else {
			console.log(
				`\n${this.nombre} debe incuir a ${Empleado.nombre} en el equipo para enomendarle tareas`
			);
		}
	}

	quitarTareas(Empleado) {
		if (this.aSuCargo.includes(Empleado.nombre)) {
			if (Empleado.tareaActual != null) {
				console.log(
					`\n${this.nombre} le ha quitado a ${Empleado.nombre} la tarea ${Empleado.tareaActual}`
				);
				Empleado.tareaActual = null;
			} else {
				console.log(`\n${Empleado.nombre} no tiene tareas pendientes`);
			}
		} else {
			console.log(
				`\nEste empleado no pertenece a la carga de empleados de ${this.nombre}. No se cambiarán sus tareas pendientes`
			);
		}
	}
}

class Programador extends Empleado {
	constructor(nombre, id, lenguajes, tareaActual, cargo) {
		super(cargo, nombre, id);
		this.lenguajes = lenguajes;
		this.tareaActual = tareaActual;
		this.cargo = 'Programador';
	}

	concluirTarea() {
		if (this.tareaActual != null) {
			console.log(
				`\n${this.nombre} ha terminado su tarea actual: ${this.tareaActual}`
			);
			this.tareaActual = null;
		} else {
			console.log(`\n${this.nombre} no tiene tareas asignadas`);
		}
	}

	programar() {
		console.log(`\n${this.nombre} está programando...`);
	}

	verCargaDeEmpleados() {
		console.log(`\n${this.nombre} no puede tener empleados a su cargo`);
	}
}

console.log(
	'\nHemos simulado la jerarquía de una empresa de desarrollo. Para ello creamos una súper clase "Empleados", de la cual heredan sus propiedades las clases "Gerente", "GerenteDeProyecto" y "Programador", cada una con métodos específicos según su cargo'
);

//Gerente del área de desarrollo web

let manager = new Gerente('Peter', 1632);

//Gerentes de proyecto

let projectManager1 = new GerenteDeProyecto('Alicia', 1390);
let projectManager2 = new GerenteDeProyecto('Jaime', 1001);

//Equipo de programadores

let progamer1 = new Programador('Alex', 1200, ['Python', 'Java', 'Php']);
let progamer2 = new Programador('Erika', 1435, ['Kotlin', 'Swift']);
let progamer3 = new Programador('Fabian', 2345, ['Python', 'TypeScript']);
let progamer4 = new Programador('Ric', 1437, ['JavaScript', 'Html/Css', 'C++']);

//Aquí me divertí un rato creando y probando métodos
console.log(
	'\nHe creado unos cuantos objetos derivados de estas clases para probar y añadir métodos'
);

manager.verCredencial();

projectManager1.verCredencial();

progamer4.verCredencial();

manager.asignarProyecto(projectManager1, 'Calculadora Web personalizable');

projectManager1.sumarAlEquipo(progamer4);
projectManager1.sumarAlEquipo(progamer1);
projectManager1.asignarTareas(progamer4, 'elaborar los ficheros de Html y Css');
projectManager1.asignarTareas(progamer1, 'programar la interactividad');
projectManager1.verCargaDeEmpleados();

manager.cancelarProyecto(projectManager1);

projectManager1.asignarTareas(progamer4, 'elaborar los ficheros de Html y Css');

progamer4.concluirTarea();

manager.asignarProyecto(projectManager2, 'Tienda online');

projectManager2.sumarAlEquipo(progamer1);
projectManager2.sumarAlEquipo(progamer2);
projectManager2.sumarAlEquipo(progamer3);
projectManager2.asignarTareas(progamer3, 'organizar el menú de interacción');
projectManager2.sumarAlEquipo(progamer4);
projectManager2.verCargaDeEmpleados();

let todosLosEmpleados = [
	projectManager2,
	progamer1,
	progamer2,
	progamer3,
	progamer4,
];
for (let i = 0; i < todosLosEmpleados.length; i++) {
	todosLosEmpleados[i].trabaja();
}

progamer3.concluirTarea();

manager.cancelarProyecto(projectManager2);

projectManager2.retirarDelEquipo(progamer1);
projectManager2.retirarDelEquipo(progamer2);
projectManager2.retirarDelEquipo(progamer3);
projectManager2.retirarDelEquipo(progamer4);
