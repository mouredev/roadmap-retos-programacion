// -1-

// Operadores aritméticos: Realizar operaciones matemáticas

let suma = 4 + 4 // También es un operador de cadenas y se puede usar para enlazar cadenas
console.log(suma)

let resta = 12 - 4
console.log(resta)

let multiplicación = 2 * 4
console.log(multiplicación)

let división = 40 / 5
console.log(división)

let módulo = 35 % 9
console.log(módulo)

let exponenciacion = 2.82842712475 ** 2
console.log(exponenciacion)

let incremento = 7
incremento++
console.log(incremento)

let decremento = 9
decremento--
console.log(decremento)

// Operadores de Bits: Realizar operaciones a nivel de bits (hay más pero estos son los que me interesaban)

let DesplazamientoIzquierda = 2 << 2
console.log(DesplazamientoIzquierda)

let DesplazamientoDerecha = 32 >> 2
console.log(DesplazamientoDerecha)

// Operadores de asignación: Asignar valores a las variables

let asignación = '8 = 8'
console.log(asignación)

let asignaciónDeSuma = 6
asignaciónDeSuma += 2
console.log(asignaciónDeSuma)

let asignaciónDeResta = 10
asignaciónDeResta -= 2
console.log(asignaciónDeResta)

let asignaciónDeMultiplicacion = 4
asignaciónDeMultiplicacion *= 2
console.log(asignaciónDeMultiplicacion)

let asignaciónDeDivision = 16
asignaciónDeDivision /= 2
console.log(asignaciónDeDivision)

let asignaciónDeModulo = 35
asignaciónDeModulo %= 9
console.log(asignaciónDeModulo)

let asignaciónDeExponenciacion = 2.82842712475
asignaciónDeExponenciacion **= 2
console.log(asignaciónDeExponenciacion)

let asignaciónDeDesplazamientoIzquierda = 2
asignaciónDeDesplazamientoIzquierda <<= 2
console.log(asignaciónDeDesplazamientoIzquierda)

let asignaciónDeDesplazamientoDerecha = 32
asignaciónDeDesplazamientoDerecha >>= 2
console.log(asignaciónDeDesplazamientoDerecha)

// Operadores de Comparación: Comparar dos variables

let igualA = '8'
igualA == 8

let estrictamenteIgualA = 8
estrictamenteIgualA === 8

let noIgualA = '-8'
noIgualA != 8

let estrictamenteNoIgualA = -8
estrictamenteNoIgualA != 8

let mayorQue = 9
mayorQue > 8

let menorQue = 7
menorQue < 8

let mayorOIgualQue = 8
mayorOIgualQue >= 8

let menorOIgualQue = 8
menorOIgualQue <= 8

// Operadores Lógicos: Realizar operaciones lógicas

let AND = 8
if (AND == 8 && AND !== 8) {
    console.log('Mucho 8')
}

let OR = 8
if (OR == 8 || OR > 8) {
    console.log('O 8 o mayor')
}

let NOT = false
!NOT //= true
console.log()

// Operadores de Tipo: determinan el tipo de una variable u objeto

let value = 8
function object(){
}

console.log(typeof(value)) // number

console.log(value instanceof object); // false

// Operadores Unarios: Operan en un solo operando (hay más pero estos son los que me interesaban)

let string = '8'

let convertirANumero = +string
console.log()

let convertirANumeroNegativo = -string
console.log()

// -2-

// Estructuras de Control Condicional: Tomar decisiones basadas en condiciones

if (value == 8) {
    console.log('Es 8')
} else if (value == 40320) {
    console.log('Es 8!')
} else {
    console.log('No es 8')    
} 

let resultado = (value == 8) ? "Es 8" : "No es 8"

switch (value) {
    case 8:
        console.log('Es 8')
      break;
    case 40320:
        console.log('Es 8!')
      break;
    default:
        console.log('No es 8')    
  }

// Estructuras de Control de Bucles: Repetir bloques de código varias veces

for (var forVar = 0; forVar <= 8; forVar++) {
    console.log(forVar) // 0, 1, 2, 3, 4, 5, 6, 7, 8
  }

while (value == 8) {
    console.log('Es 8')
    break;
}

do {
    console.log('Es 8')
    break;
} while (value == 8)

// Estructuras de Control de Saltos (representadas por el código de este archivo)

/*

break --> Sale del bucle
continue --> Omite el resto del código del bucle y continúa
return --> Sale de la función y devuelve el valor de la función
throw --> Lanza una función definida por el usuario

*/

// Estructuras de Control de Excepciones: Manejar errores y excpeciones

try {
    if (value == 8) {
        throw new Error('Demasiado igualación a 8, estoy harto')
    }
  } catch (error) {
    console.error(`Se produjo el error: ${error.message}`)
  } finally {
    console.log('Operación finalizada')
  }


// -3- Dificultad extra

for (var ejercicioExtra = 10; ejercicioExtra <= 55; ejercicioExtra++) {
    if (ejercicioExtra % 2 || ejercicioExtra == 16 || !(ejercicioExtra % 3)) {
        continue;
    }
    console.log(ejercicioExtra)
}
