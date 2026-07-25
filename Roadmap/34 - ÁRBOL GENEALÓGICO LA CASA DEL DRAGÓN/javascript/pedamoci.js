import readline from "readline"

const colors = {
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  cyan: "\x1b[34m",
  reset: "\x1b[0m",
}

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

  async askLabel(label) {
    const response = await this.#ask(colors.cyan + `Enter the ${label}: ` + colors.reset)
    return response
  }

  async askForOperation() {
    const operation = (await this.#ask(colors.cyan + "Choose an action: " +
                                      "\nAP  --> For add Person             RP  --> For remove Person" + 
                                      "\nAF  --> For add Father             RF  --> For remove Father" + 
                                      "\nAM  --> For add Mother             RM  --> For remove Mother" + 
                                      "\nAPT --> For add Partner            RPT --> For remove Partner" + 
                                      "\nAC  --> For add child              RC  --> For remove child" +  
                                      "\nVT  --> View Tree                  GI  --> get person ID" + 
                                      "\nE   --> Exit" +
                                      "\nYour choice: " + colors.reset)).toUpperCase()
    return operation
  }
}

const asks = new Asks()

class Validator {
  static alreadyHasFather(childID, childParents) {
    return !!childParents[childID]?.father
  }

  static alreadyHasMother(childID, childParents) {
    return !!childParents[childID]?.mother
  }

  static isExistingChild(childID, childParents) {
    return !!childParents[childID]
  }

  static isExistingFather(fatherID, childParents) {
    for (const childID in childParents) {
      if (childParents[childID].father === fatherID) {
        return true
      }
    }
    return false
  }

  static isExistingMother(motherID, childParents) {
    for (const childID in childParents) {
      if (childParents[childID].mother === motherID) {
        return true
      }
    }
    return false
  }

  static isExistingPartner(personID, partners) {
    for (const parentID in partners) {
      if (parentID === personID) return true
    }
    return false
  }

  static isExistingPerson(id, people) {
    for (const personID in people) {
      if (personID === id) return true
    }
    return false
  }

  static isHisFather(childID, fatherID, childParents) {
    return (childParents[childID].father === fatherID)
  }

  static isHisMother(childID, motherID, childParents) {
    return (childParents[childID].mother === motherID)
  }

  static isTryingToSetSameParent(childID, newParentID, childParents){
    const { mother, father } = childParents[childID] || {}

    return (newParentID === mother || newParentID === father)
  }

  static isValidID(id) {
    return /^\d+$/.test(id)
  }

  static isValidName(name) {
    return (typeof name === "string" && name.trim().length > 0)
  }

  static treeIsEmpty(people) {
    return !!(people == {})
  }
}

class ValidatorHelper {
  static validatePersonID(id, people) {
    if (!Validator.isValidID(id)){
      Renderer.error(`ID ${id} is invalid`)
      return false
    }

    if (!Validator.isExistingPerson(id, people)){
      Renderer.error(`Person with ID ${id} does not exist`)
      return false
    }

    return true
  }
}

class PersonManager {
  constructor() {
    this.people = {}
  }

  addPerson(id, name) {
    this.people[id] = { name }
  }

  removePerson(id) {
    delete this.people[id]
  }

  getID(name) {
    for (const id in this.people) {
      if (this.people[id].name === name) {
        return id
      }
    }
    return false
  }
}

class RelationManager {
  constructor() {
    this.childParents = {}
    this.partners = {}
  }

  addChild(childID, motherID, fatherID) {
    if (!this.childParents[childID]) this.childParents[childID] = {}
    this.childParents[childID].mother = motherID
    this.childParents[childID].father = fatherID
  }

  addFather(childID, fatherID) {
    if (!this.childParents[childID]) this.childParents[childID] = {}
    this.childParents[childID].father = fatherID
  }

  addMother(childID, motherID) {
    if (!this.childParents[childID]) this.childParents[childID] = {}
    this.childParents[childID].mother = motherID
  }

  addPartner(personID, partnerID) {
    this.partners[personID] = partnerID
    this.partners[partnerID] = personID
  }

  removeChild(childID) {
    delete this.childParents[childID]
  }

  removeFather(childID) {
    delete this.childParents[childID].father
  }

  removeMother(childID) {
    delete this.childParents[childID].mother
  }

  removePartner(personID) {
    const partnerID = this.partners[personID]

    delete this.partners[personID]
    delete this.partners[partnerID]
  }

  removePersonFather(fatherID){
    for (const childID in this.childParents) {
      if (this.childParents[childID].father === fatherID) {
        delete this.childParents[childID].father
      }
    }
  }

  removePersonMother(motherID){
    for (const childID in this.childParents) {
      if (this.childParents[childID].mother === motherID) {
        delete this.childParents[childID].mother
      }
    }
  }
}

