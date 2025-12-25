// ------------------------- ASIGNACION DE VARIABLES -------------------------
  /* --> variables con valores primitivos <-- */
    let varValorNumber = 123
    let varValorStrig = 'string'
    let varValorBoolean = true
    let varValorUndefined = undefined
    let varValorNull = null

  // POR VALOR --> se copia el valor de una variable (tiene que contener un dato primitivo) a otra
    let asignacionValorNumber = varValorNumber
    let asignacionValorString = varValorStrig
    let asignacionValorBoolean = varValorBoolean
    let asignacionValorUndefined = varValorUndefined
    let asignacionValorNull = varValorNull 
    // cada variable 'asignacion' contiene copia del valor que contiene la variable original

  /* --> variables con valores tipo objeto<--*/
    let varTOArray = [12, 'messi', true, 98567]
    let varTOObjeto = {'messi': 'futbolista', 'Del Potro': 'tenista', 'Hamilton': 'Piloto'}
    let varTOFuncion = function saludar() {
      console.log('Hola')
    }

  // POR REFERENCIA --> se copia la referencia a un valor almacenado en memoria
    let asignacionReferenciaArray = varTOArray
    let asignacionReferenciaObjeto = varTOObjeto
    let asignacionReferenciaFuncion = varTOFuncion

// ------------------------- EJEMPLOS DE FUNCIONES CON VARIABLES -------------------------
  // POR VALOR
  function modificarVarXValor(valorNum) {
    valorNum = 852
    console.log('valor de la variable dentro de la función: ' + valorNum)
  }
  console.log('valor de la variable antes de ingresar a la función: ' + asignacionValorNumber)
  modificarVarXValor(asignacionValorNumber)
  console.log('valor de la variable despues de ingresar a la función: ' + asignacionValorNumber)

  // POR REFERENCIA
  function modificarVarXReferencia(valorArr) {
    valorArr.push('dato ingresado dentro de la funcion')
    console.log('valor de la variable dentro de la función: ' + valorArr)
  }
  console.log('valor de la variable antes de ingresar a la función: ' + asignacionReferenciaArray)
  modificarVarXReferencia(asignacionReferenciaArray)
  console.log('valor de la variable despues de ingresar a la función: ' + asignacionReferenciaArray)
  // la variable se modifica fuera de la funcion ya que al ingresar como dato un array en verdad lo que hace es ingresar la ubicacion en memoria del array original y ese es el   que modifica el push que esta adentro de la funcion

// ----------------------------------- DIFICULTAD EXTRA -----------------------------------
// INTERCAMBIO DE PARAMETROS POR VALOR
let parametroValor1 = 5
let parametroValor2 = 8
function intercambiarXValor(v1, v2) {
  return [v2, v1]
}
let [intercambiadoValor1, intercambiadoValor2] = intercambiarXValor(parametroValor1, parametroValor2)
console.log(`El valor original 1 es: ${parametroValor1} y el 2 es: ${parametroValor2}` + "\n" + `El valor intercambiado del 1 es: ${intercambiadoValor1} y del 2 es: ${intercambiadoValor2}`)


// INTERCAMBIO DE PARAMETROS POR REFERENCIA
let parametroReferencia1 = [5, 6454, 324, 2, 878]
let parametroReferencia2 = ['jaime', 'pepe', 'juan', 'jesus', 'hector']
function intercambiarXReferencia(v1, v2) {
  let valorIntercambiador = [...v1]
  v1 = [...v2]
  v2 = [...valorIntercambiador]
  return [v1, v2]
}
let [intercambiadoReferencia1, intercambiadoReferencia2] = intercambiarXReferencia(parametroReferencia1, parametroReferencia2)
console.log(`El valor original 1 es: ${parametroReferencia1} y el 2 es: ${parametroReferencia2}` + "\n" + `El valor intercambiado del 1 es: ${intercambiadoReferencia1} y del 2 es: ${intercambiadoReferencia2}`)