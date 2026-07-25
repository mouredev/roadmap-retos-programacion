// Herencia y Polimorfismo

class Animal {
    
    constructor(nombre){
        this.nombre = nombre;
    }

}

class Perro extends Animal {

    sonido(){
        console.log('El Perro Ladra')
    }
}

class Gato extends Animal {

    sonido(){
        console.log('El Gato Maulla')
    }
}

const miPerro = new Perro('Milca');

miPerro.sonido()

const miGato = new Gato('Mishi');

miGato.sonido();


/*
* DIFICULTAD EXTRA (opcional):
* Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
* pueden ser Gerentes, Gerentes de Proyectos o Programadores.
* Cada empleado tiene un identificador y un nombre.
* Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
* actividad, y almacenan los empleados a su cargo.
*/

class Empleado {
    
    constructor(id, nombre){
        this.id =id;
        this.nombre = nombre;
    }

}

class Gerente extends Empleado {

    constructor(id, nombre){
        super(id, nombre);
        this.empleados = [];
    }

    mostrarInformacion(){
        console.log(`Gerente: ${this.nombre}, ID: ${this.id}`);
    }

    agregarEmpleado(empleado){
        this.empleados.push(empleado);
    }

    mostrarEmpleados(){

        console.log('Empleados a cargo: ');

        this.empleados.forEach( empleado => { console.log(`Gerente de Proyecto: ${empleado.nombre}`); });
    }
}

class GerenteProyecto extends Empleado {

    constructor(id, nombre){
        super(id, nombre);
        this.empleados = [];
    }

    mostrarInformacion(){
        console.log(`Gerente de Proyecto: ${this.nombre}, ID: ${this.id}`);
    }

    agregarEmpleado(empleado){
        this.empleados.push(empleado)
    }

    mostrarEmpleados(){

        console.log('Empleados a cargo: ');

        this.empleados.forEach( empleado => { console.log(`Programador: ${empleado.nombre}`); });
    }



}

class Programador extends Empleado {

    mostrarInformacion(){
        console.log(`Programador: ${this.nombre}, ID: ${this.id}`);
    }

}


const gerente = new Gerente(1, 'Juan');
const gerenteProyecto = new GerenteProyecto(2, 'Pedro');
const programador1 = new Programador(3, 'Luis');
const programador2 = new Programador(4, 'Carlos');

gerente.agregarEmpleado(gerenteProyecto);
gerenteProyecto.agregarEmpleado(programador1);
gerenteProyecto.agregarEmpleado(programador2);

gerente.mostrarInformacion();
gerente.mostrarEmpleados();
console.log('------------------------------')
gerenteProyecto.mostrarInformacion();
gerenteProyecto.mostrarEmpleados();
console.log('------------------------------')
programador1.mostrarInformacion();
programador2.mostrarInformacion();
