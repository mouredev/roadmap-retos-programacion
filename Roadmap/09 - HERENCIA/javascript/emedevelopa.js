class Animal {
    constructor(animal, name, sound) {
        this.animal = animal;
        this.name = name;
        this.sound = sound;
    }

    emiteSonido() {
        console.log(`${this.animal} ${this.name} hace ${this.sound}`);
    }
}

class Perro extends Animal {
    
}
let perro = new Perro("El perro","Pipo", "Woof");
perro.emiteSonido();

class Gato extends Animal {

}
let gato = new Gato("La gata", "Misi", "meow");
gato.emiteSonido();

//

class Empleado {
    constructor(cargo, id, name) {
        this.cargo = cargo;
        this.id = id;
        this.name = name;
    }
    datos() {
        console.log(`${this.name} ocupa el cargo de ${this.cargo} y su ID es ${this.id}`);
    }
}

class Gerente extends Empleado {
    constructor(cargo, id, name, empleadosACargo) {
        super(cargo, id, name);
        this.empleadosACargo = empleadosACargo;
    }
    aCargo() {
        console.log(`${this.name} tiene ${this.empleadosACargo} empleados a cargo`);
    }
}


class gerenteDeProyectos extends Empleado {
    constructor(cargo, id, name, proyecto) {
        super(cargo, id, name);
        this.proyecto = proyecto;
    }
    gestionProyecto() {
        console.log(`${this.name} esta gestionando ${this.proyecto} proyectos`);
    }
}


class Desarrollador extends Empleado {
    constructor(cargo, id, name, lenguaje) {
        super(cargo, id, name)
        this.lenguaje = lenguaje;
    }
    code() {
        console.log(`${this.name} esta usando ${this.lenguaje}`);
    }
}

let gerente = new Gerente("gerente", 1234, "Roberto", 13);
gerente.datos();
gerente.aCargo();

let gerenteDeProyecto = new gerenteDeProyectos("gerente de proyectos", 7774, "Luis", 3);
gerenteDeProyecto.datos();
gerenteDeProyecto.gestionProyecto();

let desarrollador = new Desarrollador("desarrollador", 6765, "Benito", "Javascript");
desarrollador.datos();
desarrollador.code();
