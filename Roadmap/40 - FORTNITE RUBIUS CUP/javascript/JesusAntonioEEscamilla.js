/** #37 - JavaScript -> Jesus Antonio Escamilla */

/**
 * FORTNITE RUBIUS CUP.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const participants = [
    'Abby', 'Ache', 'Adri Contreras', 'Agustin', 'Alexby', 'Ampeter', 'Ander', 'Ari Gameplays',
    'Arigely', 'Auronplay', 'Axozer', 'Beniju', 'By Calitos', 'Byviruzz', 'Carrera', 'Celopan',
    'Cheto', 'CrystalMolly', 'Dario Eme Hache', 'Dheyo', 'DjMariio', 'Doble', 'Elvisa', 'Elyas360',
    'Folagor', 'Grefg', 'Guanyar', 'Hika', 'Hiper', 'Ibai', 'Ibelky', 'Illojuan', 'Imantado',
    'Irina Isasia', 'JessKiu', 'Jopa', 'JordiWild', 'Kenai Souza', 'Keroro', 'Kidd Keo', 'Kiko Rivera',
    'Knekro', 'Koko', 'KronnoZomber', 'Leviathan', 'Lit Killah', 'Lola Lolita', 'Lolito', 'Luh',
    'Luzu', 'Mangel', 'Mayichi', 'Melo', 'MissaSinfonia', 'Mixwell', 'Mr. Jagger', 'Nate Gentile',
    'Nexxuz', 'Nia', 'Nil Ojeda', 'NissaXter', 'Ollie', 'Orslok', 'Outconsumer', 'Papi Gavi',
    'Paracetamor', 'Patica', 'Paula Gonu', 'Pausenpaii', 'Perxitaa', 'Plex', 'Polispol', 'Quackity',
    'RecueroDP', 'Reven', 'Rivers', 'RobertPG', 'Roier', 'Rojuu', 'Rubius', 'Shadoune', 'Silithur',
    'SpokSponha', 'Spreen', 'Spursito', 'Staxx', 'SuzyRoxx', 'Vicens', 'Vituber', 'Werlyb', 'Xavi',
    'Xcry', 'Xokas', 'Zarcort', 'Zeling', 'Zorman'
];

const twitch_clientId = 'y6di6t9mk7ihz9hyqt32wh67rguhzi';
const twitch_clientSecret = 'o887i5ph5u94u6aapqvocrnpedl3oo';

// Para obtener un token
async function tokenAccessTwitch(clientId, clientSecret) {
    const response = await fetch(`https://id.twitch.tv/oauth2/token`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `client_id=${clientId}&client_secret=${clientSecret}&grant_type=client_credentials`
    });

    if (!response.ok) {
        console.error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    return result.access_token;
}

// Para obtener el acceso a Twitch
async function fetchTwitchAPI(endpoint) {
    const tokenAccess = await tokenAccessTwitch(twitch_clientId, twitch_clientSecret)
    const response = await fetch(`https://api.twitch.tv/helix${endpoint}`, {
        headers:{
            'Client-ID': twitch_clientId,
            'Authorization': `Bearer ${tokenAccess}`
        }
    });

    if (!response.ok) {
        console.error(`Error en la API de Twitch: ${response.status}`);
    }
    return response.json();
}

// Para obtener los datos los participantes
async function getUserInfo(username) {
    username = username.replace(/[^a-zA-Z0-9_]/g, '');
    const userData = await fetchTwitchAPI(`/users?login=${username}`)
    if (userData.data.length > 0) {
        const user = userData.data[0];
        const followersData = await fetchTwitchAPI(`/channels/followers?broadcaster_id=${user.id}`)
        return{
            username: user.login,
            displayName: user.display_name,
            followers: followersData.total,
            createdAt: user.created_at
        };
    }
    return null;
}

async function rankingGammer() {
    const participantInfo = [];

    for (const participant of participants) {
        const info = await getUserInfo(participant)
        if (info) {
            participantInfo.push(info);
        } else {
            console.log(`${participant} no tiene cuenta de Twitch o no se pudo obtener la información.`);
        }
    }

    // Ranking por número de seguidores
    const followerRanking = [...participantInfo].sort((a, b) => b.followers - a.followers);
    
    console.log("Ranking por número de seguidores:");
    followerRanking.forEach((p, index) => {
        console.log(`${index + 1}. ${p.displayName}: ${p.followers} seguidores`);
    });

    // Ranking por antigüedad
    const ageRanking = [...participantInfo].sort((a, b) => new Date(a.createdAt) - new Date(b.createdAt));
    
    console.log("\nRanking por antigüedad de cuenta:");
    ageRanking.forEach((p, index) => {
        console.log(`${index + 1}. ${p.displayName}: Cuenta creada el ${new Date(p.createdAt).toLocaleDateString()}`);
    });
}

// Ejecutar el programa
rankingGammer()