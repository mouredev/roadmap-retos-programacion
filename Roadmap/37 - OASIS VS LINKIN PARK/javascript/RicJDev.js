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

  return token['access_token']
}

const accessToken = await getToken(CLIENT_ID, CLIENT_SECRET)

console.log(accessToken)

const authorization = {
  method: 'GET',
  headers: {
    Authorization: `Bearer  ${accessToken}`,
  },
}

async function getArtistData(artistId) {
  const url = `https://api.spotify.com/v1/artists/${artistId}`
  const artistData = await fetch(url, authorization).then((response) => response.json())

  return artistData
}

async function getArtistAlbumsData(artistId) {
  const url = `https://api.spotify.com/v1/artists/${artistId}/albums?include_groups=album,single&market=VE&limit=50`
  const albumData = await fetch(url, authorization).then((response) => response.json())

  return albumData
}

// Almacenamos las id's de Oasis y Linkin Park.

const Oasis = {
  id: '2DaxqgrOhkeH0fpeiQq2f4',
}

const LinkinPark = {
  id: '6XyY86QOPPrYVGvF9ch6wz',
}

Oasis.data = await getArtistData(Oasis.id)
LinkinPark.data = await getArtistData(Oasis.id)

console.log(Oasis.data)
console.log(LinkinPark.data)

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
