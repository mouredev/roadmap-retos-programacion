/*
  EJERCICIO:

  @RicJDev
*/

class Person {
  /**
   * @param {string} name
   */
  constructor(name) {
    this.name = name

    this.parents = {
      father: null,
      mother: null,
    }

    this.childrenList = []
  }

  get children() {
    return this.childrenList || []
  }

  get father() {
    return this.parents.father
  }

  get mother() {
    return this.parents.mother
  }
}

class FamilyTree {
  constructor() {
    this.people = {}
  }

  addPerson(name) {
    let id = Object.keys(this.people).length + 1
    this.people[id] = new Person(name)
  }

  /**
   * @param {number} id
   */
  deletePerson(id) {
    if (this.people[id]) {
      console.log(`${this.people[id].name} ha desaparecido de los registros!`)
      delete this.people[id]
    } else {
      console.log('Esa persona no existe')
    }
  }

  setParents(id, fatherId, motherId) {
    this.people[id].parents.father = this.people[fatherId].name
    this.people[id].parents.mother = this.people[motherId].name
  }
}

const TREE = new FamilyTree()

TREE.addPerson('Milena')
TREE.addPerson('Josue')
TREE.addPerson('Juana')

TREE.setParents(1, 2, 3)

console.log(TREE.people[1])