class Renderer {
  static error(message) {
    console.log(colors.red + "Error: " + message + colors.reset)
  }

  static success(message) {
    console.log(colors.green + "Success: " + message + colors.reset)
  }

  static info(info) {
    console.log(info)
  }
}

class TreePrinter {
  static buildChildrenMap(people, childParents) {
    const childrenMap = {}
    
    Object.keys(people).forEach(id => childrenMap[id] = [])

    for (const [childID, parents] of Object.entries(childParents)) {
      if (parents.father && childrenMap[parents.father]) {
        childrenMap[parents.father].push(childID)
      }
      if (parents.mother && childrenMap[parents.mother]) {
        childrenMap[parents.mother].push(childID)
      }
    }
    return childrenMap
  }

  static print(personManager, relationManager) {
    const people = personManager.people
    const childParents = relationManager.childParents
    const partners = relationManager.partners

    const childrenMap = this.buildChildrenMap(people, childParents)
    const visited = new Set()

    const roots = Object.keys(people).filter(id => !childParents[id])

    const allIds = roots.length > 0 ? roots : Object.keys(people)

    allIds.forEach(rootId => {
      if (!visited.has(rootId)) {
        this.printNode(rootId, 0, people, childrenMap, partners, visited, childParents)
        Renderer.info("")
      }
    })
  }

  static printNode(id, level, people, childrenMap, partners, visited, childParents) {
    if (visited.has(id)) return
    visited.add(id)

    const personName = people[id].name
    const indent = "    ".repeat(level)

    let partnerInfo = "";
    if (partners[id]) {
      const partnerId = partners[id]
      const partnerName = people[partnerId].name

      if (!Validator.isExistingChild(partnerId, childParents)) visited.add(partnerId)

      partnerInfo = `${colors.red}❤${colors.reset}  ${partnerName}`
    }

    (level === 0) ? Renderer.info(`${indent}${personName} ${partnerInfo}`)
                  : Renderer.info(`${indent}${colors.green}└─ ${colors.reset}${personName} ${partnerInfo}`)

    const children = childrenMap[id] || []
    if (children.length > 0) {
        children.forEach(childId => {
            this.printNode(childId, level + 1, people, childrenMap, partners, visited, childParents)
        })
    }
  }
}

class MenuController {
  constructor(personManager, relationManager) {
    this.personManager = personManager
    this.relationManager = relationManager
    this.init = true
  }

  async start() {
    while (this.init) {
      const option = (await asks.askForOperation()).toUpperCase()
      await this.processOption(option)
    }
  }

