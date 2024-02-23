//Clases: funciones especiales. Poseen dos componentes.

/*Declaración de clases*/

class Vehiculo {//Utilizamos la palabra reservada class y por convención el nombre en mayuscula.
  constructor(ruedas, puertas) {//Solo puede ser llamado un constructor o inicializador por clase.
    this.ruedas = ruedas;
    this.puertas = puertas;
  }
  caracteristicas() {
    console.log(`El carro posee ${this.ruedas} ruedas y ${this.puertas} puertas`);
  }
}
let corrolla = new Vehiculo(4, 2);
console.log(`Compre un corrolla ${corrolla.puertas} puertas.`);
console.log(`El corrolla tiene neumáticos nuevos en las ${corrolla.ruedas} ruedas.`);
corrolla.caracteristicas();
corrolla.puertas = 4;
console.log(corrolla.puertas);

/*Expresión de clases*/

//Anónima
let Perro = class {
  constructor(patas, cola, raza) {
    this.patas = patas;
    this.cola = cola;
    this.raza = raza;
  }
}

//Nombrada
let Rectangulo = class Rectangulo1 {
  constructor(alto, ancho) {
    this.alto = alto;
    this.ancho = ancho;
  }
}