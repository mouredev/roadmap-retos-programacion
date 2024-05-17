const baseURL: string = 'https://pokeapi.co/api/v2/pokemon'

const getData = async (number: number) => {
  try{
    const res = await fetch(`${baseURL}/${number}`)
    const data = await res.json()
    
    console.log('Name: ', data.name)
    console.log('ID: ', data.id)
    console.log('Weight: ', data.weight)
    console.log('Height: ', data.height)

    const types: Array<string> = data.types.map(type => type.type.name)
    console.log('Types: ', types)

    const games: Array<string> = data.game_indices.map(game => game.version.name)
    console.log('Games: ', games)
  }catch(error){
    console.log(error)
  }
}

getData(9)