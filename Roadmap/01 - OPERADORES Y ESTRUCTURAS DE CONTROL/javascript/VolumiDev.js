/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// ✅ Operadores aritméticos
var result = 2 + 2 // suma
result = 3 - 2// resta
result = 3 * 2// multiplicación
result = 6 / 2// división
result = 2 % 2// resto
result = 4 ** 2// exponenciación
result++// Incremeto
result--// decremento

// ✅ Operadiores lógicos
var bol = true && false// Operador AND
bol = true || false// Operador OR
bol = !true// Operador de negación

// ✅ Operadores de comparación
bol = 3 == 3// igualdad
bol = 3 != 4// desigual
bol = 3 === '3'// igualdad estricta o de identidad
bol = 3 !== '3'// desigualdad estricta
bol = 4 < 5// menor que
bol = 3 > 2// mayor que
bol = 3 <= 3//menor o igual
bol = 3 >= 3// mayor o igual

// ✅ Operadores de asignación
var n1 = 2
var n2 = 5
n1 = n2// asignacion
n1 += n2// asignacion de adicion
n2 -= n2// asignación de resta
n1 *= n2// asignación de multiplicación
n1 /= n2// asignación de división
n1 %= n2// asignación de resto
n1 **=// asignación de eexponenciación 
n1 <<= n2// asignación de desplazamiento a la izquierda
n1 >>= n2// asignación de desplazamiento a la derecha
n1 >>>= n2// asignación de desplazamiento a la izquierda sin signo
n1 &= n2// asignación AND bit bit
n1 ^= n2// asignación XOR bit a bit
n1 |= n2// asignación OR bit a bit
bol &&= bol// asignación AND lógico
bol ||= bol// asignación OR lógico
bol ??= bol// asignación de anulación lógica
console.log(bol)

// ✅  If:
bol = true
if (bol){
  console.log('verdadero')
}else {
  console.log('falso')
}

// ✅ switch
var option = 3
switch (option) {
  case 1:
    console.log('Esta es la opcion 1')
    break;
  case 2:
    console.log('Esta es la opcion 2')
    break;
  case 3:
      console.log('Esta es la opcion 3')
      break;
  default:
    console.log('Esta es la opcion cuando no es ninguna de las anteriores.')
    break;
}

// ✅ while
var rep = 0 
while (rep < 5){
  console.log(`Estamos en la ronda ${rep}`)
  rep ++
}

// ✅ do..while
do {
  console.log(`Estamos en la ronda ${rep}`)
  rep --
} while (rep > 0);

// ✅ for 
for (let i = 0; i < 10; i++) {
  console.log(`Estamos en un for en la iteracion ${i}`)
}

/**
 *  * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 * 
 */

var num = 10 
while(num <= 55){
  if (num % 2 == 0 && num != 16 && num % 3 != 0){
    console.log('Resultado: ',num)
  }
  num++
}