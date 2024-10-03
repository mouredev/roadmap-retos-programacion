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

const requestBody = {
  headers: {
    'Client-ID': CLIENT_ID,
    Accept: 'application/vnd.twitchtv.v5+json',
    Authorization: `Bearer ${accessToken}`,
  },
}

async function getChannelData(name) {
  const url = `https://api.twitch.tv/helix/search/channels?query=${name}&first=1`

  const results = await fetch(url, requestBody).then((response) => {
    if (response.status !== 200)
      throw new Error(`Error al obtener informacion del canal buscado: ${name}.`)

    return response.json()
  })

  return { name: results.data[0].display_name, id: results.data[0].id }
}

async function getTotalFollowers(broadcasterId) {
  const url = `https://api.twitch.tv/helix/channels/followers?broadcaster_id=${broadcasterId}`

  const results = await fetch(url, requestBody).then((response) => {
    if (response.status !== 200)
      throw new Error(`Error al obtener seguidores del canal con la id: ${broadcasterId}.`)

    return response.json()
  })

  return results.total
}

const ari = {
  data: null,
  followers: null,
  createdDate: null,
}

ari.data = await getChannelData('Ari Gameplays')
ari.followers = await getTotalFollowers(ari.data.id)

console.log(ari)

const participants = [
  'Abby',
  'Ache',
  'Adri Contreras',
  'Agustin',
  'Alexby',
  'Ampeter',
  'Ander',
  'Ari Gameplays',
  'Arigelli',
  'Auronplay',
  'Axozer',
  'Beniju',
  'By Calitos',
  'Byviruzz',
  'Carrerra',
  'Celopan',
  'Cheeto',
  'Crystalmolly',
  'Dario Eme Hache',
  'Dheylo',
  'DJMarrio',
  'Doble',
  'Elvisa',
  'Elyas360',
  'Folagor',
  'Grefg',
  'Guanyar',
  'Hika',
  'Hiper',
  'Ibai',
  'Ibelky',
  'Illojuan',
  'Imantado',
  'Irina Isasia',
  'Jesskiu',
  'Jopa',
  'JordiWild',
  'Kenai Souza',
  'Keroro',
  'Kidd Keo',
  'Kiko Rivera',
  'Knekro',
  'KronnoZomber',
  'Leviathan',
  'Lit Killah',
  'Lola Lolita',
  'Luh',
  'Luzu',
  'Mangel',
  'Mayichi',
  'Melo',
  'MissaSinfonia',
  'Mixwell',
  'Mr.Jagger',
  'Nate Gentile',
  'Nexxuz',
  'Nia',
  'Nil Ojeda',
  'Nissaxter',
  'Ollie',
  'Outsconsumer',
  'OrsloK',
  'Papi Gavi',
  'Paracetarol',
  'Patica',
  'Paula Gonu',
  'Pausenpaii',
  'Perxitaa',
  'Plex',
  'Polispol',
  'Quackity',
  'Recuerdop',
  'Reven',
  'Rivers',
  'RoberTPG',
  'Roier',
  'Rojuu',
  'Rubius',
  'Shadoune',
  'Silithur',
  'Spoksponha',
  'Spreen',
  'Spursiti',
  'Staxx',
  'Suzyroxx',
  'Vicens',
  'Vituber',
  'Werlyb',
  'Xavi',
  'Xcry',
  'Xokas',
  'Xraas',
  'Zarcort',
  'Zeling',
  'Zorman',
]
