/* 
    Creado por Rafa Canosa / Rafacv23
    Github: https://github.com/Rafacv23
    Website: https://www.rafacanosa.dev
*/

const readline = require("readline") // importamos para poder pedir al usuario inputs a través de la terminal.

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const getEvolutionChain = async (pokemon) => {
  const url = `https://pokeapi.co/api/v2/pokemon-species/${pokemon}`

  try {
    const res = await fetch(url)

    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`)
    }

    const pokemonSpecies = await res.json()

    // comprobar si el pokemon tiene cadena de evolución
    if (pokemonSpecies.evolution_chain) {
      const chainUrl = pokemonSpecies.evolution_chain.url

      try {
        const res = await fetch(chainUrl)

        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`)
        }

        const chain = await res.json()

        // función para recorrer recursivamente la cadena de evoluciones
        const parseEvolutionChain = (chain) => {
          const evolutions = []
          let current = chain.chain

          do {
            evolutions.push(current.species.name)
            current = current.evolves_to[0]
          } while (current && current.evolves_to.length)

          if (current) {
            evolutions.push(current.species.name)
          }

          return evolutions
        }

        const evolutionNames = parseEvolutionChain(chain)
        console.log(`Cadena de evolución: ${evolutionNames.join(" -> ")}`)
      } catch (err) {
        console.error("Error fetching evolution chain:", err.message)
        return null // Devolvemos null si hubo un error al pedir la cadena de evolución.
      }
    } else {
      console.log("Este Pokémon no tiene evoluciones.")
      return null
    }
  } catch (err) {
    console.error("Error fetching Pokémon:", err.message)
    return null // Devolvemos null si hubo un error al pedir la cadena de evolución.
  }
}

;(async () => {
  const getPokemon = async (pokeName) => {
    const url = `https://pokeapi.co/api/v2/pokemon/${pokeName.toLowerCase()}`
    try {
      const res = await fetch(url)

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`)
      }

      const pokemon = await res.json()

      console.log(
        `El Pokémon que buscaste es: ${pokemon.name}, id: ${
          pokemon.id
        }, peso: ${pokemon.weight}, altura: ${
          pokemon.height
        }, tipos: ${pokemon.types.map((type) => type.type.name)}`
      )

      const games = pokemon.game_indices.map((game) => game.version.name)

      console.log(`Juegos en los que ha aparecido: ${games.join(", ")}`)

      await getEvolutionChain(pokemon.id)
    } catch (error) {
      console.error("Error fetching Pokémon:", error.message)
    } finally {
      rl.close() // cierra la interfaz de readline
    }
  }

  rl.question("Qué Pokémon estás buscando? ", (name) => {
    getPokemon(name)
  })
})()
