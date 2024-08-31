/*
  EJERCICIO
  @RicJDev
*/

class Person {
  constructor(id, name) {
    this.name = name
    this.id = id

    this.parents = []
    this.children = []

    this.partner = null
  }

  addChild(child) {
    if (!this.children.includes(child)) {
      if (child.hasParents()) {
        const parentsNames = [child.parents[0].name, child.parents[1].name]
        console.log(`${child.name} ya tiene padres: ${parentsNames.join(', ')}.`)
      } else {
        child.parents.push(this)
        this.children.push(child)

        console.log(`${this.name} ha tenido un hijo: ${child.name}.`)
      }
    } else {
      console.log(`${child.name} ya es hijo de ${this.name}.`)
    }
  }

  setPartner(partner) {
    if (partner.hasPartner() || this.hasPartner()) {
      this.hasPartner()
        ? console.log(`${this.name} ya tiene pareja: ${this.partner.name}.`)
        : console.log(`${partner.name} ya tiene pareja: ${partner.partner.name}.`)
    } else {
      this.partner = partner
      partner.partner = this

      console.log(`${this.name} ahora es pareja de ${partner.name}.`)
    }
  }

  hasPartner() {
    return !(this.partner === null)
  }

  hasParents() {
    return this.parents.length === 2
  }
}

class FamilyTree {
  constructor() {
    this.people = {}
  }

  addPerson(id, name) {
    if (this.people[id]) {
      console.log(`El ID ${id} ya ha sido registrado.`)
    } else {
      this.people[id] = new Person(id, name)

      console.log(`Se ha registrado a ${name}: ${id}.`)
    }
  }

  deletePerson(id) {
    this.people[id]
      ? delete this.people[id]
      : console.log(`No se ha encontrado a ninguna persona con la ID: ${id || 0}.`)
  }

  setPartner(id1, id2) {
    const person1 = this.people[id1]
    const person2 = this.people[id2]

    person1 && person2
      ? person1.setPartner(person2)
      : console.log(`Una de las ID's no coincide con ningún registro: ${id1 || 0}, ${id2 || 0}`)
  }

  addChild(id, childId) {
    const parent = this.people[id]
    const child = this.people[childId]

    if (parent && child) {
      parent.addChild(child)

      if (parent.hasPartner()) {
        parent.partner.addChild(child)
      }
    } else {
      console.log(`Una de las ID's no coincide con ningún registro: ${id || 0}, ${childId || 0}`)
    }
  }

  displayTree() {
    const rootPersons = Object.values(this.people).filter((person) => person.parents.length === 0)
    rootPersons.forEach((root) => this.printTree(root, 0))
  }

  printTree(person, level) {
    console.log(' '.repeat(level * 4) + person.name)
    person.children.forEach((child) => this.printTree(child, level + 1))
  }
}

const tree = new FamilyTree()

tree.addPerson(12, 'Juan')
tree.addPerson(14, 'Peter')
tree.addPerson(14, 'Peter')
tree.addPerson(121, 'Monica')
tree.addPerson(45, 'Erika')
tree.addPerson(90, 'Kyle')

tree.setPartner(12, 121)
tree.addChild(12, 90)

tree.addChild(45, 90)

tree.printTree(tree.people[12], 2)
