/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
*/

class Rectangulo {
    constructor(ancho, alto) {
        this.ancho = ancho
        this.alto = alto
    }

    setAncho(ancho) {
        this.ancho = ancho
    }

    setAlto(alto) {
        this.alto = alto
    }

    calcularArea() {
        return this.ancho * this.alto
    }
}

class Cuadrado extends Rectangulo {
    setAncho(lado) {
        this.ancho = lado
        this.alto = lado
    }

    setAlto(lado) {
        this.ancho = lado
        this.alto = lado
    }
}

class MostrarArea {

     area(rectangulo) {
        rectangulo.setAncho(2)
        rectangulo.setAlto(3)

        console.log(`Area = ${rectangulo.calcularArea()}`)
    }
}

const rectangulo1 = new Rectangulo(2, 3)
const mostrarElArea =  new MostrarArea()

mostrarElArea.area(rectangulo1)


const cuadrado1 = new Cuadrado(2, 3)

mostrarElArea.area(cuadrado1)


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
*/


class Vehiculo {
    constructor(marca) {
        this.marca = marca
        this.velocidad = 0
    }

    acelerar() {
        this.velocidad += 10
        console.log(`${this.marca} acelera. Velocidad: ${this.velocidad} km/h.`)
    }

    frenar() {
        this.velocidad -= 10

        if(this.velocidad < 0) {
            this.velocidad = 0
        }

        console.log(`${this.marca} frena. Velocidad: ${this.velocidad} km/h.\n`)
    }
}

// Subclase 1

class Coche extends Vehiculo {
    acelerar() {
        this.velocidad += 20
        console.log(`${this.marca} acelera. Velocidad: ${this.velocidad} km/h.`)
    }
}

// Subclase 2
class Moto extends Vehiculo {
    acelerar() {
        this.velocidad += 30
        console.log(`${this.marca} acelera. Velocidad: ${this.velocidad} km/h.`)
    }
}

// Subclase 3
class Camion extends Vehiculo {
    acelerar() {
        this.velocidad += 10
        console.log(`${this.marca} acelera. Velocidad: ${this.velocidad} km/h.`)
    }
}


function probarVehiculo(vehiculo) {
    vehiculo.acelerar()
    vehiculo.frenar()
}

const coche = new Coche("BMW")
probarVehiculo(coche)

const moto = new Moto("Honda")
probarVehiculo(moto)

const camion = new Camion("Scania")
probarVehiculo(camion)