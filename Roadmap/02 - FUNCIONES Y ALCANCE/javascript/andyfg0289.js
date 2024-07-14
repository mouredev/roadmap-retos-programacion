/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

//Función básica. declarando una función 
let nombre = 'Andy Fernandez';
let edad = 35;
var color = 'rojo';
let objetos = {
    coche: 'deportivo',
    estancia: 'Motel',
    dolares: 200
}

function identidad(nombreCompleto, edad) {
    return `El usuario se llama ${nombreCompleto} y tiene ${edad} años de edad`;
}

console.log(identidad(nombre, edad));
console.log('\n');

function cambioIdentidad(nombreCompleto, edad, color) {
    //Solo modifica los datos de las variables de forma local
    nombreCompleto = 'Martin Pérez';
    edad = 25;
    color = 'verde';
    return `El usuario se llama ${nombreCompleto} y tiene ${edad} años de edad y le gusta el color ${color}`;

}

console.log(cambioIdentidad(nombre, edad, color));//El usuario se llama Martin Pérez y tiene 25 años de edad
console.log(`El usuario se llama realmente ${nombre}y tiene ${edad} años de edad`);
console.log('\n');

function masDatos(datos) {
    this.dolares = 100;

    return `El usuario maneja un ${datos.coche} y se esta quedando en un ${datos.estancia} de ${this.dolares} dólares`;
}

console.log(masDatos(objetos));

//console.log(`El usuario evito pagar un ${datos.estancia} de ${datos.dolares} de renta`);// Solo se puede acceder a datos desde la funcion masDatos
console.log(`El usuario evito pagar un ${objetos.estancia} de ${objetos.dolares} dólares de renta`);
console.log('\n');

/////Expresiones function

const mayorDedad = function (edad) {
    if (edad < 18) {
        return 'Eres menor de edad';
    } else {
        return 'Eres mayor de edad';
    }
}

console.log(mayorDedad(edad));//eres mayor de edad

///Expresión función con nombre


const hacerMayor = function menor(edad) {
    if (edad <= 18) {

        edad = menor(edad + 1);
    }
    return edad;
}

console.log("Te hiciste mayor ahora tienes " + hacerMayor(9) + "años de edad.");
console.log('\n');

//Función que recibe como parámetro otra función

let array = [1, 2, 3, 4, 5, 6, 7, 8, 9];

function fun(x) {
    return x * 2;
}

function map(f, a) {
    let result = [];
    for (let i = 0; i < a.length; i++) {
        result[i] = f(a[i]);
    }
    return result

}

console.log(map(fun, array));//(9) [2, 4, 6, 8, 10, 12, 14, 16, 18]

//  Recursividad 

let access = false;
let pass = 123456;
let keys = 3;

function checkUser() {
    let password = prompt("Introduce el password");
    if (pass == password && password !== "" && keys >= 0) {
        access = true;
        console.log("Puedes acceder");
        alert("Puedes acceder");
    } else if (keys === 0) {
        console.log("Agotado el máximo de intentos, vuelva a intentarlo más tarde");
        return alert("Agotado el máximo de intentos, vuelva a intentarlo más tarde");
    } else {
        alert("Password incorrecto");
        console.log("Acceso denegado, Password incorrecto");
        keys--;
        console.log(keys);
        checkUser();
    }
}
//DESCOMENTAR PARA PROGAR EL CODIGO
//checkUser();

//Ambito con funcion anidada

function getData() {

    let yob = 1989;

    function tellme() {
        return nombre + " tiene " + edad + " años y nació en " + yob;
    }
    return tellme()
}

console.log(getData());//Andy Fernández tiene 35 y nació en1989
console.log('\n');

function getName(name) {
    function getAge(age) {
        return name + " " + age;
    }
    return getAge;
}

giveName = getName(nombre);//Aqui definimos name con el valor nombre
giveAge = giveName(edad); //Aqui ya que name = nombre por lo tanto age = edad

console.log(giveAge);// Andy Fernández 35
console.log(getName(nombre)(edad));// Andy Fernández 35
console.log('\n');

//Funciones multianidadas 

function salario(num1) {
    let clave = 123;
    //console.log(clave2);// Da error ya que no se puede acceder a la funcion interna de  vacaciones()
    function vacaciones(num2) {//permanece privado para salario
        let clave2 = 456;
        // console.log(clave3);// Da error ya que no se puede acceder a la funcion interna de  tiempoExtra()
        console.log(clave)// Puede acceder a salario ya que tiene un cierre con este 
        function tiempoExtra(num3) {//permanece privado para salario y vacaciones
            console.log(clave)// 123 // Si puede acceder a las variables de funciones exteriores ya que crea un cierre de vacaciones y salario
            console.log(clave2)// 456
            let clave3 = 789;
            console.log(num1 + num2 + num3);
        }
        tiempoExtra(3);
    }
    vacaciones(2);
}
salario(1); //6

//Funciones con parámetros predeterminados

let phone;

function tellPhone(number = 911) {
    return number;
}

console.log(tellPhone());

//Funciones con parámetros rest

function resto(resto, ...numbers) {
    return numbers.map((n) => resto - n);
}

let num = resto(10, 5, 4, 2);//A 10 le vamos restando numbers en cada caso
console.log(num);// [5,6,8]

//Funciones flecha

const saludo = ((nombre, edad) => {
    console.log(`Hola ${nombre} de ${edad} años.`)
})

saludo(nombre, edad);

//Ejemplo de función ya creada en el lenguaje
const float = 12.4;

console.log(parseFloat(float));//12.4

/*  * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. */

function numCounter(cadena1, cadena2) {
    let count = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(i + ' ' + cadena1 + ' y ' + cadena2);
        } else {
            if (i % 3 === 0) {
                console.log(i + ' ' + cadena1);
            } else if (i % 5 === 0) {
                console.log(i + ' ' + cadena2);
            } else {
                count++;
                console.log(i + ' ' + count);

            }
        }
    }
    return count;
}

console.log(numCounter('es múltiplo de 3', 'es múltiplo de 5'));