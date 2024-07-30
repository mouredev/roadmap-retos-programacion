//EJERCICIO
//Incorrecto ❎
class ButtonNoDPI {
	turnOn() {
		console.log('Lamp is on!')
	}

	turnOff() {
		console.log('Lamp is off!')
	}
}

class LampNoDPI {
	constructor() {
		this.button = new ButtonNoDPI()
	}

	operate(command) {
		if (command === 'on') {
			this.button.turnOn()
		} else if (command === 'off') {
			this.button.turnOff()
		}
	}
}

const lamp1 = new LampNoDPI()
lamp1.operate('on')
lamp1.operate('off')

//Correcto ✅
class ButtonInterface {
	constructor() {
		if (new.target === ButtonInterface) {
			throw new TypeError('Unable to instantiate interface "ButtonInterface"')
		}
	}

	turnOn() {
		throw new Error('The method "turnOn()" must be implemented')
	}

	turnOff() {
		throw new Error('The method "turnOff()" must be implemented')
	}
}

class LampButton extends ButtonInterface {
	turnOn() {
		console.log('Lamp is on!')
	}

	turnOff() {
		console.log('Lamp is off!')
	}
}

class Lamp {
	constructor(button) {
		this.button = button
	}

	operate(command) {
		if (command === 'on') {
			this.button.turnOn()
		} else {
			this.button.turnOff()
		}
	}
}

//EXTRA
class NotifierInterface {
	constructor() {
		if (new.target === NotifierInterface) {
			throw new TypeError('Unable to instantiate interface "NotifierInterface"')
		}
	}

	send(message) {
		throw new Error('The method "send()" must be implemented')
	}
}

class EmailNotifier extends NotifierInterface {
	send(message) {
		console.log(`Sending by email: ${message}`)
	}
}

class PushNotifier extends NotifierInterface {
	send(message) {
		console.log(`Sending by push: ${message}`)
	}
}

class SMSNotifier extends NotifierInterface {
	send(message) {
		console.log(`Sending by SMS: ${message}`)
	}
}

class NotificationService {
	constructor(notifier) {
		this.notifier = notifier
	}

	notify(message) {
		this.notifier.send(message)
	}
}

const pushService = new NotificationService(new PushNotifier())
const SMSService = new NotificationService(new SMSNotifier())
const emailService = new NotificationService(new EmailNotifier())

let message = 'Hello, notifier!'

pushService.notify(message)
SMSService.notify(message)
emailService.notify(message)
