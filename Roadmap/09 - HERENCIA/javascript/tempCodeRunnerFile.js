class Employee {
    constructor(name, id, employees = []) {
        this.name = name
        this.id = id
        this.employees = employees
    }

    task() {
        return `${this.name} trabaja en la empresa de desarrollo`
    }

    viewEmployees() { return this.employees }


}

class Programer extends Employee {
    task() { return `${this.name} es programdor y no tiene personal a cargo` }
}

class ProjectManager extends Employee {

    task() { return `${this.name} es gerente de proyecto y tiene programadores a cargo` }

    addEmployees(employee) { return this.employees.push(employee) }

    countEmployess() { return this.employees.length }

}

class Manager extends Employee {
    task() { return `${this.name} es gerente y tiene gerentes de proyectos a cargo` }

    addEmployees(employee) { return this.employees.push(employee) }

    countEmployess() { return this.employees.length }
}



const pedro = new Programer("Pedro", 1)
const max = new Programer("Max", 1)

const laura = new ProjectManager("Laura", 2)

const sebastian = new Manager("Sebastian", 3)

console.log(pedro)
console.log(max)

console.log(laura.addEmployees(pedro))
console.log(laura.addEmployees(max))
console.log(laura)
console.log(laura.viewEmployees())
console.log(laura.countEmployess())

console.log(sebastian.addEmployees(laura))
console.log(sebastian.task())
console.log(sebastian.countEmployess())
console.log(sebastian)