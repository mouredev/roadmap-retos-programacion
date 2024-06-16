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

// Comprobando si existe
console.log(conectarSingleton === desconectarSingleton);


/**-----DIFICULTAD EXTRA-----*/

//  Creo la clase para la sesión de usuario
class userLogin {
    constructor(){
        if (!!userLogin.instance) {   // Aquí compruebo si existe la instancia
            return userLogin.instance;
        }

        this.user = null;   // Aun no se agrega nada entonces los dejo vació
        userLogin.instance = this;  // Instanciando la clase si tiene datos

        return this;
    }

    //  Guardo los datos este método
    setUser(id, username, name, email){
        this.user = { id, username, name, email }
    }

    //  Este método retorno los que se guardo
    getUser(){
        return this.user;
    }

    //  Limpio todo de la instancia
    clearUser(){
        this.user = null;
    }
}

//  Ejemplo de las instancia de sesión de usuario
//  Creo la instancia por primera vez
session1 = new userLogin();
session1.setUser(1,"JesusA", "Jesus Antonio", "jesus@hola.com");
console.log(session1.getUser());

//  Se vuelve a crear la instancia pero ya existe
session2 = new userLogin();
console.log(session2.getUser());

//  Limpiando la instancia
session3 = new userLogin();
session3.clearUser();


/**-----DIFICULTAD EXTRA-----*/