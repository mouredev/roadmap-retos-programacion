/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#37 OASIS VS LINKIN PARK
-------------------------------------------------------
* ¡Dos de las bandas más grandes de la historia están de vuelta!
* Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
* Desarrolla un programa que se conecte al API de Spotify y los compare.
* Requisitos:
* 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
* 2. Conéctate al API utilizando tu lenguaje de programación.
* 3. Recupera datos de los endpoint que tú quieras.
* Acciones:
* 1. Accede a las estadísticas de las dos bandas.
*    Por ejemplo: número total de seguidores, escuchas mensuales,
*    canción con más reproducciones...
* 2. Compara los resultados de, por lo menos, 3 endpoint.
* 3. Muestra todos los resultados por consola para notificar al usuario.
* 4. Desarrolla un criterio para seleccionar qué banda es más popular.
*/
// ________________________________________________________
require('dotenv').config();
const https = require('https');

const SPOTIFY_CLIENT_ID = process.env.SPOTIFY_CLIENT_ID;
const SPOTIFY_CLIENT_SECRET = process.env.SPOTIFY_CLIENT_SECRET;

const getSpotifyAccessToken = async () => {
  const options = {
    hostname: "accounts.spotify.com",
    path: "/api/token",
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      Authorization: `Basic ${Buffer.from(
        `${SPOTIFY_CLIENT_ID}:${SPOTIFY_CLIENT_SECRET}`
      ).toString("base64")}`,
    },
  };

  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let data = "";

      res.on("data", (chunk) => {
        data += chunk;
      });

      res.on("end", () => {
        const response = JSON.parse(data);
        resolve(response.access_token);
      });
    });

    req.on("error", (e) => {
      reject(e);
    });

    req.write("grant_type=client_credentials");
    req.end();
  });
};

const spotifyAPIRequest = async (endpoint, accessToken) => {
  const options = {
    hostname: "api.spotify.com",
    path: endpoint,
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  };

  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let data = "";

      res.on("data", (chunk) => {
        data += chunk;
      });

      res.on("end", () => {
        resolve(JSON.parse(data));
      });
    });

    req.on("error", (e) => {
      reject(e);
    });

    req.end();
  });
};

class Spotify {
  constructor() {
    this.accessToken = null;
  }

  async authenticate() {
    this.accessToken = await getSpotifyAccessToken();
  }

  async getArtists(name) {
    const results = await spotifyAPIRequest(
      `/v1/search?q=artist:${encodeURIComponent(name)}&type=artist&limit=3`,
      this.accessToken
    );
    return results.artists ? results.artists.items : [];
  }

  async getMostPopularArtist(name) {
    const artists = await this.getArtists(name);
    if (artists.length === 0) return null;

    return artists.sort((a, b) => b.popularity - a.popularity)[0];
  }

  async artistTopTracks(artistId) {
    const results = await spotifyAPIRequest(
      `/v1/artists/${artistId}/top-tracks?market=US`,
      this.accessToken
    );
    return results.tracks || [];
  }

  async artistAlbums(artistId) {
    const results = await spotifyAPIRequest(
      `/v1/artists/${artistId}/albums?album_type=album`,
      this.accessToken
    );
    return results.items || [];
  }
}

// Clase Versus
class Versus {
  constructor(artist1, artist2, spotifyInstance) {
    this.a1 = artist1;
    this.a2 = artist2;
    this.sp = spotifyInstance;
    this.a1Score = 0;
    this.a2Score = 0;
  }

  popularity() {
    console.log(`Popularidad: ${this.a1.popularity} vs ${this.a2.popularity}`);
    if (this.a1.popularity > this.a2.popularity) this.a1Score++;
    else if (this.a2.popularity > this.a1.popularity) this.a2Score++;
  }

  followers() {
    console.log(
      `Seguidores: ${this.a1.followers.total} vs ${this.a2.followers.total}`
    );
    if (this.a1.followers.total > this.a2.followers.total) this.a1Score++;
    else if (this.a2.followers.total > this.a1.followers.total) this.a2Score++;
  }

  async top3Tracks() {
    const a1Tracks = await this.sp.artistTopTracks(this.a1.id);
    const a2Tracks = await this.sp.artistTopTracks(this.a2.id);

    const a1Popularity = a1Tracks.slice(0, 3).reduce((sum, track) => sum + track.popularity, 0);
    const a2Popularity = a2Tracks.slice(0, 3).reduce((sum, track) => sum + track.popularity, 0);

    console.log(`Popularidad Top 3 canciones: ${a1Popularity} vs ${a2Popularity}`);
    if (a1Popularity > a2Popularity) this.a1Score++;
    else if (a2Popularity > a1Popularity) this.a2Score++;
  }

  async albumsAndActiveYears() {
    const a1Albums = await this.sp.artistAlbums(this.a1.id);
    const a2Albums = await this.sp.artistAlbums(this.a2.id);

    console.log(`Número de álbumes: ${a1Albums.length} vs ${a2Albums.length}`);
    if (a1Albums.length > a2Albums.length) this.a1Score++;
    else if (a2Albums.length > a1Albums.length) this.a2Score++;

    const a1Years = new Set(a1Albums.map((album) => album.release_date.slice(0, 4)));
    const a2Years = new Set(a2Albums.map((album) => album.release_date.slice(0, 4)));

    console.log(`Años activos: ${a1Years.size} vs ${a2Years.size}`);
    if (a1Years.size > a2Years.size) this.a1Score++;
    else if (a2Years.size > a1Years.size) this.a2Score++;
  }

  finalResult() {
    console.log("\nRESULTADO FINAL:");
    console.log(`${this.a1.name}: ${this.a1Score} puntos`);
    console.log(`${this.a2.name}: ${this.a2Score} puntos`);

    if (this.a1Score > this.a2Score) {
      console.log(`\n¡'${this.a1.name}' gana el versus!`);
    } else if (this.a2Score > this.a1Score) {
      console.log(`\n¡'${this.a2.name}' gana el versus!`);
    } else {
      console.log("\n¡Es un empate!");
    }
  }

  async start() {
    console.log(`${this.a1.name} vs ${this.a2.name}`);
    this.popularity();
    this.followers();
    await this.top3Tracks();
    await this.albumsAndActiveYears();
    this.finalResult();
  }
}

const main = async () => {
  const spotify = new Spotify();
  await spotify.authenticate();

  const artist1 = await spotify.getMostPopularArtist("Oasis");
  const artist2 = await spotify.getMostPopularArtist("Linkin Park");

  if (!artist1 || !artist2) {
    console.log("Artistas no encontrados");
    return;
  }

  const versus = new Versus(artist1, artist2, spotify);
  await versus.start();
};

main();
