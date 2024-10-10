/**
 * Teoría sobre peticiones HTTP en TypeScript:
 *
 * TypeScript añade tipado estático a JavaScript, lo que nos permite:
 * 1. Definir interfaces para las respuestas de la API
 * 2. Tener mejor autocompletado y detección de errores en tiempo de compilación
 * 3. Hacer el código más mantenible y autodocumentado
 *
 * Para peticiones HTTP, podemos usar:
 * - fetch en navegadores o con 'node-fetch' en Node.js
 * - axios como una alternativa más robusta
 *
 * Este ejemplo usa 'node-fetch' y requiere:
 * npm install typescript @types/node node-fetch @types/node-fetch
 */

import fetch from "node-fetch";
import * as readline from "readline";

// Interfaces para tipar las respuestas de la API
interface Pokemon {
  name: string;
  id: number;
  weight: number;
  height: number;
  types: Array<{
    type: {
      name: string;
    };
  }>;
  game_indices: Array<{
    version: {
      name: string;
    };
  }>;
  species: {
    url: string;
  };
}

interface PokemonSpecies {
  evolution_chain: {
    url: string;
  };
}

interface EvolutionChain {
  chain: ChainLink;
}

interface ChainLink {
  species: {
    name: string;
  };
  evolves_to: ChainLink[];
}

// Configuración de readline para entrada/salida en consola
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Función para realizar preguntas al usuario y obtener respuesta
function pregunta(pregunta: string): Promise<string> {
  return new Promise((resolve) => {
    rl.question(pregunta, resolve);
  });
}

// Función genérica para realizar peticiones HTTP
async function hacerPeticionHttp<T>(url: string): Promise<T> {
  try {
    const respuesta = await fetch(url);
    if (!respuesta.ok) {
      throw new Error(`HTTP error! status: ${respuesta.status}`);
    }
    return (await respuesta.json()) as T;
  } catch (error) {
    throw new Error(
      `Error al realizar la petición: ${
        error instanceof Error ? error.message : "Unknown error"
      }`
    );
  }
}

// Función para mostrar la cadena de evolución
function mostrarCadenaEvolucion(cadena: ChainLink, nivel: number = 0): void {
  const indentacion = "  ".repeat(nivel);
  console.log(`${indentacion}- ${cadena.species.name}`);

  if (cadena.evolves_to.length > 0) {
    for (const evolucion of cadena.evolves_to) {
      mostrarCadenaEvolucion(evolucion, nivel + 1);
    }
  }
}

// Función principal que ejecuta el programa
async function main(): Promise<void> {
  console.log("=== Ejemplo básico de petición HTTP ===");
  try {
    await hacerPeticionHttp("https://www.example.com");
    console.log("Petición exitosa a example.com");
  } catch (error) {
    console.error(error instanceof Error ? error.message : "Unknown error");
  }

  while (true) {
    console.log("\n=== Búsqueda de Pokémon ===");
    const entrada = await pregunta(
      "Ingrese el nombre o número del Pokémon (o 'salir' para terminar): "
    );

    if (entrada.toLowerCase() === "salir") {
      break;
    }

    try {
      // Obtener datos básicos del Pokémon
      const pokemonData = await hacerPeticionHttp<Pokemon>(
        `https://pokeapi.co/api/v2/pokemon/${entrada.toLowerCase()}`
      );

      console.log("\nInformación del Pokémon:");
      console.log(`Nombre: ${pokemonData.name}`);
      console.log(`ID: ${pokemonData.id}`);
      console.log(`Peso: ${pokemonData.weight / 10} kg`);
      console.log(`Altura: ${pokemonData.height / 10} m`);

      console.log("Tipos:");
      pokemonData.types.forEach((tipo) => {
        console.log(`- ${tipo.type.name}`);
      });

      // Obtener y mostrar cadena de evolución
      const speciesData = await hacerPeticionHttp<PokemonSpecies>(
        pokemonData.species.url
      );
      const evolutionData = await hacerPeticionHttp<EvolutionChain>(
        speciesData.evolution_chain.url
      );

      console.log("\nCadena de evolución:");
      mostrarCadenaEvolucion(evolutionData.chain);

      // Mostrar juegos
      console.log("\nJuegos en los que aparece:");
      pokemonData.game_indices.forEach((juego) => {
        console.log(`- ${juego.version.name}`);
      });
    } catch (error) {
      console.error(
        "Error: No se pudo encontrar el Pokémon. Asegúrese de escribir el nombre o número correctamente."
      );
    }
  }

  rl.close();
}

// Ejecutar el programa
main().catch((error) => {
  console.error(
    "Error en la ejecución del programa:",
    error instanceof Error ? error.message : "Unknown error"
  );
  process.exit(1);
});
