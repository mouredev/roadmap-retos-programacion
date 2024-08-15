// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";

// Clase base abstracta para todos los vehículos. Define dos métodos abstractos
// que deben ser implementados por las subclases: acelerar y frenar.
class Vehiculo {
    /**
     * Método abstracto para acelerar. Debe ser implementado por las subclases.
     * @throws {Error} Si no se implementa en una subclase.
     */
    acelerar() {
        throw new Error("Este método debe ser implementado por una subclase.");
    }

    /**
     * Método abstracto para frenar. Debe ser implementado por las subclases.
     * @throws {Error} Si no se implementa en una subclase.
     */
    frenar() {
        throw new Error("Este método debe ser implementado por una subclase.");
    }
}

// Clase que representa un coche. Implementa los métodos acelerar y frenar
// de acuerdo a la interfaz definida por la clase base Vehiculo.
class Coche extends Vehiculo {
    acelerar() {
        return "[+] - El coche está acelerando.";
    }

    frenar() {
        return "[+] - El coche está frenando.";
    }
}

// Clase que representa una bicicleta. Implementa los métodos acelerar y frenar
// de acuerdo a la interfaz definida por la clase base Vehiculo.
class Bicicleta extends Vehiculo {
    acelerar() {
        return "[+] - La bicicleta está acelerando.";
    }

    frenar() {
        return "[+] - La bicicleta está frenando.";
    }
}

// Clase que representa un avión. Implementa los métodos acelerar y frenar
// de acuerdo a la interfaz definida por la clase base Vehiculo.
class Avion extends Vehiculo {
    acelerar() {
        return "[+] - El avión está acelerando.";
    }

    frenar() {
        return "[+] - El avión está frenando.";
    }
}

/**
 * Función para probar el principio de sustitución de Liskov (LSP). 
 * Toma un objeto Vehiculo y llama a sus métodos acelerar y frenar.
 * 
 * @param {Vehiculo} vehiculo - Una instancia de una subclase de Vehiculo.
 */
function testLSP(vehiculo) {
    console.log(vehiculo.acelerar());
    console.log(vehiculo.frenar());
}

// Lista de diferentes vehículos que cumplen con el LSP
const vehiculos = [new Coche(), new Bicicleta(), new Avion()];

// Probar cada vehículo para asegurar que cumplen con el LSP
vehiculos.forEach(vehiculo => testLSP(vehiculo));
