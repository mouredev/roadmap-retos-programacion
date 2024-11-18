//Superclase
class Animal{
    //Atributos comunes
    nombre: string;
    color: string;
    //constructor
    constructor(nombre: string, color: string){
        this.nombre = nombre;
        this.color = color;
    }
    //Metodo comun
    emitirSonido(): void{
        console.log(`${this.nombre} hace un sonido`);
    }
}
// Subclase Perro
class Perro extends Animal{
    // Constructor que llama al constructor de la superclase
    constructor(nombre: string, color: string){
        super(nombre,color);
    }
    // Sobrescribir el método emitirSonido
    emitirSonido(): void {
        console.log(`${this.nombre} dice: Guau`);
    }
}

// Subclase Perro
class Gato extends Animal{
    // Constructor que llama al constructor de la superclase
    constructor(nombre: string, color: string){
        super(nombre,color);
    }
    // Sobrescribir el método emitirSonido
    emitirSonido(): void {
        console.log(`${this.nombre} dice: Miau`);
    }
}

// Función para imprimir el sonido que emite un Animal
function imprimirSonido(animal: Animal): void {
    animal.emitirSonido();
}

let miPerro = new Perro('Rex','Negro');
let miGato = new Gato('Whiskers','Blanco');

imprimirSonido(miPerro); // Rex dice: ¡Guau!
imprimirSonido(miGato); // Whiskers dice: ¡Miau!

/******************************/
/*Extra*/

class Empleado{
    id: number;
    nombre: string;
    apellido: string;
    telefono: number;
    empleadoACargo: Empleado[]=[];
    
    constructor(id:number,nombre:string,apellido:string,telefono:number){
        this.id = id;
        this.nombre =nombre;
        this.apellido = apellido;
        this.telefono = telefono;
    }

    agregarEmpleadoACargo(empleado:Empleado): void{
        this.empleadoACargo.push(empleado);
    }

    imprimirDetalles(): void{
        console.log(`ID: ${this.id}, Nombre: ${this.nombre}, Apellido: ${this.apellido}, Telefono: ${this.telefono}`)
    }
}

class Gerente extends Empleado{
    departamento: string;

    constructor(id:number,nombre:string,apellido:string,telefono:number,departamento:string){
        super(id,nombre,apellido,telefono);
        this.departamento = departamento;
    }

    imprimirDetalles(): void {
        super.imprimirDetalles;
        console.log(`Departamento: ${this.departamento}`);
        console.log(`Empleados a Cargo: ${this.empleadoACargo.map(e => e.nombre).join(", ")}`);
    }
}

class GerenteDeProyectos extends Empleado {
    proyectos: string[];
    // Constructor
    constructor(id:number,nombre:string,apellido:string,telefono:number, proyectos: string[]) {
        super(id,nombre,apellido,telefono);
        this.proyectos = proyectos;
    }

    // Método específico del Gerente de Proyectos
    imprimirDetalles(): void {
        super.imprimirDetalles();
        console.log(`Proyectos: ${this.proyectos.join(", ")}`);
        console.log(`Empleados a Cargo: ${this.empleadoACargo.map(e => e.nombre).join(", ")}`);
    }
}

// Subclase Programador
class Programador extends Empleado {
    // Propiedades específicas del Programador
    lenguajes: string[];

    // Constructor
    constructor(id: number, nombre: string,apellido:string,telefono:number, lenguajes: string[]) {
        super(id,nombre,apellido,telefono);
        this.lenguajes = lenguajes;
    }

    // Método específico del Programador
    imprimirDetalles(): void {
        super.imprimirDetalles();
        console.log(`Lenguajes: ${this.lenguajes.join(", ")}`);
    }
}

// Crear instancias de los empleados
let gerente = new Gerente(1,'Carlos','Pereira',4439357, 'Desarrollo');
let gerenteDeProyectos = new GerenteDeProyectos(2, 'Ana','Fernandez',9720435, ['Proyecto A', 'Proyecto B']);
let programador1 = new Programador(3, 'Juan','Machado',4722585, ['JavaScript', 'TypeScript']);
let programador2 = new Programador(4, 'Laura','Martinez',4425157, ['Python', 'Django']);

// Asignar empleados a cargo
gerente.agregarEmpleadoACargo(gerenteDeProyectos);
gerenteDeProyectos.agregarEmpleadoACargo(programador1);
gerenteDeProyectos.agregarEmpleadoACargo(programador2);

// Imprimir detalles de cada empleado
gerente.imprimirDetalles();
gerenteDeProyectos.imprimirDetalles();
programador1.imprimirDetalles();
programador2.imprimirDetalles();


