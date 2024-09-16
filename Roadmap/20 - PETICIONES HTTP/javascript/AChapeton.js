const baseURL = 'https://pokeapi.co/api/v2/pokemon'

const getData = async (number) => {
  try{
    const res = await fetch(`${baseURL}/${number}`)
    const data = await res.json()
    
    console.log('Name: ', data.name)
    console.log('ID: ', data.id)
    console.log('Weight: ', data.weight)
    console.log('Height: ', data.height)

    const types = data.types.map(type => type.type.name)
    console.log('Types: ', types)

    const games = data.game_indices.map(game => game.version.name)
    console.log('Games: ', games)
  }catch(error){
    console.log(error)
  }
}

getData(9)