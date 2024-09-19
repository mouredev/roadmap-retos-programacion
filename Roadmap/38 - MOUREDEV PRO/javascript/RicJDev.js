/*
  EJERCICIO:

  @RicJDev
*/

// Creamos una función para convertir los datos del .csv en un array de objetos, usando las cabeceras como las claves de los valores de cada usuario.

import fs from 'fs/promises'

async function getUsersData() {
  const usersArray = []

  try {
    const filePath = new URL('./data.csv', import.meta.url)
    const data = await fs.readFile(filePath, 'utf8')

    const lines = data.trim().split('\n')
    const headers = lines[0].split(',')

    for (let i = 1; i < lines.length; i++) {
      const user = {}
      const values = lines[i].split(',')

      headers.forEach((header, index) => {
        user[header.trim()] = values[index].trim()
      })

      usersArray.push(user)
    }
  } catch (error) {
    console.error('Error al leer el archivo CSV:', error)
  }

  return usersArray
}

// Una vez obtenidos los datos, creamos una función que nos retornará un usuario al azar.

const usersData = await getUsersData()
const getRandomUser = () => usersData[Math.floor(Math.random() * usersData.length)]

// Haremos las comprobaciones para el ganador de cada premio y lo almacenaremos en un objeto.

const winners = {
  suscription: null,
  discount: null,
  book: null,
}

let winner = getRandomUser()

winners.suscription = winner

while (Object.values(winners).includes(winner)) {
  winner = getRandomUser()
}

winners.discount = winner

while (Object.values(winners).includes(winner) || winner.status !== 'activo') {
  winner = getRandomUser()
}

winners.book = winner

// Finalmente mostramos los resultados en consola.

console.log('\nEstos son los resultados:')

console.log(`\nEl ganador de una suscripción es:
  ${winners.suscription.id}. ${winners.suscription.email}`)

console.log(`\nEl ganador de un descuento es:
  ${winners.discount.id}. ${winners.discount.email}`)

console.log(`\nEl ganador de un libro es:
  ${winners.book.id}. ${winners.book.email}`)
