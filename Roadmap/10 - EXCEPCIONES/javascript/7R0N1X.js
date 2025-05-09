let array = [1, 2, 3, 4, 5]

try {
  console.log(array[6].toString())
} catch (error) {
  console.error(`Error: ${error}`)
} finally {
  console.log('Fin de ejecución')
}

console.log('El flujo del programa continua')