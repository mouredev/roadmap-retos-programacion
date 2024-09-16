/**
 * Genera un token de acceso, necesario para hacer peticiones a la API de Spotify.
 *
 * @param {string} clientId
 * @param {string} clientSecret
 *
 * @see https://developer.spotify.com/dashboard
 */

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
  }).then((response) => response.json())

  return token
}

/*

* IMPORTANTE *

Estoy importando mis id's del archivo RicJDev_client.js (lo cual dará error, ya que no lo he subido al repo).
Si desea ejecutar este código deberá usar sus propias id's.

*/

import { myClientId, myClientSecret } from './RicJDev_client.js'

const token = await getToken(myClientId, myClientSecret)
const GET_requestMethod = {
  method: 'GET',
  headers: {
    Authorization: `${token.token_type} ${token.access_token}`,
  },
}

/**
 * Retorna la información sobre un artista utilizando la API de Spotify.
 *
 * @param {string} artistId se obtiene de la página del artista en Spotify (https://open.spotify.com/intl-es/artist/ `artistId`).
 * @returns {Promise<object>}
 *
 * @see https://developer.spotify.com/dashboard
 */

async function getArtistData(artistId) {
  const artistData = await fetch(
    `https://api.spotify.com/v1/artists/${artistId}`,
    GET_requestMethod
  ).then((response) => response.json())

  return artistData
}

/**
 * Retorna la data de los albums de un artista utilizando la API de Spotify.
 *
 * @param {string} artistId se obtiene de la página del artista en Spotify (https://open.spotify.com/intl-es/artist/ `artistId`).
 *
 * @see https://developer.spotify.com/dashboard
 */

async function getArtistAlbumsData(artistId) {
  const artistData = await fetch(
    `https://api.spotify.com/v1/artists/${artistId}/albums?include_groups=album,single&market=VE&limit=50`,
    GET_requestMethod
  ).then((response) => response.json())

  return artistData
}

// Almacenamos las id's de Oasis y Linkin Park.

const Oasis = {
  id: '2DaxqgrOhkeH0fpeiQq2f4',

  data: null,

  topTracks: null,

  albums: null,
}

const LinkinPark = {
  id: '6XyY86QOPPrYVGvF9ch6wz',

  data: null,

  topTracks: null,

  albums: null,
}

Oasis.data = await getArtistData(Oasis.id, token)
LinkinPark.data = await getArtistData(Oasis.id, token)

/*
TODO: 

Acciones:
1. Accede a las estadísticas de las dos bandas.
  Por ejemplo: número total de seguidores, escuchas mensuales,
  canción con más reproducciones...
2. Compara los resultados de, por lo menos, 3 endpoint.
3. Muestra todos los resultados por consola para notificar al usuario.
4. Desarrolla un criterio para seleccionar qué banda es más popular.

*/
