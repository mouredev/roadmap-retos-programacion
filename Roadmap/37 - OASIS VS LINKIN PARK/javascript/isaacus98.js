/*
 * EJERCICIO:
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
 * Desarrolla un programa que se conecte al API de Spotify y los compare.
 * Requisitos:
 * 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
 * 2. Conéctate al API utilizando tu lenguaje de programación.
 * 3. Recupera datos de los endpoint que tú quieras.
 * Acciones:
 * 1. Accede a las estadísticas de las dos bandas.
 *    Por ejemplo: número total de seguidores, escuchas mensuales,
 *    canción con más reproducciones...
 * 2. Compara los resultados de, por lo menos, 3 endpoint.
 * 3. Muestra todos los resultados por consola para notificar al usuario.
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular.
 */

class Band {
    constructor(name, followers, bandPopularity, songName, songPopularity) {
        this.name = name
        this.followers = followers
        this.bandPopularity = bandPopularity
        this.songName = songName
        this.songPopularity = songPopularity
    }
}
const idLinkinPark = "6XyY86QOPPrYVGvF9ch6wz"
const idOasis = "2DaxqgrOhkeH0fpeiQq2f4"

let client_id = ""//'CLIENT_ID';
let client_secret = "" //'CLIENT_SECRET';

// Obtener token de spotify
async function getTokenAsync() {
    const response = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        body: new URLSearchParams({
            'grant_type': 'client_credentials',
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + (Buffer.from(client_id + ':' + client_secret).toString('base64')),
        },
    });
    
    return await response.json();
}

async function getArtistInfoAsync(access_token, idArtist) {
    const response = await fetch("https://api.spotify.com/v1/artists/" + idArtist, {
        method: "GET",
        headers: { 'Authorization': 'Bearer ' + access_token }
    })

    return await response.json()
}

async function getTopTracksAsync(access_token, idArtist) {
    const response = await fetch("https://api.spotify.com/v1/artists/" + idArtist + "/top-tracks", {
        method: "GET",
        headers: { 'Authorization': 'Bearer ' + access_token }
    })

    return await response.json()
}

async function mainAsync() {
    const token = await getTokenAsync()
    const infoLinkinPark = await getArtistInfoAsync(token.access_token, idLinkinPark)
    const topTrackLinkinPark = await getTopTracksAsync(token.access_token, idLinkinPark)
    const infoOasis = await getArtistInfoAsync(token.access_token, idOasis)
    const topTrackOasis = await getTopTracksAsync(token.access_token, idOasis)

    let linkinPark = new Band(infoLinkinPark.name, infoLinkinPark.followers.total, infoLinkinPark.popularity, topTrackLinkinPark.tracks[0].name, topTrackLinkinPark.tracks[0].popularity)
    let oasis = new Band(infoOasis.name, infoOasis.followers.total, infoOasis.popularity, topTrackOasis.tracks[0].name, topTrackOasis.tracks[0].popularity)
    
    console.group(linkinPark.name)
    console.log(`Número de seguidores: ${linkinPark.followers}`)
    console.log(`Popularidad de la banda: ${linkinPark.bandPopularity}`)
    console.log(`Canción mas escuchada actualmente: ${linkinPark.songName}, popularidad: ${linkinPark.songPopularity}`)
    console.groupEnd()

    console.group(oasis.name)
    console.log(`Número de seguidores: ${oasis.followers}`)
    console.log(`Popularidad de la banda: ${oasis.bandPopularity}`)
    console.log(`Canción mas escuchada actualmente: ${oasis.songName}, popularidad: ${oasis.songPopularity}`)
    console.groupEnd()

    // Comparación
    let linkinParkScore = 0
    let oasisScore = 0

    linkinPark.followers > oasis.followers ? linkinParkScore++ : oasisScore++
    linkinPark.bandPopularity > oasis.bandPopularity ? linkinParkScore++ : oasisScore++
    linkinPark.songPopularity > oasis.songPopularity ? linkinParkScore++ : oasisScore++

    console.log(`La banda ${linkinParkScore > oasisScore ? linkinPark.name : oasis.name} es mas popular que ${linkinParkScore < oasisScore ? linkinPark.name : oasis.name}`)
}

mainAsync()