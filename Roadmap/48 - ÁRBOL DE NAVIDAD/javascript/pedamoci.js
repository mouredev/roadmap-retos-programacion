import readline from "readline"

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const ask = q => new Promise(r => rl.question(q,r))

class Renderer {
  static error(msg) {
    console.error(`\nError: ${msg}\n`)
  }

  static success(msg) {
    console.log(`\nSuccess: ${msg}\n`)
  }

  static tree(tree, height) {
    for (const row of tree) {
      const padding = " ".repeat(Math.max(height - Math.ceil(row.length / 2), 0))
      console.log(padding + row.join(""))
    }
  }

  static menu() {
    console.log("---------------------------- OPTIONS ----------------------------\n" +
                "| 1. Add star                  2. Take down Star                |\n" +
                "| 3. Add christmas ornaments   4. Take down christmas ornaments |\n" +
                "| 5. Add lights                6. Take down lights              |\n" +
                "| 7. Turn on lights            8. Turn off lights               |\n" +
                "| 9. Exit                                                       |\n" +
                "-----------------------------------------------------------------\n"
    )
  }
}

class StarService {
  constructor(tree) {
    this.tree = tree
  }

  addStar() {
    if (this.tree[0][0] === "@") throw new Error("The star is already on top of the tree") 
    this.tree[0][0] = "@"
    return Renderer.success("The star has been added successfully")
  }

  deleteStar() {
    if (this.tree[0][0] !== "@") throw new Error("The star isn't at the top of the tree") 
    this.tree[0][0] = "~"
    return Renderer.success("The star has been take down successfully")
  }
}

class ChristmasOrnamentService {
  constructor(tree, availableSpots) {
    this.tree = tree
    this.availableSpots = availableSpots
    this.christmasOrnamentPositions = []
  }

  addChristmasOrnament() {
    if (this.availableSpots.length < 2) throw new Error("There's no more room on the tree for any more christmas ornaments")

    for (let i = 0; i < 2; i++) {
      const ornamentIndex = Math.floor(Math.random() * this.availableSpots.length)
      this.tree[this.availableSpots[ornamentIndex][0]][this.availableSpots[ornamentIndex][1]] = "o"
      this.christmasOrnamentPositions.push(this.availableSpots[ornamentIndex])
      this.availableSpots.splice(ornamentIndex, 1)
    }

    return Renderer.success("The christmas ornaments have been added successfully")
  }

  deleteChristmasOrnament() {
    if (this.christmasOrnamentPositions.length < 2) throw new Error("There aren't enough christmas ornaments to take down")
    for (let i = 0; i < 2; i++) {
      const ornamentIndex = Math.floor(Math.random() * this.christmasOrnamentPositions.length)
      this.tree[this.christmasOrnamentPositions[ornamentIndex][0]][this.christmasOrnamentPositions[ornamentIndex][1]] = "~"
      this.availableSpots.push(this.christmasOrnamentPositions[ornamentIndex])
      this.christmasOrnamentPositions.splice(ornamentIndex, 1)
    }
    return Renderer.success("The christmas ornaments have been take down successfully")
  }
}

class LightsService {
  constructor(tree, availableSpots) {
    this.tree = tree
    this.availableSpots = availableSpots
    this.lightsPositions = []
    this.lightsOn = false
  }

  addLights() {
    if (this.availableSpots.length < 3) throw new Error("There's no more room on the tree for any more lights")
    if (this.lightsOn) throw new Error("You cannot add lights while they are on")
    for (let i = 0; i < 3; i++) {
      const ornamentIndex = Math.floor(Math.random() * this.availableSpots.length)
      this.tree[this.availableSpots[ornamentIndex][0]][this.availableSpots[ornamentIndex][1]] = "*"
      this.lightsPositions.push(this.availableSpots[ornamentIndex])
      this.availableSpots.splice(ornamentIndex, 1)
    }
    return Renderer.success("The lights have been added successfully")
  }

