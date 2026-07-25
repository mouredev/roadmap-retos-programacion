// LSP MAL HECHO
class WrongPersona {
  constructor(idCard, name, lastName, card) {
    this.idCard = idCard
    this.name = name
    this.lastName = lastName
    this.card = card
  }

  pagar(price) {
    console.log(`Se ha usado para pagar $${price} la tarjeta ${this.card}`)
  }
}

const wrongAdulto = new WrongPersona(84987, 'Raul', 'Hectorio', 762456342464)
wrongAdulto.pagar(543)

// No cumple con el LSP ya que si queremos asignar un niño a persona tenemos que poner valores nulos y estonces un niño no cumpliria con lo de persona
const wrongNiño = new WrongPersona(null, 'Caterina', 'Escamilla', null)


// LSP BIEN HECHO
class Persona {
  constructor(name, lastName) {
    this.name = name
    this.lastName = lastName
  }
}

class Adulto extends Persona {
  constructor(name, lastName, idCard, card) {
    super(name, lastName)
    this.idCard = idCard
    this.card = card
  }

  pagar(price) {
    console.log(`Se ha usado para pagar $${price} la tarjeta ${this.card}`)
  }
}

class Niño extends Persona {
  constructor(name, lastName) {
    super(name, lastName)
  }
}

const adulto = new Adulto(84987, 'Raul', 'Hectorio', 762456342464)
adulto.pagar(543)
const niño = new Niño('Caterina', 'Escamilla')

// ------------------------------------------------- DIFICULTAD EXTRA -------------------------------------------------
class Vehicle {
  constructor(acceleration, deceleration) {
    this.acceleration = acceleration
    this.deceleration = deceleration
    this.speed = 0
  }

  accelerate(targetSpeed) {
    if (this.speed >= targetSpeed) return Promise.reject('ERROR ingresaste una velocidad igual o menor a la actual')
    const startTime = performance.now()
    return new Promise(resolve => {
      setTimeout(() => {
        this.speed = targetSpeed
        const endTime = performance.now()
        console.log(`Tardo en acelerar hasta ${targetSpeed}km/h ${((endTime - startTime)/1000).toFixed(2)}s`)
        resolve()
      }, 1000 * ((targetSpeed - this.speed)/this.acceleration))
    })
  }

  decelerate(targetSpeed) {
    if (this.speed <= targetSpeed) return Promise.reject('ERROR ingresaste una velocidad igual o menor a la actual')
    const startTime = performance.now()
    return new Promise(resolve => {
      setTimeout(() => {
        this.speed = targetSpeed
        const endTime = performance.now()
        console.log(`Tardo en desacelerar hasta ${targetSpeed}km/h ${((endTime - startTime)/1000).toFixed(2)}s`)
        resolve()
      }, (targetSpeed === 0) ? 1000 * (this.speed/this.deceleration)
                              : 1000 * (targetSpeed/this.deceleration))
    })
  }
}

class Bicycle extends Vehicle{
  constructor(acceleration, deceleration) {
    super(acceleration, deceleration)
  }

  tocarBocina() {
    console.log('¡Ting ting!')
  }
}

class Car extends Vehicle{
  constructor(acceleration, deceleration) {
    super(acceleration, deceleration)
  }

  ponerGuiño(direction) {
    if (direction === 'derecha') console.log('→')
    if (direction === 'izquierda') console.log('←')
  }
}

class Plane extends Vehicle{
  constructor(acceleration, deceleration) {
    super(acceleration, deceleration)
  }

  notificarPorAltavoz() {
    console.log('Señores pasajeros tengan la amabilidad de abrocharse el cinturon')
  }
}

async function program() {
  const bicycle = new Bicycle(10, 5)
  const car = new Car(100, 50)
  const plane = new Plane(400, 150)

  plane.notificarPorAltavoz()

  await Promise.all([
    plane.accelerate(2500),
    car.accelerate(120),
    bicycle.accelerate(30)
  ])
  
  await plane.accelerate(4000)
  
  car.ponerGuiño('derecha')
  await car.decelerate(80)
  car.ponerGuiño('izquierda')

  await bicycle.decelerate(0)
  bicycle.tocarBocina()
}

program()