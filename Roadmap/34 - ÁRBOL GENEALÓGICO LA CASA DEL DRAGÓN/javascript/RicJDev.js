/*
  EJERCICIO
  @RicJDev
*/

class Person {
  constructor(id, name) {
    this.name = name
    this.id = id

    this.partner = null
    this.parents = {}

    this.children = []
  }

  addChild(child) {
    if (!this.children.includes(child)) {
      this.children.push(child)
    } else {
      console.log(`${child.name} ya es hijo de ${this.name}.`)
    }
  }

  setPartner(partner) {
    if (this.partner === null) {
      this.partner = partner
      partner.partner = this
    } else {
      console.log(`${this.name} ya tiene pareja: ${this.partner.name}.`)
    }
  }
}

class FamilyTree {
  constructor() {
    this.people = {}
  }

  addPerson(name) {
    const id = Object.keys(this.people).length + 1
    const person = new Person(id, name)

    this.people[id] = person

    return person
  }

  deletePerson(id) {
    this.people[id]
      ? delete this.people[id]
      : console.log(`No se ha encontrado a ninguna persona con la ID: ${id}.`)
  }

  setPartner(id1, id2) {
    const person1 = this.people[id1]
    const person2 = this.people[id2]

    person1.setPartner(person2)
  }

  addChild(id, childName) {
    const parent = this.people[id]
    const child = this.addPerson(childName)

    if (parent) {
      parent.addChild(child)
    }
  }
}

const TREE = new FamilyTree()

TREE.addPerson('Milena')
TREE.addPerson('Josue')
TREE.addPerson('Juana')

TREE.setPartner(1, 2)