  deleteLights() {
    if (this.lightsPositions.length < 3) throw new Error("There aren't enough lights to take down")
    if (this.lightsOn) throw new Error("You cannot take down lights while they are on")
    for (let i = 0; i < 3; i++) {
      const ornamentIndex = Math.floor(Math.random() * this.lightsPositions.length)
      this.tree[this.lightsPositions[ornamentIndex][0]][this.lightsPositions[ornamentIndex][1]] = "~"
      this.availableSpots.push(this.lightsPositions[ornamentIndex])
      this.lightsPositions.splice(ornamentIndex, 1)
    }
    return Renderer.success("The lights have been take down successfully")
  }

  turnOnLights() {
    if (this.lightsOn) throw new Error("The lights are already on")
    if (this.lightsPositions.length < 3) throw new Error("There are no lights to turn on")
    for (const [row, position] of this.lightsPositions) {
      this.tree[row][position] = "+"
    }
    this.lightsOn = true
    return Renderer.success("The lights on the tree have been turned on")
  }

  turnOffLights() {
    if (!this.lightsOn) throw new Error("The lights are already off")
    if (this.lightsPositions.length < 3) throw new Error("There are no lights to turn off")
    for (const [row, position] of this.lightsPositions) {
      this.tree[row][position] = "*"
    }
    this.lightsOn = false
    return Renderer.success("The lights on the tree have been turned off")
  }
}

class TreeService {
  constructor(treeHeight) {
    this.treeHeight = treeHeight
    this.tree = this.createTree(treeHeight)
    this.availableSpots = this.getAvailableSpots(this.tree, treeHeight)
    this.starService = new StarService(this.tree)
    this.christmasOrnamentService = new ChristmasOrnamentService(this.tree, this.availableSpots)
    this.lightsService = new LightsService(this.tree, this.availableSpots)
  }

  createTree = height => {
    const tree = []
    let row = []
  
    for (let  quantityPerRow = 1;  tree.length < height; quantityPerRow += 2) {
      let i = 0
      while (i < quantityPerRow) {
        row.push("~")
        i++
      }
  
      tree.push(row)
      row = []
    }
  
    tree.push(["|", "|", "|"], ["|", "|", "|"])
  
    return tree
  }

  getAvailableSpots = (tree, height) => {
    const availableSpots = []
    let row = 1
    while (row < height) {
      for (let i = 0; i < tree[row].length; i++) {
        availableSpots.push([row,i])
      }
      row++
    }
    return availableSpots
  }
}

const sleep = ms => new Promise(r => setTimeout(r, ms))

class Program {
  async start() {
    while (true) {
      try {
        const treeHeight = Number(await ask("Enter the tree's height: "))
        if (Number.isNaN(treeHeight) || !Number.isInteger(treeHeight)) throw new Error("The height of the tree height must be an integer")
        this.treeService = new TreeService(treeHeight)
        Renderer.success("Creating tree...")
        return this.main()
      } catch (e) { Renderer.error(e.message) }
    }
  }

  async main() {
    let opt
    do {
      try {
        await sleep(500)
        Renderer.menu()
        Renderer.tree(this.treeService.tree, this.treeService.treeHeight)

        opt = Number(await ask("\nEnter the option number: "))
        if (Number.isNaN(opt) || !Number.isInteger(opt) || opt > 9 || opt < 1) throw new Error("The option must be an integer between 1 and 9")

        switch (opt) {
          case 1: this.treeService.starService.addStar(); break
          case 2: this.treeService.starService.deleteStar(); break
          case 3: this.treeService.christmasOrnamentService.addChristmasOrnament(); break
          case 4: this.treeService.christmasOrnamentService.deleteChristmasOrnament(); break
          case 5: this.treeService.lightsService.addLights(); break
          case 6: this.treeService.lightsService.deleteLights(); break
          case 7: this.treeService.lightsService.turnOnLights(); break
          case 8: this.treeService.lightsService.turnOffLights(); break
          default:break
        }
      } catch (e) { Renderer.error(e.message) }
    } while (opt !== 9)

    rl.close()
  }
}

const program = new Program()
program.start()