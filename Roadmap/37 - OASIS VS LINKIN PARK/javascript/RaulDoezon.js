/*
  EJERCICIO:
  ¡Dos de las bandas más grandes de la historia están de vuelta!
  Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
  Desarrolla un programa que se conecte al API de Spotify y los compare.
  Requisitos:
  1. Crea una cuenta de desarrollo en https://developer.spotify.com.
  2. Conéctate al API utilizando tu lenguaje de programación.
  3. Recupera datos de los endpoint que tú quieras.
  Acciones:
  1. Accede a las estadísticas de las dos bandas.
     Por ejemplo: número total de seguidores, escuchas mensuales,
     canción con más reproducciones...
  2. Compara los resultados de, por lo menos, 3 endpoint.
  3. Muestra todos los resultados por consola para notificar al usuario.
  4. Desarrolla un criterio para seleccionar qué banda es más popular.
*/

// SPOTIFY DEVELOPER DOCUMENTATION: https://developer.spotify.com/documentation/web-api
let oasisData = {}
let linkinParkData = {};
let oasisPoints = 0;
let linkinParkPoints = 0;
const accessToken = 'BQAA3qx2W-B2a48L9gNndfSRf4uxIUUzUHQh9Z7VNMgPoO3bCK3v1jAACqbRHTU9mtu6_24NUgvg1P7FFFmZ0tr6mW_8YX30aMWRRh1Oc6X0-EMzFwo';
const oasisID = '2DaxqgrOhkeH0fpeiQq2f4';
const linkinParkID = '6XyY86QOPPrYVGvF9ch6wz';

async function fetchWebApi(endpoint, method, body) {
  const response = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
    method,
    body:JSON.stringify(body),
  });

  return await response.json();
}

const getArtist = async (artistID) => await fetchWebApi(`v1/artists/${artistID}`, 'GET');
const getAlbums = async (artistID) => await fetchWebApi(`v1/artists/${artistID}/albums`, 'GET');
const getTopTracks = async (artistID) => await fetchWebApi(`v1/artists/${artistID}/top-tracks`, 'GET');

const oasisInformation = getArtist(oasisID);
const oasisAlbums = getAlbums(oasisID);
const oasisTopTracks = getTopTracks(oasisID);
const linkinParkInformation = getArtist(linkinParkID);
const linkinParkAlbums = getAlbums(linkinParkID);
const linkinParkTopTracks = getTopTracks(linkinParkID);

const artistInformation = ((artistArray, data) => {
  artistArray.artist_name = data.name;
  artistArray.total_followers = data.followers.total;
  artistArray.popularity = data.popularity;
});

const albumInformation = ((artistArray, data) => {
  artistArray.recent_album = data.items[0].name;
  artistArray.album_release_date = data.items[0].release_date;
});

const topTracksInformation = ((artistArray, data) => {
  artistArray.track_name = data.tracks[0].name;
  artistArray.track_popularity = data.tracks[0].popularity;
});

oasisInformation.then((response) => artistInformation(oasisData, response));
oasisAlbums.then((response) => albumInformation(oasisData, response));
oasisTopTracks.then((response) => topTracksInformation(oasisData, response));
linkinParkInformation.then((response) => artistInformation(linkinParkData, response));
linkinParkAlbums.then((response) => albumInformation(linkinParkData, response));
linkinParkTopTracks.then((response) => topTracksInformation(linkinParkData, response));

const showData = () => {
  console.log(`${oasisData.artist_name} vs ${linkinParkData.artist_name}`);
  console.log(`Popularity:\n${oasisData.popularity} | ${linkinParkData.popularity}`);
  console.log(`Followers:\n${oasisData.total_followers} | ${linkinParkData.total_followers}`);
  console.log(`Top Track:\n${oasisData.track_name} | ${linkinParkData.track_name}`);
  console.log(`Track popularity:\n${oasisData.track_popularity} | ${linkinParkData.track_popularity}`);
  console.log(`Recent album:\n${oasisData.recent_album} | ${linkinParkData.recent_album}`);
  console.log(`Release date:\n${oasisData.album_release_date} | ${linkinParkData.album_release_date}`);

  oasisData.popularity > linkinParkData.popularity ? oasisPoints += 1 : linkinParkPoints += 1;
  oasisData.total_followers > linkinParkData.total_followers ? oasisPoints += 1 : linkinParkPoints += 1;
  oasisData.track_popularity > linkinParkData.track_popularity ? oasisPoints += 1 : linkinParkPoints += 1;

  console.log(`\n¡${oasisPoints > linkinParkPoints ? oasisData.artist_name : linkinParkData.artist_name} es más popular!`);
}

async function main() {
  await Promise.all([oasisInformation, oasisAlbums, oasisTopTracks, linkinParkInformation, linkinParkAlbums, linkinParkTopTracks]);

  showData();
}

main();
