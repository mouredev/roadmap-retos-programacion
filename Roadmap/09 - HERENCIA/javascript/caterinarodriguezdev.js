/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Animal {
    
    constructor(nombre){
        this.nombre = nombre;
    }

    print() {
        console.log('Soy un animal.');
    }
}

class Perro extends Animal {

    constructor(nombre, raza) {
        super(nombre);
        this.raza = raza;
    }

    sonido() {
       return 'Guau!'
    }

    print() {
        console.log(`Este perro se llama ${this.nombre}, es de raza ${this.raza} y hace: ${this.sonido()}`);
    }
}

class Gato extends Animal {
    
    constructor(nombre, raza) {
        super(nombre);
        this.raza = raza;
    }

    sonido() {
        return 'Miaaaau';
    }

    print() {
        console.log(`Este gato se llama ${this.nombre}, es de raza ${this.raza} y hace: ${this.sonido()}`);
    }
}

const loki = new Perro('Loki', 'border collie');
const gatoConBotas = new Gato('El gato con botas','siames');

loki.print();
gatoConBotas.print();

// * DIFICULTAD EXTRA (opcional):
// * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
// * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
// * Cada empleado tiene un identificador y un nombre.
// * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
// * actividad, y almacenan los empleados a su cargo.
// */

class Empleado {

    constructor(id, nombre) {
        this.id = id;
        this.nombre = nombre;
    }
}

class Gerente extends Empleado {

    constructor(id, nombre, departamentosSupervisados, empleadosGestionados) {
        super(id, nombre);
        this.departamentosSupervisados = departamentosSupervisados;
        this.empleadosGestionados = empleadosGestionados;
    }

    listDepartamentos() {
        return this.departamentosSupervisados;
    }

    listEmpleadosGestionados() {
        return this.empleadosGestionados;
    }

    print() {
        console.log(`El gerente ${this.nombre} con id ${this.id} supervisa los departamentos: ${this.departamentosSupervisados} y tiene a cargos los siguientes empleados: ${this.empleadosGestionados}.`);
    }
}

class GerenteProyecto extends Empleado {

    constructor(id, nombre, proyectosActivos, metasProyectos) {
        super(id, nombre);
        this.proyectosActivos = proyectosActivos;
        this.metasProyectos = metasProyectos;
    }

    listProyectosActivos() {
        return this.proyectosActivos;
    }

    listMetasProyectos() {
        return this.metasProyectos;
    }

    print() {
        console.log(`El gerente de proyecto ${this.nombre} con id ${this.id} tiene los siguientes proyectos activos: ${this.proyectosActivos} y las siguientes metas: ${this.metasProyectos}.`);
    }
}

class Programadora extends Empleado {

    constructor(id, nombre, tickets, rol) {
        super(id, nombre);
        this.tickets = tickets;
        this.rol = rol;
    }

    countOpenTickets() {
        return this.tickets.filter(ticket => ticket.open).length;
    }

    getRol() {
        return this.rol;
    }

    print() {
        console.log(`El programador ${this.nombre} con id ${this.id} tiene ${this.countOpenTickets()} tickets abiertos. Su rol es ${this.getRol()}.`);
    }
}

const gerente = new Gerente('001', 'Mike', ['contabilidad', 'economato'], ['Robo, Tere, Shin Shan'])
gerente.print();

const gerenteProyecto = new GerenteProyecto('002', 'Tere', ['FaceLibro', 'JustCome'], 'completar el 80% de tareas de cada sprint');
gerenteProyecto.print();

const programadora = new Programadora('003', 'Caterina', [{id: 't1', open: true}, {id: 't2', open: false}, {id: 't3', open: true}], 'FullStack');
programadora.print();