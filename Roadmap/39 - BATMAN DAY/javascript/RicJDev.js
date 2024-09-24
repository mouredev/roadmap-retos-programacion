/*
  EJERCICIO:

  @RicJDev
*/

// RETO 1: Día de Batman.

// Nos creamos una función que generará un día de Batman para el año que le pasemos como parámetro.

function getBatmanDay(year = 2014) {
  let week = 0

  let day = 1
  let date = new Date(year, 8, day)

  while (date.getDay() !== 6 || week !== 3) {
    day++
    date = new Date(year, 8, day)

    if (date.getDay() === 6) week++
  }

  return date
}

// Luego mostramos los días de Batman de los siguientes 15 años. El último será el aniversario 100.

let year = 2024

for (let i = 0; i < 15; i++) {
  console.log(getBatmanDay(year).toLocaleDateString())
  year++
}

// RETO 2: El Bati-sistema de seguridad.

// Creamos nuestro tablero de 20x20 que representará a Gotham City.

const GothamCity = Array(20)

for (let i = 0; i < GothamCity.length; i++) {
  GothamCity[i] = Array(20).fill(0)
}

// TODO: lo que falta del reto 2