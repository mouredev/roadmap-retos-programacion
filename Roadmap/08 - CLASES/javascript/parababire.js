//Clases: funciones especiales. Poseen dos componentes.

/*Declaración de clases*/

class Vehiculo {//Utilizamos la palabra reservada class y por convención el nombre en mayuscula.
  constructor(fabricante, modelo) {//Solo puede ser llamado un constructor o inicializador por clase.
    this.fabricante = fabricante;
    this.modelo = modelo;
  }
  get caracteristicas() {
    return `El carro marca ${this.fabricante} es modelo ${this.modelo}.`;
  }
  set caracteristicas(val1) {
    [this.fabricante, this.modelo] = val1.split(" ");
  }
}
let carro = new Vehiculo("Toyota", "Corrolla");
console.log(`Compre un ${carro.fabricante} ${carro.modelo}.`);
console.log(carro.caracteristicas);
carro.caracteristicas = "Ford Bronco";
console.log(carro.caracteristicas);

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