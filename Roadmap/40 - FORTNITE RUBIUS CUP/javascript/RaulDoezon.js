/*
  EJERCICIO:
  ¡Rubius tiene su propia skin en Fortnite!
  Y va a organizar una competición para celebrarlo.
  Esta es la lista de participantes:
  https://x.com/Rubiu5/status/1840161450154692876
 
  Desarrolla un programa que obtenga el número de seguidores en
  Twitch de cada participante, la fecha de creación de la cuenta 
  y ordene los resultados en dos listados.
  - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
    (NO subas las credenciales de autenticación)
  - Crea un ranking por número de seguidores y por antigüedad.
  - Si algún participante no tiene usuario en Twitch, debe reflejarlo.
*/

const accessToken = 'ACCESS_TOKEN';
const clientID = 'CLIENT_ID';
const userNames = [
  'abby', 'Ache', 'AdriContreras4', 'agustin51', 'Alexby11', 'Ampeterby7', 'tvandeR', 'AriGameplays', 'AriGeli', 'auronplay',
  'aXoZer', 'BENIJU03', 'bycalitos', 'byViruZz', 'Carreraaa', 'Celopan', 'srcheeto', 'CrystalMolly', 'darioemehache', 'Dheylo',
  'DjMaRiiO', 'Doble', 'ElvisaYomastercard', 'elyas360', 'FolagorLives', 'TheGrefg', 'GUANYAR', 'Hika', 'Hiperop', 'ibai',
  'ibelky_', 'IlloJuan', 'imantado', 'IRINA__ISASIA', 'Jesskiu', 'JOPA', 'JordiWild', 'kenaivsouza', 'MrKeroro10', 'TheKiddKeo95',
  'KikoRivera', 'knekro', 'KOKO', 'KronnoZomberOficial', 'Leviathan', 'LITkillah', 'lolalolita', 'LolitoLp', 'Luh', 'Luzu',
  'Mangel', 'Mayichi', 'melo', 'MissaSinfonia', 'Mixwell', 'JaggerPrincesa', 'NateGentile7', 'Nexxuz', 'LakshartNia', 'nilojeda',
  'Nissaxter', 'OllieGamerz', 'orslok', 'Outconsumer', 'PapiGaviTV', 'paracetamor', 'patica1999', 'paulagonu', 'PauSenpaii', 'Perxitaa',
  'NoSoyPlex', 'polispol1', 'Quackity', 'Recuerd0p', 'ReventXz', 'rivers_gg', 'robertpg', 'Roier', 'ROJUU', 'Rubius',
  'Shadoune666', 'Silithur', 'spok_sponha', 'ElSpreen', 'Spursito', 'bysTaXx', 'Suzyroxx', 'Vicens', 'vitu', 'Werlyb',
  'Xavi', 'xCry', 'elxokas', 'theZARCORT', 'Zeling', 'ZormanWorld',
].map((nickname) => nickname.toLowerCase());
let streamersList = '';
let streamers = [];
let sortByDate;
let sortByFollowers;

for (let index = 0; index < userNames.length; index++) {
  streamersList += `${index > 0 ? '&' : ''}login=${userNames[index]}`;
}

async function fetchTwichAPI(endpoint, method, body) {
  try {
    const response = await fetch(`https://api.twitch.tv/helix/${endpoint}`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Client-id": clientID,
      },
      method,
      body: JSON.stringify(body),
    });

    return await response.json();
  } catch(error) {
    console.log(error);
  }
}

const prepareData = async (login) => {
  const broadcasters = await fetchTwichAPI(`users?${login}`, 'GET');

  for (const broadcaster of broadcasters.data) {
    let broadcasterFollowers = await fetchTwichAPI(`channels/followers?broadcaster_id=${broadcaster.id}`, 'GET');

    streamers.push({ name: broadcaster.login, date: broadcaster.created_at, followers: broadcasterFollowers.total });
  }

  sortByDate = [...streamers].sort((a, b) => new Date(a.date) - new Date(b.date));
  sortByFollowers = [...streamers].sort((c, d) => d.followers - c.followers);
}

const createTables = () => {
  console.log('\nRANKING POR ANTIGÜEDAD');

  for (let index = 0; index < sortByDate.length; index++) {
    console.log(`${index + 1}. Streamer: ${sortByDate[index].name} | Fecha de creación: ${sortByDate[index].date}`);
  }

  console.log('\nRANKING POR SEGUIDORES');

  for (let index = 0; index < sortByFollowers.length; index++) {
    console.log(`${index + 1}. Streamer: ${sortByFollowers[index].name} | Seguidores: ${sortByFollowers[index].followers}`);
  }

  console.log('\nPERSONAS SIN CUENTA EN TWICH');

  for (let index = 0; index < userNames.length; index++) {
    if (streamers.map(element => element.name).indexOf(userNames[index]) === -1) {
      console.log(`- ${userNames[index]}`);
    }
  }
}

async function showInformation() {
  await Promise.all([prepareData(streamersList)]);

  createTables();
}

showInformation();
