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

      console.log(`${this.name} ha tenido un/a hijo/a: ${child.name}.`)
    } else {
      console.log(`${child.name} ya es hijo/a de ${this.name}.`)
    }
  }

  setPartner(partner) {
    if (this.partner === null) {
      this.partner = partner
      partner.partner = this

      console.log(`${this.name} ahora es pareja de ${partner.name}.`)
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

    if (person1 && person2) {
      person1.setPartner(person2)
    } else {
      console.log(`Una de las ID's no coincide con ningún registro: ${id1}, ${id2}`)
    }
  }

  addChild(id, childName) {
    const parent = this.people[id]

    if (parent) {
      const child = this.addPerson(childName)
      parent.addChild(child)
    } else {
      console.log(`No se ha encontrado a ninguna persona con la ID: ${id}.`)
    }
  }
}

const TREE = new FamilyTree()

TREE.addPerson('Milena')
TREE.addPerson('Josue')
TREE.addPerson('Juana')

TREE.setPartner(1, 2)
TREE.setPartner(12, 24)

TREE.addChild(1, 'Oscar')
