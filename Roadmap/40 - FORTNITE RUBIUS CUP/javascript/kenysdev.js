/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#40 FORTNITE RUBIUS CUP
-------------------------------------------------------
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
// ________________________________________________________
const axios = require('axios');
const dotenv = require('dotenv');
const { DateTime } = require('luxon');

class Twitch {
    constructor(clientId, clientSecret) {
        this.clientId = clientId;
        this.clientSecret = clientSecret;
        this.accessToken = null;
    }

    async ensureAccessToken() {
        if (!this.accessToken) {
            const params = new URLSearchParams({
                client_id: this.clientId,
                client_secret: this.clientSecret,
                grant_type: 'client_credentials'
            });

            try {
                const response = await axios.post('https://id.twitch.tv/oauth2/token', params);
                this.accessToken = response.data.access_token;
            } catch (error) {
                throw new Error(`Error obtaining token: ${error.message}`);
            }
        }
    }

    getHeaders() {
        return {
            'Client-Id': this.clientId,
            'Authorization': `Bearer ${this.accessToken}`
        };
    }

    async getFollowers(userId) {
        const url = `https://api.twitch.tv/helix/channels/followers?broadcaster_id=${userId}`;
        
        try {
            const response = await axios.get(url, { headers: this.getHeaders() });
            return response.data.total || 0;
        } catch (error) {
            throw new Error(`Error getting followers: ${error.message}`);
        }
    }

    async getUserData(userName) {
        await this.ensureAccessToken();
        const url = `https://api.twitch.tv/helix/users?login=${userName}`;

        try {
            const response = await axios.get(url, { headers: this.getHeaders() });
            const userData = response.data.data[0];

            if (!userData) {
                return null;
            }

            const followers = await this.getFollowers(userData.id);

            return {
                username: userName,
                createdAt: DateTime.fromISO(userData.created_at),
                followers
            };
        } catch (error) {
            throw new Error(`Error getting user data: ${error.message}`);
        }
    }
}

function printRankings(usersData) {
    const byFollowers = [...usersData].sort((a, b) => b.followers - a.followers);
    const byDate = [...usersData].sort((a, b) => a.createdAt.toMillis() - b.createdAt.toMillis());

    console.log('\nRanking por número de seguidores:');
    byFollowers.forEach((user, i) => {
        console.log(`${i + 1} - ${user.username}: ${user.followers} seguidores`);
    });

    console.log('\nRanking por antigüedad:');
    byDate.forEach((user, i) => {
        console.log(`${i + 1} - ${user.username}: Creado el ${user.createdAt.toFormat('dd/MM/yyyy')}`);
    });
}

async function processUsers(users, tw) {
    const usersData = [];
    const notFoundUsers = [];
    console.log('Obteniendo datos...');

    for (const name of users) {
        try {
            const userData = await tw.getUserData(name);
            if (userData) {
                usersData.push(userData);
            } else {
                notFoundUsers.push(name);
            }
        } catch (error) {
            notFoundUsers.push(name);
        }
    }

    printRankings(usersData);

    if (notFoundUsers.length > 0) {
        console.log('\nUsuarios no encontrados:');
        notFoundUsers.forEach(user => console.log(user));
    }
}

async function main() {
    dotenv.config();
    const clientId = process.env.TWITCH_CLIENT_ID;
    const clientSecret = process.env.TWITCH_CLIENT_SECRET;

    if (!clientId || !clientSecret) {
        console.error('CLIENT_ID o CLIENT_SECRET no encontrados en .env');
        process.exit(1);
    }

    const twitch = new Twitch(clientId, clientSecret);
    
    const users = [
        "abby", "ache", "adricontreras", "agustin", "alexby", "ampeter", "ander",
        "arigameplays", "arigeli", "auronplay", "axozer", "beniju", "bycalitos",
        "byviruzz", "carrera", "celopan", "cheeto", "crystalmolly", "darioemehache",
        "dheyo", "djmario", "doble", "elvisa", "elyas360", "folagor", "grefg",
        "guanyar", "hika", "hiper", "ibai", "ibelky", "illojuan", "imantado",
        "irinaisasia", "jesskiu", "jopa", "jordiwild", "kenaisouza", "keroro",
        "kiddkeo", "kikorivera", "knekro", "koko", "kronnozomber", "leviathan",
        "litkillah", "lolalolita", "lolito", "luh", "luzu", "mangel", "mayichi",
        "melo", "missasinonia", "mixwell", "mrjagger", "nategentile", "nexxuz",
        "nia", "nilojeda", "nissaxter", "ollie", "orslok", "outconsumer", "papigavi",
        "paracetamor", "patica", "paulagonu", "pausenpaii", "perxitaa", "plex",
        "polispol", "quackity", "recuerdop", "reven", "rivers", "robertpg", "roier",
        "rojuu", "rubius", "shadoune", "silithur", "spoksponha", "spreen", "spursito",
        "staxx", "suzyroxx", "vicens", "vituber", "werlyb", "xavi", "xcry", "xokas",
        "zarcort", "zeling", "zorman"
    ];

    try {
        await processUsers(users, twitch);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

main();
