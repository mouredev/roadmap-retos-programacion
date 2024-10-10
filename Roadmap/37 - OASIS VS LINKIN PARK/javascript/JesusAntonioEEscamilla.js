/** #37 - JavaScript -> Jesus Antonio Escamilla */

/**
 * OASIS VS LINKIN PARK.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const clientId = SPOTIFY_CLIENT_ID_MY;
const clientSecret = SPOTIFY_CLIENT_SECRET_MY;
// Para el contador
let artist_1_counter = 0;
let artist_2_counter = 0;

// Obtener token de acceso
async function getAccessToken() {
    const response = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        headers: {
            'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret),
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'grant_type=client_credentials'
    });

    if (response.status != 200) {
        console.error(`Error obteniendo el token de Spotify: ${response.json()}`)
    }
    const data = await response.json();
    return data.access_token;
}

// Obtener los Id de las bandas
async function getSearchArtist(artistName, accessToken) {
    const response = await fetch(`https://api.spotify.com/v1/search?q=${artistName}&type=artist&limit=1`, {
        headers: {
            'Authorization': `Bearer ${accessToken}`
        }
    });

    if (response.status != 200) {
        console.error('Error obteniendo el artista')
    }
    const data = await response.json();
    return data.artists.items[0].id;
}

// Obtener los Datos de las bandas
async function getArtistData(artistId, accessToken) {
    const response = await fetch(`https://api.spotify.com/v1/artists/${artistId}`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${accessToken}`
        }
    });

    if (response.status != 200) {
        console.error('Error obteniendo los datos del artista')
    }
    const data = await response.json();
    return {
        "name": data.name,
        "followers": data.followers.total,
        "popularity": data.popularity,
    }
}

// Obtener la música mas sonada de las bandas
async function getArtistTopTrack(artistId, accessToken) {
    const response = await fetch(`https://api.spotify.com/v1/artists/${artistId}/top-tracks`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${accessToken}`
        }
    });

    if (response.status != 200) {
        console.error('Error obteniendo las canciones del artista')
    }
    const data = await response.json();
    const result = data.tracks[0]
    return {
        "name": result.name,
        "popularity": result.popularity,
    }
}

// Comparar datos de Oasis y Linkin Park
async function compareBands() {
    // Acceso al Token
    const accessToken = await getAccessToken(clientId, clientSecret);
    
    // El Id de las bandas
    const artist_1_id = await getSearchArtist('Oasis', accessToken);
    const artist_2_id = await getSearchArtist('Linkin Park', accessToken);

    const artist_1_data = await getArtistData(artist_1_id, accessToken);
    const artist_2_data = await getArtistData(artist_2_id, accessToken);

    const artist_1_topTrack = await getArtistTopTrack(artist_1_id, accessToken);
    const artist_2_topTrack = await getArtistTopTrack(artist_2_id, accessToken);

    console.group('Los artistas:');
        console.group(artist_1_data.name);
        console.log(`Seguidores es de ${artist_1_data.followers}`);
        console.log(`Popularidad al mundo es ${artist_1_data.popularity}`);
        console.log(`Canción mas popular es ${artist_1_topTrack.popularity}`);
        console.groupEnd();

        console.group(artist_2_data.name);
        console.log(`Seguidores es de ${artist_2_data.followers}`);
        console.log(`Popularidad al mundo es ${artist_2_data.popularity}`);
        console.log(`Canción mas popular es ${artist_2_topTrack.popularity}`);
        console.groupEnd();
    console.groupEnd();

    console.group('\nComparación de los artistas:');
        artist_1_data.followers > artist_2_data.followers ? (console.log(`${artist_1_data.name} es más popular en número de seguidores.`), artist_1_counter++) : (console.log(`${artist_2_data.name} es más popular en número de seguidores.`), artist_2_counter++);
        artist_1_data.popularity > artist_2_data.popularity ? (console.log(`${artist_1_data.name} es más popular a nivel general.`), artist_1_counter++) : (console.log(`${artist_2_data.name}  es más popular a nivel general.`), artist_2_counter++);
        artist_1_topTrack.popularity > artist_2_topTrack.popularity ? (console.log(`La canción ${artist_1_topTrack.name} de ${artist_1_data.name} es más popular.`), artist_1_counter++) : (console.log(`La canción ${artist_2_topTrack.name} de ${artist_2_data.name} es más popular.`), artist_2_counter++);
    console.groupEnd();

    console.log(`\nGanador es ${artist_1_counter > artist_2_counter ? artist_1_data.name : artist_2_data.name}`)
}

// Uso del programa
compareBands();