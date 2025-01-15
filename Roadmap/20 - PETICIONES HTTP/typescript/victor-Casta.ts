const readline = require('node:readline')
const { stdin: input, stdout: output } = require('node:process')

const rl = readline.createInterface({ input, output })


interface Products {
  id: number
  title: string
  price: number
  description: string
  category: Category
  images: string[]
}

interface Category {
  id: number
  name: string
  image: string
}

async function getProducts(): Promise<Products[]> {
  try {
    const response = await fetch('https://api.escuelajs.co/api/v1/products')

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const results: Products[] = await response.json()
    console.log('Petición exitosa')
    return results
  } catch (error) {
    console.log('Error al obtener productos:', error)
    return []
  }
}

async function printData() {
  const productsInformation = await getProducts()
  console.log(productsInformation)
}


/*
  * Extra
*/

const baseUrl: string = 'https://pokeapi.co/api/v2/pokemon/'

interface Pokemon {
  id: number
  name: string
  weight: number
  height: number
  abilities: Ability[]
  types: Type[]
  stats: Stat[]
  sprites: Sprite
}

interface Ability {
  ability: NamedAPIResource
  is_hidden: boolean
  slot: number
}

interface NamedAPIResource {
  name: string
  url: string
}

interface Type {
  slot: number
  type: NamedAPIResource
}

interface Stat {
  base_stat: number
  effort: number
  stat: NamedAPIResource
}

interface Sprite {
  front_default: string
  back_default?: string
}

async function getPokemonInformation(
  url: string,
  pokemonName: string
): Promise<Pokemon | null> {
  try {
    const response = await fetch(`${url}${pokemonName}`)
    if (!response.ok) {
      console.log(`Error en la respuesta de la API: ${response.status}`)
      return null
    }
    const result: Pokemon = await response.json()
    console.log('Petición exitosa')
    return result
  } catch (error) {
    console.error('Error al realizar la petición:', error)
    return null
  }
}

rl.question('Ingresa el nombre de un Pokémon: ', async (pokemonNameAnswer: string) => {
  const pokemonInformation = await getPokemonInformation(baseUrl, pokemonNameAnswer.toLowerCase())

  if (pokemonInformation) {
    console.log(`Información de ${pokemonInformation.name}:`)
    console.log(`ID: ${pokemonInformation.id}`)
    console.log(`Peso: ${pokemonInformation.weight}`)
    console.log(`Altura: ${pokemonInformation.height}`)
    console.log('Tipos:')
    pokemonInformation.types.forEach((type) => console.log(` - ${type.type.name}`))
    console.log('Estadísticas:')
    pokemonInformation.stats.forEach((stat) => console.log(` - ${stat.stat.name}: ${stat.base_stat}`))
  } else {
    console.log('No se encontró información para el Pokémon ingresado.')
  }

  rl.close()
})