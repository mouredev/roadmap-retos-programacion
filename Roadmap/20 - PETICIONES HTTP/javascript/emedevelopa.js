/*Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.*/

// URL de la API pública
const url1 = 'https://jsonplaceholder.typicode.com/posts/1';

// Hacer una petición GET utilizando fetch
fetch(url1)
    .then(response => {
        // Verificar si la respuesta fue exitosa (código de estado en el rango 200-299)
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        // Parsear la respuesta como JSON
        return response.json();
    })
    .then(data => {
        // Mostrar el contenido de la respuesta en la consola
        console.log('Contenido de la web:', data);
    })
    .catch(error => {
        // Manejar cualquier error que ocurra durante la petición
        console.error('Hubo un problema con la petición fetch:', error);
    });


    /*Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */

const url = "https://pokeapi.co/api/v2/pokemon";

const getPokemon = async (number) => {
    try{
        const res  = await fetch(`${url}/${number}`)
        const data = await res.json()
    
        console.log( data ); // verificar la respuesta
    
        const{ name, id, weight, height, types, game_indices } = data
    
        console.log( 'Nombre :' , name );
        console.log( 'ID     :' , id );
        console.log( 'Peso   :' , weight );
        console.log( 'Altura :' , height );
    
        const [ type ] = types
        console.log( 'Tipo   :' , type.type.name );
    
        console.log( 'Games  :' );
        game_indices.forEach( game => {
          console.log( game.version.name );
        });
        
    
      }catch( error ){
        console.log( error );
      }
    
    };
    
    getPokemon( 61 );



