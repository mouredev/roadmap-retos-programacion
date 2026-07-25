// ------------------------------- EJERCICIO -------------------------------
// function recursiva(cant) {
//   let i = cant
//   if (i >= 0){
//     console.log(i)
//     i--
//     recursiva(i)
//   }
// }
// recursiva(100)

// ---------------------------- DIFICULTAD EXTRA ----------------------------
let vFactorial = 0
function factorial(num) {
  vFactorial = vFactorial + num
  num--
  if (num !== 0 ) {
    factorial(num)
  }
}

let posicion = 0
let default1 = 0
let default2 = 1
function fibonacci(pos) {
  if (posicion !== pos) {
    posicion++
    (posicion % 2 === 0) ? default2 = default1 + default2
                          : default1 = default1 + default2
    fibonacci(pos)
  }
}

function calcular() {
  let operation = prompt('Que desea calcular factorial o fibonacci').toLowerCase()
  do {
    if (operation === 'y'|| operation === 's') operation = prompt('Que desea calcular factorial o fibonacci').toLowerCase()
    switch (operation) {
      case 'factorial':
        let num = prompt('Ingrese el valor del que desee calcular el factorial')
        factorial(parseInt(num))
        alert(`El valor de ${num}! es: ${vFactorial}`)
        break;
      case 'fibonacci':
        let pos = prompt('Ingrese la posición de fibonacci que desea averiguar (la secuencia inicia con los valores 0 y 1)' + "\n" + 
                          `posición 1 = 1 --> (0 + 1)` + "\n" + `posición 2 = 2 --> (1 + 1) ` + "\n" + 
                          `posición 3 = 3 --> (2 + 1)` + "\n" + `posición 4 = 5 --> (3 + 2)`
        )
        fibonacci(parseInt(pos))
        alert(`El valor de fibonacci de la posicion ${pos} es ${ pos % 2 === 0 ? default2 : default1}`)
        break;
      default:
        alert('Operación no valida')
        break;
    }
    operation = prompt('Deseas hacer otra operación? Y/N').toLowerCase()
  } while (operation !== 'n')
}
calcular()