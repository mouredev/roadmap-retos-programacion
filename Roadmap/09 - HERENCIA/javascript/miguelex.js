class Animal {
    constructor(nombre, sonido) {
        this.nombre = nombre
        this.sonido = sonido
    }
}

class Perro extends Animal {
    constructor(nombre, sonido) {
        super(nombre, sonido)
    }
    get Sonido() {
        return "El perro " + this.nombre + " hace " + this.sonido + "!"
    }
}

class Gato extends Animal {
    constructor(nombre, sonido) {
        super(nombre, sonido)
    }
    get Sonido() {
        return "El gato " + this.nombre + " hace " + this.sonido + "!"
    }
}

const milu = new Perro('Milu', 'Guau, guau')
console.log(milu.Sonido)

const garfield = new Gato('Garfield', 'Miauuuu')
console.log(garfield.Sonido)

// Extra

class Empleado {
    constructor(id, nombre) {
        this.id = id
        this.nombre = nombre
    }
}

class Gerente extends Empleado {
    constructor(id, nombre, empleados) {
        super(id, nombre)
        this.empleados = empleados
    }
    
    get gestiona() {
        return "El gerente " + this.nombre + " gestiona a " + this.empleados.length + " empleados, que son " + this.empleados.join(", ") + "."
    }
}

class GerenteP extends Empleado {
    constructor(id, nombre, empleados) {
        super(id, nombre)
        this.empleados = empleados
    }
    
    get gestiona() {
        return "El gerente " + this.nombre + " gestiona a " + this.empleados.length + " empleados, que son " + this.empleados.join(", ") + "."
    }

}

class Programador extends Empleado {
    constructor(id, nombre, lenguaje) {
        super(id, nombre)
        this.lenguaje = lenguaje
    }
    
    get programa() {
        return "El programador " + this.nombre + " programa en " + this.lenguaje.join(", ") + "."
    }

}

const gerente = new Gerente(1, 'Migue', ['Ana', 'Pedro', 'Luis'])
console.log(gerente.gestiona)

const gerenteP = new GerenteP(2, 'Ana', ['Rafa', 'Maria', 'Luisa'])
console.log(gerenteP.gestiona)

const programador = new Programador(3, 'Pedro', ['JavaScript', 'Python', 'Java'])
console.log(programador.programa)