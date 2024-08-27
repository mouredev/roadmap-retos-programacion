/* 
    Creado por Rafa Canosa
    Github: https://github.com/Rafacv23
    Website: https://www.rafacanosa.dev
*/

let characters = [] // array donde vamos a ir guardando todos los personajes

class Character {
  constructor(name, partner = null, children = []) {
    this.name = name
    this.partner = partner // Solo un partner permitido
    this.children = children
  }

  // Método para establecer un partner
  setPartner(partner) {
    if (partner instanceof Character) {
      if (this.partner === null) {
        //si es null significa que no tiene una pareja y le podemos asignar una
        this.partner = partner
        partner.partner = this // asignamos la pareja a ambos personajes a la vez, para no tener que llamar al método dos veces
        console.log(`Àhora ${partner.name} y ${this.name} son pareja`)
      } else {
        console.error(
          `${this.name} ya tiene una pareja por lo tanto no le podemos asignar otra.`
        )
      }
    } else {
      console.error("Partner debe ser una instancia de Character.")
    }
  }

  // Método para agregar un child
  addChild(child) {
    if (child instanceof Character) {
      this.children.push(child)
    } else {
      console.error("Child debe ser una instancia de Character.")
    }
  }

  // Método para mostrar la información del personaje
  displayInfo() {
    console.log(`Name: ${this.name}`)
    console.log(`Partner: ${this.partner ? this.partner.name : "Ninguno"}`)
    console.log(
      `Children: ${
        this.children.length >= 1
          ? this.children.map((c) => c.name).join(", ")
          : "Ninguno"
      }`
    )
  }
}

const john = new Character("John")
const jane = new Character("Jane")
const paco = new Character("Paco")
const child = new Character("Child")

john.setPartner(jane)
john.setPartner(paco)

john.addChild(child)
jane.addChild(child)

john.displayInfo()
jane.displayInfo()
paco.displayInfo()
