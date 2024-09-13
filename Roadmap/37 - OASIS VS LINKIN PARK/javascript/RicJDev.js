/*
fetch('https://accounts.spotify.com/api/token', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
  },
  body: new URLSearchParams({
    grant_type: 'client_credentials',
    client_id: clientId,
    client_secret: clientSecret,
  }),
})
  .then((response) => response.json())
  .then((data) => {
    const artistId = '4Z8W4fKeB5YxbusRsdQVPb'

    const url = `https://api.spotify.com/v1/artists/${artistId}`

    fetch(url, {
      method: 'GET',
      headers: {
        Authorization: `${data.token_type} ${data.access_token}`,
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        return response.json()
      })
      .then((dataArtist) => {
        console.log(dataArtist)
      })
      .catch((error) => {
        console.error('Error:', error)
      })
  })
  .catch((error) => {
    console.error('Error:', error)
  })
*/

// import * as readline from 'readline/promises'

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// })

// async function getToken(clientId, clientSecret) {
//   fetch('https://accounts.spotify.com/api/token', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/x-www-form-urlencoded',
//     },
//     body: new URLSearchParams({
//       grant_type: 'client_credentials',
//       client_id: clientId,
//       client_secret: clientSecret,
//     }),
//   })
//     .then((response) =>
//       response
//         .json()
//         .then((data) => {
//           return `${data.token_type} ${data.access_token}`
//         })
//         .catch((err) => console.log(err))
//     )
//     .catch((err) => console.log(err))
// }

// const clientId = await rl.question('Ingrese su client ID. ')
// const clientSecret = await rl.question('Ingrese su client secret ID. ')

// const token = await getToken(clientId, clientSecret).catch((err) => console.log(err))

// const artistId = '4Z8W4fKeB5YxbusRsdQVPb'

// const url = `https://api.spotify.com/v1/artists/${artistId}`

// fetch(url, {
//   method: 'GET',
//   headers: {
//     Authorization: token,
//   },
// })
//   .then((response) => {
//     if (!response.ok) {
//       throw new Error('Network response was not ok')
//     }
//     return response.json()
//   })
//   .then((dataArtist) => {
//     console.log(dataArtist)
//   })
//   .catch((error) => {
//     console.error('Error:', error)
//   })

// rl.close()

/*

* El archivo client.js (que no estará disponible dentro del repo) contiene las ID's de mi cuenta.

* Para ejecutar el programa deberá crear las variables clientId y clientSecret y asignarles
* sus propias ID's o pasarlas como parámetros de la función getToken().

*/
import { clientId, clientSecret } from './client.js'

console.log(clientId)
console.log(clientSecret)
