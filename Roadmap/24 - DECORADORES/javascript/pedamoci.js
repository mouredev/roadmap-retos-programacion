class Notificacion {
  notificacion() {
    console.log('Notificación de la empresa a través de Facebook')
  }
}

class NotificacionDecorator {
  constructor(base) {
    this.base = base
  }

  notificacion() {
    this.base.notificacion()
  }
}

class NotificacionSMS extends NotificacionDecorator {
  constructor(base) {
    super(base)
  }
  notificacion() {
    console.log('Notificación de la empresa a través de SMS')
    super.notificacion()
  }
}

class NotificacionTelegram extends NotificacionDecorator {
  constructor(base) {
    super(base)
  }
  notificacion() {
    console.log('Notificación de la empresa a través de Telegram')
    super.notificacion()
  }
}

let base = new Notificacion()
base = new NotificacionSMS(base)
base = new NotificacionTelegram(base)
base.notificacion()

// --------------------------------- DIFUCULTAD EXTRA ---------------------------------
function sumar(num1, num2) {
  console.log(num1 + num2)
}

function contador(fn) {
  let count = 0
  return function(...args) {
    count++
    console.log(`Llamada número ${count}`);
    return fn(...args);
  };
}

let result = contador(sumar)
result(2, 3)
result(2545, 321)
result(58, 21)
result(97, 68)
result(12, 345)