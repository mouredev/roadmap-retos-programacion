//---Herencia--
class Empleado{
    constructor(id, nombre){
        this.id = id;
        this.nombre = nombre;
        this.empleados =[];
    }
    guardar(emp){
        this.empleados.push(emp);
    }
    imprimir_empleados(){
        this.empleados.forEach((emp)=>{
            console.log(emp.nombre);
        });
    }
}

class Gerente extends Empleado{
    cordinador_general(){
        console.log(`${this.name} es el Gerente general del proyecto`);
    }
}

class GerenteProyecto extends Empleado{
    constructor(id, nombre, proyecto){
        super(id, nombre);
        this.proyecto = proyecto;       
    }
    coordinador_proyecto(){
        console.log(`${this.nombre} es el coordinador del proyecto `);
    }
}

class Programador extends Empleado{
    constructor(id, nombre, lenguaje){
        super(id, nombre);
        this.lenguaje = lenguaje;       
    }
    codigo(){
        console.log(`${this.nombre} esta programando en ${this.lenguaje}`);
    }
    guardar(emp){
        console.log(`EL programador no tiene ningun empleado a su cargo, ${emp.nombre} no se añadirá`);
    }
}


let gerente = new Gerente(1, "Julio")
let gerenteProyecto1 = new GerenteProyecto(2, "Pedro", "Proyecto 1");
let gerenteProyecto2 = new GerenteProyecto(3, "Roberto", "Proyecto 2");
let programador1 = new Programador(4, "José", "Javascript");
let programador2 = new Programador(5, "Marcos", "Java");
let programador3 = new Programador(6, "William", "Phtyon");

//En la funcion guardar se le añade los empleados a su cargo
gerente.guardar(gerenteProyecto1);
gerente.guardar(gerenteProyecto2);

gerenteProyecto2.guardar(programador1);
gerenteProyecto2.guardar(programador2);
gerenteProyecto2.guardar(programador3);

programador1.guardar(programador2)

//Imprime el nombre del programador y su lenguaje
programador1.codigo();

//Imprime los empleados a su cargo
gerente.imprimir_empleados(); // [Pedro, Roberto]
gerenteProyecto2.imprimir_empleados(); // [José, Marcos, William]
programador1.imprimir_empleados();



