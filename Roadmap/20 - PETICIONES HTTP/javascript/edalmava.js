async function peticionHTTP() {
  try {
    const respuesta = await fetch('https://edalmava.co')
    if (respuesta.ok) {
      const datos = await respuesta.text()
      console.log(datos)
    } else {
      console.log("Respuesta de red OK pero respuesta HTTP no OK: ")
    }
  } catch(error) {
    console.log("Hubo un problema con la petición Fetch:" + error.message)
  }
}

async function buscarPokemon(name) {
  try {  
    const respuesta = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`)
    if (respuesta.ok) {
      const datos = await respuesta.json()
      
      const nombre = datos.name
      const id = datos.id
      const peso = datos.weight
      const altura = datos.height
      const tipos = datos.types.map(e => e.type.name).join(',')

      console.log('Información del Pokémon: ')
      console.log('Nombre: ', nombre)
      console.log('ID: ', id)
      console.log('Peso: ', peso)
      console.log('Altura: ', altura)
      console.log('Tipo(s): ', tipos)

      const res_evolution_chain = await fetch(`https://pokeapi.co/api/v2/evolution-chain/${id}/`)
      if (res_evolution_chain.ok) {
        const datos_chain = await res_evolution_chain.json()
        console.log('Cadena de Evolución: ', datos_chain)
      }
    } else { 
      console.log("Respuesta de red OK pero respuesta HTTP no OK: ")
      if (respuesta.status === 404) {
        console.log('Pokémon no encontrado')
      } else {
        console.log(respuesta.statusText)
      }
    }
  } catch(error) {
    console.log("Hubo un problema con la petición Fetch:" + error.message)
  }
}

async function inicio() {
  console.log('*****Petición HTTP al sitio https://edalmava.co*****')
  await peticionHTTP()
  console.log('****************************************************')
  console.log('****************************************************')
  console.log('*****RETO EXTRA*****')
  const readline = require('node:readline');
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  rl.question(`¿Nombre o número del Pokémon a buscar? `, name => {
    buscarPokemon(name)
    rl.close();
  });
}

inicio()