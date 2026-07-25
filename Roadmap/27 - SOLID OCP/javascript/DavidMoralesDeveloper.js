//  * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
//  * y crea un ejemplo simple donde se muestre su funcionamiento
//  * de forma correcta e incorrecta.

class CalcularAreas {
    ecuacionDeAreas(){

    }
}

class Cuadrado extends CalcularAreas{
    constructor(lado){
        super()
        this.lado=lado
        
    }
    ecuacionDeAreas(lado){
        return lado * lado
    }
}

class Circulo extends CalcularAreas{
    constructor (radio) {
        super()
        this.radio=radio
    }
    ecuacionDeAreas(radio){
        return 3.14 *radio*radio
    }
}
// esta clase es SRP 
class SumatoriaDeAreas {
    
    sumarAreas(formas){
        if(Array.isArray(formas)){
            
            return formas.reduce((num1, num2) => num1 + num2, 0)
        }else console.log("solo acepta Arr")
    }
}



const areaCuadrado = new Cuadrado()
const cuadrado1 = areaCuadrado.ecuacionDeAreas(2)
const cuadrado2 = areaCuadrado.ecuacionDeAreas(5)

const areaCirculo = new Circulo()
const circulo1 = areaCirculo.ecuacionDeAreas(5)

const sumAreas = new SumatoriaDeAreas()

const formas = [cuadrado1, cuadrado2,circulo1]
console.log(formas)
console.log(sumAreas.sumarAreas(formas))

console.log("-------------------------Extra-----------------------")

// Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
//  * Requisitos:
//  * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
//  * Instrucciones:
//  * 1. Implementa las operaciones de suma, resta, multiplicación y división.
//  * 2. Comprueba que el sistema funciona.
//  * 3. Agrega una quinta operación para calcular potencias.
//  * 4. Comprueba que se cumple el OCP.

class Calculadora {
    constructor(){

    }
    operacionesMatematicas(){

    }
}

class Suma extends Calculadora {
    constructor(num1, num2){
        super()
        this.num1 = num1
        this.num2= num2
    }

    mas (num1, num2){
        return num1 + num2
    }
    
}
class Resta extends Calculadora {
    constructor(num1, num2){
        super()
        this.num1 = num1
        this.num2= num2
    }

    menos (num1, num2){
        return num1 - num2
    }

}
class Multiplicar extends Calculadora {
    constructor(num1, num2){
        super()
        this.num1 = num1
        this.num2= num2
    }

    por (num1, num2){
        return num1 * num2
    }

}
class Dividir extends Calculadora {
    constructor(num1, num2){
        super()
        this.num1 = num1
        this.num2= num2
    }

    entre (num1, num2){
        return num1 / num2
    }

}

class Potencia extends Calculadora {
    constructor(base, exponente) {
        super();
        this.base = base;
        this.exponente = exponente;
    }
    elevar(base, exponente) {
        return Math.pow(base, exponente);
    }
}


const sumas = new Suma();
const resta = new Resta()
const multiplcacion = new Multiplicar()
const divicion = new Dividir()

console.log(sumas.mas(5,5))
console.log(resta.menos(5,5))
console.log(multiplcacion.por(5,5))
console.log(divicion.entre(5,5))