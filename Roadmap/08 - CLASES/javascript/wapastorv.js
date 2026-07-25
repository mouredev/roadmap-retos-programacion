/*
EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (en javascript).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
*/
/* ¿Que es una clase?
    Una clase es un modelo que define un conjunto de atributos y métodos que tendrán los objetos que se creen a partir de ella.

    Ejemplo:
*/
class Persona{
    constructor(nombre, edad, sexo) {
        //Propiedades de la clase
        // el this hace referencia al objeto que se está creando a partir de la clase, en este caso, Persona
        // this.nombre, this.edad y this.sexo son atributos de la clase Persona
        // nombre, edad y sexo son los parámetros que recibe el constructor
        /* el metodo constructor es un método especial que se ejecuta automaticamente al crear una nueva instancia de la clase. 
        Se inicializan los atributos de la clase con los valores que se pasan como parámetros*/
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
    }
    /*Método de la clase
        Un método es una función que pertenece a un objeto, en este caso, a la clase Persona.
        En este caso, el método saludar() imprime un mensaje con los atributos de la clase Persona
    */
    saludar(){
        console.log(`Hola, mi nombre es ${this.nombre}, tengo ${this.edad} años y soy ${this.sexo}`);
    }
}

//Creación de un objeto a partir de la clase Persona
const persona1 = new Persona('Juan', 30, 'Hombre');
persona1.saludar(); //la salida será: Hola, mi nombre es Juan, tengo 30 años y soy Hombre

// Modificación de los atributos del objeto persona1
persona1.nombre = 'Maria';
persona1.edad = 25;
persona1.sexo = 'Mujer';
persona1.saludar(); //la salida será: Hola, mi nombre es Maria, tengo 25 años y soy Mujer

//Creación de un nuevo objeto a partir de la clase Persona
const persona2 = new Persona('Pedro', 40, 'Hombre');
persona2.saludar(); //la salida será: Hola, mi nombre es Pedro, tengo 40 años y soy Hombre

/* Herencia en clases:
    La herencia es un mecanismo que permite que una clase (clase hija) herede los atributos y métodos de otra clase (clase padre).
    En javascript, la herencia se logra utilizando la palabra clave extends.
    Ejemplo:
*/
class Empleado extends Persona{
    constructor(nombre, edad, sexo, salario){
        //El método super() se utiliza para llamar al constructor de la clase padre (Persona)
        super(nombre, edad, sexo);
        this.salario = salario;
    }
    //Método de la clase Empleado
    mostrarSalario(){
        console.log(`Mi salario es de ${this.salario}`);
    }
}

//Creación de un objeto a partir de la clase Empleado
const empleado1 = new Empleado('Carlos', 35, 'Hombre', 2000);
empleado1.saludar(); //la salida será: Hola, mi nombre es Carlos, tengo 35 años y soy Hombre
empleado1.mostrarSalario(); //la salida será: Mi salario es de 2000

/* Método Estático: 
    Un método estático es un método que pertenece a la clase en lugar de a los objetos creados a partir de ella.
    Para definir un método estático, se utiliza la palabra clave static.
    Ejemplo:
*/
class Calculadora{
    //Método estático de la clase Calculadora
    static sumar(a, b){
        return a + b;
    }
    static restar(a, b){
        return a - b;
    }
    static multiplicar(a, b){
        return a * b;
    }
}
console.log(Calculadora.sumar(5, 3)); //la salida será: 8
console.log(Calculadora.restar(5, 3)); //la salida será: 2
console.log(Calculadora.multiplicar(5, 3)); //la salida será: 15

/* Getter y Setter:
    Los métodos getter y setter son métodos especiales que se utilizan para obtener y establecer el valor de un atributo de un objeto.
    Para definir un getter o un setter, se utiliza la palabra clave get o set, respectivamente.
    Ejemplo:

*/
class Rectangulo{
    constructor(base, altura){
        this.base = base;
        this.altura = altura;
    }
    //Getter para obtener el área del rectángulo
    get area(){
        return this.base * this.altura;
    }
    //Setter para establecer la base del rectángulo
    set nuevaBase(base){
        this.base = base;
    }
    //Setter para establecer la altura del rectángulo
    set nuevaAltura(altura){
        this.altura = altura;
    }
}

const rectangulo = new Rectangulo(5, 3);
console.log(rectangulo.area); //la salida será: 15
rectangulo.nuevaBase = 10;
rectangulo.nuevaAltura = 6;
console.log(rectangulo.area); //la salida será: 60

/* Encapsulamiento 
    El encapsulamiento es un concepto que se refiere a la ocultación de los detalles de implementación de un objeto y la exposición de una interfaz para interactuar con él.
    En javascript, el encapsulamiento se logra utilizando métodos getter y setter para acceder a los atributos de un objeto.
    Ejemplo:
 
*/
class Banco {
    #saldo; //Atributo privado
    constructor(saldoInicial){
        this.#saldo = saldoInicial;
    }
    depositar(monto){
        this.#saldo += monto;
        console.log(`Se depositaron ${monto} dólares. Saldo actual: ${this.#saldo} dólares`);
    }

    retirar(monto){
        if(monto <= this.#saldo){
            this.#saldo -= monto;
            console.log(`Se retiraron ${monto} dólares. Saldo actual: ${this.#saldo} dólares`);
        } else {
            console.log('Fondos insuficientes');
        }
    }
}

const cuenta = new Banco(1000);
cuenta.depositar(500); //la salida será: Se depositaron 500 dólares. Saldo actual: 1500 dólares
cuenta.retirar(200); //la salida será: Se retiraron 200 dólares. Saldo actual: 1300 dólares
cuenta.retirar(1500); //la salida será: Fondos insuficientes

/* Polimorfismo:
    El polimorfismo permie que un objeto pueda comportarse de diferentes maneras según el contexto en el que se encuentre.
    En javascript, el polimorfismo se logra al redefinir un método en una clase hija.
    Ejemplo:
*/
class Figyra{
    calcularArea(){
        return 0; //Método a ser redefinido en las clases hijas
    }
}
class Cuadrado extends Figyra{
    constructor(lado){
        super();
        this.lado = lado;
    }
    calcularArea(){
        return this.lado * this.lado;
    }
}
class Circulo extends Figyra{
    constructor(radio){
        super();
        this.radio = radio;
    }
    calcularArea(){
        return Math.PI * this.radio * this.radio;
    }
}
const cuadrado = new Cuadrado(5);
console.log(`El Area del cuadrado es: ${cuadrado.calcularArea()}`); //la salida será: 25

const circulo = new Circulo(3);
console.log(`El Area del Circulo es: ${circulo.calcularArea()}`); //la salida será: 28.274333882308138

