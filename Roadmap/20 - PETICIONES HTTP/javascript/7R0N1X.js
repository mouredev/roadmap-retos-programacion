const peticion = async () => {
  const response = await fetch('https://tronix-portfolio.vercel.app')
  if (response.ok) {
    const data = await response.text()
    console.log(data)
  }
}

// peticion()

// DIFICULTAD EXTRA
const obtenerInfoPokemon = async (pokemon) => {
  const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`)
  if (response.ok) {
    const { id, forms: [{ name }], weight, height, types, game_indices } = await response.json()
    return {
      id, name, height, weight, types, game_indices
    }
  }
}

const mostrarInformacion = async (pokemon) => {
  const response = await obtenerInfoPokemon(pokemon)
  const { id, name, weight, height, types, game_indices } = response
  const tipos = types.map(type => type.type.name)
  const juegos = game_indices.map(juego => juego.version.name)

  console.log(`
    ID: ${id}
    Nombre: ${name}
    Altura: ${height}
    Peso: ${weight}
    Tipo(s): ${tipos}
    Juegos: ${juegos}
    `)
}

mostrarInformacion(1)
