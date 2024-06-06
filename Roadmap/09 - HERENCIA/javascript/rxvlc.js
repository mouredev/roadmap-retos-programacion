// Superclase
class Animal {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
}

// Heredera Perro
class Perro extends Animal {
    constructor(nombre, edad) {
        super(nombre, edad);
    }

    sonido() {
        console.log("¡guau guau!");
    }
}

// Heredera Gato
class Gato extends Animal {
    constructor(nombre, edad) {
        super(nombre, edad);
    }

    sonido() {
        console.log("¡miau miau!");
    }
}

// Clase base para representar a un empleado genérico
class Empleado {
    constructor(id, nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    informacion() {
        console.log(`ID: ${this.id}, Nombre: ${this.nombre}`);
    }
}

// Clase Gerente hereda de Empleado
class Gerente extends Empleado {
    constructor(id, nombre) {
        super(id, nombre);
        this.empleadosACargo = [];
    }

    agregarEmpleado(empleado) {
        this.empleadosACargo.push(empleado);
    }

    informacion() {
        super.informacion();
        console.log("Tipo: Gerente");
        console.log(`Empleados a cargo: ${this.empleadosACargo.length}`);
    }
}

// Clase GerenteProyecto hereda de Gerente
class GerenteProyecto extends Gerente {
    constructor(id, nombre, areaProyecto) {
        super(id, nombre);
        this.areaProyecto = areaProyecto;
    }

    informacion() {
        super.informacion();
        console.log(`Área del Proyecto: ${this.areaProyecto}`);
    }
}

// Clase Programador hereda de Empleado
class Programador extends Empleado {
    constructor(id, nombre, lenguaje) {
        super(id, nombre);
        this.lenguaje = lenguaje;
    }

    informacion() {
        super.informacion();
        console.log(`Lenguaje: ${this.lenguaje}`);
    }
}

// Creación de instancias de Perro y Gato
let miPerro = new Perro("Bobby", 5);
let miGato = new Gato("Whiskers", 3);

// Llamada a los métodos específicos de cada clase
miPerro.sonido(); // Salida: ¡guau guau!
miGato.sonido(); // Salida: ¡miau miau!

// Creación de instancias de empleados
let gerente1 = new Gerente(1, "Juan");
let gerenteProyecto1 = new GerenteProyecto(2, "María", "Desarrollo Web");
let programador1 = new Programador(3, "Pedro", "C#");

// Agregar empleados a cargo del gerente
gerente1.agregarEmpleado(gerenteProyecto1);
gerenteProyecto1.agregarEmpleado(programador1);

// Mostrar información de los empleados
console.log("Información del Gerente:");
gerente1.informacion();
console.log("\nInformación del Gerente de Proyecto:");
gerenteProyecto1.informacion();
console.log("\nInformación del Programador:");
programador1.informacion();
