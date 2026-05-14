import fs from "fs"
import readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const MONTHS = Object.freeze(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]);

const ask = q => new Promise((r) => { rl.question(q, r)})

const printMenu = () => {
  console.log("1. Add New Year's Resolutions\n2. Print New Year's Resolutions\n3. Export New Year's Resolutions (.txt)\n4. Exit")
} 

class NewYearResolutionsService {
  constructor() {
    this.newYearResolutions = {}
  }

  addNewYearResolution(target, quantity, unit, period) {
    const index = Object.keys(this.newYearResolutions).length

    if (index > 9) console.error("You can no longer add any more New Year's Resolutions")
    else this.newYearResolutions[index] = {target, quantity, unit, period}
  }
}

function createPlanData(newYearResolutions) {
  return MONTHS.map((month, index) =>{
    const monthNumber = index + 1

    const items = Object.values(newYearResolutions)
      .filter(resolution => resolution.period >= monthNumber)
      .map((resolution, i) => ({
        index: i + 1,
        target: resolution.target,
        perMonth: (resolution.quantity / resolution.period).toFixed(2),
        unit: resolution.unit,
        total: resolution.quantity
      }))

    return { month, items }
  })
}

function formatPlan(planData) {
  return (planData.map( data => {
    const items = data.items.map(item => `[ ] ${item.index}. ${item.target} (${item.perMonth} ${item.unit}/month). Total: ${item.total}.`).join("\n")

    return `${data.month}:\n${items}\n`
  })).join("")
}

function printNewYearResolutions(newYearResolutions) {
  const planData = createPlanData(newYearResolutions)
  const planDataTXT = formatPlan(planData)
  console.log(planDataTXT)
}

function createArchiveTXT(newYearResolutions) {
  const planData = createPlanData(newYearResolutions)
  const planDataTXT = formatPlan(planData)
  fs.writeFileSync("new_year_resolutions.txt", planDataTXT)
}

class InputService {
  async requestTarget() {
    while (true) {
      const target = (await ask("What is your New Year's Resolutions?")).trim()
  
      if (target.length === 0) console.error("Target cannot be empty.")
      else return target
    }
  }

  async requestUnit() {
    while (true) {
      const unit = (await ask("What is the unit of measurement?")).trim()
  
      if (unit.length === 0) console.error("Unit cannot be empty.")
      else return unit
    }
  }

  async requestQuantity() {
    while (true) {
      const quantity = Number(await ask("What is the quantity you want to achieve?"))
  
      if (Number.isNaN(quantity) || !(quantity > 0)) console.error("Quantity must be a number.")
      else return quantity
    }
  }

  async requestPeriod() {
    while (true) {
      const period = Number(await ask("What is the quantity you want to achieve?"))
  
      if (Number.isNaN(period) || period > 12 || period < 1) console.error("Period must be a number between 1 and 12.")
      else return period
    }
  }
}

class Program {
  constructor(newYearResolutionsService, inputService) {
    this.newYearResolutionsService = newYearResolutionsService
    this.inputService = inputService
  }

  async main() {
    while (true) {
      printMenu()
      const response = (await ask("Enter a option: ")).trim()

      switch (response) {
        case "1":
          const target = await this.inputService.requestTarget()
          const quantity = await this.inputService.requestQuantity()
          const unit = await this.inputService.requestUnit()
          const period = await this.inputService.requestPeriod()

          this.newYearResolutionsService.addNewYearResolution(target, quantity, unit, period)
          break;
        case "2":
          if (Object.keys(this.newYearResolutionsService.newYearResolutions).length === 0) console.error("You haven't added New Year's Resolutions yet")
          else printNewYearResolutions(this.newYearResolutionsService.newYearResolutions)
          break;
        case "3":
          if (Object.keys(this.newYearResolutionsService.newYearResolutions).length === 0) console.error("You haven't added New Year's Resolutions yet")
          else createArchiveTXT(this.newYearResolutionsService.newYearResolutions)
          break;
        default:
          break;
      }

      if (response === "4") break
    }

    rl.close()
  }
}

const program = new Program(new NewYearResolutionsService(), new InputService())
program.main()