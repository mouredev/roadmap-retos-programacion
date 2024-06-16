//Ejemplos de tipos de operadores

//Operadores aritméticos
//Suma
let number1 = 10
let number2 = 5
let result = number1 + number2
console.log(result)

//Resta
result = number1 - number2
console.log(result)

//Multiplicación
result = number1 * number2
console.log(result)

//División
result = number1 / number2
console.log(result)

//Módulo
result = number1 % number2
console.log(result)

//Incremento
number1++
console.log(number1)

//Decremento
number2--
console.log(number2)

//Operadores de asignación
let number3 = 10
let number4 = 5

//Asignación
result = number3
console.log(result)

//Suma y asignación
result += number4
console.log(result)

//Resta y asignación
result -= number4
console.log(result)

//Multiplicación y asignación

result *= number4
console.log(result)

//División y asignación
result /= number4
console.log(result)

//Módulo y asignación
result %= number4
console.log(result)

//Operadores de comparación
let number5 = 10
let number6 = 5

//Igualdad
result = number5 === number6
console.log(result)

//Desigualdad
result = number5 !== number6
console.log(result)

//Estrictamente igual
result = number5 === number6
console.log(result)

//Estrictamente desigual
result = number5 !== number6
console.log(result)

//Mayor que
result = number5 > number6
console.log(result)

//Menor que
result = number5 < number6
console.log(result)

//Mayor o igual que

result = number5 >= number6
console.log(result)

//Menor o igual que

result = number5 <= number6
console.log(result)

//Operadores lógicos
let isTrue = true
let isFalse = false

//AND
result = isTrue && isFalse
console.log(result)

//OR
result = isTrue || isFalse
console.log(result)

//NOT
result = !isTrue
console.log(result)

//Operadores de concatenación
let name = "Mia"
let lastName = "Sanchez"

//Concatenación
result = name + " " + lastName
console.log(result)

//Concatenación y asignación
result += " es mi nombre"
console.log(result)

//Operadores de tipo
let number7 = 10
let string = "10"

//Igualdad
result = number7 === string
console.log(result)

//Estrictamente igual
result = number7 === string
console.log(result)

//Operador ternario
let age = 18
result = age >= 18 ? "Eres mayor de edad" : "Eres menor de edad"
console.log(result)

//Estructuras de control
//If
let number8 = 10
if (number8 > 5) {
    console.log("El número es mayor que 5")
}

//If else
if (number8 > 15) {
    console.log("El número es mayor que 15")
}

else {
    console.log("El número es menor que 15")
}

//Else if

if (number8 > 15) {
    console.log("El número es mayor que 15")
}

  else if (number8 < 15) {
      console.log("El número es menor que 15")
  }

  else {
      console.log("El número es igual a 15")
  }

  //Switch
  let color = "red"

  switch (color) {
      case "blue":
          console.log("El color es azul")
          break
      case "red":
          console.log("El color es rojo")
          break
      case "green":
          console.log("El color es verde")
          break
      default:
          console.log("El color no es azul, rojo o verde")
  }

  //While
  let number9 = 0
  while (number9 < 5) {
      console.log(number9)
      number9++
  }

  //Do while
  let number10 = 0
  do {
      console.log(number10)
      number10++
  } while (number10 < 5)

  //For
  for (let i = 0; i < 5; i++) {
      console.log(i)
  }

  //For in
  let colors = ["red", "blue", "green"]
  for (let index in colors) {
      console.log(colors[index])
  }

  //For of
  for (let color of colors) {
      console.log(color)
  }

  //Break
  for (let i = 0; i < 5; i++) {
      if (i === 3) {
          break
      }
      console.log(i)
  }

  //Continue

  for (let i = 0; i < 5; i++) {
      if (i === 3) {
          continue
      }
      console.log(i)

  }

  //Funciones
  function myFunction() {
      console.log("¡Hola, JavaScript!")
  }
  myFunction()

  //Funciones con parámetros
  function myFunction2(name) {
      console.log(`¡Hola, ${name}!`)
  }
  myFunction2("JavaScript")

//Crea un programa que imprima por consola todos los números comprendidos
//  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i)
    }

}

