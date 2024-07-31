/*
funciones básicas en javascript 
*/

// Simple
function showName(){
  console.log("daniback")
}
showName()

// Retorno de valor
function add(){
  return 3 + 9
}
let result = add()
console.log(result)

// Parámetros y argumentos
function argGretting(name){
  console.log(`Hola, ${name}!`)
}
argGretting("Dani")

function argsGretting(text, name) {
  console.log(`${text}, ${name}!`)
}
argsGretting("Saludos", "Dani")

// Parámetro con valor predeterminado
function argSinDefaultGretting (lenguage){
  console.log(`Hola mundo desde ${lenguage}`)
}
argSinDefaultGretting()
function argDefaultGretting(lenguage = "JavaScript") {
  console.log(`Hola mundo desde ${lenguage}`)
}
argDefaultGretting()

// Con parámetros y retorno de valores
function operations(message, city){
  return `$`
}