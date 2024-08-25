/*
  EJERCICIO
  @RicJDev
*/

class Person {
  constructor(name) {
    this.name = name
    this.partner = {}

    this.parents = {}
    this.children = []
  }

  addChild(child) {
    this.children.push(child)
  }
}

class FamilyTree {
  constructor() {
    this.people = {}
  }

  addPerson(name) {
    const id = Object.keys(this.people).length + 1
    const person = new Person(name)
    person.id = id

    this.people[id] = person

    return person
  }

  deletePerson(id) {
    if (this.people[id]) {
      delete this.people[id]
    } else {
      console.log('Cannot delete a record that does not exist')
    }
  }

  setPartner(id1, id2) {
    const person1 = this.people[id1]
    const person2 = this.people[id2]

    if (person1 && person2) {
      person1.partner[id2] = person2
      person2.partner[id1] = person1
    }
  }

  setParents(id, parentId) {
    const person = this.people[id]
    const parent = this.people[parentId]

    person.parents[parentId] = parent
  }

  addChild(id, childName) {
    const person = this.people[id]
    const child = this.addPerson(childName)

    this.setParents(child.id, person.id)

    person.addChild(child)
  }
}

const TREE = new FamilyTree()

TREE.addPerson('Milena')
TREE.addPerson('Josue')
TREE.addPerson('Juana')

TREE.setPartner(1, 2)
TREE.addChild(1, 'Eloise')
