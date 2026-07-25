class Animal{

    protected nombre:string;
    constructor(_nombre:string){
        this.nombre=_nombre;
    }

    protected printSound(){
        console.log(`el ${this.nombre} hace un sonido`);
    }
}

class Perro extends Animal{

    constructor(nombre:string){
        super(nombre);
    }
    printSound(){
        console.log(`${this.nombre} hace guau!`)
    }
}

class Gato extends Animal{

    constructor(nombre:string){
        super(nombre);
    }
    printSound(){
        console.log(`${this.nombre} hace miau!`);
    }
}

let perro:Perro= new Perro("Kimmy");
perro.printSound();

let gato:Gato= new Gato("Mishi");
gato.printSound();

//EXTRA
class Empleado{

    public id:number;
    public nombre:string;
    public puesto:string;
    constructor(_id:number, _nombre:string, _puesto:string){
        this.id=_id;
        this.nombre=_nombre;
        this.puesto=_puesto;
    }
    
    public verInformacion(){
        console.log(`\nInformación del empleado: id: ${this.id}, nombre: ${this.nombre}, Puesto: ${this.puesto}`);
    }
    public verLabor(){
    }
}

class Gerente extends Empleado{
    private empleados:Empleado[];
    constructor(id:number, nombre:string, _empleados:Empleado[]){
        super(id,nombre,"Gerente")
        this.empleados=_empleados;
    }

    verLabor(){
        super.verInformacion();
        console.log(`Labor: El gerente tiene la labor de supervisar a los empleados: `)
        this.empleados.forEach((empleado)=>console.log(empleado.nombre));
    }
}
class GerenteProyectos extends Empleado{
    private empleados:Empleado[];
    private proyectos:string[];
    constructor(id:number, nombre:string, _empleados:Empleado[], _proyectos:string[]){
        super(id,nombre,"Gerente De Proyectos");
        this.empleados=_empleados;
        this.proyectos=_proyectos;
    }

    verLabor(){
        super.verInformacion();
        console.log(`Labor: El gerente de proyectos tiene la labor de supervisar los proyectos: `) 
            console.log(this.proyectos);
        console.log(`y los empleados a su cargo: `)
        this.empleados.forEach((empleado)=>console.log(empleado.nombre));
    }
}
class Programador extends Empleado{
    private tareas:string[];
    constructor(id:number, nombre:string, _tareas:string[]){
        super(id,nombre, "Programador")
        this.tareas=_tareas;
    }

    verLabor(){
        super.verInformacion();
        console.log(`Labor: El programador tiene la labor de trabajar en las tareas que se le tienen asignadas: ${this.tareas}`)
    }
}

let proyectos:string[]=["Pro1","Pro2","Pro3"]
let tareas:string[]=["tarea1","tarea2","tarea3"];
let programadores:Programador[]=[new Programador(12,"Edgar",tareas),new Programador(13,"Ramiro",tareas)]
let gerentesProyectos:GerenteProyectos[]=[new GerenteProyectos(12,"Jose",programadores,proyectos)];
let gerentes:Gerente[]=[new Gerente(12, "Roberto", gerentesProyectos)]


gerentes[0].verLabor();
gerentesProyectos[0].verLabor();
programadores[0].verLabor();
programadores[1].verLabor();
