import readline from "readline"

const COLORS = Object.freeze({
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
})

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const ask = question => new Promise(resolve => 
  rl.question(question, resolve)
)

const printError = msg => { console.error(COLORS.red + "Error: " + msg + COLORS.reset) }
const printFinish = () => { console.log(COLORS.green + "The countdown is finished!" + COLORS.reset) }
const printInfo = msg => { console.log(COLORS.cyan + "Time remaining: " + COLORS.yellow + msg + COLORS.reset) }

const asks = Object.freeze({
  year: async () => { return await ask("Enter the full year for the countdown (ej: 2093): ") },
  month: async () => { return await ask("Enter the month for the countdown (1 - 12): ") },
  day: async () => { return await ask("Enter the day for the countdown (1 - 31): ") },
  hour: async () => { return await ask("Enter the hour for the countdown (0 - 23): ") },
  minutes: async () => { return await ask("Enter the minutes for the countdown (0 - 59): ") },
  seconds: async () => { return await ask("Enter the seconds for the countdown (0 - 59): ") },
})

const validators = Object.freeze({
  year: async year => { 
    while (year < new Date().getFullYear()) {
      printError("INVALID_YEAR")
      year = await asks.year()
    }
    return year
  },
  month: async month => { 
    while (month < 1 || month > 12) {
      printError("INVALID_MONTH")
      month = await asks.month()
    }
    return month
  },
  day: async (year, month, day) => {
    while (day <= 0 || day > (new Date(year, month, 0).getDate())) {
      printError("INVALID_DAY")
      day = await asks.day()
    }
    return day
  },
  hour: async hour => { 
    while (hour < 0 || hour > 23) {
      printError("HOUR_OUT_OF_RANGE")
      hour = await asks.hour()
    }
    return hour
  },
  minutes: async minutes => { 
    while (minutes < 0 || minutes > 59) {
      printError("MINUTES_OUT_OF_RANGE")
      minutes = await asks.minutes()
    }
    return minutes
  },
  seconds: async seconds => { 
    while (seconds < 0 || seconds > 59) {
      printError("SECONDS_OUT_OF_RANGE")
      seconds = await asks.seconds()
    }
    return seconds
  },
  date: date => {
    if (date > new Date()) {
      return true
    }
    return false
  },
  isNumber: num => {
    if (Number.isNaN(Number(num))) {
      return -1
    }
    return Number(num)
  }
})

async function getTargetDate() {
  while (true) {
    const year =  await validators.year( validators.isNumber( await asks.year()))
    const month =  await validators.month( validators.isNumber( await asks.month()))
    const day =  await validators.day( year, month, validators.isNumber( await asks.day()))
    const hour =  await validators.hour( validators.isNumber( await asks.hour()))
    const minutes =  await validators.minutes( validators.isNumber( await asks.minutes()))
    const seconds =  await validators.seconds( validators.isNumber( await asks.seconds()))
  
    const targetDate = new Date(Date.UTC(year, (month - 1), day, hour, minutes, seconds) )

    if (validators.date(targetDate)) return targetDate

    printError("INVALID_DATE")
  }
}

function countdown(targetDate, intervalId) {
    console.clear()
  
    const secondsToTargetTime = Math.floor((targetDate - new Date()) / 1000)
  
    const days = Math.floor(secondsToTargetTime / 60 / 60 / 24)
    const hours = Math.floor(secondsToTargetTime / 60 / 60) - (days * 24)
    const minutes = Math.floor(secondsToTargetTime / 60) - (days * 24 * 60) - (hours * 60)
    const seconds = secondsToTargetTime - (days * 24 * 60 * 60) - (hours * 60 * 60) - (minutes * 60)
  
    if (days <= 0 && hours <= 0 && minutes <= 0 && seconds <= 0) {
      clearInterval(intervalId)
      printFinish()
      rl.close()
      return
    }
  
    printInfo(`${`${days}`.padStart(2, "0")}:${`${hours}`.padStart(2, "0")}:${`${minutes}`.padStart(2, "0")}:${`${seconds}`.padStart(2, "0")}`)
}

async function startProgram() {
  const targetDate = await getTargetDate()

  const intervalId = setInterval(() => {
    countdown(targetDate, intervalId)
  }, 1000)
}

startProgram()