/*
  EJERCICIO:

  @RicJDev
*/

console.log('RETO 1: Día de Batman.')

// Nos creamos una función que generará un día de Batman para el año que le pasemos como parámetro.

function getBatmanDay(year = 2014) {
  let day = 1,
    date = new Date(year, 8, day)

  while (date.getDay() !== 6) {
    day++
    date = new Date(year, 8, day)
  }

  date = new Date(year, 8, day + 14)

  return date
}

// Luego mostramos los días de Batman de los siguientes 15 años. El último será el aniversario 100.

console.log(' ')

let currentYear = 2024
const creationYear = 1939

while (currentYear - creationYear <= 100) {
  const aniversary = currentYear - creationYear

  console.log(`${getBatmanDay(currentYear).toLocaleDateString()}. ${aniversary} aniversario.`)

  currentYear++
}

console.log('\nRETO 2: El Bati-sistema de seguridad.')

// Creamos nuestro tablero de 20x20 que representará a Gotham City. Inicialmente todos los cuadros tendran un nivel de amenaza 0.

const GothamCity = Array(20)

for (let i = 0; i < GothamCity.length; i++) {
  GothamCity[i] = Array(20).fill(0)
}

/*
    Creamos una función que reciba una lista con los reportes de amenazas.

    Debido a que en JavaScript no hay tuplas, las simularemos con arrays.
    Cada reporte tendrá tres valores: [coordenada y, coordenada x, nivel de amenaza]

    Usaremos esto para ubicar y asignar el valor de cada amenaza dentro de nuestro GothamCity.
*/

function updateCityStatus(reports) {
  reports.forEach((report) => {
    const [y, x, level] = report

    GothamCity[y][x] = level
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
  [9, 4, 8],
  [10, 5, 10],
  [10, 6, 10],
  [2, 9, 6],
  [7, 15, 8],
  [1, 9, 2],
  [17, 3, 4],
]

updateCityStatus(reports)

// Esta función copia 'áreas' de 3x3 del mapa según las coordenadas que le pasemos.

function getArea(y, x) {
  const area = []

  for (let i = 0; i < 3; i++) area.push(GothamCity[y + i].slice(x, x + 3))

  return area
}

// Para obtener el nivel de amenaza (la sumatoria total) de cada área tendremos la siguiente función.

function getThreatLevelOf(area) {
  const total = []

  area.forEach((row) => total.push(row.reduce((counter, value) => counter + value)))

  return total.reduce((counter, value) => counter + value)
}

/*
    Finalmente creamos una función para escanear toda la ciudad.

    Esta devuelve un objeto con las siguientes claves:
    - level: la sumatoria de los sensores de área.
    - coords: las coordenadas del centro de área ( [coordenada y, coordenada x] ).
*/

function scanCity() {
  const result = { level: 0, coords: [0, 0] }

  for (let i = 0; i < GothamCity.length - 3; i++) {
    for (let j = 0; j < GothamCity[0].length - 3; j++) {
      const area = getArea(i, j),
        level = getThreatLevelOf(area)

      if (level > result.level) {
        result.level = level
        result.coords = [i + 1, j + 1]
      }
    }
  }

  return result
}

/*
    Implementamos esto en nuestro sistema de seguridad.

    Al pasar el umbral, Batman se dirige a la zona y empieza a repartir putazos (actualizando los valores a cero en esa área).
*/

function securitySystem() {
  const { level, coords } = scanCity(),
    [y, x] = coords

  console.log('Analizando ciudad en busca de amenazas potenciales...')

  //prettier-ignore
  console.log(
    `Se ha detectado un nivel de amenaza ${level} en las coordenadas (${x}, ${y}), a ${x + y} kilómetros de la Bati-cueva.`
  )

  if (level < 20) {
    console.log(`No supera el umbral de amenaza. No se ha activado el protocolo de seguridad.`)
    return
  }

  console.log('El protocolo de seguridad ha sido activado. Batman está en camino.')

  for (let i = y - 1; i < y + 2; i++) {
    for (let j = x - 1; j < x + 2; j++) {
      GothamCity[i][j] = 0
    }
  }
}

console.log(' ')
securitySystem()

console.log(' ')
securitySystem()
