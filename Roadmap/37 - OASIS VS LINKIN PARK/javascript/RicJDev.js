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
    if (response.status !== 200) {
      throw new Error(`Error al obtener el artista ${artist}`)
    }

    return response.json()
  })

  if (!results.artists.items) {
    throw new Error(`Artista ${artist} no ha sido encontrado.`)
  }

  return results.artists.items[0].id
}

// E iremos almacenando la información de nuestros artistas.

const LinkinPark = {
  id: await getArtistId('Linkin Park'),
}

const Oasis = {
  id: await getArtistId('Oasis'),
}

// Creamos una función que nos retorne los datos del artista desde la API.

async function getArtistData(artistId) {
  const url = `https://api.spotify.com/v1/artists/${artistId}`
  const results = await fetch(url, authorization).then((response) => {
    if (response.status !== 200) {
      throw new Error(`Error al obtener datos del artista`)
    }

    return response.json()
  })

  return {
    name: results.name,
    followers: results.followers.total,
    popularity: results.popularity,
  }
}

LinkinPark.data = await getArtistData(LinkinPark.id)
Oasis.data = await getArtistData(Oasis.id)

// Creamos otra función para obtener la canción más escuchada de la semana.

async function getArtistTopTrack(artistId) {
  const url = `https://api.spotify.com/v1/artists/${artistId}/top-tracks?market=VE`
  const results = await fetch(url, authorization).then((response) => {
    if (response.status !== 200) {
      throw new Error(`Error al obtener cancion mas popular.`)
    }

    return response.json()
  })

  return {
    name: results.tracks[0].name,
    popularity: results.tracks[0].popularity,
    album: results.tracks[0].album.name,
  }
}

LinkinPark.topTrack = await getArtistTopTrack(LinkinPark.id)
Oasis.topTrack = await getArtistTopTrack(Oasis.id)

// Aquí empezamos a comparar.

//TODO
