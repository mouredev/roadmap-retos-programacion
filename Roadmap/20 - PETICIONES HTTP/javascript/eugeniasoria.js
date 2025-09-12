/*
# #20 PETICIONES HTTP
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */


async function fetchSomething() {
  console.log("Peticion cualquiera");
  const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");
  const result = await response.json();
  console.log(result);
}

/* DIFICULTAD EXTRA (opcional):
* Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
* terminal al que le puedas solicitar información de un Pokémon concreto
* utilizando su nombre o número.
* - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
* - Muestra el nombre de su cadena de evoluciones
* - Muestra los juegos en los que aparece
* - Controla posibles errores
*/

async function quienEsEsePokemon(pokemonName) {  
  if (!pokemonName) {
    error = new Error('Ingrese un nombre de Pokemon');
    throw error;
  }
    
  try {    
    const response = await fetch("https://pokeapi.co/api/v2/pokemon/" + pokemonName);
    console.log("\n\nQuién es ese Pokemon?")
    const {name, id, weight, height, types, game_indices} = await response.json();
    console.log(`Pokemon: ${name}`);
    console.log(` >Id: ${id}`);
    console.log(` >Peso: ${weight}`);
    console.log(` >Altura: ${height}`);
    console.log(` >Tipos: ${JSON.stringify(types)}`);    

    const responseChain = await fetch("https://pokeapi.co/api/v2/pokemon-species/" + id);
    const {evolution_chain} = await responseChain.json();
    
    const responseEvolutionChain = await fetch(evolution_chain.url);
    
    const evolutionChain = await responseEvolutionChain.json();
    console.log(" >Cadena de evolucion: ", JSON.stringify(evolutionChain.chain));
    console.log(" >Juegos: ", game_indices);

  } catch (error) {
    console.error(error.message);
  }    
}      

/*Ejecucion*/
async function main() {
  await fetchSomething();
  await quienEsEsePokemon('oshawott');  
}

main()
