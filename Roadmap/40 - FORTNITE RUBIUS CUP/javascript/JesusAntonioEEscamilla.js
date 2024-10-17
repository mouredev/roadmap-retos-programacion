/** #40 - JavaScript -> Jesus Antonio Escamilla */

/**
 * FORTNITE RUBIUS CUP.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const participants = [
    "littleragergirl", "ache", "adricontreras4", "agustin51", "alexby11", "ampeterby7", "tvander",
    "arigameplays", "arigeli_", "auronplay", "axozer", "beniju03", "bycalitos",
    "byviruzz", "carreraaa", "celopan", "srcheeto", "crystalmolly", "darioemehache",
    "dheylo", "djmariio", "doble", "elvisayomastercard", "elyas360", "folagorlives", "thegrefg",
    "guanyar", "hika", "hiperop", "ibai", "ibelky_", "illojuan", "imantado",
    "irinaissaia", "jesskiu", "jopa", "jordiwild", "kenaivsouza", "mrkeroro10",
    "thekiddkeo95", "kikorivera", "knekro", "kokoop", "kronnozomberoficial", "leviathan",
    "litkillah", "lolalolita", "lolitofdez", "luh", "luzu", "mangel", "mayichi",
    "melo", "missasinfonia", "mixwell", "jaggerprincesa", "nategentile7", "nexxuz",
    "lakshartnia", "nilojeda", "nissaxter", "olliegamerz", "orslok", "outconsumer", "papigavitv",
    "paracetamor", "patica1999", "paulagonu", "pausenpaii", "perxitaa", "nosoyplex",
    "polispol1", "quackity", "recuerd0p", "reventxz", "rivers_gg", "robertpg", "roier",
    "ceuvebrokenheart", "rubius", "shadoune666", "silithur", "spok_sponha", "elspreen", "spursito",
    "bystaxx", "suzyroxx", "vicens", "vitu", "werlyb", "xavi", "xcry", "elxokas",
    "thezarcort", "zeling", "zormanworld", "mouredev"
];

const twitch_clientId = 'MY_ID_TWITCH';
const twitch_clientSecret = 'MY_SECRET_TWITCH';

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