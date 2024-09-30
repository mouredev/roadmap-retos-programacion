const fs = require("fs") //importamos libreria nativa de node para leer archivos del sistema
const readline = require("readline")

// utilizamos el método readFile para obtener la información del .csv

const stream = fs.createReadStream("./usuarios.csv")

const reader = readline.createInterface({ input: stream })

let data = []
let isFirstLine = true

// función para coger un item random del array de usuarios
function getRandomItem(exclude = []) {
  let item
  do {
    item = data[Math.floor(Math.random() * data.length)]
  } while (exclude.includes(item)) //buscamos otro ganador si el usuario previo ya ha sido premiado
  return item
}

reader.on("line", (row) => {
  if (isFirstLine) {
    isFirstLine = false
    return // salimos del evento linea ya que no queremos procesar la primera línea (cabecera) del CSV.
  }

  const columns = row.split(",")
  const status = columns[2].trim() //cogemos el valor de columna status

  // solo añadimos al "sorteo" a los usuarios con el status === activo
  if (status === "activo") {
    data.push(columns)
  }
})

reader.on("close", () => {
  // manejo de errores por si no hubiese suficientes usuarios

  if (data.length === 0) {
    console.log("No hay usuarios activos disponibles para seleccionar.")
    return
  }

  const suscriptionWinner = getRandomItem() // Elegimos el primer ganador
  console.log(`${suscriptionWinner} es el ganador de una suscripción`)

  const discountWinner = getRandomItem([suscriptionWinner]) // Elegimos otro ganador distinto
  console.log(`${discountWinner} es el ganador de un descuento`)

  const bookWinner = getRandomItem([suscriptionWinner, discountWinner]) // Elegimos un tercer ganador distinto
  console.log(`${bookWinner} es el ganador de un libro`)
})
