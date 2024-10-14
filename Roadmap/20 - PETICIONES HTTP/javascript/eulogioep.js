// Se requiere el módulo 'node-fetch' para realizar peticiones HTTP en Node.js
// Instalar con: npm install node-fetch
const fetch = require("node-fetch");
const readline = require("readline");

/**
 * Teoría sobre peticiones HTTP en JavaScript:
 *
 * En JavaScript moderno, podemos realizar peticiones HTTP de varias formas:
 * 1. Fetch API (nativo en navegadores, requiere módulo en Node.js)
 * 2. XMLHttpRequest (método más antiguo)
 * 3. Bibliotecas como axios
 *
 * La Fetch API utiliza Promesas, lo que permite un código más limpio y
 * manejo asíncrono más sencillo usando async/await.
 *
 * Conceptos clave:
 * - async/await: Permite escribir código asíncrono que parece síncrono
 * - try/catch: Maneja errores en operaciones asíncronas
 * - JSON: Formato común para intercambiar datos en la web
 */

// Configuración de readline para entrada/salida en consola
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Función para realizar preguntas al usuario y obtener respuesta
const pregunta = (pregunta) => {
  return new Promise((resolve) => {
    rl.question(pregunta, resolve);
  });
};

// Función para realizar petición HTTP
async function hacerPeticionHttp(url) {
  try {
    const respuesta = await fetch(url);
    if (!respuesta.ok) {
      throw new Error(`HTTP error! status: ${respuesta.status}`);
    }
    return await respuesta.json();
  } catch (error) {
    throw new Error(`Error al realizar la petición: ${error.message}`);
  }
}

// Función para mostrar la cadena de evolución
function mostrarCadenaEvolucion(cadena, nivel = 0) {
  const indentacion = "  ".repeat(nivel);
  console.log(`${indentacion}- ${cadena.species.name}`);

  if (cadena.evolves_to.length > 0) {
    for (const evolucion of cadena.evolves_to) {
      mostrarCadenaEvolucion(evolucion, nivel + 1);
    }
  }
}

// Función principal que ejecuta el programa
async function main() {
  console.log("=== Ejemplo básico de petición HTTP ===");
  try {
    const ejemploData = await hacerPeticionHttp("https://www.example.com");
    console.log("Petición exitosa a example.com");
  } catch (error) {
    console.error(error.message);
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
      const pokemonData = await hacerPeticionHttp(
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
      const speciesData = await hacerPeticionHttp(pokemonData.species.url);
      const evolutionData = await hacerPeticionHttp(
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
main().catch(console.error);
