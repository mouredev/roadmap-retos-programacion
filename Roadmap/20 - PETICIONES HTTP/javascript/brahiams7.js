// * EJERCICIO:
//  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
//  * una petición a la web que tú quieras, verifica que dicha petición
//  * fue exitosa y muestra por consola el contenido de la web.
//  *
const pokemon={}

fetch('https://pokeapi.co/api/v2/pokemon/1/')
    .then(response=>response.json())
    .then(data=>console.log(""))
    .catch(error=>console.log(error)
    )

// * DIFICULTAD EXTRA (opcional):
// * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
// * terminal al que le puedas solicitar información de un Pokémon concreto
// * utilizando su nombre o número.
// * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
// * - Muestra el nombre de su cadena de evoluciones
// * - Muestra los juegos en los que aparece
// * - Controla posibles errores
// *

    async function getData(pokemonId){
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId}/`);
        const data = response.json()
        return data
}
    async function showPokemon(pokemonId){
        try {
            const datos=await getData(pokemonId);
            const tipos=datos.types.map(tipo=>tipo.type.name)
            const juegos=datos.game_indices.map(juego=>juego.version.name)
            console.log(`
                Nombre: ${datos.name}
                ID: ${datos.id} 
                Weight: ${datos.weight}
                Height:${datos.height}
                Tipos: ${tipos} 
                Juegos: ${juegos}`)
        } catch (error) {
            console.log(error);
            
        }
        
        }


let readline = require('readline')
let rl = readline.createInterface({ input: process.stdin, output: process.stdout });
function findPokemon(){
    rl.question('MENU\n 1.Buscar pokemon\n 2.Salir\n',(answer)=>{
        let ans=answer.trim().toLocaleLowerCase();
        switch (ans) {
            case "1":
                rl.question("\n Ingrese el id del pokemon: ",(answer)=>{
                    let ans=answer
                    showPokemon(ans)
                    findPokemon()
                })
                break;
            default:
                rl.close()
                break;
        }
    })
}
findPokemon()