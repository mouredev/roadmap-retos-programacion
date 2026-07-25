import { exec } from "child_process"
import readline from "readline"
import fs from "fs/promises"

const COLORS = Object.freeze({
  red: "\x1b[31m",
  green: "\x1b[32m",
  cyan: "\x1b[34m",
  purple: "\x1b[35m",
  reset: "\x1b[0m",
})

const GIT_COMMANDS = Object.freeze({
  initRepository: "git init",
  setRemote: "git remote add origin",
  newBranch: "git branch",
  switchBranch: "git switch",
  deleteBranch: "git branch -d",
  showPendings: "git status",
  addAll: "git add .",
  commit: "git commit -m",
  commitHistory: "git log",
  pull: "git pull",
  push: "git push",
})

const rL = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const asks = question => new Promise(resolve => {
  rL.question(COLORS.cyan + question + COLORS.reset, resolve)
})

const success = message => console.log(COLORS.green + "Success: " + message + COLORS.reset)
const error = message => console.log(COLORS.red + "Error: " + message + COLORS.reset)
const printMenu = () => console.log(COLORS.purple + 
                                    "--------------------------- ACTIONS ---------------------------" + "\n" +
                                    "| 1. Set up working repository       2. Initialize repository |" + "\n" +
                                    "| 3. Set remote repository           4. Create new branch     |" + "\n" +
                                    "| 5. Switch branch                   6. Show pendings         |" + "\n" +
                                    "| 7. Make a commit                   8. show commit history   |" + "\n" +
                                    "| 9. Delete branch                  10. Make a pull request   |" + "\n" +
                                    "| 11. Make a push                   12. Exit                  |" + "\n" +
                                    "---------------------------------------------------------------" + "\n" +
                                    COLORS.reset)

const validateDirectory = async path => {
  try {
    const stats = await fs.stat(path)

    if (stats.isDirectory()) {
      return {
        valid: true,
        msg: "DIRECTORY_CHANGED"
      }
    }

    return {
      valid: false,
      msg: "INCORRECT_PATH"
    }

  } catch (error) {
    return {
      valid: false,
      msg: "PATH_NOT_FOUND"
    }
  }
}

const runCommand = command =>{
  exec(command, (error, stdout, stderr) => {
    if (error) {
      error(stderr || error.message)
      return
    }

    if (stdout && stdout.trim()) {
      success(stdout)
      return
    }

    success("Command executed successfully")
  })
}

async function main() {
  let option
  do {
    printMenu()
    option = await asks("Enter the option (1-12):")
    switch (option) {
      case "1":
        const path = await asks("Enter the working directory path:")
        const result = await validateDirectory(path)
        if (!result.valid) {
          error(result.msg)
          break;
        }
        process.chdir(path)
        success(result.msg)
        break;

      case "2":
        runCommand(GIT_COMMANDS.initRepository)
        break;

      case "3":
        const url = await asks("Enter the remote repository URL:")
        const cmdRemoteRepository = GIT_COMMANDS.setRemote + ` ${url}`
        runCommand(cmdRemoteRepository)
        break;

      case "4":
        const branchName = await asks("Enter the new branch name: ")
        const cmdNewBranch = GIT_COMMANDS.newBranch + ` ${branchName}`
        runCommand(cmdNewBranch)
        break;

      case "5":
        const switchBranchName = await asks("Enter the branch name to switch: ")
        const cmdSwitchBranch = GIT_COMMANDS.switchBranch + ` ${switchBranchName}`
        runCommand(cmdSwitchBranch)
        break;

      case "6":
        runCommand(GIT_COMMANDS.showPendings)
        break;

      case "7":
        const message = await asks("Enter the commit message: ")
        runCommand(GIT_COMMANDS.addAll)
        const cmdCommit = `${GIT_COMMANDS.commit} "${message}"`
        runCommand(cmdCommit)
        break;

      case "8":
        runCommand(GIT_COMMANDS.commitHistory)
        break;

      case "9":
        const deleteBranchName = await asks("Enter the branch name to delete: ")
        const cmdDeleteBranch = GIT_COMMANDS.deleteBranch + ` ${deleteBranchName}`
        runCommand(cmdDeleteBranch)
        break;

      case "10":
        const pullBranchName = await asks("Enter the branch name to pull: ")
        const cmdPull = GIT_COMMANDS.pull + ` ${pullBranchName}`
        runCommand(cmdPull)
        break;

      case "11":
        const pushBranchName = await asks("Enter the branch name to push: ")
        const cmdPush = GIT_COMMANDS.push + ` ${pushBranchName}`
        runCommand(cmdPush)
        break;

      default:break;
    }
  } while (option !== "12")

  rL.close()
}

