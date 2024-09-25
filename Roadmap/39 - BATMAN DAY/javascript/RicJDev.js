/*
  EJERCICIO:

  @RicJDev
*/

// RETO 1: Día de Batman.

// Nos creamos una función que generará un día de Batman para el año que le pasemos como parámetro.

function getBatmanDay(year = 2014) {
  let week = 0,
    day = 1,
    date = new Date(year, 8, day)

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

/*
    Creamos una función que reciba los reportes de amenazas.

    Debido a que en JavaScript no hay tuplas, las simularemos con arrays.
    Cada uno tendrá tres valores: [coordenada y, coordenada x, nivel de amenaza]

    Usaremos esto para ubicar y asignar el valor de cada amenaza dentro de nuestro GothamCity.
*/

function updateCityStatus(reports) {
  reports.forEach((tuple) => {
    GothamCity[tuple[0]][tuple[1]] = tuple[2]
  })
}

const reports = [
  [4, 5, 9],
  [2, 8, 5],
  [4, 10, 8],
  [0, 19, 10],
  [1, 16, 8],
  [15, 1, 9],
  [12, 2, 9],
  [2, 5, 5],
  [17, 9, 6],
  [1, 16, 7],
  [2, 9, 6],
  [7, 15, 8],
  [1, 9, 2],
  [17, 3, 4],
]

updateCityStatus(reports)

// Una vez tengamos esto, podemos 'escanear' la ciudad para ver dónde debemos concentrar los recursos.

function scanCity() {
  // TODO
}
