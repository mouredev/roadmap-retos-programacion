/** #26 - JavaScript -> Jesus Antonio Escamilla */

/**
 * Los principios SOLID son un conjunto de cinco principios de diseño orientados a objetos que buscan hacer
    el software más comprensible, flexible y mantenible.
 * Principio de Responsabilidad Única (Single Responsibility Principle - SRP)
 * Una clase debe tener una, y solo una, razón para cambiar. En otras palabras, una clase debe tener una 
    única responsabilidad o propósito.
 */

//---EJERCIÓ---
// INCORRECTA
class User_Incorrecto{
    constructor(nombre, email){
        this.nombre = nombre,
        this.email = email
    };

    getUserData(){
        return{
            nombre: this.nombre,
            email: this.email
        };
    }

    saveToDatabase(){
        console.log(`Guardando el usuario ${this.nombre} en la base de datos`);
    }
}

// Uso del ejemplo Incorrecto
const user1 = new User_Incorrecto('Jesus', 'jesus_20@gmail.com');
console.log(user1.getUserData());
user1.saveToDatabase();

// CORRECTO
class User_Correcto{
    constructor(nombre, email){
        this.nombre = nombre;
        this.email = email;
    }

    getUserData(){
        return{
            nombre: this.nombre,
            email: this.email
        };
    }
}

class UserRepository{
    saveToDatabase(user){
        console.log(`Guardando el usuario ${user.nombre} en la base de datos`);
    }
}

// Uso de Ejemplo Correcto
const user = new User_Correcto('Antonio', 'antonio_25@hotmail.com');
console.log(user.getUserData());

const userRepository = new UserRepository();
userRepository.saveToDatabase(user);



/**-----DIFICULTAD EXTRA-----*/

// Pendiente

/**-----DIFICULTAD EXTRA-----*/