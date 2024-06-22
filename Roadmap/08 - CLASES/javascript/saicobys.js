class Persona {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }

  imprimirInformacion() {
    console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
  }
}

// Crear un objeto de la clase Persona
let persona1 = new Persona("Ana", 30);

// Establecer y modificar atributos
persona1.edad = 31; // Modificar la edad

// Llamar al metodo para imprimir informacion
persona1.imprimirInformacion();
