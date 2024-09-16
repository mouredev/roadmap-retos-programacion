const fs = require("fs")

fs.appendFile('7R0N1X.txt', 'Nombre: Eduardo Molina \nEdad: 24 años \nLenguaje de programación favorito: JavaScript', (error) => {
  if (error) throw error
})

fs.readFile('7R0N1X.txt', (err, data) => {
  if (err) throw err
  console.log(data.toString())
})

fs.unlink('7R0N1X.txt', (err) => {
  if (err) throw err
  console.log('Archivo eliminado')
})