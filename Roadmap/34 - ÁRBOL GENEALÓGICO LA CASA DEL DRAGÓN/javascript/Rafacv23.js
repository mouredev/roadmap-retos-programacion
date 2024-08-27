/* 
    Creado por Rafa Canosa
    Github: https://github.com/Rafacv23
    Website: https://www.rafacanosa.dev
*/

let characters = [] // array donde vamos a ir guardando todos los personajes

function printCharacters() {
  if (characters.length === 0) {
    console.log("No hay personajes para mostrar.")
    return
  }

  console.log("Lista de Personajes:")
  characters.forEach((character, index) => {
    console.log(`\nPersonaje ${index + 1}:`)
    character.displayInfo()
  })
}

class Character {
  constructor(name, partner = null, children = [], parents = []) {
    this.name = name
    this.partner = partner // Solo un partner permitido
    this.children = children
    this.parents = parents // Lista de padres del personaje
    characters.push(this)
  }

  // Método para establecer un partner
  setPartner(partner) {
    if (partner instanceof Character) {
      if (this.partner === null) {
        //si es null significa que no tiene una pareja y le podemos asignar una
        this.partner = partner
        partner.partner = this // asignamos la pareja a ambos personajes a la vez, para no tener que llamar al método dos veces
        console.log(`Ahora ${partner.name} y ${this.name} son pareja`)
      } else {
        console.error(
          `${this.name} ya tiene una pareja, por lo tanto no le podemos asignar otra.`
        )
      }
    } else {
      console.error("Partner debe ser una instancia de Character.")
    }
  }

  // Método para agregar un child
  addChild(child) {
    if (child instanceof Character) {
      if (this.children.includes(child)) {
        console.error(`${child.name} ya es hijo de ${this.name}`)
      } else if (child.parents.length >= 2) {
        console.error(`${child.name} ya tiene el máximo de 2 padres`)
      } else {
        this.children.push(child)
        if (!child.parents.includes(this)) {
          child.parents.push(this)
        }
        console.log(`${this.name} ha añadido a ${child.name} como hijo`)
      }
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
    console.log(
      `Parents: ${
        this.parents.length >= 1
          ? this.parents.map((p) => p.name).join(", ")
          : "Ninguno"
      }`
    )
  }
}

const daemon = new Character("Daemon Targaryen")
const laena = new Character("Laena Velaryion")
const baela = new Character("Baela Targaryen")
const rhaena = new Character("Rhaena Targaryen")

daemon.setPartner(laena)
daemon.addChild(baela)
daemon.addChild(rhaena)
laena.addChild(baela)
laena.addChild(rhaena)

printCharacters()
