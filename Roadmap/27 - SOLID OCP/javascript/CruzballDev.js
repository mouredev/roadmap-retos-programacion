/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
*/

// EJEMPLO INCORRECTO

const cliente = {tipo: ""}

function calcularDescuento(cliente, tipo,  precio) {
    cliente.tipo = tipo

    if(cliente.tipo === "normal") {
        return precio * 0.05;
    }

    if(cliente.tipo === "premium") {
        return precio * 0.20;
    }

    if(cliente.tipo === "vip") {
        return precio * 0.30;
    }

    console.log(`¡El tipo de cliente ${cliente.tipo} no existe!\n¡Intentalo de nuevo!`)
    return 0
    
}

console.log(calcularDescuento(cliente, "normal", 100))
console.log(calcularDescuento(cliente, "premium", 100))
console.log(calcularDescuento(cliente, "vip", 100))
console.log(calcularDescuento(cliente, "basico", 100))


// EJEMPLO CORRECTO

class Descuento {
    calcular(precio) {
        throw new Error("El método calcular debe implementarse.")
    }
}


class DescuentoNormal  extends Descuento {

    calcular(precio) {
            return precio * 0.05;
    }

}

class DescuentoPremium  extends Descuento {

    calcular(precio){
        return precio * 0.20;
    }

}

class DescuentoVip  extends Descuento {


    calcular(precio){
        return precio * 0.30;
    }
}


// Composición: La composición significa que un objeto contiene o utiliza otro objeto para realizar parte de su trabajo.
// Aquí CalcularDescuento compone su comportamiento utilizando descuento.
// Conceptualmente: CalcularDescuento ->  tiene/utiliza -> descuento
class CalcularDescuento {

    constructor(descuento) {
        this.descuento = descuento;
    }

    calcular(precio) {
            return this.descuento.calcular(precio)
    }
}


const descuento1 = new CalcularDescuento(new DescuentoNormal())
const descuento2 = new CalcularDescuento(new DescuentoPremium())
const descuento3 = new CalcularDescuento(new DescuentoVip ())
console.log(descuento1.calcular(100))
console.log(descuento2.calcular(100))
console.log(descuento3.calcular(100))


/*
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
*/


class OperacionMatematica {
    operacion(a, b) {
        throw new Error("Debe contener el método operación.")
    }
}

class Sumar extends OperacionMatematica {
    operacion(a,b) {
        return a + b
    }
}

class Restar extends OperacionMatematica {
    operacion(a, b) {
        return a - b
    }
}

class Multiplicar extends OperacionMatematica {
    operacion(a, b) {
        return a * b
    }
}

class Dividir extends OperacionMatematica {
    operacion(a, b) {
        return a / b
    }
}

class Potencia extends OperacionMatematica {
    operacion(a, b) {
       return a ** b
    }
}

class Calculadora {
    constructor(objetoCreado) {
        this.objetoCreado = objetoCreado
    }

    operacion(a, b) {
        return this.objetoCreado.operacion(a, b)
    }
}

const suma = new Calculadora(new Sumar())
console.log(suma.operacion(5, 2))

const resta = new Calculadora(new Restar())
console.log(resta.operacion(5, 2))

const multiplicacion = new Calculadora(new Multiplicar())
console.log(multiplicacion.operacion(5, 2))

const division = new Calculadora(new Dividir())
console.log(division.operacion(5, 2))

const potencia = new Calculadora(new Potencia())
console.log(potencia.operacion(5, 2))