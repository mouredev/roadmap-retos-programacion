// Creamos una función para obtener el token de acceso y le pasaremos el client_id y secret_client como parámetros.

async function getToken(clientId, clientSecret) {
  const accessToken = await fetch('https://accounts.spotify.com/api/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      grant_type: 'client_credentials',
      client_id: clientId,
      client_secret: clientSecret,
    }),
  })
    .then((response) => response.json())
    .catch((err) => console.log(err))

  return accessToken
}

/*
* IMPORTANTE *

Estoy importando mis ID's del archivo RicJDev_client.js (que no está disponible dentro del repo).
Si desea ejecutar este código deberá pasar sus propias ID's como parámetros de la función getToken().

Para obtenerlas puede revisar esta sección en su cuenta de Spotify para desarrolladores: https://developer.spotify.com/dashboard

*/

import { myClientId, myClientSecret } from './RicJDev_client.js'

const token = await getToken(myClientId, myClientSecret)
