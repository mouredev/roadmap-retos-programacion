/*
  EJERCICIO:

  @RicJDev
*/

import { CLIENT_ID, CLIENT_SECRET } from './client.js'

/*
  Función para obtener token de autenticación.
  Solo se ejecuta si se le pasa un client_id y un client_secret (los cuales no subiré al repo).

  Consulta la documentación de la API de Twitch para más información (https://dev.twitch.tv/docs).
*/

async function getAccessToken(clientId, clientSecret) {
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
    if (response.status !== 200)
      throw new Error(`Falla al obtener respuesta de la API. ${response.json()}`)

    return response.json()
  })

  return token.access_token
}

// Métodos de auntenticación que necesitaremos para las peticiones.

const accessToken = await getAccessToken(CLIENT_ID, CLIENT_SECRET)

const requestBody = {
  headers: {
    'Client-ID': CLIENT_ID,
    Accept: 'application/vnd.twitchtv.v5+json',
    Authorization: `Bearer ${accessToken}`,
  },
}

// Usaremos esta función para obtener el número total de seguidores del usuario.

async function getTotalFollowers(userId) {
  const url = `https://api.twitch.tv/helix/channels/followers?broadcaster_id=${userId}`

  const results = await fetch(url, requestBody).then((response) => {
    if (response.status !== 200)
      throw new Error(`Error al obtener seguidores del canal con la id: ${userId}.`)

    return response.json()
  })

  return results.total
}

// Y con esta obtendremos los datos los participantes.

async function getUsersData(users, ...more) {
  if (users.constructor.name === 'Array') users = users.join('&login=')
  if (more.length > 0) users += `&login=${more.join('&login=')}`

  const url = `https://api.twitch.tv/helix/users?login=${users}`
  const result = await fetch(url, requestBody).then((response) => {
    if (response.status !== 200) throw new Error(`Error al obtener los datos solicitados ${users}`)

    return response.json()
  })

  const usersData = []

  for (let i = 0; i < result.data.length; i++) {
    const user = result.data[i]

    usersData.push({
      id: user.id,
      login: user.login,
      displayName: user.display_name,
      followers: await getTotalFollowers(user.id),
      createdAt: user.created_at,
    })
  }

  return usersData
}

// Esta es la lista de participantes. La lista original ha sido modificada para que cada elemento corresponda al login del participante.

const participants = [
  'littleragergirl', 'ache', 'adricontreras4', 'agustin51', 'alexby11', 'ampeterby7', 'tvander',
  'arigameplays', 'arigeli_', 'auronplay', 'axozer', 'beniju03', 'bycalitos',
  'byviruzz', 'carreraaa', 'celopan', 'srcheeto', 'crystalmolly', 'darioemehache',
  'dheylo', 'djmariio', 'doble', 'elvisayomastercard', 'elyas360', 'folagorlives', 'thegrefg',
  'guanyar', 'hika', 'hiperop', 'ibai', 'ibelky_', 'illojuan', 'imantado',
  'irinaissaia', 'jesskiu', 'jopa', 'jordiwild', 'kenaivsouza', 'mrkeroro10',
  'thekiddkeo95', 'kikorivera', 'knekro', 'kokoop', 'kronnozomberoficial', 'leviathan',
  'litkillah', 'lolalolita', 'lolitofdez', 'luh', 'luzu', 'mangel', 'mayichi',
  'melo', 'missasinfonia', 'mixwell', 'jaggerprincesa', 'nategentile7', 'nexxuz',
  'lakshartnia', 'nilojeda', 'nissaxter', 'olliegamerz', 'orslok', 'outconsumer', 'papigavitv',
  'paracetamor', 'patica1999', 'paulagonu', 'pausenpaii', 'perxitaa', 'nosoyplex',
  'polispol1', 'quackity', 'recuerd0p', 'reventxz', 'rivers_gg', 'robertpg', 'roier',
  'ceuvebrokenheart', 'rubius', 'shadoune666', 'silithur', 'spok_sponha', 'elspreen', 'spursito',
  'bystaxx', 'suzyroxx', 'vicens', 'vitu', 'werlyb', 'xavi', 'xcry', 'elxokas',
  'thezarcort', 'zeling', 'zormanworld'
]

const participantsData = await getUsersData(participants)

// Ordenar por antigüedad.

const sortedByOld = participantsData.toSorted((a, b) => new Date(a.createdAt) - new Date(b.createdAt))

console.log('\nRanking por antigüedad.')
sortedByOld.forEach((streamer, index) => {
  console.log(`${index + 1}. ${streamer.displayName}. ${new Date(streamer.createdAt).toLocaleDateString()}`)
})

// Ordenar por número de seguidores.

const sortedByFollowers = participantsData.toSorted((a, b) => b.followers - a.followers)

console.log('\nRanking de seguidores.')
sortedByFollowers.forEach((streamer, index) => {
  console.log(`${index + 1}. ${streamer.displayName}: ${streamer.followers.toLocaleString()}`)
})

// Resultados no encontrados.

const notFound = [...participants]

participantsData.forEach((streamer) => {
  if (notFound.includes(streamer.login)) {
    notFound.splice(notFound.indexOf(streamer.login), 1)
  }
})

console.log('\nResultados no encontrados:')
notFound.forEach((participant, index) => console.log(`${index + 1}. ${participant}`))
