/** #20 - JavaScript ->Jesus Antonio Escamilla */

/**
 * Una función de callback es una función que se pasa a otra función como un argumento, que luego 
    se invoca dentro de la función externa para completar algún tipo de rutina o acción.
 * Es aquella que es pasada como argumento a otra función para que sea "llamada de nuevo" (call back)
    en un momento posterior. 
*/

//---EJERCIÓ---
// Aquí podemos ver un ejemplo con tiempo
// Hacemos una función que retorne en consola
function saludar(data) {
    console.log(data);
}

// Creamos el CALLBACK que retornara un texto para imprimirlo en consola
function fetchData(name ,callback) {
    setTimeout(() => {
        const responder = `Hola soy, ${name}`;
        callback(responder);    //Aquí vemos como retorna la función CallBack
    }, 2000);
}

// Aquí solo llamamos el CALLBACK
fetchData('Jesus Antonio', saludar);


// También podemos crear primero el Callback con una suma de números
function sum(a, b, callback) {
    const resultado = a + b;
    callback(resultado);    //Aquí vemos como retorna la función CallBack
}

// Después el torno del Callback a la consola
function printSum(resultado) {
    console.log('El resultado es:', resultado)
}

// Aquí solo llamamos el CALLBACK
sum(3,6,printSum);



/**-----DIFICULTAD EXTRA-----*/

//Pendientes

/**-----DIFICULTAD EXTRA-----*/