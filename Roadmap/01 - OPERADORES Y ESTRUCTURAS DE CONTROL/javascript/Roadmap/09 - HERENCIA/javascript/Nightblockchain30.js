class Animal {
    constructor(name,age){
        this.name = name
        this.age = age  
    }

    speakAnimmal(){
        return `Animal Power!`;
    }
}


class Dog extends Animal {
    constructor(name,age,breed){
        super(name,age)
        this.breed = breed
    }

    speakDog(){
        return `GUAU GUAU`
    }
}


class Cat extends Animal {
    constructor(name,age,size){
        super(name,age)
        this.size = size
    }

    speakCat(){
        return `MIAU MIAU`
    }
}


// CASOS DE USO
let animal1 = new Animal("caballo",10)
let dog1= new Dog("perro",5,"Bull Terrier")
let cat1= new Cat("gato",10,"small")

console.log(animal1.speakAnimmal());
console.log(dog1.speakDog());
console.log(cat1.speakCat());


// << EXTRA >>

class Employee {
    constructor(id,name){
        this.id = id;
        this.name = name;
        this.empleadosAsignados = [];
    }

    getInfo(){
        console.log(`ID:${this.id} | NAME:${this.name}`);
    }
}

class Manager extends Employee {
    constructor(id,name,age){
        super(id,name)
        this.age = age;
    }

    getInfo(){
        super.getInfo();
        console.log(`AGE: ${this.age}`);
    }
}


class ProjectManager extends Employee {
    constructor(id,name,experience){
        super(id,name)
        this.experience = experience
    }
}


class Programmer extends Employee{
    constructor(id,name,language){
        super(id,name)
        this.language = language
    }


}

let empleado1 = new Employee(1234,"Pepe");
let empleado2 = new Employee(6789,"María");

console.log(empleado1);
console.log(empleado1.getInfo());

let manager1 = new Manager(333,"Juan",37)
console.log(manager1);

let projectManager1 = new ProjectManager(555,"Lydia",7)
console.log(projectManager1);

let programmer1 = new Programmer(888,"Pedro","Java Script")
console.log(programmer1);


// Agregamos empleados al manager1 y al projectManager1
manager1.empleadosAsignados.push(empleado1);
manager1.empleadosAsignados.push(empleado2);
console.log(manager1.empleadosAsignados);

// Mostramos por pantalla los empleados a cargo del manager1
for (const empleado of manager1.empleadosAsignados){
    console.log(empleado.getInfo());
}