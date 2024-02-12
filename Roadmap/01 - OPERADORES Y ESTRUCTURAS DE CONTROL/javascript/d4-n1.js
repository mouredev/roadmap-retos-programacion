// Operadores aritméticos básicos
let add = 9 + 7
let sub = 2 - 1
const mult = 2 * 2
const div = 5 / 2
const rem = 6 % 2
const exp = 2 ** 3

// Aritmética para strings
const name = "d4" + "-" + "n1"

// Atajos aritméticos
const addShort = add++
const subShort = sub--

// Operadores de comparación
const equal = add == 9
const notEqual = sub != 4
const strictEqual = mult === "multiplicación"
const strictNotEqual = div !== "2.5"
const greater = 3 > 2
const greaterEqual = 3 >= 3
const less = 2 < 3
const lessEqual = 2 <= 3

// Operadores lógicos
const and = true && true
const or = true || false
const not = !true

// Operadores condicionales
const age = 21
const readyToDrive = age >= 18 ? "Listo para conducir 🚗" : "Debes esperar un poco ⏳"

// Estructuras de control
if (age >= 18) {console.log("Listo para conducir 🚗")}
else if(age == 17){console.log("Ya mismo puedes conducir 😎")}
else {console.log("Debes esperar un poco ⏳")}

const fruit = "naranja"
switch (fruit) {
  case "naranja": 
    console.log("Me encanta la naranja 🍊")
    break
  case "mango":
    console.log("No me gusta el mango 🥭")
    break
  case "limón":
    console.log("También me gusta el limón 🍋")
    break
}

let number = 0
while (number <= 3) {
  console.log(number)
  number++
}

do {
  console.log("do se ejectuta al menos una vez")
} while (number <= 3)

for (let x = 0; x <= 3; x++) {
  console.log(x)
}

console.log(`
Operadores aritméticos básicos
${add}, ${sub}, ${mult}, ${div}, ${rem}, ${exp}

Aritmética para strings
${name}

Atajos aritméticos
${addShort}, ${subShort}

Operadores de comparación
${equal}, ${notEqual}, ${strictEqual}, ${strictNotEqual}, ${greater}, ${greaterEqual}, ${less}, ${lessEqual}

Operadores lógicos
${and}, ${or}, ${not}

Operadores condicionales
${age}, ${readyToDrive}
`)

/* 
Dificultad extra
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for (let x = 10; x <= 55; x++) {
  if (x % 2 != 0){   
  } else if (x == 16){
  } else if (x % 3 == 0) {
  } else {console.log(x)}
}