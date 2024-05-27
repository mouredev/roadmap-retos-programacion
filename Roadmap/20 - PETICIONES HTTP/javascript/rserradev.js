// Ejercicio

url = "https://moure.dev";

fetch(url)
  .then(response => response.text())
  .then(data => {
    console.log(data);
  })
  .catch(error => console.log(error));

// Ejercicio extra

url = 'https://pokeapi.co/api/v2/';

let pokemonName = "ditto";

const getPokemonData = async() => {
  try {
    const response = await fetch(`${url}pokemon/${pokemonName}`);
    if (!response.ok) {
      throw new Error("Error al obtener la información del pokemon");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
}

let dataApi;

getPokemonData()
  .then(data => {
    const dataApi = data;

    const {name, weight, height, types} = dataApi;

    // Nombre
    console.log("Nombre del pokemon: " + name);

    // Id
    console.log("Id del pokemon: " + dataApi.id);
    // Peso
    console.log("Peso del pokemon: " + weight);
    // Altura
    console.log("Altura del pokemon: " + height);
    
    // Tipo
    console.log("Tipo del pokemon: " + types[0].type.name);

    // Cadena de evolucion
    

    let games = [];
    //Juegos en los que aparece el pokemon
    for (let i = 0; i < dataApi.game_indices.length; i++) {
      games.push(dataApi.game_indices[i].version.name);
    }

    console.log("Juegos en los que aparece el pokemon: " + games);

});