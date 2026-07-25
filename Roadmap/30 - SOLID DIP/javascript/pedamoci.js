// ----------------------- DIP MAL HECHO -----------------------
class MongoDB {
  save(data) {
    // Aca iria la logica para guardar los datos n la base de datos MongoDB
  }
}

class WrongPrograma {
  constructor() {
    this.database = new MongoDB()
  }

  saveUser(user) {
    this.database.save(user)
  }
}

const wrongProgram = new WrongPrograma()

class MySQL {
  save(data) {
    // Aca iria la logica para guardar los datos n la base de datos MySQL
  }
}

/* --> Si quisieras cambiar la base de datos necesitaias re escribir el programa principal <-- */
class NewWrongPrograma {
  constructor() {
    this.database = new MySQL()
  }

  saveUser(user) {
    this.database.save(user)
  }
}


// ----------------------- DIP BIEN HECHO -----------------------
class DataRepository {
  save(data) {
    throw new Error("Este metodo deberia estar sobreescrito por las subclases");
  }
}
class PostgreeSQL extends DataRepository {
  save(data) {
    // Aca iria la logica para guardar los datos n la base de datos PostgreeSQL
  }
}

class Oracle extends DataRepository {
  save(data) {
    // Aca iria la logica para guardar los datos n la base de datos Oracle
  }
}

class Programa {
  constructor(database) {
    this.database = database
  }

  saveUser(user) {
    this.database.save(user)
  }
}

const postgreeSQL = new PostgreeSQL
const programa = new Programa(postgreeSQL)
/* --> Si quisieras cambiar la base de datos necesitaias pasarsela como parametro al programa principal <-- */
const oracle = new Oracle
programa.database = oracle

// --------------------------------- DIFICULTAD EXTRA ---------------------------------
class ServiceMessage {
  send(msg) {
    throw new Error("Este metodo deberia estar sobreescrito por las subclases");
  }
}

class Email extends ServiceMessage {
  send(msg) {
    console.log('Enviando el email...')
    return new Promise(resolve => {
      setTimeout(() => {
        console.log(`Se ha enviado: ${msg}`)
        resolve()
      }, 500);
    })
  }
}

class Push extends ServiceMessage {
  send(msg) {
    console.log('Enviando el push...')
    return new Promise(resolve => {
      setTimeout(() => {
        console.log(`Se ha enviado: ${msg}`)
        resolve()
      }, 500);
    })
  }
}

class Sms extends ServiceMessage {
  send(msg) {
    console.log('Enviando el sms...')
    return new Promise(resolve => {
      setTimeout(() => {
        console.log(`Se ha enviado: ${msg}`)
        resolve()
      }, 500);
    })
  }
}

class Program {
  constructor(msgService) {
    this.msgService = msgService
  }

  async notify(msg) {
    await this.msgService.send(msg)
  }
}

const email = new Email()
const push = new Push()
const sms = new Sms()
const program = new Program(email)

async function tester() {
  console.log('\nEl testeo ha iniciado enviando el primer mensaje por email')
  await program.notify('Enviando un mensaje por email')

  console.log('\nCambiando el servicio de mensajeria a sms')
  program.msgService = sms
  await program.notify('Enviando un mensaje por sms')

  console.log('\nCambiando el servicio de mensajeria a push')
  program.msgService = push
  await program.notify('Enviando un mensaje por push')
}
tester()