/*

# #05 VALOR Y REFERENCIA
> #### Dificultad: Fácil | Publicación: 29/01/24 | Corrección: 05/02/24

## Ejercicio

```
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.

```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
 */

// Por valor
let value = 25
let valueTwo = value

function add(a, b) {
  return a + b
}

console.log(add(value, 25))

// Por referencia
let array = [1, 2, 3]
let array2 = array
let objeto = { a: 1, b: 2, c: 3 }
let objeto2 = objeto

console.log(array)
console.log(objeto)
array2.push(99)
objeto2["z"] = 99

console.log(array2)

console.log(objeto2)

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 *
 * */
// 1️⃣ Intercambio de valores POR VALOR (Primitivos)
function intercambiarPorValor(a, b) {
    let temp = a
    a = b
    b = temp
    return [a, b] // Retornamos los valores intercambiados
  }
  
  // Definimos variables primitivas
  let num1 = 10,
    num2 = 20
  
  // Llamamos a la función y guardamos el resultado en nuevas variables
  let [nuevoNum1, nuevoNum2] = intercambiarPorValor(num1, num2)
  
  // Imprimimos los valores antes y después del intercambio
  console.log("🔹 Intercambio por VALOR:")
  console.log(`Originales: num1 = ${num1}, num2 = ${num2}`)
  console.log(`Nuevos: nuevoNum1 = ${nuevoNum1}, nuevoNum2 = ${nuevoNum2}`)
  
  // 2️⃣ Intercambio de valores POR REFERENCIA (Objetos)
  function intercambiarPorReferencia(obj) {
    let temp = obj.valor1
    obj.valor1 = obj.valor2
    obj.valor2 = temp
  }
  
  // Definimos un objeto con propiedades para almacenar valores
  let objValores = { valor1: "Hola", valor2: "Mundo" }
  
  // Clonamos el objeto para demostrar la diferencia entre original y referencia
  let objClonado = { ...objValores }
  
  // Llamamos a la función que intercambia los valores dentro del objeto
  intercambiarPorReferencia(objClonado)
  
  // Imprimimos los valores antes y después del intercambio
  console.log("\n🔹 Intercambio por REFERENCIA:")
  console.log(
    `Originales: valor1 = ${objValores.valor1}, valor2 = ${objValores.valor2}`
  )
  console.log(
    `Nuevos: valor1 = ${objClonado.valor1}, valor2 = ${objClonado.valor2}`
  )
  