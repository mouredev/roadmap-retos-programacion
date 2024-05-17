
//! funciones

//! Funciones de declaracion y alcance global sin retorno
let name = "alejandro"; //! variable con alcance global
function saludar() {
    console.log(`Bienvenido, ${name}`);
}
saludar();
//! con retorno
function isActive() {
    let userActive = true;
    return userActive;
} 
//console.log(userActive); //! not defined ya que userActive es de alcance local
console.log("user is active", isActive());

//! con parametros
let user = {
    firstName: "Hector Alejandro",
    lastName: "Toro Bernal",
    age: 29,
    hobbies: ["estudiar","videojuegos","leer","musica"]
}

function userList(user) {
    console.log("muestro el parametro user", user);
}
userList(user);

//! funciones de expresión
/**
 * Otra manera de definir funciones, la cual podemos asignarlas a variables
 */

const getAgeUser = function(user) {
    return `La edad del usuario -> ${user.age}`;
}
console.log(getAgeUser(user));

//! funciones de flecha -> arrow fuction
const newUser = (user) => {
    return user.firstName;
}
console.log("Se crea el nuevo usuario " + newUser(user));

//! metodos de objetos
let userTwo = {
    firstName: "Sebastian",
    lastName: "Rodriguez",
    age: 29,
    hobbies: ["estudiar","videojuegos","leer","musica"],
    saludar() {
        return `Soy el usuario ${this.firstName}`;
    }
}
console.log(userTwo.saludar());

//! funciones que crea otra funcion

function sum (a) {
    return (b) => {
        return a + b;
    }
}

const sumar = sum(2);
console.log("suma creada en una funcion que crea otra funcion ",sumar(3));

//! EJERCICIO EXTRA

const printText = (a,b) => {
    let i = 1;
    while( i <= 100 ) {
        
        if( i % 3 == 0 ) console.log(a);
        if( i % 5 == 0 ) console.log(b);
        if( i % 3 == 0 && i % 5 == 0 ) console.log(`${a} - ${b}`);
        console.log(i);
        i++;
    }
} 

printText("hola","adios");