main()

/*
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
    const response = await this.#ask(COLORS.cyan + `Enter the ${info}: ` + COLORS.reset)
    return response
  }
}

const asks = new Asks()

class Renderer {
  static error(message) {
    console.log(COLORS.red + "Error: " + message + COLORS.reset)
  }

  static success(message) {
    console.log(COLORS.green + "Success: " + message + COLORS.reset)
  }

  static actionsMenu() {
    console.log(COLORS.purple + 
      "--------------------------- ACTIONS ---------------------------" + "\n" +
      "| 1. Set up working repository       2. Initialize repository |" + "\n" +
      "| 3. Set remote repository           4. Create new branch     |" + "\n" +
      "| 5. Switch branch                   6. Show pendings         |" + "\n" +
      "| 7. Make a commit                   8. show commit history   |" + "\n" +
      "| 9. Delete branch                  10. Make a pull request   |" + "\n" +
      "| 11. Make a push                   12. Exit                  |" + "\n" +
      "---------------------------------------------------------------" + "\n" +
      COLORS.reset)
  }
}

class Validator {
  static async validateDirectory(path) {
    try {
      await fs.access(path)

      const stats = await fs.stat(path)

      if (stats.isDirectory()) {
        return [true, null]
      }

      return [false, "INCORRECT_PATH"]

    } catch (error) {
      return [false, "PATH_NOT_FOUND"]
    }
  }
}

class GitController {
  static runCommand(command) {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        Renderer.error(stderr || error.message)
        return
      }

      if (stdout && stdout.trim()) {
        Renderer.success(stdout)
        return
      }

      Renderer.success("Command executed successfully")
    })
  }
}

class Controller {
  constructor() {
    this.command = null
  }

  async startProgram() {
    let option 

    do { 
    Renderer.actionsMenu()
    option = await asks.askLabel("option (1-11)")

      switch (option) {
        case "1":
          const path = await asks.askLabel("working directory path")
          const [isValid, error] = await Validator.validateDirectory(path)

          if (!isValid) {
            Renderer.error(error)
            break;
          }

          process.chdir(path)
          break;

        case "2":
          GitController.runCommand(GIT_COMMANDS.initRepository)
          break;

        case "3":
          const url = await asks.askLabel("remote repository URL")
          this.command = GIT_COMMANDS.setRemote + ` ${url}`

          GitController.runCommand(this.command)
          break;

        case "4":
          const branchName = await asks.askLabel("new branch name")
          this.command = GIT_COMMANDS.newBranch + ` ${branchName}`

          GitController.runCommand(this.command)
          break;

        case "5":
          const switchBranchName = await asks.askLabel("branch name to switch")
          this.command = GIT_COMMANDS.switchBranch + ` ${switchBranchName}`

          GitController.runCommand(this.command)
          break;

        case "6":
          GitController.runCommand(GIT_COMMANDS.showPendings)
          break;

        case "7":
          const message = await asks.askLabel("commit message")
          GitController.runCommand(GIT_COMMANDS.addAll)
          this.command = `${GIT_COMMANDS.commit} "${message}"`

          GitController.runCommand(this.command)
          break;

        case "8":
          GitController.runCommand(GIT_COMMANDS.commitHistory)
          break;

        case "9":
          const deleteBranchName = await asks.askLabel("branch name to delete")
          this.command = GIT_COMMANDS.deleteBranch + ` ${deleteBranchName}`

          GitController.runCommand(this.command)
          break;

        case "10":
          const pullBranchName = await asks.askLabel("branch name to pull")
          this.command = GIT_COMMANDS.pull + ` ${pullBranchName}`

          GitController.runCommand(this.command)
          break;

        case "11":
          const pushBranchName = await asks.askLabel("branch name to push")
          this.command = GIT_COMMANDS.push + ` ${pushBranchName}`

          GitController.runCommand(this.command)
          break;

        default:
          break;
      }

    } while (option !== "12") 

    asks.close()
  }
}

const controller = new Controller()
controller.startProgram() */

