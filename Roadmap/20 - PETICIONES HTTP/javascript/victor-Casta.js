const readline = require('readline')
/*
  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
  * una petición a la web que tú quieras, verifica que dicha petición
  * fue exitosa y muestra por consola el contenido de la web.
*/

fetch('https://api.escuelajs.co/api/v1/products')
  .then(response => {
    if (!response.ok) {
      throw new Error('Error en la petición');
    }
    return response.json();
  })
  .then(data => console.log( /*data*/))
  .catch(error => console.error('Error en la petición:', error));

/*
  * DIFICULTAD EXTRA (opcional):
  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
  * terminal al que le puedas solicitar información de un Pokémon concreto
  * utilizando su nombre o número.
  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
  * - Muestra el nombre de su cadena de evoluciones
  * - Muestra los juegos en los que aparece
  * - Controla posibles errores
*/

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question('Escribe el nombre o id de un pokémon: ', userData => {
  const nameOfPokemon = userData
  fetch(`https://pokeapi.co/api/v2/pokemon/${nameOfPokemon}/`)
    .then(response => response.json())
    .then(data => {
      console.log(`Nombre: ${data.name}`)
      console.log(`Id: ${data.id}`)
      console.log(`Peso: ${data.weight}`)
      console.log(`Altura: ${data.height}`)
      console.log('Tipos:')
      data.types?.map((item, index) => {
        console.log(`Tipo ${index}: ${item.type.name}`)
      })
      console.log('Juegos:')
      data.game_indices?.map(item => {
        console.log(
          `Indice de Juego: ${item.game_index}, Nombre del Juego: ${item.version.name}`
        )
      })
    })
    .catch(error => console.error(error))
  rl.close()
})