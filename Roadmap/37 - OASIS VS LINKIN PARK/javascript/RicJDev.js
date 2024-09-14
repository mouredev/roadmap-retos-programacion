/**
 * Genera un token de acceso, necesario para hacer peticiones a la API de Spotify.
 *
 * @param {string} clientId
 * @param {string} clientSecret
 * @returns {Promise<object>}
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

/**
 * Retorna la información sobre un artista utilizando la API de Spotify.
 *
 * @param {string} artistId se obtiene de la página del artista en Spotify (https://open.spotify.com/intl-es/artist/ `artistId`).
 * @param {object} token token de acceso. Use `getToken()` para obetenerlo.
 * @returns {Promise<object>}
 */

async function getArtistData(artistId, token) {
  const artistData = await fetch(`https://api.spotify.com/v1/artists/${artistId}`, {
    method: 'GET',
    headers: {
      Authorization: `${token.token_type} ${token.access_token}`,
    },
  }).then((response) => response.json())

  return artistData
}

// Almacenamos las id's de Oasis y Linkin Park.

const OasisId = '2DaxqgrOhkeH0fpeiQq2f4'
const LinkinParkId = '6XyY86QOPPrYVGvF9ch6wz'

const OasisData = await getArtistData(OasisId, token)
const LinkinParkData = await getArtistData(LinkinParkId, token)

console.log('\nDatos de Oasis')
console.log(OasisData)

console.log('\nDatos de Linkin Park')
console.log(LinkinParkData)

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
