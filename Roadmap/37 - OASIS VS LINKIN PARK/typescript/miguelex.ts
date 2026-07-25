import fetch from 'node-fetch';
import readlineSync from 'readline-sync';

const clientId = 'YOUR_CLIENT_ID';
const clientSecret = 'YOUR_CLIENT_SECRET';

async function getAccessToken(): Promise<string> {
    const response = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        headers: {
            'Authorization': `Basic ${Buffer.from(`${clientId}:${clientSecret}`).toString('base64')}`,
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'grant_type=client_credentials',
    });
    
    const data = await response.json();
    return data.access_token;
}

async function getArtistData(token: string, artistName: string) {
    const response = await fetch(`https://api.spotify.com/v1/search?q=${encodeURIComponent(artistName)}&type=artist`, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    const data = await response.json();
    return data.artists.items[0];  
}

async function getArtistStats(artistId: string, token: string) {
    const response = await fetch(`https://api.spotify.com/v1/artists/${artistId}`, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    const data = await response.json();
    return {
        name: data.name,
        followers: data.followers.total,
        popularity: data.popularity,
        genres: data.genres
    };
}

async function getArtistTopTracks(artistId: string, token: string) {
    const response = await fetch(`https://api.spotify.com/v1/artists/${artistId}/top-tracks?market=US`, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    const data = await response.json();
    const mostPopularTrack = data.tracks[0];
    return {
        name: mostPopularTrack.name,
        playCount: mostPopularTrack.popularity,
        album: mostPopularTrack.album.name
    };
}

async function compareBands(band1: string, band2: string) {
    const token = await getAccessToken();
    
    const band1Data = await getArtistData(token, band1);
    const band2Data = await getArtistData(token, band2);
    
    const band1Stats = await getArtistStats(band1Data.id, token);
    const band2Stats = await getArtistStats(band2Data.id, token);
    
    const band1TopTrack = await getArtistTopTracks(band1Data.id, token);
    const band2TopTrack = await getArtistTopTracks(band2Data.id, token);
    
    console.log(`${band1} Stats:`, band1Stats);
    console.log(`Canción más popular de ${band1}:`, band1TopTrack);
    
    console.log(`${band2} Stats:`, band2Stats);
    console.log(`Canción más popular de ${band2}:`, band2TopTrack);
    
    const moreFollowers = (band1Stats.followers > band2Stats.followers) ? band1 : band2;
    const morePopularTrack = (band1TopTrack.playCount > band2TopTrack.playCount) ? band1 : band2;
    
    console.log(`\nLa banda con más seguidores es: ${moreFollowers}`);
    console.log(`La banda con la canción más popular es: ${morePopularTrack}`);
}

const band1 = readlineSync.question('Introduce el nombre del primer grupo: ');
const band2 = readlineSync.question('Introduce el nombre del segundo grupo: ');

compareBands(band1, band2);
