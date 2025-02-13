/* crear algoritmo que genere la contraseña secreta
 * tiene que tener 4 caracteres
 * letras: A, B o C
 * numeros: 1, 2 o 3
 * no se pueden repetir caracteres
 */

function generateSecretCode() {
  // lista con los posibles caracteres
  const characters = ["A", "B", "C", 1, 2, 3]

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

const secretCode = generateSecretCode()

console.log(secretCode)
