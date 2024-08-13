// Forma incorrecta

class PERSON_INCORRECTA {
  constructor(name, mail) {
    this.name = name,
    this.mail = mail
  }
  show_name() {
    console.log(this.name)
  }
  show_mail() {
    console.log(this.mail)
  }
}

let user = new PERSON_INCORRECTA('Ángel', 'angelenarvaez@gmail.com')
user.show_name()
user.show_mail()

// Forma correcta

class PERSON {
  constructor(name, mail) {
    this.name = name,
    this.mail = mail
  }
}
class PERSON_NAME {
  saludo(person) {
    return `Hola mi nombre es ${person.name}`
  }
}
class SEND_MAIL {
  send(person, message) {
    return `${person.mail} ${message}`
  }
}

let person1 = new PERSON('Ángel', 'angelenarvaez@gmail.com')

let message = new SEND_MAIL()
console.log(message.send(person1, 'Bienvenido a nuestra plataforma'))

let bienvenida = new PERSON_NAME()
console.log(bienvenida.saludo(person1))