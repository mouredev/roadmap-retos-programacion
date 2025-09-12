/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#20 PETICIONES HTTP
---------------------------------------
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
// ________________________________________________________

import fetch from "node-fetch";

async function getUser(userId) {
    try {
        const url = `https://jsonplaceholder.typicode.com/users/${userId}`;
        const response = await fetch(url);

        if (response.ok) {
            return await response.json();
        } else {
            console.log(`Id: ${userId} no encontrado`);
            console.log("status_code: ", response.status);
            return {};
        }
    } catch (error) {
        console.error("Error de conexión:", error.message);
        return {};
    }
}

function printUser(userData) {
    if (Object.keys(userData).length > 0) {
        console.log(`\nUsuario con id: '${userData.id}':\n` +
            `Nombre:  ${userData.name}\n` +
            `Usuario: ${userData.username}\n` +
            `Email:   ${userData.email}\n` +
            `Teléfono: ${userData.phone}`);
    }
}

// ________________________________________________________
// DIFICULTAD EXTRA

class GetPokemon {
    constructor() {
        this.baseUrl = "https://pokeapi.co/api/v2/pokemon/";
        this.pokemon = null;
    }

    async load(id) {
        try {
            const url = `${this.baseUrl}${id}`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`Pokémon '${id}' no encontrado (status: ${response.status})`);
            }

            this.pokemon = await response.json();
            console.log(`\nPokémon '${id}' ha sido cargado.`);
        } catch (error) {
            GetPokemon.handleExceptions(error);
        }
    }

    info() {
        if (!this.pokemon) {
            console.log("El Pokémon aún no ha sido cargado.");
            return;
        }

        console.log(`Información Básica \n` +
            `* Id:      ${this.pokemon.id} \n` +
            `* Nombre:  ${this.pokemon.name} \n` +
            `* Peso:    ${this.pokemon.weight} kg \n` +
            `* Altura:  ${this.pokemon.height} m \n` +
            `* Tipo(s):`
        );

        this.pokemon.types.forEach((typeInfo) => {
            console.log(`         - ${typeInfo.type.name}`);;
        });
    }

    async evolutionChain() {
        if (!this.pokemon) {
            console.log("El Pokémon aún no ha sido cargado.");
            return;
        }

        try {
            const speciesUrl = this.pokemon.species.url;
            const speciesData = await fetch(speciesUrl).then((res) => res.json());
            const evolutionChainUrl = speciesData.evolution_chain.url;
            const evolutionChainData = await fetch(evolutionChainUrl).then((res) => res.json());

            console.log("\nCadena de evoluciones:");
            let currentEvolution = evolutionChainData.chain;

            while (currentEvolution) {
                console.log(`- ${currentEvolution.species.name}`);
                currentEvolution = currentEvolution.evolves_to[0] || null;
            }
        } catch (error) {
            GetPokemon.handleExceptions(error);
        }
    }

    showGames() {
        if (!this.pokemon) {
            console.log("El Pokémon aún no ha sido cargado.");
            return;
        }

        console.log("\nJuegos en los que aparece:");
        if (this.pokemon.game_indices.length > 0) {
            this.pokemon.game_indices.forEach((gameInfo) => {
                console.log(`- ${gameInfo.version.name}`);
            });
        } else {
            console.log("No aparece en ninguno.");
        }
    }

    static handleExceptions(error) {
        if (error.name === "FetchError") {
            console.log("Error de conexión:", error.message);
        } else {
            console.log("Error inesperado:", error.message);
        }
    }
}

// ________________________________________________________
(async () => {
    const u1 = await getUser(1);
    printUser(u1);

    const u2 = await getUser(2);
    printUser(u2);

    const u3 = await getUser(777); // No existente.
    printUser(u3);

    console.log("\nDIFICULTAD EXTRA:");

    try {
        const p1 = new GetPokemon();
        await p1.load(1);
        p1.info();
        await p1.evolutionChain();
        p1.showGames();

        const p2 = new GetPokemon();
        await p2.load("ivysaur");
        p2.info();
        await p2.evolutionChain();
        p2.showGames();
    } catch (error) {
        GetPokemon.handleExceptions(error);
    }
})();
