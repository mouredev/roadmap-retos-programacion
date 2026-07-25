import readline from "readline"

const colors = {
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
}

const QUESTIONS = [
  {
    question: "1. What gives you the most satisfaction when finishing a project?",
    answers: {
      A: "A) That the interface is pixel-perfect and animations are fluid.",
      B: "B) That the logic is robust, secure, and scales well under pressure.",
      C: "C) Seeing people using my creation anywhere from their phone.",
      D: "D) Discovering hidden patterns and predicting behaviors with data."
    }
  },
  {
    question: "2. You encounter a terrible bug on a Friday afternoon. What is it?",
    answers: {
      A: "A) A `div` that refuses to center in Safari.",
      B: "B) A database query that takes 10 seconds to respond.",
      C: "C) The app crashes unexpectedly only on old Android models.",
      D: "D) The prediction model has a 40% bias and gives wrong data."
    }
  },
  {
    question: "3. If you had to choose a magic weapon (tool), which would you pick?",
    answers: {
      A: "A) The React/Vue Brush: To paint interactive realities.",
      B: "B) The Docker/Kubernetes Hammer: To build indestructible fortresses.",
      C: "C) The Swift/Kotlin Mirror: To reflect the world in the palm of your hand.",
      D: "D) The Python/Pandas Crystal Ball: To see the future through numbers."
    }
  },
  {
    question: "4. Which phrase best defines your work philosophy?",
    answers: {
      A: "A) Everything enters through the eyes; if it's not pretty, it's not used.",
      B: "B) The essential is invisible to the eyes; what matters is the engine.",
      C: "C) Accessibility and immediacy are everything.",
      D: "D) Data doesn't lie, opinions do."
    }
  },
  {
    question: "5. You are in a dark dungeon (terminal). What command do you type first?",
    answers: {
      A: "A) npm start (I want to see visual changes now).",
      B: "B) sudo systemctl status (I need to know if the service is alive).",
      C: "C) flutter run / ./gradlew (Let's see how this runs in the emulator).",
      D: "D) jupyter notebook (Let's clean this dataset)."
    }
  },
  {
    question: "6. The Hat offers you a superpower. Which do you choose?",
    answers: {
      A: "A) Total Compatibility: Your code looks the same in all browsers.",
      B: "B) Infinite Uptime: Your server never goes down, no matter what.",
      C: "C) Eternal Battery: Your app never consumes excessive resources.",
      D: "D) Omniscience: Knowing the exact answer to any question based on statistics."
    }
  },
  {
    question: "7. What is your natural enemy in the world of code?",
    answers: {
      A: "A) Internet Explorer and browser cache.",
      B: "B) Spaghetti Code and SQL injections.",
      C: "C) Old Android models.",
      D: "D) Data doesn't lie, opinions do."
    }
  },
  {
    question: "8. You have to explain your job to a Muggle (non-programmer). What do you say?",
    answers: {
      A: "A) I want to see visual changes now.",
      B: "B) I need to know if the service is alive.",
      C: "C) Let's see how this runs in the emulator.",
      D: "D) Let's clean this dataset."
    }
  },
  {
    question: "9. Which environment do you prefer to perform your magic?",
    answers: {
      A: "A) A browser with DevTools open and three monitors.",
      B: "B) A black terminal with green text and lyric-less music.",
      C: "C) A device emulator and a cable connected to the real phone.",
      D: "D) Charts, spreadsheets, and interactive notebook environments."
    }
  },
  {
    question: "10. Finally, how would you like to be remembered in Hogwarts history?",
    answers: {
      A: "A) As the artist who designed the ultimate user experience.",
      B: "B) As the architect who built the most secure system in the world.",
      C: "C) As the creator of the app that changed the daily lives of millions.",
      D: "D) As the sage who discovered the hidden truth in the chaos of information."
    }
  }
]

class Asks {
  constructor() {
    this.readline = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    })
  }

  #ask(question) {
    return new Promise(resolve => {
      this.readline.question(question, (answer) => resolve(answer))
    })
  }

  close() {
    this.readline.close()
  }

  async askLabel(info) {
    const response = (await this.#ask(colors.cyan + info + colors.reset))
    return response
  }
  
  async askQuestion(question) {
    const response = (await this.#ask(colors.cyan + question +  colors.reset)).toUpperCase()
    return response
  }
}

const asks = new Asks()

class Validator {
  static isValidAnswer(answer) {
    return answer === 'A' || answer === 'B' || answer === 'C' || answer === 'D'
  }
}

class Renderer {
  static error(msg){
    console.error(colors.red + msg + colors.reset)
  }

  static info(msg){
    console.info(colors.yellow + msg + colors.reset)
  }
}

class SortingHat {
  constructor() {
    this.points = {
      Frontend: 0,
      Backend: 0,
      Mobile: 0,
      Data: 0
    }

    this.HOUSES_FOR_ANSWER = {
      A: "Frontend",
      B: "Backend",
      C: "Mobile",
      D: "Data"
    }
  }

  setPoints(answers) {
    for (const answer of answers) {
      this.points[this.HOUSES_FOR_ANSWER[answer]]++
    }
  }

  checkHouse(answers){
    this.setPoints(answers)

    const maxPoints = Math.max(...Object.values(this.points))

    const houses = Object.keys(this.points).filter(key => this.points[key] === maxPoints)

    if (houses.length > 1) {
      Renderer.info("The decision was complicated...")
    }

    return houses[Math.floor(Math.random() * houses.length)]
  }
}

class QuestionController {
  constructor(sortingHat) {
    this.sortingHat = sortingHat
    this.answers = []
  }

  async askQuestion(question) {

    const answer = await asks.askQuestion(question)

    if (Validator.isValidAnswer(answer)) {
      this.answers.push(answer)
    } else {
      Renderer.error("Invalid answer. Please try again.")
      return this.askQuestion(question)
    }
  }

  formatQA({ question, answers }) {
    return `\n${question}
      \n${answers.A}
      \n${answers.B}
      \n${answers.C}
      \n${answers.D}
      \n\n(Answer with 'A', 'B', 'C' or 'D') Answer: `
  }

  async askQuestions() {
    for (let i = 0; i < QUESTIONS.length; i++) {
      await this.askQuestion(this.formatQA(QUESTIONS[i]))
    }
  }

  async run() {
    const name = await asks.askLabel("\nWhat is your name? ")
    await this.askQuestions()
    const house = this.sortingHat.checkHouse(this.answers)
    Renderer.info(`${name}, you are in ${house}`)
    asks.close()
  }
}

const questionController = new QuestionController(new SortingHat())
questionController.run()