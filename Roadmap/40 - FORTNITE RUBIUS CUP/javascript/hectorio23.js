// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

// npm install axios
const axios = require('axios');

// Función para obtener datos de un usuario de Twitch.
async function getTwitchUserData(username, authToken) {
    const headers = {
        'Client-ID': 'YOUR_CLIENT_ID',
        'Authorization': `Bearer ${authToken}`
    };
    
    try {
        const response = await axios.get(`https://api.twitch.tv/helix/users?login=${username}`, { headers });
        if (response.data.data.length > 0) {
            const user = response.data.data[0];
            const followers = await getTwitchFollowers(user.id, authToken);
            return { username, followers, created_at: user.created_at };
        } else {
            return { username, followers: null, created_at: null };
        }
    } catch (error) {
        console.error(`Error fetching data for ${username}:`, error);
    }
}

// Función para obtener el número de seguidores de un usuario de Twitch.
async function getTwitchFollowers(userId, authToken) {
    const headers = {
        'Client-ID': 'YOUR_CLIENT_ID',
        'Authorization': `Bearer ${authToken}`
    };
    
    const response = await axios.get(`https://api.twitch.tv/helix/users/follows?to_id=${userId}`, { headers });
    return response.data.total;
}

// Genera el ranking por seguidores y por antigüedad.
async function generateRankings(participants, authToken) {
    const userData = await Promise.all(participants.map(user => getTwitchUserData(user, authToken)));
    
    // Ranking por seguidores.
    const byFollowers = userData.filter(u => u.followers !== null).sort((a, b) => b.followers - a.followers);
    
    // Ranking por antigüedad.
    const byCreationDate = userData.filter(u => u.created_at !== null).sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
    
    return { byFollowers, byCreationDate };
}

// Ejemplo de uso.
(async () => {
    const participants = ["user1", "user2", "user3"];
    const authToken = "YOUR_AUTH_TOKEN";

    const { byFollowers, byCreationDate } = await generateRankings(participants, authToken);

    console.log("Ranking por seguidores:");
    byFollowers.forEach(user => console.log(`${user.username} - ${user.followers} seguidores`));

    console.log("\nRanking por antigüedad:");
    byCreationDate.forEach(user => console.log(`${user.username} - Creado el ${user.created_at}`));
})();
