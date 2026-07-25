// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const axios = require('axios');

// Credenciales
const clientId = 'client_id';
const clientSecret = 'client_secret';

// Función para obtener el token de acceso
async function getAccessToken() {
  const response = await axios.post('https://accounts.spotify.com/api/token', null, {
    params: {
      grant_type: 'client_credentials',
      client_id: clientId,
      client_secret: clientSecret
    },
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  });
  return response.data.access_token;
}

// Función para obtener los datos de una banda/artista
async function getArtistData(artistName, token) {
  const response = await axios.get(`https://api.spotify.com/v1/search?q=${artistName}&type=artist&limit=1`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });
  return response.data.artists.items[0];
}

// Comparación de bandas
async function compareBands() {
  const token = await getAccessToken();
  const oasisData = await getArtistData('Oasis', token);
  const linkinParkData = await getArtistData('Linkin Park', token);

  console.log('Oasis:', oasisData.followers.total, 'seguidores');
  console.log('Linkin Park:', linkinParkData.followers.total, 'seguidores');

  if (oasisData.followers.total > linkinParkData.followers.total) {
    console.log('Oasis es más popular en seguidores.');
  } else {
    console.log('Linkin Park es más popular en seguidores.');
  }
}

compareBands();
