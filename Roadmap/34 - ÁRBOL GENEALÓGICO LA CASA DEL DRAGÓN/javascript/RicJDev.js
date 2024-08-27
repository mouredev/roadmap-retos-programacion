/*
  EJERCICIO
  @RicJDev
*/

class Person {
  constructor(id, name) {
    this.name = name
    this.id = id

    this.hasParents = false

    this.children = []

    this.partner = null
  }

  addChild(child) {
    if (!this.children.includes(child)) {
      this.children.push(child)

      console.log(`${this.name} ha tenido un/a hijo/a: ${child.name}.`)
    } else {
      console.log(`${child.name} ya es hijo/a de ${this.name}.`)
    }
  }

  hasPartner() {
    return !(this.partner === null)
  }

  setPartner(partner) {
    if (partner.hasPartner() || this.hasPartner()) {
      this.hasPartner()
        ? console.log(`${this.name} ya tiene pareja: ${this.partner.name}.`)
        : console.log(`${partner.name} ya tiene pareja: ${partner.partner.name}.`)
    } else {
      this.partner = partner
      partner.partner = this

      console.log(`${this.name} ahora es pareja de ${partner.name}`)
    }
  }
}

/*
let test1 = new Person(12, 'Juan')
let test2 = new Person(10, 'Martha')
let test3 = new Person(13, 'Joane')

test1.setPartner(test2)
test1.setPartner(test3)

test2.setPartner(test3)
*/

class FamilyTree {
  constructor() {
    this.people = {}
  }

  addPerson(id, name) {
    if (this.people[id]) {
      console.log(`Este ID ${id} ya ha sido registrado`)
    } else {
      this.people[id] = new Person(id, name)
    }
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

  addChild(id, childId) {
    const parent = this.people[id]
    const child = this.people[childId]

    if (parent && child) {
      parent.addChild(child)
    } else {
      console.log(`Una de las ID's no coincide con ningún registro: ${id}, ${childId}`)
    }
  }
}
