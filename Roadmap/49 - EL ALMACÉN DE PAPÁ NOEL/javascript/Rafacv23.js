// Autor: Rafael Canosa, Github: https://github.com/rafacv23
const readline = require("node:readline")
const { stdin: input, stdout: output } = require("node:process")

const rl = readline.createInterface({ input, output })
const characters = ["A", "B", "C", 1, 2, 3]

/* crear algoritmo que genere la contraseña secreta
 * tiene que tener 4 caracteres
 * letras: A, B o C
 * numeros: 1, 2 o 3
 * no se pueden repetir caracteres
 */
function generateSecretCode() {
  // lista con los posibles caracteres

  let secretCode = ""

  // generamos los 4 caracteres
  for (let i = 0; i <= 4; i++) {
    const randomCharacter =
      characters[Math.floor(Math.random() * characters.length)]

    // si el caracter es repetido, volvemos a generar
    if (secretCode.includes(randomCharacter)) {
      continue
    }
    secretCode += randomCharacter
  }

  // solo terminamos el bucle si la contraseña tiene 4 caracteres
  if (secretCode.length !== 4) {
    return generateSecretCode()
  }

  return secretCode
}

// funcion que compara la respuesta con la contraseña secreta
function compare(secretCode, answer) {
  // comprobamos que la respuesta tiene 4 caracteres
  if (answer.length !== 4) {
    console.log("❌ El código debe tener exactamente 4 caracteres.")
    return
  }

  // comprobamos que los characters son los correctos
  if (![...answer].every((char) => characters.includes(char))) {
    console.log("❌ Solo se permiten los caracteres A, B, C, 1, 2, 3.")
    return
  }

  let feedback = []

  for (let i = 0; i < 4; i++) {
    if (answer[i] === secretCode[i]) {
      feedback.push("✅ Correcto")
    } else if (secretCode.includes(answer[i])) {
      feedback.push("🟡 Presente")
    } else {
      feedback.push("❌ Incorrecto")
    }
  }

  console.log("Pista:", feedback.join(" | "))
}

// Creamos la funcion que iniciara el juego y que se autoinvoque
;(function play() {
  console.log("🎅 ¡Hola! Soy Papá Noel. Intenta descifrar el código secreto.")
  const secretCode = generateSecretCode()

  // debug  console.log(secretCode)
  let attempts = 0

  function ask() {
    if (attempts >= 10) {
      console.log(`🎄 Lo siento, has perdido. El código era: ${secretCode}`)
      rl.close()
      return
    }

    rl.question(
      `Intento ${attempts + 1}/10. Introduce tu código: `,
      (answer) => {
        compare(secretCode, answer)

        if (answer === secretCode) {
          console.log("🎉 ¡Felicidades! Has descifrado el código.")
          rl.close()
        } else {
          attempts++
          ask()
        }
      }
    )
  }

  ask()
})()
