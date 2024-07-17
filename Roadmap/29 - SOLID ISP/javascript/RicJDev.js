//EJERCICIO
/*
Incorrecto ❎

Se le está dando a la clase DogNoISP un método que no tiene sentido que tenga, lo que en un caso más complejo afectaría a la implementación de las clases

*/
class AnimalNoISP {
	constructor(name) {
		this.name = name
	}

	speak() {
		console.log(`${this.name} emite un sonido`)
	}

	fly() {
		console.log(`${this.name} vuela`)
	}
}

class DogNoISP extends AnimalNoISP {
	constructor(name) {
		super(name)
	}

	speak() {
		console.log(`${this.name} ladra`)
	}
}

const pepe = new DogNoISP('Pepe')

pepe.speak()
pepe.fly()

/*
Correcto ✅

"Las interfaces deben ser específicas y enfocarse en los requerimientos de los clientes que las utilizan."

*/
class CanFly {
	constructor(name) {
		this.name = name
	}

	fly() {
		console.log(`${this.name} vuela`)
	}
}

class CanSpeak {
	constructor(name) {
		this.name = name
	}

	speak() {
		console.log(`${this.name} emite un sonido`)
	}
}

class Dog extends CanSpeak {
	constructor(name) {
		super(name)
	}

	speak() {
		console.log(`${this.name} ladra`)
	}
}

const firulais = new Dog('Firulais')

firulais.speak()

//EXTRA
class Printer {
	print(document) {
		console.log(`Se ha imprimido ${document}`)
	}
}

class ColorPrinter extends Printer {
	print(document) {
		console.log(`Se ha imprimido ${document} a color`)
	}
}

class BlackAndWhitePrinter extends Printer {
	print(document) {
		console.log(`Se ha imprimido ${document} en blanco y negro`)
	}
}

class MultifuntionalPrinter extends Printer {
	print(document) {
		console.log(`Se ha imprimido ${document} en multifunción`)
	}

	scan(document) {
		console.log(`Se ha escaneado ${document}`)
	}

	sendFax(document) {
		console.log(`Se ha enviado ${document} por medio de fax`)
	}
}
