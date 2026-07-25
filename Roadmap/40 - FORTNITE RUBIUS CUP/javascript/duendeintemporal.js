//#40 - FORTNITE RUBIUS CUP
/*
 * EJERCICIO:
 * ¡Rubius tiene su propia skin en Fortnite!
 * Y va a organizar una competición para celebrarlo.
 * Esta es la lista de participantes:
 * https://x.com/Rubiu5/status/1840161450154692876
 *
 * Desarrolla un programa que obtenga el número de seguidores en
 * Twitch de cada participante, la fecha de creación de la cuenta 
 * y ordene los resultados en dos listados.
 * - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
 *   (NO subas las credenciales de autenticación)
 * - Crea un ranking por número de seguidores y por antigüedad.
 * - Si algún participante no tiene usuario en Twitch, debe reflejarlo.
 */

//We will use https://jpgtoexcel.com/es to extract the list of the participants from the post image related with the first url of the challenge to a Excell file an then incorpore it to a participant list.

/* We will use Axios to make HTTP requests. You can install it using npm:
#bash
npm install axios */

let log = console.log;

const axios = require('axios');

// Replace here with your Twitch client ID and client secret
const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';

const participants = [
    'ABBY',
    'DJMARIIO',	
    'KIKO RIVERA',
    'NISSAXTER',
    'SHADOUNE',	
    'SILTHURA',
    'ACHE',
    'DOBLE',
    'KNEKRO',
    'OLLI',
    'SPOKSPHORA',
    'SPREEN',
    'ADRI CONTRERAS',
    'ELVISA',
    'KOKO',
    'OUTCONSUMER',
    'PAPI GAVI',
    'PARACETAMOR',
    'AGUSTIN',
    'ELYAS360',
    'KRONONOMZOR',
    'LEVIATHAN',
    'LT KILAH',
    'PATTAC',
    'ALEXBY',
    'FOLAGOR',
    'LOLA LOLITA',
    'PAULA GONI',
    'PAUSENPAI',
    'PERKITA',
    'AMPETER',
    'GREGR',
    'LUH',
    'MANGEL',
    'PLEX',
    'QUACKITY',
    'ARI GAMEPLAYS',
    'HIKA',
    'HIPER',
    'ILAI',
    'MELO',
    'RECEDROP',
    'AUXOZER',
    'IBELKY',
    'ILOI JUAN',
    'MAYICH',
    'RIVERS',
    'ROBERTP',
    'BYCLITOS',
    'IMANOTAD',
    'IRINA ISAIA',
    'MIKEL',
    'ROJER',
    'ROHI',
    'BYVIRUZZ',
    'JESKSU',
    'JOPA',
    'MR. JAGGER',
    'ROJER',
    'RUBIUS',
    'CARRERA',
    'JORIDWILD',
    'KEANI SOUZA',
    'NEXUZ',
    'RIVERA',
    'ZELIN',
    'CHEETO',
    'KERSO',
    'KIDD KEO',
    'NIL OJEDA',
    'SUZYROXX',
    'VICENS',
    'CRYSTALMOLLY',
    'DARIO MELACHE',
    'DHEYO',
    'MOUREDEV',
    'FATZ',
    'BUBBCODE',
    'CODETRAIN',
    'NINJACODE',

];

async function getOAuthToken() {
    const response = await axios.post('https://id.twitch.tv/oauth2/token', null, {
        params: {
            client_id: CLIENT_ID,
            client_secret: CLIENT_SECRET,
            grant_type: 'client_credentials'
        }
    });
    return response.data.access_token;
}

async function getUserData(username, token) {
    try {
        const response = await axios.get(`https://api.twitch.tv/helix/users?login=${username}`, {
            headers: {
                'Client-ID': CLIENT_ID,
                'Authorization': `Bearer ${token}`
            }
        });
        return response.data.data[0]; // Return the first user data
    } catch (error) {
        console.error(`Error fetching data for ${username}:`, error.message);
        return null; 
    }
}

async function getFollowerCount(username, token) {
    try {
        // First, get the user ID for the username
        const userResponse = await axios.get(`https://api.twitch.tv/helix/users?login=${username}`, {
            headers: {
                'Client-ID': CLIENT_ID,
                'Authorization': `Bearer ${token}`
            }
        });

        const userId = userResponse.data.data[0].id;

        // Now, get the followers for that user
        const followsResponse = await axios.get(`https://api.twitch.tv/helix/users/follows?to_id=${userId}`, {
            headers: {
                'Client-ID': CLIENT_ID,
                'Authorization': `Bearer ${token}`
            }
        });

        // The number of followers is the total count
        return followsResponse.data.total; // This gives the total number of followers
    } catch (error) {
        console.error(`Error fetching follower count for ${username}:`, error.message);
        return 'N/A'; // Return 'N/A' if there's an error
    }
}

// Main function to fetch and display data
async function fetchParticipantsData() {
    const token = await getOAuthToken();
    const results = [];

    for (const username of participants) {
        const userData = await getUserData(username, token);
        if (userData) {
            const followerCount = await getFollowerCount(username, token);
            results.push({
                username: userData.login,
                followers: followerCount,
                createdAt: new Date(userData.created_at),
            });
        } else {
            results.push({
                username: username,
                followers: 'N/A',
                createdAt: 'N/A',
            });
        }
    }

    // Sort by followers
    const sortedByFollowers = results.sort((a, b) => {
        return (b.followers === 'N/A' ? -1 : b.followers) - (a.followers === 'N/A' ? -1 : a.followers);
    });

    // Sort by account creation date
    const sortedByCreationDate = results.sort((a, b) => {
        return new Date(b.createdAt) - new Date(a.createdAt);
    });

    log('Ranking by Followers:');
    console.table(sortedByFollowers);

    log('Ranking by Account Creation Date:');
    console.table(sortedByCreationDate);
}

fetchParticipantsData();
