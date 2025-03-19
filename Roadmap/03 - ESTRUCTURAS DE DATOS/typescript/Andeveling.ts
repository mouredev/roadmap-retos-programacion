// Ejemplos de estructuras de datos
// Arrays
const numeros: number[] = [1, 2, 3, 4, 5]

// Inserción
numeros.push(6) // Agrega un elemento al final
numeros.unshift(0) // Agrega un elemento al principio

// Borrado
numeros.pop() // Elimina el último elemento
numeros.shift() // Elimina el primer elemento

// Actualización
numeros[6] = 8
numeros[7] = 10
numeros[8] = 20

// Objetos
let persona = {
  nombre: "Juan",
  apellido: "",
  edad: 30,
  estaActiva: true,
}

// Inserción
persona.apellido = "Pérez"
// Borrado Lógico
persona.estaActiva = false
// Actualización
persona.edad = 40

// Tuplas
const tupla: [number, string, boolean] = [1, "andres", true]

// Enum
enum Color {
  Rojo,
  Verde,
  Azul,
}
let color: Color = Color.Rojo

// Uniones de Tipos
let variable: number | string
variable = 123
variable = "andres"

// Agenda de contactos
import * as readline from "readline"

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

class Entity {
  id: number
  constructor() {
    this.id = this.generateId()
  }

  generateId(): number {
    let id = Math.floor(Math.random() * 10000)
    return id
  }
}
class Contact extends Entity {
  name: string
  cellphone: string
  constructor(name: string, cellphone: string) {
    super()
    this.name = name
    this.cellphone = cellphone
  }
}
class Validator {
  static validateName(name: string): boolean {
    return /^[a-zA-Z\s]{3,15}$/.test(name)
  }

  static validateCellphone(cellphone: string): boolean {
    return /^\d{10}$/.test(cellphone)
  }
}
class AddressBook extends Entity {
  private static instance: AddressBook
  private contacts: Array<Contact> = []

  private constructor() {
    super()
  }

  public static getInstance(): AddressBook {
    if (!AddressBook.instance) {
      AddressBook.instance = new AddressBook()
    }
    return AddressBook.instance
  }
  addContact(contact: Contact) {
    this.contacts.push(contact)
  }

  getContacts() {
    return this.contacts
  }

  deleteContact(id: number) {
    const findContact = this.findById(id)
    if (findContact) {
      this.contacts = this.contacts.filter((contact) => contact.id !== id)
    } else {
      console.log(`Contact not found with id ${id}`)
    }
  }

  updateContact(id: number, contact: Contact) {
    const findContact = this.findById(id)
    if (findContact) {
      findContact.name = contact.name
      findContact.cellphone = contact.cellphone
    } else {
      console.log(`Contact not found with id ${id}`)
    }
  }

  findById(id: number) {
    const findContact = this.contacts.find((contact) => contact.id === id)
    if (findContact) {
      return findContact
    } else {
      return null
    }
  }
}

async function main() {
  let execute = true

  const menu = async () => {
    console.log("Welcome to Address Book")
    console.log("Choose an option:")
    console.log("1. Add contact")
    console.log("2. Show contacts")
    console.log("3. Search contact")
    console.log("4. Delete contact")
    console.log("5. Update contact")
    console.log("6. Exit")

    const answer = await questionAsync("Enter an option: ")
    const option = Number(answer)

    if (option < 1 || option > 6) {
      console.log("Invalid option")
      await menu() // Reiterar el menú si la opción es inválida
      return
    }

    const addressBook = AddressBook.getInstance()
    let name = ""
    let cellphone = ""

    switch (option) {
      case 1:
        console.log("Add contact")
        do {
          name = await questionAsync("Enter name, only letters, min 3 max 15 chars: ")
          if (!Validator.validateName(name)) console.warn("Invalid name")
        } while (!Validator.validateName(name))

        do {
          cellphone = await questionAsync("Enter cellphone, only numbers and 10 digits: ")
          if (!Validator.validateCellphone(cellphone)) console.warn("Invalid cellphone")
        } while (!Validator.validateCellphone(cellphone))

        const newContact = new Contact(name, cellphone)

        addressBook.addContact(newContact)
        console.log(`Contact added: ${name} - ${cellphone}`)
        await menu() // Llamar nuevamente a la función de menú para continuar
        break
      case 2:
        console.log("Show contacts")
        const contacts = AddressBook.getInstance().getContacts()
        if (contacts.length === 0) {
          console.log("No contacts found")
        }
        console.table(contacts)
        break
      case 3:
        console.log("Search contact")
        const id = await questionAsync("Enter contact id to search: ")
        const contactFind = addressBook.findById(Number(id))
        if (contactFind) {
          console.log(contactFind)
        } else {
          console.error(`Contact not found with id ${id}`)
        }
        break
      case 4:
        console.log("Delete contact")
        const idDelete = await questionAsync("Enter contact id to delete: ")
        const contactDelete = addressBook.findById(Number(idDelete))
        if (contactDelete) {
          addressBook.deleteContact(Number(idDelete))
          console.log(`Contact deleted: ${contactDelete.name} - ${contactDelete.cellphone}`)
        } else {
          console.error(`Contact not found with id ${idDelete}`)
        }

        break
      case 5:
        console.log("Update contact")
        const idUpdate = await questionAsync("Enter contact id to update: ")
        const contactUpdate = addressBook.findById(Number(idUpdate))
        if (contactUpdate) {
          do {
            name = await questionAsync("Enter name, only letters, min 3 max 15 chars: ")
            if (!Validator.validateName(name)) console.warn("Invalid name")
          } while (!Validator.validateName(name))

          do {
            cellphone = await questionAsync("Enter cellphone, only numbers and 10 digits: ")
            if (!Validator.validateCellphone(cellphone)) console.warn("Invalid cellphone")
          } while (!Validator.validateCellphone(cellphone))
        }

        break
      case 6:
        execute = false
        rl.close()
        console.log("Goodbye!")
        break
      default:
        console.log("Invalid option")
    }

    if (execute) {
      await menu() // Si aún se debe ejecutar, mostrar el menú nuevamente
    }
  }

  await menu() // Llamar a la función de menú para comenzar
}

async function questionAsync(question: string): Promise<string> {
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      resolve(answer)
    })
  })
}

main()




