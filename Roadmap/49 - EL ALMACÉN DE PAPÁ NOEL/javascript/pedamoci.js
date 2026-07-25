import readline from "readline"

const COLORS = Object.freeze({
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
})

const RESULT = Object.freeze({
  correct: "green",
  present: "yellow",
  wrong: "red"
})

const PASSWORD_CHARS = Object.freeze(["A", "B", "C", "1", "2", "3"])

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const ask = q => new Promise(r => rl.question(q,r))

const generatePassword = () => {
  const password = []
  const passwordChars = [...PASSWORD_CHARS]

  while (password.length < 4) {
    const indexChar = Math.floor(Math.random() * passwordChars.length)
    password.push(passwordChars[indexChar])
    passwordChars.splice(indexChar, 1)
  }

  return password
}

const evaluateGuess = (password, guess) => {
  const result = []
  for (let i = 0; i < guess.length; i++) {
    if (password.includes(guess[i])) {
      if (password[i] === guess[i]) {
        result.push(RESULT.correct)
      } else result.push(RESULT.present)
    } else result.push(RESULT.wrong)
  }

  return result 
}

const printResults = (guess, result) => {
  const message = guess.map((char, i) => COLORS[result[i]] + char + COLORS.reset + "").join("")

  console.log(message)
}

const main = async () => {
  const password = generatePassword()
  let finish = false
  let attempts = 0
  console.log("Remember that the password contains the following characters: A, B, C, 1, 2, 3\nYou have 10 attempts to guess the password. Good luck!\n")
  while (!finish) {
    try {
      const guess = (await ask("Enter your guess: ")).trim().toUpperCase().split("")
      if (guess.length !== 4) throw new Error("Invalid guess length")

      const result = evaluateGuess(password, guess)
      printResults(guess, result)
      attempts++

      if (result.every(color => color === "green")) {
        console.log(COLORS.cyan + "Congratulations! You've guessed the password!" + COLORS.reset)
        finish = true
      } else if (attempts >= 10) {
        console.log("Game over! You've used all your attemps")
        finish = true
      }
    } catch (e) {
      console.error("\n" + e.message)
    }
  }

  rl.close()
}

main()