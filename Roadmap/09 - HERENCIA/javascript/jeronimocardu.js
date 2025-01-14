class Animal{
    constructor(animal){
        this.animal = animal;
    }

    sonido(){
        console.log(`${this.animal} hace un sonido.`);
    }
}

class Perro extends Animal{
    sonido(){
        console.log(`${this.animal} hace Guau Guau!`);
    }
}
class Gato extends Animal{
    sonido(){
        console.log(`${this.animal} hace Miau Miau!`);
    }
}

let perro1 = new Perro('Videl');
perro1.sonido();
let gato1 = new Gato('Kira');
let gato2 = new Gato('Wendy');
let gato3 = new Gato('Margo');
gato1.sonido();
gato2.sonido();
gato3.sonido();

////////////////////////////////////////////////////////////
//              Extra

class Employes{
    constructor(id, name){
        this.id = id;
        this.name = name;
        this.employes = [];
    }

    add(employe){
        this.employes.push(employe);
    }
    show(){
        console.log(this.employes);
    }
}

class Manager extends Employes{
    showManager(){
        console.log(`${this.name} está controlando todos los proyectos`);
    }
}
class ProjectsManager extends Employes{
    constructor(id, name, project){
        super(id, name);
        this.project = project;
    }
    showPoject(){
        console.log(`${this.project} está siendo dirigido por ${this.name}`);
    }

}
class Programmers extends Employes{
    constructor(id, name, language){
        super(id, name);
        this.language = language;
    }
    showProgrammer(){
        console.log(`${this.name} está programando en ${this.language}`);
    }
}


let manager = new Manager(1, 'Jeronimo');
let programmer1 = new Programmers(2, 'Camila', 'javascript');
let programmer2 = new Programmers(3, 'Jose', 'Python');
let programmer3 = new Programmers(4, 'Thiago', 'GO');
let projectManager1 = new ProjectsManager(5, 'Enzo', 'proyecto 1');
let projectManager2 = new ProjectsManager(5, 'Riquelme', 'proyecto 2');
let projectManager3 = new ProjectsManager(5, 'Esteban', 'proyecto 3');

manager.add(programmer1);
manager.add(programmer2);
manager.add(programmer3);
projectManager1.add(programmer3);
projectManager2.add(programmer2);
projectManager3.add(programmer1);

programmer1.add(programmer3);

manager.showManager();
projectManager1.showPoject();
projectManager2.showPoject();
projectManager3.showPoject();
programmer1.showProgrammer()
programmer2.showProgrammer()
programmer3.showProgrammer()

projectManager3.show();