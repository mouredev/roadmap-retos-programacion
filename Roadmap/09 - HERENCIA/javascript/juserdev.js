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
    constructor(name) {
        this.name = name
    }

    speak() { console.log(`${this.name} hace un ruido`) }
}

class Dog extends Animal {
    speak() { console.log(`${this.name} ladra.`) }
}

class Cat extends Animal {
    speak() { console.log(`${this.name} maulla.`) }
}

const maxDog = new Dog("Max dog")
const maxCat = new Cat("Max cat")


maxDog.speak()
maxCat.speak()

console.log("")
console.log("----------------- Dificultad extra -----------------")
console.log("")

class Employee {
    constructor(name, id) {
        this.name = name
        this.id = id
    }

    task() { return `${this.name} trabaja en la empresa de desarrollo` }

}

class PeopleManager extends Employee {
    constructor(name, id, employees = []) {
        super(name, id)
        this.employees = employees
    }

    addEmployees(employee) {
        this.employees.push(employee)
        return employee
    }
    countEmployess() { return this.employees.length }
    viewEmployees() { return this.employees }

}

class Programer extends Employee {
    task() { return `${this.name} es programdor y no tiene personal a cargo` }
}

class ProjectManager extends PeopleManager {
    task() { return `${this.name} es gerente de proyecto y tiene programadores a cargo` }
}

class Manager extends PeopleManager {
    task() { return `${this.name} es gerente y tiene gerentes de proyectos a cargo` }
}

const pedro = new Programer("Pedro", 1)
const max = new Programer("Max", 2)
const milton = new Programer("Milton", 3)
const filipino = new Programer("Filipino", 4)

const laura = new ProjectManager("Laura", 5)
const jeronimo = new ProjectManager("Jeronimo", 6, [milton])

const sebastian = new Manager("Sebastian", 7)

console.log(pedro)
console.log(max)

console.log(laura)
console.log(laura.addEmployees(pedro))
console.log(laura.addEmployees(max))
console.log(laura.viewEmployees())
console.log(laura.countEmployess())
console.log(laura)

console.log(jeronimo)
console.log(jeronimo.addEmployees(filipino))
console.log(jeronimo.viewEmployees())
console.log(jeronimo.countEmployess())
console.log(jeronimo)

console.log(sebastian)
console.log(sebastian.addEmployees(laura))
console.log(sebastian.task())
console.log(sebastian.countEmployess())
console.log(sebastian)
