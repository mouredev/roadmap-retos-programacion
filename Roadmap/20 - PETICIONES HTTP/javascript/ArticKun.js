
// ⚡ PETICIONES HTTP

const url = 'https://jsonplaceholder.typicode.com/todos/1';

fetch(url)
    .then( (response) =>  {
        if (!response.ok) {
            throw new Error('NETWORK RESPONSE ERROR');
        }
        return response.json();
    })
    .then( data => console.log(data) )
    .catch( error => console.log(error) );


/*

DIFICULTAD EXTRA (opcional):
     Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
     terminal al que le puedas solicitar información de un Pokémon concreto
     utilizando su nombre o número.
     - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
     - Muestra el nombre de su cadena de evoluciones
     - Muestra los juegos en los que aparece
     - Controla posibles errores

*/

    const URL = 'https://pokeapi.co/api/v2/pokemon';

    const catchPokemon = async ( number ) => {
    
      try{
        const res  = await fetch(`${URL}/${number}`)
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
    
    catchPokemon( 6 );