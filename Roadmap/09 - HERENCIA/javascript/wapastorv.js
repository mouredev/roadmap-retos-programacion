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
/* Herencia en JavaScript 
    * En JavaScript, la herencia se logra mediante la propiedad prototype de los objetos.
    * En el siguiente ejemplo, se define una superclase Animal y dos subclases Perro y Gato.
    * La función emitirSonido() se define en la superclase Animal y se sobreescribe en las subclases.
*/
class Animal {
    constructor(nombre, sonido){
        this.nombre = nombre;
        this.sonido = sonido;
    }
    hacerSonido(){
        console.log(`${this.nombre} dice ${this.sonido}`);
    }
}
class Perro extends Animal {
    constructor(nombre){
        super(nombre, 'guau');// Llama al constructor de la superclase Animal, con super() y le pasa los argumentos necesarios. 
    }
}
class Gato extends Animal {
    constructor(nombre){
        super(nombre, 'miau'); // Llama al constructor de la superclase Animal, con super() y le pasa los argumentos necesarios.
    }
}
const perro = new Perro('Firulais');
const gato = new Gato('Garfield');
perro.hacerSonido();// Firulais dice guau
gato.hacerSonido();// Garfield dice miau

/*DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Empleado {
    #id; // Propiedad privada  para encapsular el id
    constructor(id, nombre){
        this.#id = id;// ID privado
        this.nombre = nombre;
    }
    // Getter para acceder al id
    getid(){
        return this.#id;
    }

    //Método comun para todos los empleados
    trabajar(){
        console.log(`${this.nombre} está trabajando.`);
    }
}

// clase Gerente que hereda de Empleado
class Gerente extends Empleado {
    constructor(id, nombre){
        super(id, nombre);
        this.empleadosACargo = [];// Lista de empleados a cargo
    }
    // Método exclusivo de la clase Gerente
    agregarEmpleado(empleado){
        this.empleadosACargo.push(empleado);
    }

    // Método exclusivo de la clase Gerente
    trabajar(){
        console.log(`${this.nombre} está gestionado su equipo de ${this.empleadosACargo.length} empleados.`);
    }

    mostarEquipo(){
        console.log(`${this.nombre} tiene a su cargo a:`);
        this.empleadosACargo.forEach((empleado, index) => {
            console.log(`${index + 1}. ${empleado.nombre} (ID: ${empleado.getid()})`);
        });
    }
}

//clase GerenteProyecto que hereda de Gerente

class GerenteProyecto extends Gerente {
    constructor(id, nombre){
        super(id, nombre);
        this.proyectos = [];// Lista de proyectos
    }

    // Método exclusivo de la clase GerenteProyecto
    agregarProyecto(proyecto){
        this.proyectos.push(proyecto);
    }

    // Método exclusivo de la clase GerenteProyecto
    trabajar(){
        console.log(`${this.nombre} está gestionando los siguientes proyectos: ${this.proyectos.join(", ")} proyectos.`);
    }
}

// clase Programador que hereda de Empleado
class Programador extends Empleado {
    constructor(id, nombre, lenguaje){
        super(id, nombre);
        this.lenguaje = lenguaje;
    }
    // Método exclusivo de la clase Programador
    desarrollar(){
        console.log(`${this.nombre} está desarrollando en ${this.lenguaje}.`);
    }

    trabajar(){
        console.log(`${this.nombre} está escribiendo código en ${this.lenguaje}.`);
    }
}

// Clase Diseñador que hereda de Empleado
class Diseñador extends Empleado {
    constructor(id, nombre, especialidad){
        super(id, nombre);
        this.especialidad = especialidad;
    }
    diseñar(){
        console.log(`${this.nombre} está creadi un diseño ${this.especialidad}.`);
    }

    trabajar(){
        console.log(`${this.nombre} está creado un diseño ${this.especialidad}.`);
    }
}

// Implementación de la jerarquía de empleados
const gerente = new Gerente(1, 'Laura');
const gerenteProyecto = new GerenteProyecto(2, 'Carlos');
const programador1 = new Programador(3, 'Juan', 'JavaScript');
const programador2 = new Programador(4, 'Ana', 'Python');
const diseñador = new Diseñador(5, 'María', 'UI/UX');

// Asignación de empleados  a los gerentes
gerente.agregarEmpleado(gerenteProyecto);
gerenteProyecto.agregarEmpleado(programador1);
gerenteProyecto.agregarEmpleado(programador2);
gerenteProyecto.agregarEmpleado(diseñador);

// Asignación de proyectos a los gerentes de proyecto
gerenteProyecto.agregarProyecto('Sistema de ventas');
gerenteProyecto.agregarProyecto('Aplicación móvil');
gerenteProyecto.agregarProyecto('Plataforma web');

// Interacturar con la jerarquía de empleados

gerente.trabajar();// Laura está gestionado su equipo de 1 empleados.
gerenteProyecto.trabajar();// Carlos está gestionando los siguientes proyectos: Sistema de ventas, Aplicación móvil, Plataforma web proyectos.
programador1.trabajar();// Juan está escribiendo código en JavaScript.
programador2.trabajar();// Ana está escribiendo código en Python.
diseñador.trabajar();// María está creado un diseño UI/UX.

// Mostrar equipos
gerente.mostarEquipo(); // Laura tiene a su cargo a: 1. Carlos (ID: 2)

gerenteProyecto.mostarEquipo(); // Carlos tiene a su cargo a: 1. Juan (ID: 3) 2. Ana (ID: 4) 3. María (ID: 5)
