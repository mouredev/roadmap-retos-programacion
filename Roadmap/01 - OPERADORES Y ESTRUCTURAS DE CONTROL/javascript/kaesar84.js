/*
# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
> #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio

```
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

/*```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
*/

console.log("** OPERADORES **")
console.log("--------------------------------------")
// Operadores aritméticos
let a = 10
let b = 25

console.log("** Operadores aritméticos **")
console.log(`Suma: a + b = ${a + b}`)
console.log(`Resta:  a - b =  ${a - b}`)
console.log(`Multiplicación:  a * b = ${a + b}`)
console.log(`División:  a / b = ${a + b}`)
console.log(`Módulo:  a % b = ${a % b}`)
console.log(`Potencia:  a ** b = ${a ** b}`)

console.log("** Auto increment - Auto decremento **")

a++ //auto-incremento
console.log(`a++ // auto-incremento -> ${a}`)
a-- //auto-decremento
console.log(`a-- // auto-incremento -> ${a}`)
console.log("--------------------------------------")

// Operadores de asignación
console.log("** Operadores de asignación **")
let c = 15
console.log(`c=${c} -> ${c}`)
c += 5 // c = c + 5
console.log(`c+=5 // c = c + 5 -> ${c}`)
c -= 5 // c = c - 5
console.log(`c-=5 // c = c - 5 -> ${c}`)
c *= 5 // c = c * 5
console.log(`c*=5 // c = c * 5 -> ${c}`)
c /= 5 // c = c / 5
console.log(`c/=5 // c = c / 5 -> ${c}`)
console.log("--------------------------------------")

// Operadores Relacionales
console.log("** Operadores relacionales **")
a = 55
b = 69
console.log("a = " + a)
console.log("b = " + b)

console.log(`a === b // estrictamente igual -> ${a === b}`) // estrictamente igual
console.log(`a == b //  igual -> ${a == b}`) // igual
console.log(`a != b //  distinto -> ${a != b}`) // distinto
console.log(`a > b //  mayor que -> ${a > b}`) // mayor
console.log(`a >= b //  mayor o igual que -> ${a > b}`) // mayor o igual
console.log(`a < b //  menor que -> ${a < b}`) // menor
console.log(`a <= b //  menor o igual que -> ${a <= b}`) // menor o igual
console.log("--------------------------------------")

// Truthy (valores verdaderos determinados por el lenguaje)
// Todos los números, excepto 0
// Todos los strings, excepto "" (vacío)
// Todos los booleans, excepto false
console.log(`** Valores Truthy **
// Todos los números, excepto 0
// Todos los strings, excepto "" (vacío)
// Todos los booleans, excepto false\n`)

// Falsy (valores falsos determinados por el lenguaje)
// 0 (número)
// "" (string vacío)
// false (boolean)
// null
// undefined
// NaN (número no numérico)
console.log(` ** Valores Falsy **
// Falsy (valores falsos determinados por el lenguaje)
// 0 (número)
// "" (string vacío)
// false (boolean)
// null
// undefined
// NaN (número no numérico)`)
console.log("--------------------------------------")

// Operadores lógicos
console.log("** Operadores lógicos **")
a = 55
b = 76
console.log("a = " + a)
console.log("b = " + b)

console.log(`AND -> a > b && a > b -> ${a > b && a > b}`) //AND
console.log(`OR -> a < b || a > b -> ${a < b || a > b}`) //OR
console.log(`NOT -> !(a > b && a > b) -> ${!(a > b && a > b)}`) //NOT
console.log("--------------------------------------")

// Operadores ternarios
console.log("** Operador ternario **")
let isIce = 0
console.log(`isIce = 0`)
console.log(
  `isIce == 0 ? console.log("Agua Congelada") : console.log("Agua líquida")`
)
isIce == 0 ? console.log("Agua Congelada\n") : console.log("Agua líquida\n")
isIce = 10
console.log(`isIce = 10`)
console.log(
  `isIce == 10 ? console.log("Agua Congelada") : console.log("Agua líquida")`
)
isIce == 0 ? console.log("Agua Congelada\n") : console.log("Agua líquida\n")
console.log("--------------------------------------")

console.log("** ESTRUCTURAS DE CONTROL **")
console.log("--------------------------------------")

console.log("** if **")
c = "js"
console.log(`c=${c}`)
console.log(`
    if(c=="js"){
    console.log("El lenguaje seleccionado es JavaScript\n")
}
    `)
console.log("-- Respuesta:")
if (c == "js") {
  console.log("El lenguaje seleccionado es JavaScript\n")
}
console.log("---------")
console.log("** if else **")
c = "other"
console.log(`c=${c}`)
console.log(`
    if(c=="other"){
    console.log("El lenguaje seleccionado es JavaScript\n")
}else{
    console.log("El lenguajes NO es Javascript\n")
}
    `)
