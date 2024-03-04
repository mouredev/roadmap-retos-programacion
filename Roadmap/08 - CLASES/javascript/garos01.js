// Clases

class Vehiculo {
  constructor(marca, modelo, anio, color) {
    this.marca = marca;
    this.modelo = modelo;
    this.anio = anio;
    this.color = color;
  }

  imprimirInformacion() {
    console.log(`Marca: ${this.marca}`);
    console.log(`Modelo: ${this.modelo}`);
    console.log(`Año: ${this.anio}`);
    console.log(`Color: ${this.color}`);
  }
}

// Crear una instancia de la clase Vehiculo
let vehiculo1 = new Vehiculo("Toyota", "Camry", 2022, "Azul");

// Imprimir la información inicial
console.log("Información inicial del vehículo:");
vehiculo1.imprimirInformacion();

// Modificar algunos atributos
vehiculo1.anio = 2021;
vehiculo1.color = "Blanco";

// Imprimir la información después de la modificación
console.log("\nInformación después de la modificación:");
vehiculo1.imprimirInformacion();

// Ejercicio extra

class NavegadorWeb {
  constructor() {
    this.historial = [];
  }

  navegarA(pagina) {
    this.historial.push(pagina);
    console.log("Navegando a:", pagina);
  }

  adelante() {
    const paginaSiguiente = this.historial.pop();
    if (paginaSiguiente) {
      console.log("Avanzando a:", paginaSiguiente);
    } else {
      console.log("No hay páginas siguientes en el historial");
    }
  }

  atras() {
    const paginaAnterior = this.historial.pop();
    if (paginaAnterior) {
      console.log("Retrocediendo a:", paginaAnterior);
    } else {
      console.log("No hay páginas anteriores en el historial");
    }
  }
}

const navegador = new NavegadorWeb();

navegador.navegarA("Google");
navegador.navegarA("Facebook");
navegador.navegarA("Twitter");

navegador.atras();
navegador.adelante();
navegador.atras();
navegador.atras();
