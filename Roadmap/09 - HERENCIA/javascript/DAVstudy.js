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
    constructor(name, owner) {
        this.name = name
        this.owner = owner
    }

    sound = () => 'Sonido sin identificar'
    
}

class Dog extends Animal {

    sound = () => 'Guau'
}

class Cat extends Animal {

    sound = () => 'Miau'
}


let oreo = new  Cat('Oreo', 'Diego')
let chasca = new  Dog('Chasca', 'Juan')

console.log(oreo.sound());
console.log(chasca.sound());

 /*
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Employees {
    constructor(id, name) {
        this.id = id
        this.name = name
    }
}

class Manager extends Employees {

    constructor(id, name, area, projectManagers = []) {
        super(id, name);
        this.area = area;
        this.projectManagers = projectManagers;
    }

    addProjectManager(id, name, area, team) {
        this.projectManagers.push(new ProjectManager(id, name, area, team));
    }

    removeProjectManager(id) {
        this.projectManagers = this.projectManagers.filter(pm => pm.id !== id);
    }
    
}

class ProjectManager extends Employees {

    constructor(id, name, area, team = []) {
        super(id, name);
        this.area = area;
        this.team = team;
    }

    addDeveloper(id, name, level) {
        this.team.push(new Developers(id, name, level));
    }

    removeDeveloper(id) {
        this.team = this.team.filter(dev => dev.id !== id);
    }
}

class Developers extends Employees {
    constructor(id, name,level) {
        super(id, name)
        this.level = level
    }
}

let juan = new Developers(255, 'Juan', 'Senior')
let miguel = new Developers(256, 'Miguel', 'Mid-Senior')
let luis = new Developers(257, 'Luis', 'Senior')
let fabian = new Developers(258, 'Fabian', 'Junior')

let team1 = [juan, miguel]
let team2 = [luis, fabian]

let carlos = new ProjectManager(127, 'Carlos', 'Backend', team1)
let felipe = new ProjectManager(128, 'Felipe', 'Frontend', team2)

let diego = new Manager(0, 'Diego', 'Web Development', [carlos, felipe])

console.log(diego.projectManagers)
diego.removeProjectManager(128)
console.log(diego.projectManagers)


console.log(carlos.team)
carlos.addDeveloper(12, 'Joaquim', 'Mid-Senior')
console.log(carlos.team)
