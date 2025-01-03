/*
    Creado por Rafa Canosa
    Github: https://github.com/Rafacv23
    Website: https://www.rafacanosa.dev
*/

let rings = 8 // número inicial de anillos

let elfos = 0 // reciben números impares, como mínimo reciben 1
let enanos = 0 // reciben números primos, como mínimo reciben 2
let hombres = 0 // reciben números pares, como mínimo reciben 0
let sauron = 0 // siempre recibe uno

if (rings >= 4) {
  // Otorgamos siempre 1 anillo a Sauron
  sauron = 1
  rings -= 1

  // Mientras haya anillos para repartir
  while (rings > 0) {
    // Seleccionamos un número aleatorio de anillos a repartir (de 1 a rings)
    let asignar = Math.floor(Math.random() * rings) + 1

    // Si el número aleatorio es impar, asignamos a los Elfos
    if (asignar % 2 !== 0 && rings > 0) {
      elfos += asignar
      rings -= asignar
    }

    // Si el número aleatorio es primo, asignamos a los Enanos
    if (esPrimo(asignar) && rings > 0) {
      enanos += asignar
      rings -= asignar
    }

    // Si el número aleatorio es par, asignamos a los Hombres
    if (asignar % 2 === 0 && rings > 0) {
      hombres += asignar
      rings -= asignar
    }
  }

  console.log(`Sauron: ${sauron}`)
  console.log(`Elfos: ${elfos}`)
  console.log(`Enanos: ${enanos}`)
  console.log(`Hombres: ${hombres}`)
} else {
  console.error(
    "El número de anillos que has introducido es menor de 4, por lo tanto no podemos realizar un reparto equitativo de los mismos"
  )
}

// Función para verificar si un número es primo
function esPrimo(num) {
  if (num < 2) return false
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false
  }
  return true
}
