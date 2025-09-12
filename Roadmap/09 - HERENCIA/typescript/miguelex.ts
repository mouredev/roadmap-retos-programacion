class Animal {
    nombre: string;
    sonido: string;

    constructor(nombre: string, sonido: string) {
        this.nombre = nombre;
        this.sonido = sonido;
    }
}

class Perro extends Animal {
    constructor(nombre: string, sonido: string) {
        super(nombre, sonido);
    }

    get Sonido(): string {
        return `El perro ${this.nombre} hace ${this.sonido}!`;
    }
}

class Gato extends Animal {
    constructor(nombre: string, sonido: string) {
        super(nombre, sonido);
    }

    get Sonido(): string {
        return `El gato ${this.nombre} hace ${this.sonido}!`;
    }
}

const milu = new Perro('Milu', 'Guau, guau');
console.log(milu.Sonido);

const garfield = new Gato('Garfield', 'Miauuuu');
console.log(garfield.Sonido);

// Extra

class Empleado {
    id: number;
    nombre: string;

    constructor(id: number, nombre: string) {
        this.id = id;
        this.nombre = nombre;
    }
}

class Gerente extends Empleado {
    empleados: string[];

    constructor(id: number, nombre: string, empleados: string[]) {
        super(id, nombre);
        this.empleados = empleados;
    }

    get gestiona(): string {
        return `El gerente ${this.nombre} gestiona a ${this.empleados.length} empleados, que son ${this.empleados.join(", ")}.`;
    }
}

class GerenteP extends Empleado {
    empleados: string[];

    constructor(id: number, nombre: string, empleados: string[]) {
        super(id, nombre);
        this.empleados = empleados;
    }

    get gestiona(): string {
        return `El gerente ${this.nombre} gestiona a ${this.empleados.length} empleados, que son ${this.empleados.join(", ")}.`;
    }
}

class Programador extends Empleado {
    lenguajes: string[];

    constructor(id: number, nombre: string, lenguajes: string[]) {
        super(id, nombre);
        this.lenguajes = lenguajes;
    }

    get programa(): string {
        return `El programador ${this.nombre} programa en ${this.lenguajes.join(", ")}.`;
    }
}

const gerente = new Gerente(1, 'Migue', ['Ana', 'Pedro', 'Luis']);
console.log(gerente.gestiona);

const gerenteP = new GerenteP(2, 'Ana', ['Rafa', 'Maria', 'Luisa']);
console.log(gerenteP.gestiona);

const programador = new Programador(3, 'Pedro', ['JavaScript', 'Python', 'Java']);
console.log(programador.programa);
