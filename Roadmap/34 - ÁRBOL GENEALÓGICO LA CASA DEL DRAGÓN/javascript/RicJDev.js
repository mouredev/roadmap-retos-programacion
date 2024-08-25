/*
  EJERCICIO:

  @RicJDev
*/

const idData = []

function assignId() {
  let next = idData.length + 1
  idData.push(idData.length + 1)

  return  next
}

//Clase Component con métodos y propiedades comunes

class FamilyMemberInterface {
  /**
   * @param {string} name
   */

  constructor(name) {
    if (new.target === FamilyMemberInterface) {
      throw new TypeError('unable to instantiate class "FamilyMemberInterface"')
    }

    this.name = name
    this.id = assignId()

    this.parentsList = []
  }

  get parents() {
    return this.parentsList || []
  }
}

//Clase Leaf, que no puede almacenar objetos

class Child extends FamilyMemberInterface {
  /**
   * @param {string} name

   */

  constructor(name) {
    super(name)
  }
}

//Clase Composite, que sí puede almacenar objetos

class Parent extends FamilyMemberInterface {
  /**
   * @param {string} name

   */

  constructor(name) {
    super(name)

    this.childrenList = []
  }

  addChild(child, couple) {
    if (couple) {
      child.parentsList.push(this)
      child.parentsList.push(couple)

      couple.children.push(child)
      this.children.push(child)
    } else {
      console.log('Solo las parejas pueden tener hijos')
    }
  }

  get children() {
    return this.childrenList || []
  }
}

let test1 = new Parent('Juan')
let test2 = new Parent('Maria')

test1.addChild(new Parent('Pedro'), test2)
test1.addChild(new Parent('Lucia'), test2)
test1.addChild(new Parent('Kenny'), test2)
test1.addChild(new Child('Pepe'), test2)
test1.addChild(new Parent('Mario'), test2)

test1.children.forEach((child) => {
  child.parents.forEach((parent, index) => {
    if (index == 0) {
      console.log(`${child.name}(${child.id}) tiene a ${parent.name} como padre(${parent.id})`)
    } else if (index == 1) {
      console.log(`${child.name}(${child.id}) tiene a ${parent.name} como madre(${parent.id})`)
    }
  })
})

console.log(' ')

test2.children.forEach((child) => {
  child.parents.forEach((parent, index) => {
    if (index == 0) {
      console.log(`${child.name}(${child.id}) tiene a ${parent.name} como padre`)
    } else if (index == 1) {
      console.log(`${child.name}(${child.id}) tiene a ${parent.name} como madre`)
    }
  })
})
