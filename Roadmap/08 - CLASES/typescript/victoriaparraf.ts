class Persona {
    // Atributos
    nombre: string;
    edad: number;
    // Constructor (inicializador)
    constructor(nombre: string, edad: number) {
        this.nombre = nombre;
        this.edad = edad;
    }
    // Método para imprimir los detalles de la persona
    imprimirDetalles(): void {
        console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
    }
}

// Crear una instancia de la clase Persona
let persona1 = new Persona('Juan', 30);
// Imprimir detalles de la persona
persona1.imprimirDetalles(); // Nombre: Juan, Edad: 30
// Modificar los atributos
persona1.nombre = 'Carlos';
persona1.edad = 35;
// Imprimir los detalles actualizados
persona1.imprimirDetalles(); // Nombre: Carlos, Edad: 35
