/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */

// INCORRECTA

class Empleado {
    constructor() {
        if (this.constructor === Empleado) {
            throw new Error('No puedes instanciar una interfaz');
        }
    }
    calcularSalario() {
        throw new Error('Debe implementar el método calcular salario')
    }

    programarReunion() {
        throw new Error('Debe implementar el método programar reunión')
    }
}


class Obrero extends Empleado {

    calcularSalario() {
        return 1000;
    }
}

const empleado = new Obrero();
console.log(empleado.calcularSalario());
console.log(empleado.programarReunion());

// CORRECTA
class CalculadoraSalario {
    calcularSalario() {}
}

class ProgramadorReuniones {
    programarReunion(){}
}

class ObreroISP extends CalculadoraSalario {
    calcularSalario() {}
}

const empleadoISP = new ObreroISP();
console.log(empleadoISP.calcularSalario());


console.log('---------DIFICULTAD EXTRA-------------');

// * DIFICULTAD EXTRA (opcional):
// * Crea un gestor de impresoras.
// * Requisitos:
// * 1. Algunas impresoras sólo imprimen en blanco y negro.
// * 2. Otras sólo a color.
// * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
// * Instrucciones:
// * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
// * 2. Aplica el ISP a la implementación.
// * 3. Desarrolla un código que compruebe que se cumple el principio.
// */


class GestorImpresorasBN {
    constructor() {
        if (this.constructor === GestorImpresorasBN) {
            throw Error('No puede instanciar una interfaz');
        }
    }

    imprimirBN() {
        throw Error('Debe implementar imprimirBN')
    }
}

class GestorImpresorasColor {
    constructor() {
        if (this.constructor === GestorImpresorasColor) {
            throw Error('No puede instanciar una interfaz');
        }
    }

    imprimirColor() {
        throw Error('Debe implementar imprimirColor')
    }
}

class GestorImpresorasMulti {
    constructor() {
        if (this.constructor === GestorImpresorasMulti) {
            throw Error('No puede instanciar una interfaz');
        }
    }

    imprimir() {
        throw Error('Debe implementar imprimir')
    }

    escanear() {
        throw Error('Debe implementar escanear')
    }

    enviarFax() {
        throw Error('Debe implementar enviarFax')
    }
}

class ImpresoraBN extends GestorImpresorasBN {
    imprimirBN() {
        console.log('imprimiendo en bn');
    }
}

class ImpresoraColor extends GestorImpresorasColor {
    imprimirColor() {
        console.log('imprimiendo en color');
    }
}

class ImpresoraMulti extends GestorImpresorasMulti {
    imprimir() {
        console.log('imprimiendo');
    }

    escanear() {
        console.log('escaneando');
    }

    enviarFax() {
        console.log('enviando fax');
    }
}

const impresoraBN = new ImpresoraBN();
impresoraBN.imprimirBN();

const impresoraColor = new ImpresoraColor();
impresoraColor.imprimirColor();

const impresoraMulti = new ImpresoraMulti();
impresoraMulti.imprimir();
impresoraMulti.escanear();
impresoraMulti.enviarFax();