/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 */




fetch('https://jsonplaceholder.typicode.com/postss/1')
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al realizar la petición: ' + response.status 
                + ' ' + response.statusText) ;
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.log('Error: ' + error);
    });