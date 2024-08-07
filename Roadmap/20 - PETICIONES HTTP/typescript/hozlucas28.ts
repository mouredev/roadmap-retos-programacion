/*
    HTTP request...
*/

interface Fact {
    id: string
    type: string
    attributes: {
        body: string
    }
}

interface DogFact {
    data: Fact[]
}

async function httpRequestMain() {
    console.log('HTTP request...')

    try {
        const response = await fetch('https://dogapi.dog/api/v2/facts')

        if (response.status === 200) {
            const dogFact: DogFact = await response.json()
            console.log(`\nRandom dog fact: ${dogFact.data[0].attributes.body}`)
        } else {
            throw new Error(`${response.status} ${response.statusText}`)
        }
    } catch (error) {
        console.error(`\n${error}`)
    }
}

/*
    Additional challenge...
*/

interface GameIndex {
    game_index: number
    version: {
        name: string
    }
}

interface Type {
    slot: number
    type: {
        name: string
    }
}

interface Pokemon {
    game_indices: GameIndex[]
    height: number
    id: number
    name: string
    types: Type[]
}

async function getPokemonData(id: number | string): Promise<never | Pokemon> {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)

    if (response.status === 200) {
        const pokemon: Pokemon = await response.json()
        return pokemon
    } else {
        throw new Error(`${response.status} ${response.statusText}`)
    }
}

async function additionalChallengeMain() {
    console.log(
        '\n# ---------------------------------------------------------------------------------- #\n'
    )

    console.log('Additional challenge...')

    const formatter = new Intl.ListFormat('en', {
        style: 'long',
        type: 'conjunction',
    })

    console.log('\nPokemon with id number five...')

    try {
        const fifthPokemon: Pokemon = await getPokemonData(5)
        const fifthPokemonGames = fifthPokemon.game_indices.map(
            (gameIndex) => gameIndex.version.name
        )
        const fifthPokemonTypes = fifthPokemon.types.map(
            (type) => type.type.name
        )

        console.log(`\nid: ${fifthPokemon.id}`)
        console.log(`name: ${fifthPokemon.name}`)
        console.log(`height: ${fifthPokemon.height}`)
        console.log(`type: ${formatter.format(fifthPokemonTypes)}`)
        console.log(`games: ${formatter.format(fifthPokemonGames)}`)
    } catch (error) {
        console.error(`\n${error}`)
    }

    console.log('\nPokemon with "Bulbasaur" name...')

    try {
        const bulbasaur: Pokemon = await getPokemonData('bulbasaur')
        const bulbasaurGames = bulbasaur.game_indices.map(
            (gameIndex) => gameIndex.version.name
        )
        const bulbasaurTypes = bulbasaur.types.map((type) => type.type.name)

        console.log(`\nid: ${bulbasaur.id}`)
        console.log(`name: ${bulbasaur.name}`)
        console.log(`height: ${bulbasaur.height}`)
        console.log(`type: ${formatter.format(bulbasaurTypes)}`)
        console.log(`games: ${formatter.format(bulbasaurGames)}`)
    } catch (error) {
        console.error(`\n${error}`)
    }
}

Promise.all([httpRequestMain()]).then(
    async () => await additionalChallengeMain()
)
