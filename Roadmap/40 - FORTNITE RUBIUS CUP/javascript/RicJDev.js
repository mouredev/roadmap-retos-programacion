import { CLIENT_ID, CLIENT_SECRET } from './client.js'

async function getAuthToken(clientId, clientSecret) {
  const token = await fetch('https://id.twitch.tv/oauth2/token', {
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

const accessToken = await getAuthToken(CLIENT_ID, CLIENT_SECRET)

const authorization = {
  headers: {
    'Client-ID': CLIENT_ID,
    Accept: 'application/vnd.twitchtv.v5+json',
    Authorization: 'Bearer ' + accessToken,
  },
}

async function searchChannel(channel) {
  const url = `https://api.twitch.tv/helix/search/channels?query=${channel}`

  const results = await fetch(url, authorization).then((response) => {
    if (response.status !== 200)
      throw new Error(`Error al obtener informacion del canal ${channel}.`)

    return response.json()
  })

  return results
}

const midu = await searchChannel('midudev')

console.log(midu)
