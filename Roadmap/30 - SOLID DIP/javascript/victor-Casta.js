/*
  * EJERCICIO:
  * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
  * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento
  * de forma correcta e incorrecta.
*/

// Forma incorrecta

class Game {
  start() {
    return 'start'
  }
}

class getTypeOfGame {
  constructor() {
    this.game = new Game()
  }
}

// Forma correcta

class Game {
  start() {
    return 'start'
  }
}

class GameType {
  constructor(typeOfGame) {
    this.typeOfGame = typeOfGame
  }

  displayGame() {
    return this.typeOfGame.start()
  }
}

const gameInstance = new Game()
const gameType = new GameType(gameInstance)
console.log(gameType.displayGame())

/*
  * DIFICULTAD EXTRA (opcional):
  * Crea un sistema de notificaciones.
  * Requisitos:
  * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
  * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
  * Instrucciones:
  * 1. Crea la interfaz o clase abstracta.
  * 2. Desarrolla las implementaciones específicas.
  * 3. Crea el sistema de notificaciones usando el DIP.
  * 4. Desarrolla un código que compruebe que se cumple el principio.
*/

class Notification {
  send(message) {
    throw new Error('Método send() debe ser implementado')
  }
}

class EmailNotification extends Notification {
  send(email) {
    console.log(`Sending Email: ${email}`)
  }
}

class PushNotification extends Notification {
  send(push) {
    console.log(`Sending Push: ${push}`)
  }
}

class SMSNotification extends Notification {
  send(sms) {
    console.log(`Sending SMS: ${sms}`)
  }
}

class NotificationSystem {
  constructor(notificationService) {
    this.notificationService = notificationService
  }

  sendNotification(message) {
    this.notificationService.send(message)
  }
}

const emailService = new EmailNotification()
const pushService = new PushNotification()
const smsService = new SMSNotification()

const emailSystem = new NotificationSystem(emailService)
emailSystem.sendNotification('Hello via Email')

const pushSystem = new NotificationSystem(pushService)
pushSystem.sendNotification('Hello via Push')

const smsSystem = new NotificationSystem(smsService)
smsSystem.sendNotification('Hello via SMS')
