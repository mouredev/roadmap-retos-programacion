/*
  EJERCICIO:
  Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
  Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
  de forma correcta e incorrecta.
*/

console.log("+++++++++ FORMA INCORRECTA +++++++++");

class reminderServiceProof {
  reminder(message) {
    console.log(message);
  }
}

class AlarmServiceProof {
  constructor() {
    this.reminderService = new reminderServiceProof();
  }

  setAlarm(message) {
    this.reminderService.reminder(message);
  }
}

const alarmServiceProof = new AlarmServiceProof();
alarmServiceProof.setAlarm("Nueva alarma.");

console.log("\n+++++++++ FORMA CORRECTA +++++++++");

class ReminderService {
  reminder(message) {
    console.log(message);
  }
}

class AlarmService {
  constructor(reminderService) {
    this.reminderService = reminderService;
  }

  setAlarm(message) {
    this.reminderService.reminder(message);
  }
}

const reminderService = new ReminderService();
const alarmService = new AlarmService(reminderService);
alarmService.setAlarm("Nueva alarma.");

/*
  DIFICULTAD EXTRA (opcional):
  Crea un sistema de notificaciones.
  Requisitos:
  1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
  2. El sistema de notificaciones no puede depender de las implementaciones específicas.
  Instrucciones:
  1. Crea la interfaz o clase abstracta.
  2. Desarrolla las implementaciones específicas.
  3. Crea el sistema de notificaciones usando el DIP.
  4. Desarrolla un código que compruebe que se cumple el principio.
*/

console.log("\n+++++++++ SISTEMA DE NOTIFICACIONES +++++++++");

class Notifications {
  email(emailNotification) {
    console.log(emailNotification);
  }

  push(pushNotification) {
    console.log(pushNotification);
  }

  sms(smsNotification) {
    console.log(smsNotification);
  }
}

class EmailService {
  constructor(notification) {
    this.notification = notification;
  }

  sendNotification(message) {
    this.notification.email(message);
  }
}

class PushService {
  constructor(notification) {
    this.notification = notification;
  }

  sendNotification(message) {
    this.notification.email(message);
  }
}

class SmsService {
  constructor(notification) {
    this.notification = notification;
  }

  sendNotification(message) {
    this.notification.email(message);
  }
}

const notification = new Notifications();
const email = new EmailService(notification);
const push = new PushService(notification);
const sms = new SmsService(notification);

function testNotifications(notificationType) {
  notificationType.sendNotification(`Notificación ${notificationType.constructor.name}`);
}

testNotifications(sms);
testNotifications(push);
testNotifications(email);
