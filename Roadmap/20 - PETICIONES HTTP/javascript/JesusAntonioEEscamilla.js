/** #20 - JavaScript ->Jesus Antonio Escamilla */

const { error } = require("console");

/**
 * HTTP define un conjunto de métodos de petición para indicar la acción que se desea realizar para un recurso determinado.
 * La API Fetch proporciona una interfaz JavaScript para acceder y manipular partes del canal HTTP, tales como peticiones y respuestas.
 */

//---EJERCIÓ---
// URL donde se utilizara las peticiones
const url = 'https://jsonplaceholder.typicode.com/posts/1';

// Realizaron las peticiones HTTP
fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('La respuesta de NETWORK no fue correcta' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Hubo un error con la peticiones fetch:', error);
    });



/**-----DIFICULTAD EXTRA-----*/

//Pendiente

/**-----DIFICULTAD EXTRA-----*/