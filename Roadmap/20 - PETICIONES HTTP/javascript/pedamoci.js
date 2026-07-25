const respuesta = await fetch('https://retosdeprogramacion.com/roadmap')
if (respuesta.ok) {
  const contenido = await respuesta.text()
  console.log(contenido)
}

// ------------------------------ DIFICULTAD EXTRA ------------------------------
import  readline  from "readline"

function preguntar(pregunta) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  })

  return new Promise(resolve => {
    rl.question(pregunta, (respuesta) => {
      rl.close()
      resolve(respuesta)
    })
  })
}

async function Pokemon(pokemon) {
  const urlApi = 'https://pokeapi.co/api/v2/pokemon/'
  try {
    const responsePokemon = await fetch(`${urlApi}${pokemon}`)
    if (!responsePokemon.ok) throw new Error("No se pudo obtener información sobre ese pokemon")
    const characteristic = await responsePokemon.json()
    console.log('Caracteristicas del pokemon ingresado:\n' + 
                `Nombre: ${characteristic.name}\n` +
                `ID: ${characteristic.id}\n` +
                `Peso: ${characteristic.weight}\n` +
                `Altura: ${characteristic.height}\n` + 
                `Tipos: ${characteristic.types[0].type.name}, ${characteristic.types[1].type.name}`)

    const responseSpecies = await fetch(`${characteristic.species.url}`)               //
    const infoSpecies = await responseSpecies.json()                                    // INFORMACION NECESARIA PARA LLEGAR A LA CADENA EVOLUTIVA
    const responceChainEvolutions = await fetch(`${infoSpecies.evolution_chain.url}`)   //
    const infoChainEvolutions = await responceChainEvolutions.json()
    if (infoChainEvolutions.chain.evolves_to.length === 0) console.log('El pokemon no tiene cadena evolutiva')
    else {
      let evolutionChain = infoChainEvolutions.chain
      let evolutions = [evolutionChain.species.name]
      while (evolutionChain.evolves_to.length !== 0) {
        evolutions.push(evolutionChain.evolves_to[0].species.name)
        evolutionChain = evolutionChain.evolves_to[0]
      }
      console.log(`Cadena evolutiva: ${evolutions.join(', ')}`)
    }

    if (characteristic.game_indices.length === 0) console.log('La información sobre en que juegos aparece este pokemon no esta disponible')
      else {
        const games = characteristic.game_indices.map((x) => x.version.name)
        console.log(`Juegos en los que aparece: ${games.join(', ')}`)
      }

  } catch (e) {
    console.log(e)
  }
}

Pokemon(await preguntar('De que pokemon quieres obtener información?? (inserta el nobre o el número de la pokedex)\n'))