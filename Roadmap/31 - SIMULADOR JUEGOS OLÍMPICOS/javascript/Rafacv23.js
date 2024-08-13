// Importa el módulo readline para pedir datos por consola
const readline = require("readline")

// Crea una interfaz para leer la entrada del usuario
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

// Pregunta al usuario por su nombre
rl.question("¿Cuál es tu nombre? ", (nombre) => {
  console.log(`Hola, ${nombre}!`)

  // Cierra la interfaz
  rl.close()
})
