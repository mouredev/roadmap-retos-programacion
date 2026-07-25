/*
  EJERCICIO:

  @RicJDev
*/

import { CLIENT_ID, CLIENT_SECRET } from './client.js'

/*
IMPORTANTE:

Estoy importando mis id's del archivo client.js, el cual no está subido al repo.
Si desea ejecutar este código deberá usar sus propias id's.
*/

// Creamos una función para obtener el token de acceso.

async function getToken(clientId, clientSecret) {
  const token = await fetch('https://accounts.spotify.com/api/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      grant_type: 'client_credentials',
      client_id: clientId,
      client_secret: clientSecret,
    }),
  }).then((response) => {
    if (response.status !== 200) {
      throw new Error(`Falla al obtener respuesta de la API. ${response.json()}`)
    }

    return response.json()
  })

  return token.access_token
}

// Nos almacenamos el método de autenticación que usaremos para las peticiones.

const accessToken = await getToken(CLIENT_ID, CLIENT_SECRET)
const authorization = { headers: { Authorization: `Bearer  ${accessToken}` } }

// Creamos una función para aprovechar el sitema de búsqueda de la API.

async function getArtistId(artist) {
  const url = `https://api.spotify.com/v1/search?q=${artist}&type=artist&limit=1`
  const results = await fetch(url, authorization).then((response) => {
    if (response.status !== 200) throw new Error(`Error al obtener el artista ${artist}.`)

    return response.json()
  })

  if (!results.artists.items) throw new Error(`Artista ${artist} no ha sido encontrado.`)

  return results.artists.items[0].id
}

// E iremos almacenando la información de nuestros artistas.

const artist1 = {
  id: await getArtistId('Linkin Park'),
}

const artist2 = {
  id: await getArtistId('Oasis'),
}

// Creamos una función que nos retorne los datos del artista desde la API.

async function getArtistData(artistId) {
  const url = `https://api.spotify.com/v1/artists/${artistId}`
  const results = await fetch(url, authorization).then((response) => {
    if (response.status !== 200) throw new Error(`Error al obtener datos del artista.`)

    return response.json()
  })

  return {
    name: results.name,
    followers: results.followers.total,
    popularity: results.popularity,
  }
}

artist1.data = await getArtistData(artist1.id)
artist2.data = await getArtistData(artist2.id)

// Creamos otra función para obtener la canción más escuchada de la semana.

async function getArtistTopTrack(artistId) {
  const url = `https://api.spotify.com/v1/artists/${artistId}/top-tracks?market=VE`
  const results = await fetch(url, authorization).then((response) => {
    if (response.status !== 200) throw new Error(`Error al obtener canción más popular.`)

    return response.json()
  })

  return {
    name: results.tracks[0].name,
    popularity: results.tracks[0].popularity,
    album: results.tracks[0].album.name,
  }
}

artist1.topTrack = await getArtistTopTrack(artist1.id)
artist2.topTrack = await getArtistTopTrack(artist2.id)

// Aquí empezamos a comparar.

console.log('COMPARANDO ARTISTAS.\n')

console.log(`- ${artist1.data.name}.`)
console.log(`- ${artist2.data.name}.`)

artist1.points = 0
artist2.points = 0

// Ronda 1: seguidores.

console.log('\n¿Quién tiene más seguidores?')

console.log(`${artist1.data.name}:`, artist1.data.followers)
console.log(`${artist2.data.name}:`, artist2.data.followers)

if (artist1.data.followers > artist2.data.followers) {
  console.log(`\n¡Punto para ${artist1.data.name}!`)

  artist1.points++
} else {
  console.log(`\n¡Punto para ${artist2.data.name}!`)

  artist2.points++
}

// Ronda 2: popularidad.

console.log('\n¿Quién tiene más popularidad a nivel general?')

console.log(`${artist1.data.name}:`, artist1.data.popularity)
console.log(`${artist2.data.name}:`, artist2.data.popularity)

if (artist1.data.popularity > artist2.data.popularity) {
  console.log(`\n¡Punto para ${artist1.data.name}!`)

  artist1.points++
} else {
  console.log(`\n¡Punto para ${artist2.data.name}!`)

  artist2.points++
}

// Ronda 3: canción más escuchada.

console.log(
  '\nTenemos la canción más escuchada de cada artista. ¿Cuál tiene mayor popularidad general?'
)

console.log(`${artist1.data.name}: ${artist1.topTrack.name}:`, artist1.topTrack.popularity)
console.log(`${artist2.data.name}: ${artist2.topTrack.name} :`, artist2.topTrack.popularity)

if (artist1.topTrack.popularity > artist2.topTrack.popularity) {
  console.log(`\n¡Punto para ${artist1.data.name}!`)

  artist1.points++
} else {
  console.log(`\n¡Punto para ${artist2.data.name}!`)

  artist2.points++
}

console.log('\nRESULTADOS:')

artist1.points > artist2.points
  ? console.log(`Ha ganado ${artist1.data.name}:`, artist1.points)
  : console.log(`Ha ganado ${artist2.data.name}:`, artist2.points)
