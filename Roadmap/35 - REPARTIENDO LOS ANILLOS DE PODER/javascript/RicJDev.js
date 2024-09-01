/*
  EJERCICIO:

- Se ejecuta en Node.js, importando el módulo 'Readline/promises' (https://nodejs.org/api/readline.html)

  @RicJDev
*/

function isPrime(num) {
  if (num <= 1) return false
  if (num <= 3) return true
  if (num % 2 === 0 || num % 3 === 0) return false

  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) {
      return false
    }
  }

  return true
}

const isEven = (num) => num % 2 === 0

function distributeRings(totalRings) {
  let rings = null

  if (totalRings < 6) {
    console.warn('No hay suficientes anillos para repartir')
    return rings
  }

  totalRings -= 1

  let bestDiference = Number.MAX_SAFE_INTEGER

  for (let elvesRings = 1; elvesRings <= totalRings; elvesRings += 2) {
    for (let dwarvesRings = 2; dwarvesRings <= totalRings; dwarvesRings++) {
      if (isPrime(dwarvesRings)) {
        let humansRings = totalRings - elvesRings - dwarvesRings

        if (isEven(humansRings) && humansRings > 0) {
          const diference =
            Math.max(elvesRings, dwarvesRings, humansRings) -
            Math.min(elvesRings, dwarvesRings, humansRings)

          if (diference < bestDiference) {
            bestDiference = diference

            rings = {
              elves: elvesRings,
              dwarves: dwarvesRings,
              humans: humansRings,
              sauron: 1,
            }
          }
        }
      }
    }
  }

  if (rings === null) {
    console.warn('No se ha encontrado una combinación para repartir los anillos')
  }

  return rings
}

//Implementación en terminal

import * as readline from 'readline/promises'
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

console.clear()

while (true) {
  let answer = await rl.question('Indique la cantidad de anillos a repartir. ')

  let totalRings = parseInt(answer.match(/\d+/g))

  if (isNaN(totalRings)) {
    console.log('Por favor igresar numeros enteros')
  } else {
    const rings = distributeRings(totalRings)

    if (rings !== null) {
      console.log(`\nSe han distribuido los ${totalRings} anillos de la siguiente manera: `)
      console.log('Elfos:', rings.elves)
      console.log('Enanos:', rings.dwarves)
      console.log('Hombres:', rings.humans)
      console.log('Sauron:', rings.sauron)

      rl.close()
      break
    }
  }
}
