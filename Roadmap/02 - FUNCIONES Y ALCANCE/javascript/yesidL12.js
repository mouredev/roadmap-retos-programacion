// Por declaración
 function nombre(p1, p2){
    //Bloque de código
 }

 // Ejemplo

 function saludar() {
    console.log('Hola');
 }

 saludar(); // 'Hola'

 // por expresión

 let name = function(p1, p2) {
    //Bloque de código
 }

 // Ejemplo

 const saludo = function saludar() {
    console.log('Hola');
 }

 saludo(); // 'Hola'

 // funciones anonimas
// ===> son un tipo de funciones que se declaran sin definr un nombre de función, alojándolas en el interior de una variable.

const nombre = function (name) {
    console.log(name);
}

nombre('Yesid'); // 'Yesid'

// Funciones autoejecutables
// ===> Ideal para funciones que  no vas a volver a necesitar y es necesario ejecutarla inmediatamente.

(function () {
    console.log('Hola!!');
}) ();

// Clausuras Y funciones dentro de funciones
// ===> Clausura se define como una función que <<encierra>> variables en su propio ámbito.

const incr = (function () {
    let num = 0;
    return function() {
        num++;
        return num;
    }
}) ();

/** Analicemos primero lo que tenemos en este codigo:
 * Tenemos una funcón anónima que es tambien una función autoejecutable.
 * Obsrva que la función aujtoejecutable devuelve otra funcion diferente.
 * AL ejecutar la función la primera vez (autoejecutable) devolvemos esa otra función que es la que se guarda en INCR para futuras ejecuciones.
 */

// Callback
// ===> Es pasar una funcion por parametro a otra funcion de modo que esta última función puede ejecutar la función pasada por parametro de forma genérica desde su propio código, y nosotros podemos definirlas desde fuera de dicha función.

//Ejemplo,

const action = function () {
    console.log('Acción ejecutada');
}

const mainFunction = function(Callback) {
    Callback ();
}

mainFunction(action);

/** Definimos una función action que realiza una tarea.
 * Definimos una función mainFunction, que recibe como parámetro una función callback genérica.
 * Llamamos a mainFunction, pasándole como parámetro la función concreta, que en este caso es action.
 */

// Funciones de orden superior (HOF)
// ===> Son funciones que reciben por parámetro otra función y/o devuelven una función mediante el return.

const accion = function () {
    console.log('Acción ejecutada');
}

const error = function () {
    console.error('Ha ocurrido un error');
}

const doTask = function (callback, callbackError) {
    const isError = Math.random() < 0.5;

    if(!isError) callback();
    else callbackError();
}

doTask(accion, error);

// arrow Function

const func = () => {
     console.log('Arrow function');
}


//Dificultad extra
function cadenaDeTexto (str1, str2) {
    for (let numero = 1; numero < 100; numero++ ) {
        if(numero % 3 == 0 && numero % 5 == 0) {
            console.log(str1 + str2);
        } else if(numero % 3 == 0) {
            console.log(str1);
        } else if(numero % 5 == 0) {
            console.log(str2);
        } else {
            console.log(numero);
        }
    }

}

cadenaDeTexto('fizz','buzz');