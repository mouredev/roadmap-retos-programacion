/* 🔥 EJERCICIO:
Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.
*/

console.log("----- EJEMPLO SIMPLE -----");

//  * Ejemplo Incorrecto (viola LSP)
// --------------------------------------------------------------------------------------------------------------
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    setWidth(width) {
        this.width = width;
    }

    setHeight(height) {
        this.height = height;
    }

    area() {
        return this.width * this.height;
    }
}

class Square extends Rectangle {
    constructor(side) {
        super(side, side);
    }

    // Override que rompe el comportamiento esperado
    setWidth(side) {
        this.width = side;
        this.height = side; // Modifica ambos lados
    }

    setHeight(side) {
        this.width = side;
        this.height = side; // Modifica ambos lados
    }
}

// Función que espera un Rectangle (pero falla con Square)
function printArea(rectangle) {
    rectangle.setWidth(5);
    rectangle.setHeight(4);
    console.log(`Área esperada: 20, Área real: ${rectangle.area()}`);
}

// Violación de LSP: El cuadrado no se comporta como un rectángulo
const rect = new Rectangle(5, 5);
const square = new Square(5);
printArea(rect); // Área: 20 (correcto)
printArea(square); // Área: 16 (incorrecto, viola LSP)

//  * Ejemplo Correcto (cumple LSP)
// --------------------------------------------------------------------------------------------------------------
class Shape {
    area() {
        throw new Error("Método no implementado.");
    }
}

class RectangleCorrecto extends Shape {
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
    }

    setWidth(width) {
        this.width = width;
    }

    setHeight(height) {
        this.height = height;
    }

    area() {
        return this.width * this.height;
    }
}

class SquareCorrecto extends Shape {
    constructor(side) {
        super();
        this.side = side;
    }

    setSide(side) {
        this.side = side;
    }

    area() {
        return this.side * this.side;
    }
}

// Función que cumple LSP
function printAreaLSP(shape) {
    console.log(`Área: ${shape.area()}`);
}

// Uso correcto
const rectLSP = new RectangleCorrecto(5, 4);
const squareLSP = new SquareCorrecto(5);
printAreaLSP(rectLSP); // Área: 20
printAreaLSP(squareLSP); // Área: 25

// --------------------------------------------------------------------------------------------------------------
/* 🔥 DIFICULTAD EXTRA (opcional):
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
cumplir el LSP.
Instrucciones:
1. Crea la clase Vehículo.
2. Añade tres subclases de Vehículo.
3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
4. Desarrolla un código que compruebe que se cumple el LSP.
*/
console.log("\n----- JERARQUÍA DE VEHÍCULOS (LSP) -----");

// Clase base: Vehículo
class Vehiculo {
    constructor() {
        this.velocidad = 0;
    }

    acelerar() {
        throw new Error("Método no implementado.");
    }

    frenar() {
        throw new Error("Método no implementado.");
    }

    mostrarVelocidad() {
        return `Velocidad: ${this.velocidad} km/h`;
    }
}

// Subclase 1: Coche
class Coche extends Vehiculo {
    acelerar() {
        this.velocidad += 10;
        console.log("Coche acelerando...");
    }

    frenar() {
        this.velocidad -= 5;
        if (this.velocidad < 0) this.velocidad = 0;
        console.log("Coche frenando...");
    }
}

// Subclase 2: Bicicleta
class Bicicleta extends Vehiculo {
    acelerar() {
        this.velocidad += 3;
        console.log("Bicicleta pedaleando...");
    }

    frenar() {
        this.velocidad -= 2;
        if (this.velocidad < 0) this.velocidad = 0;
        console.log("Bicicleta frenando...");
    }
}

// Subclase 3: Motocicleta
class Motocicleta extends Vehiculo {
    acelerar() {
        this.velocidad += 15;
        console.log("Motocicleta acelerando...");
    }

    frenar() {
        this.velocidad -= 7;
        if (this.velocidad < 0) this.velocidad = 0;
        console.log("Motocicleta frenando...");
    }
}

// Función que cumple LSP: Trabaja con cualquier vehículo
function probarVehiculo(vehiculo) {
    console.log(`Probando ${vehiculo.constructor.name}:`);
    vehiculo.acelerar();
    vehiculo.acelerar();
    vehiculo.frenar();
    console.log(vehiculo.mostrarVelocidad());
}

// Crear vehículos
const coche = new Coche();
const bicicleta = new Bicicleta();
const moto = new Motocicleta();

// Probar cada vehículo (sin errores)
probarVehiculo(coche); // Velocidad: 15 km/h
probarVehiculo(bicicleta); // Velocidad: 4 km/h
probarVehiculo(moto); // Velocidad: 23 km/h

//  * Comprobación de LSP
// --------------------------------------------------------------------------------------------------------------
// Si sustituimos Vehiculo por cualquier subclase, el comportamiento es consistente
const vehiculos = [coche, bicicleta, moto];
vehiculos.forEach(vehiculo => {
    probarVehiculo(vehiculo);
    console.log("-----");
});