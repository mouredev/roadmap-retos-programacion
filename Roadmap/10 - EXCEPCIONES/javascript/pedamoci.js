try {
  // creo un objeto y le hago un push para forzar un error ya que push es un metodo de array
  const obj = new Object
  obj.push() 

} catch (error) { // capturo el error
  // imprimo el error completo y despues el nombre (tipo) y el mensaje por separado
  console.log(error)
  console.log(error.name)
  console.log(error.message)
}

// -------------------------------------- DIFICULTAD EXTRA --------------------------------------
class TipoDeDatoErroneo extends Error {  // creo mi propio error sin mensaje (en este ejercicio no hace falta)
  constructor() {
    super()
    this.name = "TipoDeDatoErroneo"
  }
}

// datos correctos
let tipoDato = 'array'
let longitud = 4
let estructuraBase = []

// datos erroneos
let tipoDatoErroneo = 'object'
let longitudErronea = -1
let longitudNaN = parseInt('g')
let longitudUndefined = undefined
let estructuraBaseErronea = {}

function crear(tipo, longitud, estructuraBase) {
  try { 
    if (tipo !== 'array') throw new TipoDeDatoErroneo 
    if (isNaN(longitud) || longitud < 0 || longitud === undefined) new Array(-1) // RangeError
    estructuraBase.push() // TypeError
    console.log('No ha ocurrido ningún error')
  } 
  catch (e) { 
    console.log(e.name)
  } finally {
    return 'La ejecución ha finalizado'
  }
}

// ejecución sin errores
console.log(crear(tipoDato, longitud, estructuraBase))

// ejecución con error propio
console.log(crear(tipoDatoErroneo, longitud, estructuraBase))

// ejecuciones con RangeError
console.log(crear(tipoDato, longitudErronea, estructuraBase))
console.log(crear(tipoDato, longitudNaN, estructuraBase))
console.log(crear(tipoDato, longitudUndefined, estructuraBase))

// ejecución con TypeError  
console.log(crear(tipoDato, longitud, estructuraBaseErronea))