/* 🔥 EJERCICIO:
Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
*/

console.log("----- EJEMPLO SIMPLE -----");

//  * Ejemplo Incorrecto (viola ISP): Interfaz grande y forzada
// --------------------------------------------------------------------------------------------------------------
class TrabajadorIncorrecto {
    trabajar() {}
    comer() {}
    dormir() {}
}

class Robot extends TrabajadorIncorrecto {
    trabajar() {
        console.log("🤖 Robot trabajando...");
    }

    // Métodos no necesarios, pero obligados por la interfaz
    comer() {
        throw new Error("❌ Los robots no comen.");
    }

    dormir() {
        throw new Error("❌ Los robots no duermen.");
    }
}

// Función que usa la interfaz incorrecta
function gestionarTrabajador(trabajador) {
    trabajador.trabajar();
    try {
        trabajador.comer(); // ¡Falla con Robot!
    } catch (error) {
        console.error(error.message);
    }
}

// Uso incorrecto
const robot = new Robot();
gestionarTrabajador(robot); // Error: Los robots no comen.


//  * Ejemplo Correcto (cumple ISP): Interfaces segregadas
// --------------------------------------------------------------------------------------------------------------
class Trabajable {
    trabajar() {
        throw new Error("Implementa el método 'trabajar'");
    }
}

class Comible {
    comer() {
        throw new Error("Implementa el método 'comer'");
    }
}

class Dormible {
    dormir() {
        throw new Error("Implementa el método 'dormir'");
    }
}

class RobotCorrecto extends Trabajable {
    trabajar() {
        console.log("🤖 Robot trabajando correctamente...");
    }
}

class Humano extends Trabajable {
    constructor() {
        super();
        this.comible = new Comible();
        this.dormible = new Dormible();
    }

    trabajar() {
        console.log("👤 Humano trabajando...");
    }

    comer() {
        this.comible.comer();
    }

    dormir() {
        this.dormible.dormir();
    }
}

// Función que cumple ISP
function gestionarTrabajo(trabajable) {
    trabajable.trabajar();
}

// Uso correcto
const robotCorrecto = new RobotCorrecto();
gestionarTrabajo(robotCorrecto); // Correcto: solo usa 'trabajar'

/* 🔥 DIFICULTAD EXTRA (opcional):
Crea un gestor de impresoras.
Requisitos:
1. Algunas impresoras sólo imprimen en blanco y negro.
2. Otras sólo a color.
3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
Instrucciones:
1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
2. Aplica el ISP a la implementación.
3. Desarrolla un código que compruebe que se cumple el principio.
 */
// --------------------------------------------------------------------------------------------------------------
console.log("\n----- GESTOR DE IMPRESORAS (ISP) -----");

// Interfaz base para impresoras
class Impresora {
    imprimir() {
        throw new Error("Método 'imprimir' no implementado");
    }
}

// Interfaz para escáner
class Escaner {
    escanear() {
        throw new Error("Método 'escanear' no implementado");
    }
}

// Interfaz para fax
class Fax {
    enviarFax() {
        throw new Error("Método 'enviarFax' no implementado");
    }
}

// Impresora B/N (solo implementa impresión)
class ImpresoraBN extends Impresora {
    imprimir() {
        console.log("🖨️ Imprimiendo en blanco y negro.");
    }
}

// Impresora color (solo implementa impresión)
class ImpresoraColor extends Impresora {
    imprimir() {
        console.log("🌈 Imprimiendo a color.");
    }
}

// Multifunción (implementa todas las interfaces)
class Multifuncion extends Impresora {
    constructor() {
        super();
        this.escaner = new Escaner();
        this.fax = new Fax();
    }

    escanear() {
        this.escaner.escanear();
    }

    enviarFax() {
        this.fax.enviarFax();
    }

    imprimir() {
        console.log("🖨️ 🌈 Imprimiendo en B/N o color (multifunción).");
    }
}

// Funciones del gestor que cumplen ISP
function imprimirDocumento(impresora) {
    if (impresora instanceof Impresora) {
        impresora.imprimir();
    } else {
        console.log("⚠️ No es una impresora válida.");
    }
}

function escanearDocumento(escaner) {
    if (escaner instanceof Escaner) {
        escaner.escanear();
    } else {
        console.log("⚠️ No es un escáner válido.");
    }
}

function enviarFax(fax) {
    if (fax instanceof Fax) {
        fax.enviarFax();
    } else {
        console.log("⚠️ No es un fax válido.");
    }
}

console.log("\n--- Pruebas de impresoras ---");
const impresoraBN = new ImpresoraBN();
const impresoraColor = new ImpresoraColor();
const multifuncion = new Multifuncion();

imprimirDocumento(impresoraBN); // Imprime B/N
imprimirDocumento(impresoraColor); // Imprime color
imprimirDocumento(multifuncion); // Imprime multifunción

escanearDocumento(multifuncion); // Escanea (multifunción)
escanearDocumento(impresoraBN); // Error: No es escáner

enviarFax(multifuncion); // Envia fax (multifunción)
enviarFax(impresoraColor); // Error: No es fax