console.log("-- Respuesta:")
if (c == "js") {
  console.log("El lenguaje seleccionado es JavaScript\n")
} else {
  console.log("El lenguajes NO es Javascript\n")
}
console.log("---------")
console.log("** if - else if - else **")
c = "python"
console.log(`c=${c}`)
console.log(`
if(c=="js"){
    console.log("El lenguaje seleccionado es JavaScript\n")
}
else if(c=="python"){
    console.log("El lenguaje seleccionado es Python\n")
}
else{
    console.log("El lenguajes NO es Javascript ni Python\n")
}
    `)
console.log("-- Respuesta:")

if (c == "js") {
  console.log("El lenguaje seleccionado es JavaScript\n")
} else if (c == "python") {
  console.log("El lenguaje seleccionado es Python\n")
} else {
  console.log("El lenguajes NO es Javascript ni Python\n")
}
console.log("--------------------------------------")

console.log("** switch **")
// switch
let colorSemaforo = "verde"
console.log(`colorSemaforo=${colorSemaforo}`)

console.log(`
   switch (colorSemaforo) {
  case "rojo":
    console.log("Prohibido el paso")
    break
  case "verde":
    console.log("Puedes pasar")
    break
  case "amarillo":
    console.log("Precaución")
    break
  default:
    console.log("El color no es reconocido")
}`)

console.log("-- Respuesta:")

switch (colorSemaforo) {
  case "rojo":
    console.log("Prohibido el paso")
    break
  case "verde":
    console.log("Puedes pasar")
    break
  case "amarillo":
    console.log("Precaución")
    break
  default:
    console.log("El color no es reconocido")
}

console.log("--------------------------------------")
console.log("** LOOPS **")
console.log("** for **")
console.log(`-- Bucle que imprime los números del 1 al 10\n
for (let i = 1; i <= 10; i++) {
    console.log("Valor: " + i)
}\n`)

console.log("-- Respuesta:")
for (let i = 1; i <= 10; i++) {
  console.log("Valor: " + i)
}

console.log("--------------------------------------")

console.log("** while **")
console.log(`-- Bucle que imprime mientras la rotación sea menor que 5\n
let d=0
    while(d<5){
        console.log("Rotación núm: " + (d+1))
        d++
    }\n`)

console.log("-- Respuesta:")
let d = 0
while (d < 5) {
  console.log("Rotación núm: " + (d + 1))
  d++
}

console.log("--------------------------------------")
console.log("** do while **")
console.log(`-- Buecle que se ejecuta mínimo una vez\n
en este caso la condición es ejecutarse en números positivos
d=-1
    do{
        console.log("Ejecución forzada")
    }while(d>0)\n`)

console.log("-- Respuesta:")
d = -1
do {
  console.log("Ejecución forzada")
} while (d > 0)
console.log("--------------------------------------")

console.log("** EXCEPCIONES **")
console.log("--------------------------------------")

console.log("** try catch **")
console.log(` Producimos error, se intenta ejecutar el try, en caso de error aplica el catch\n
    try{
        g>10
    }catch{
        console.log("La variable no existe")
    }
    `)

console.log("-- Respuesta:")
try {
  g > 10
} catch {
  console.log("La variable no existe")
}
console.log("--------------------------------------")

console.log("** try catch - Captura de errores**")
console.log(`Producimos error y capturamos mensaje a traves del objeto error\n
    try {
    g > 10
  } catch (error) {
    console.log("¡Se ha producido un error:! ", error.message)
  }
    `)

console.log("-- Respuesta:")
try {
  g > 10
} catch (error) {
  console.log("¡Se ha producido un error:! ", error.message)
}

console.log("--------------------------------------")

console.log("** try catch finally **")
console.log(`El bloque finally se ejecuta siempre\n
    try {
  console.log(g > 69)
} catch (error) {
  console.log("Se ha producido un error:", error.message)
} finally {
  console.log("Este código se ejecuta siempre")
}
    `)

console.log("-- Respuesta:")
try {
  console.log(g > 69)
} catch (error) {
  console.log("Se ha producido un error:", error.message)
} finally {
  console.log("Este código se ejecuta siempre")
}
console.log("--------------------------------------")

console.log("** throw - Lanzamiento de errores **")
console.log(`
throw new Error("Error Lanzado")
    `)
// throw new Error("Error Lanzado")
console.log("--------------------------------------")

console.log("** throw - Personalizado **")
console.log(
  `try {
        throw new ErrorPersonalizado("Se ha producido un error")
      } catch (error) {
        console.log(
          "Error personalizado:" + "***" + error.name + "***\n" + error.message
        )
      }
      `
)

console.log("-- Respuesta:")

try {
  throw new ErrorPersonalizado("Se ha producido un error")
} catch (error) {
  console.log(
    "Error personalizado:" + "***" + error.name + "***\n" + error.message
  )
}

// EXTRA
// Crea un programa que imprima por consola todos los números comprendidos
// entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
console.log("--------------------------------------")
console.log("--------------------------------------")
console.log("** EXTRA **")
console.log("--------------------------------------")

for (let i = 10; i <= 55; i++) {
  if ((i % 2 == 0) && (i!=16) & (!(i%3==0))) {
    console.log(i)
  }
}
