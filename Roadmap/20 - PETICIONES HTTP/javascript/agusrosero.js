/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 */
const url = "https://google.com";

fetch(url)
  .then((response) => {
    if (response.ok) {
      return response.text();
    } else {
      throw new Error("Network response was not ok.");
    }
  })
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.log("Error:", error);
  });

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
const pokeapiUrl = "https://pokeapi.co/api/v2";

const getPokemon = async (name) => {
  try {
    const response = await fetch(`${pokeapiUrl}/pokemon/${name}`);
    if (response.ok) {
      const data = await response.json();
      return data;
    }
  } catch (error) {
    console.log(error);
  }
};

getPokemon("gengar").then((data) => {
  const dataApi = data;
  const { name, weight, height, types } = dataApi;
  console.log("Nombre: " + name);
  console.log("Id: " + dataApi.id);
  console.log("Peso: " + weight);
  console.log("Altura: " + height);
  console.log("Tipo: " + types[0].type.name);

  const games = [];
  for (let i = 0; i < dataApi.game_indices.length; i++) {
    games.push(dataApi.game_indices[i].version.name);
  }
  console.log("Juegos: " + games);
});
