class Person {
  constructor(id, name) {
    this.id = id
    this.name = name
    this.partner = null
    this.children = []
  }
}

class FamilyTree {
  constructor() {
    this.people = new Map()
  }

  addPerson(id, name) {
    if (this.people.has(id)) {
      console.log(`La persona con ID ${id} ya existe.`)
      return
    }
    const newPerson = new Person(id, name)
    this.people.set(id, newPerson)
    console.log(`Persona ${name} añadida al árbol.`)
  }

  removePerson(id) {
    if (!this.people.has(id)) {
      console.log(`La persona con ID ${id} no existe.`)
      return
    }

    const person = this.people.get(id)
    if (person.partner) {
      person.partner.partner = null
    }

    this.people.forEach((p) => {
      p.children = p.children.filter((child) => child.id !== id)
    })

    this.people.delete(id)
    console.log(`Persona con ID ${id} eliminada del árbol.`)
  }

  setPartner(id1, id2) {
    if (!this.people.has(id1) || !this.people.has(id2)) {
      console.log(`Una o ambas personas no existen.`)
      return
    }

    const person1 = this.people.get(id1)
    const person2 = this.people.get(id2)

    if (person1.partner || person2.partner) {
      console.log(`Una de las personas ya tiene pareja.`)
      return
    }

    person1.partner = person2
    person2.partner = person1
    console.log(`${person1.name} y ${person2.name} ahora son pareja.`)
  }

  addChild(parentId, childId) {
    if (!this.people.has(parentId) || !this.people.has(childId)) {
      console.log(`Una o ambas personas no existen.`)
      return
    }

    const parent = this.people.get(parentId)
    const child = this.people.get(childId)

    if (!parent.children.includes(child)) {
      parent.children.push(child)
      console.log(`${child.name} añadido como hijo/a de ${parent.name}.`)
    } else {
      console.log(`${child.name} ya es hijo/a de ${parent.name}.`)
    }
  }

  printTree() {
    this.people.forEach((person) => {
      console.log(`ID: ${person.id}, Nombre: ${person.name}`)
      if (person.partner) {
        console.log(`  Pareja: ${person.partner.name}`)
      }
      if (person.children.length > 0) {
        const childNames = person.children.map((child) => child.name).join(", ")
        console.log(`  Hijos: ${childNames}`)
      }
    })
  }
}

const tree = new FamilyTree()
tree.addPerson(1, "Alicent")
tree.addPerson(2, "Viserys")
tree.addPerson(3, "Rhaenyra")
tree.addPerson(4, "Daemon")

tree.setPartner(1, 2)
tree.addChild(1, 3)
tree.setPartner(3, 4)

tree.printTree()
tree.removePerson(3)
tree.printTree()