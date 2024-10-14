// Incorrecto

// Modulo de alto nivel

/* class Store {
  constructor(user) {
    this.stripe = new Stripe(user)
  }
  purchaseBike(quantity) {
    this.stripe.makePayment(200 * quantity * 100)
  }
  purchaseHelment(quantity) {
    this.stripe.makePayment(15 * quantity * 100)
  }
}

// Modulo de bajo nivel

class Stripe {
  constructor(user) {
    this.user = user
  }
  makePayment(amountInCents) {
    console.log(`${this.user} made payment of $${amountInCents / 100} with Stripe`)
  }
}

const store = new Store('John')
store.purchaseBike(2)
store.purchaseHelment(2) */

// Correcto

class AbstracPayment {
  constructor(user) {
    this.user = user
    if (new.target === AbstracPayment) {
      throw new Error("AbstracPayment es una interface no se debe instanciar")
    }
    if (!this.payment) {
      throw new Error("Debes implementar el método payment")
    }
  }
}

class PaymentProcess extends AbstracPayment {
  constructor(user) {
    super(user)
  }
  payment(amountInDollars) {
    console.log(`${this.user} made payment of $${amountInDollars}`)
  }
}

class Store {
  constructor(paymentProcess) {
    this.paymentProcess = paymentProcess
  }
  purchaseBike(quantity) {
    this.paymentProcess.payment(200 * quantity)
  }
  purchaseHelment(quantity) {
    this.paymentProcess.payment(15 * quantity)
  }
}

const store = new Store(new PaymentProcess('John'))
store.purchaseBike(2)
store.purchaseHelment(2)

// Extra

class AbstractNotifier {
  constructor(message) {
    this.message = message
    if (new.target === AbstractNotifier) {
      throw new Error("AbstractNotifier es una interface no se debe instanciar")
    }
    if (!this.send) {
      throw new Error("Debes implementar el método send")
    }
  }
}

class EmailNotifier extends AbstractNotifier {
  send() {
    console.log(`Se ha enviado mail: ${this.message}`)
  }
}
class PUSHNotifier extends AbstractNotifier {
  send() {
    console.log(`Se ha enviado PUSH: ${this.message}`)
  }
}
class SMSNotifier extends AbstractNotifier {
  send() {
    console.log(`Se ha enviado SMS: ${this.message}`)
  }
}

class NotificationService {
  constructor(notifier) {
    this.notifier = notifier
  }
  notify() {
    this.notifier.send()
  }
}

const notificationService = new NotificationService(new EmailNotifier('Hola Ángel'))
notificationService.notify()