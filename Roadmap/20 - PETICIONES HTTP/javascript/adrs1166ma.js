/* 🔥 EJERCICIO:
Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
una petición a la web que tú quieras, verifica que dicha petición
fue exitosa y muestra por consola el contenido de la web.
*/
// Fetch API con Promises - No requeriere de una funcion
const url = 'https://jsonplaceholder.typicode.com/comments'


// status : 200 , quiere decir que Si lo encontro
// status : 404 , quiere decir que No lo encontro
fetch(url)
    .then((response) => {
        if(response.ok){
            return response.json()
        }
        throw new Error('Hubo un error...') // el error para al CATCH
    })
    .then(data=>{
        console.log(data)
    })
    // Captura si hay error de red.
    // ejm: no hay conexion a wifi
    .catch(error => {
        console.log(error.message)
    })
    
    // en flecha
    // .then(data=> console.log(data))
    // .catch(error => console.log(error.message))
    
// (500) [{…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, …]



/*🔥 DIFICULTAD EXTRA (opcional): ------------------------------------------------------------------------------------------------------------------------------------
Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
terminal al que le puedas solicitar información de un Pokémon concreto
utilizando su nombre o número.
- Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
- Muestra el nombre de su cadena de evoluciones
- Muestra los juegos en los que aparece
- Controla posibles errores
*/

// Función para obtener información de un Pokémon usando fetch
function obtenerInfoPokemon(nombreOId) {
    const url = `https://pokeapi.co/api/v2/pokemon/${nombreOId}`;

    fetch(url)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error ${response.status}: ${response.statusText}`);
            }
            return response.json();
        })
        .then(async (pokemon) => {
            // Extraer información básica del Pokémon
            const nombre = pokemon.name;
            const id = pokemon.id;
            const peso = pokemon.weight;
            const altura = pokemon.height;
            const tipos = pokemon.types.map(tipo => tipo.type.name);
            const juegos = pokemon.game_indices.map(juego => juego.version.name);

            // Consultar la cadena de evoluciones
            const especieResponse = await fetch(pokemon.species.url);
            if (!especieResponse.ok) {
                throw new Error(`Error al obtener la especie del Pokémon.`);
            }
            const especie = await especieResponse.json();

            const cadenaEvolucionesResponse = await fetch(especie.evolution_chain.url);
            if (!cadenaEvolucionesResponse.ok) {
                throw new Error(`Error al obtener la cadena de evoluciones.`);
            }
            const cadenaEvoluciones = await cadenaEvolucionesResponse.json();

            const nombreCadenaEvoluciones = cadenaEvoluciones.chain.species.name;

            // Mostrar la información
            console.log(`Nombre: ${nombre}`);
            console.log(`ID: ${id}`);
            console.log(`Peso: ${peso}`);
            console.log(`Altura: ${altura}`);
            console.log(`Tipos: ${tipos.join(", ")}`);
            console.log(`Cadena de evoluciones: ${nombreCadenaEvoluciones}`);
            console.log(`Juegos en los que aparece: ${juegos.join(", ")}`);
        })
        .catch((error) => {
            console.error("Ocurrió un error:", error.message);
        });
}


const args = process.argv.slice(2);
if (args.length === 0) {
    console.log("Uso: node script.js <nombre_o_id>");
} else {
    const nombreOId = args[0];
    obtenerInfoPokemon(nombreOId);
}
// node nombreDeArchivo.js pikachu

// Nombre: pikachu
// ID: 25
// Peso: 60
// Altura: 4
// Tipos: electric
// Cadena de evoluciones: pichu
// Juegos en los que aparece: red, blue, yellow, gold, silver, crystal, ruby, sapphire, emerald, firered, leafgreen, diamond, pearl, platinum, heartgold, soulsilver, black, white, black-2, white-2