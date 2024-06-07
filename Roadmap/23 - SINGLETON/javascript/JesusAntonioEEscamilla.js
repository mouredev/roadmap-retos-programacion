/** #23 - JavaScript ->Jesus Antonio Escamilla */

/**
 * El patrón Singleton es uno de los patrones de diseño más utilizados en la industria del desarrollo de software.
 * Singleton es un patrón de diseño creacional que nos permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia.
 * El patrón de diseño Singleton se utiliza cuando solo se necesita una instancia de una clase en toda la aplicación.
*/

//---EJERCIÓ---
// Aquí tenemos una clase para usar el Patron de Diseño Singleton
class Singleton {
    // Se usa un constructor que valida si ya fue instanciado o no
    constructor() {
    if (!!Singleton.instance) {
        return Singleton.instance;
    }

    // Inicializa las propiedades de la clase aquí
    // Las propiedades pueden cambiar
    this.someProperty = 'someValue';

    // Retornamos la instancia creada
    // Una vez instanciada no se puede volver a instancia o crear nueva
    Singleton.instance = this;
    }

    // Un método de la clase
    someMethod() {
    console.log('Hola, soy un método del Singleton y ya fue creado.');
    }
}

// Ejemplos del Patron de Diseño Singleton
const conectarSingleton = new Singleton();
conectarSingleton.someMethod();
console.log(conectarSingleton.someProperty);

const desconectarSingleton = new Singleton();
desconectarSingleton.someMethod();
desconectarSingleton.someProperty = 'newSomeValue';
console.log(desconectarSingleton.someProperty);



/**-----DIFICULTAD EXTRA-----*/

//  Pendiente

/**-----DIFICULTAD EXTRA-----*/