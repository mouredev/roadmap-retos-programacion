const readline = require('readline');

// Configurar la interfaz para leer la entrada de la terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const clientId = '4cc0a0d989f54e4f8e44da158cf646b0';
const clientSecret = '05fa3d3be3c54a4d941d648c980ca228';

// Obtener el token de acceso de Spotify
async function getAccessToken() {
    const response = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret),
        },
        body: 'grant_type=client_credentials'
    });
    const data = await response.json();
    return data.access_token;
}

// Obtener datos de una banda por su nombre
async function getArtistData(token, artistName) {
    const response = await fetch(`https://api.spotify.com/v1/search?q=${artistName}&type=artist`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    const data = await response.json();
    return data.artists.items[0];  // Retorna la primera coincidencia
}

// Obtener las estadísticas principales
async function getArtistStats(artistId, token) {
    const response = await fetch(`https://api.spotify.com/v1/artists/${artistId}`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    const data = await response.json();
    return {
        name: data.name,
        followers: data.followers.total,
        popularity: data.popularity,
        genres: data.genres,
    };
}

// Obtener las canciones más populares de un artista
async function getArtistTopTracks(artistId, token) {
    const response = await fetch(`https://api.spotify.com/v1/artists/${artistId}/top-tracks?market=US`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    const data = await response.json();
    const mostPopularTrack = data.tracks[0]; // La canción más popular es la primera
    return {
        name: mostPopularTrack.name,
        playCount: mostPopularTrack.popularity, // Popularidad de la canción
        album: mostPopularTrack.album.name
    };
}

// Función para comparar las bandas introducidas por el usuario
async function compareBands(band1, band2) {
    const token = await getAccessToken();
    
    const band1Data = await getArtistData(token, band1);
    const band2Data = await getArtistData(token, band2);
    
    const band1Stats = await getArtistStats(band1Data.id, token);
    const band2Stats = await getArtistStats(band2Data.id, token);
    
    const band1TopTrack = await getArtistTopTracks(band1Data.id, token);
    const band2TopTrack = await getArtistTopTracks(band2Data.id, token);
    
    console.log(`\n${band1} Stats:`, band1Stats);
    console.log(`Canción más popular de ${band1}:`, band1TopTrack);
    
    console.log(`\n${band2} Stats:`, band2Stats);
    console.log(`Canción más popular de ${band2}:`, band2TopTrack);
    
    // Comparar seguidores
    const moreFollowers = (band1Stats.followers > band2Stats.followers)
        ? band1
        : band2;
    
    // Comparar popularidad de las canciones
    const morePopularTrack = (band1TopTrack.playCount > band2TopTrack.playCount)
        ? band1
        : band2;
    
    console.log(`\nLa banda con más seguidores es: ${moreFollowers}`);
    console.log(`La banda con la canción más popular es: ${morePopularTrack}`);
}

// Capturar la entrada del usuario desde la terminal
rl.question('Introduce el nombre del primer grupo: ', (band1) => {
    rl.question('Introduce el nombre del segundo grupo: ', (band2) => {
        // Llamar a la función de comparación
        compareBands(band1, band2).then(() => {
            rl.close();  // Cerrar la interfaz de readline
        }).catch(err => {
            console.error('Error al comparar las bandas:', err);
            rl.close();
        });
    });
});