  async processOption(option) {
    switch (option) {
      case "AP":
        {
          const id = await asks.askLabel("person ID")
          const name = await asks.askLabel("person NAME")

          if (!Validator.isValidID(id)){
            Renderer.error("Invalid ID")
            break
          }

          if (!Validator.isValidName(name)){
            Renderer.error("Invalid NAME")
            break
          }

          if (Validator.isExistingPerson(id, this.personManager.people)){
            Renderer.error("Person already exists")
            break
          }

          this.personManager.addPerson(id, name)
          Renderer.success("The person has been added")
        }
        break;

      case "AF":
        {
          const fatherID = await asks.askLabel("father ID")
          const childID = await asks.askLabel("child ID")

          if (!ValidatorHelper.validatePersonID(fatherID, this.personManager.people)) break

          if (!ValidatorHelper.validatePersonID(childID, this.personManager.people)) break

          if (Validator.alreadyHasFather(childID, this.relationManager.childParents)){
            Renderer.error("The child already has a father")
            break
          }

          if (Validator.isTryingToSetSameParent(childID, fatherID, this.relationManager.childParents)){
            Renderer.error("Mother and father cannot be the same person")
            break
          }

          this.relationManager.addFather(childID, fatherID)
          Renderer.success("The father has been added")
        }
        break;

      case "AM":
        {
          const motherID = await asks.askLabel("mother ID")
          const childID = await asks.askLabel("child ID")

          if (!ValidatorHelper.validatePersonID(motherID, this.personManager.people)) break

          if (!ValidatorHelper.validatePersonID(childID, this.personManager.people)) break

          if (Validator.isTryingToSetSameParent(childID, this.relationManager.childParents)){
            Renderer.error("The child already has a mother")
            break
          }

          if (Validator.isHisFather(childID, motherID, this.relationManager.childParents)){
            Renderer.error("Mother and father cannot be the same person")
            break
          }

          this.relationManager.addMother(childID, motherID)
          Renderer.success("The mother has been added")
        }
        break;

      case "APT":
        {
          const personID = await asks.askLabel("person ID")
          const partnerID = await asks.askLabel("partner ID")

          if (!ValidatorHelper.validatePersonID(personID, this.personManager.people)) break

          if (!ValidatorHelper.validatePersonID(partnerID, this.personManager.people)) break

          if (Validator.isExistingPartner(personID, this.personManager.partners)){
            Renderer.error(`the person with ID ${personID} already has partner`)
            break
          }

          if (Validator.isExistingPartner(partnerID, this.personManager.partners)){
            Renderer.error(`the person with ID ${partnerID} already has partner`)
            break
          }

          this.relationManager.addPartner(personID, partnerID)
          Renderer.success("The partner has been added")
        }
        break;

      case "AC":
        {
          const childID = await asks.askLabel("child ID")
          const motherID = await asks.askLabel("mother ID")
          const fatherID = await asks.askLabel("father ID")

          if (!ValidatorHelper.validatePersonID(childID, this.personManager.people)) break

          if (!ValidatorHelper.validatePersonID(motherID, this.personManager.people)) break

          if (!ValidatorHelper.validatePersonID(fatherID, this.personManager.people)) break

          if (motherID === fatherID) {
            Renderer.error("Mother and father cannot be the same person")
            break
          }

          this.relationManager.addChild(childID, motherID, fatherID)
          Renderer.success("The child has been added")
        }
        break;

      case "RP":
        {
          const id = await asks.askLabel("person ID")

          if (!ValidatorHelper.validatePersonID(id, this.personManager.people)) break

          if (Validator.isExistingChild(id, this.relationManager.childParents))
            this.relationManager.removeChild(id)

          if (Validator.isExistingFather(id, this.relationManager.childParents))
            this.relationManager.removePersonFather(id)

          if (Validator.isExistingMother(id, this.relationManager.childParents))
            this.relationManager.removePersonMother(id)

          if (Validator.isExistingPartner(id, this.relationManager.partners))
            this.relationManager.removePartner(id)

          this.personManager.removePerson(id)
          Renderer.success("The person has been eliminated")
        }
        break;

      case "RF":
        {
          const fatherID = await asks.askLabel("father ID")
          const childID = await asks.askLabel("child ID")

          if (!ValidatorHelper.validatePersonID(fatherID, this.personManager.people)) break

          if (!ValidatorHelper.validatePersonID(childID, this.personManager.people)) break

          if (!Validator.isExistingChild(childID, this.relationManager.childParents)){
            Renderer.error(`This ID ${childID} does not correspond to a child`)
            break
          }

          if (!Validator.isHisFather(childID, fatherID, this.relationManager.childParents)){
            Renderer.error("This ID does not correspond to the father")
            break
          }

          this.relationManager.removeFather(childID)
          Renderer.success("The father has been eliminated")
        }
        break;

      case "RM":
        {
          const motherID = await asks.askLabel("mother ID")
          const childID = await asks.askLabel("child ID")

          if (!ValidatorHelper.validatePersonID(motherID, this.personManager.people)) break

          if (!ValidatorHelper.validatePersonID(childID, this.personManager.people)) break

          if (!Validator.isExistingChild(childID, this.relationManager.childParents)){
            Renderer.error(`This ID ${childID} does not correspond to a child`)
            break
          }

          if (!Validator.isHisMother(childID, motherID, this.relationManager.childParents)){
            Renderer.error("This ID does not correspond to the mother")
            break
          }

          this.relationManager.removeMother(childID)
          Renderer.success("The mother has been eliminated")
        }
        break;

      case "RPT":
        {
          const id = await asks.askLabel("partner ID")

          if (!ValidatorHelper.validatePersonID(id, this.personManager.people)) break

          if (!Validator.isExistingPartner(id, this.relationManager.partners)){
            Renderer.error("This ID has not partner")
            break
          }

          this.relationManager.removePartner(id)
          Renderer.success("The partner has been eliminated")
        }
        break;

      case "RC":
        {
          const id = await asks.askLabel("child ID")

          if (!ValidatorHelper.validatePersonID(id, this.personManager.people)) break

          if (!Validator.isExistingChild(id, this.relationManager.childParents)){
            Renderer.error("This ID does not belong to any child")
            break
          }

          this.relationManager.removeChild(id)
          Renderer.success("The child has been eliminated")
        }
        break;

      case "GI":
        {
          const name = await asks.askLabel("person NAME")

          const response = this.personManager.getID(name)

          if (!response) 
            Renderer.error("This name does not correspond to a person")

          Renderer.success(`The person ID is ${response}`)
        }
        break;

        case "VT":
          {
            if (Validator.treeIsEmpty()){
              Renderer.error("The family tree is empty")
            }

            Renderer.info(colors.yellow + "\n--- FAMILY TREE ---\n" + colors.reset)
            TreePrinter.print(this.personManager, this.relationManager)
          }
          break;

      case "E":
        this.init = false
        asks.close()
        break;
      default:
        break;
    }
  }
}

const menuController = new MenuController(new PersonManager, new RelationManager)
menuController.start()