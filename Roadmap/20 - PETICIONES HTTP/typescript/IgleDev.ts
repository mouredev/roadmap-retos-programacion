const pokemonURL : string = 'https://pokeapi.co/api/v2/pokemon'

const getData = async (number: number) => {
  try{
    const res = await fetch(`${pokemonURL}/${number}`)
    const data = await res.json()
    
    console.log('Nombre: ', data.name);
    console.log('ID Pokemon: ', data.id);
    console.log('Peso: ', data.weight);
    console.log('Altura: ', data.height);

    const tipos : Array<string> = data.types.map(tipos => tipos.type.name);
    console.log('Tipos: ', tipos);

    const juegos : Array<string> = data.game_indices.map(juegos => juegos.version.name)
    console.log('Juegos: ', juegos)
  }catch(error){
    console.log('No hemos podido conectarnos a la API')
  }
}

getData(152);