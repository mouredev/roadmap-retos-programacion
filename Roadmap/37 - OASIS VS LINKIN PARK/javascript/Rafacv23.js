// Hecho por @Rafacv23 | https://github.com/Rafacv23 | https://twitter.com/rafacanosa | https://www.rafacanosa.dev

// ID's generados por spotify, para ejecutar este código debes usar los tuyos propios, también sería interesante utilizar una extensión de archivo .mjs, para que funcione correctamente la asincronia
const CLIENT_ID = "your-client-id"
const CLIENT_SECRET = "your-client-secret"

// función para obtener el token de acceso a la api de spotify
async function getSpotifyToken(clientId, clientSecret) {
  const tokenResponse = await fetch("https://accounts.spotify.com/api/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      grant_type: "client_credentials",
      client_id: clientId,
      client_secret: clientSecret,
    }),
  })

  if (tokenResponse.status !== 200) {
    const error = await tokenResponse.json()
    throw new Error(`Error: ${JSON.stringify(error)}`)
  }

  const token = await tokenResponse.json()
  return token.access_token
}

// almacenamos el token de acceso a la api de spotify
const accessToken = await getSpotifyToken(CLIENT_ID, CLIENT_SECRET)
const authorization = { headers: { Authorization: `Bearer ${accessToken}` } }

// función encargada de recuperar la información de un artista, pasandole su nombre
async function getArtistData(artist) {
  const url = `https://api.spotify.com/v1/search?q=${encodeURIComponent(
    artist
  )}&type=artist&limit=1`

  const res = await fetch(url, authorization)

  if (res.status !== 200) {
    const error = await res.json()
    throw new Error(
      `Error retrieving artist data ${artist}: ${JSON.stringify(error)}`
    )
  }

  const results = await res.json()

  if (!results.artists || results.artists.items.length === 0) {
    throw new Error(`Artista ${artist} no ha sido encontrado.`)
  }

  const artistData = results.artists.items[0]

  return {
    id: artistData.id,
    name: artistData.name,
    followers: artistData.followers.total,
    popularity: artistData.popularity,
    genres: artistData.genres,
  }
}

// almacenamos los datos de los artistas
const linkinPark = await getArtistData("Linkin Park")
const oasis = await getArtistData("Oasis")

// comparamos la popularidad de los dos artistas
const morePopularBand =
  linkinPark.popularity > oasis.popularity ? "Linkin Park" : "Oasis"

console.log("Linkin Park Data:", linkinPark)
console.log("Oasis Data:", oasis)
console.log(`El más popular de los dos es ${morePopularBand}.`)

/**Salida esperada por consola
 * Linkin Park Data: {
  id: '6XyY86QOPPrYVGvF9ch6wz',
  name: 'Linkin Park',
  followers: 27123544,
  popularity: 92,
  genres: [
    'alternative metal',
    'nu metal',
    'post-grunge',
    'rap metal',
    'rock'
  ]
}
Oasis Data: {
  id: '2DaxqgrOhkeH0fpeiQq2f4',
  name: 'Oasis',
  followers: 10740804,
  popularity: 83,
  genres: [ 'beatlesque', 'britpop', 'madchester', 'permanent wave', 'rock' ]
}
El más popular de los dos es Linkin Park.
 */
