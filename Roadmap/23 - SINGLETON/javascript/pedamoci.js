class Singleton {
  constructor(name) {
    if (!!Singleton.instance) {
      return Singleton.instance
    }

    Singleton.instance = this 
    this.name = name

    return this
  }

  getName() {
    return this.name
  }
}

const instanceOne = new Singleton('One')
const instanceTwo = new Singleton('Two')
const instanceThree = new Singleton('Three')

console.log(`Nombre de la primera inicialización: ${instanceOne.getName()}`)
console.log(`Nombre de la segunda inicialización: ${instanceTwo.getName()}`)
console.log(`Nombre de la tercera inicialización: ${instanceThree.getName()}`)

// ------------------------------------ DIFICULTAD EXTRA ------------------------------------
class Sesion {
  constructor(id, nombreUsuario, nombre, email) {
    if (!!Sesion.instance) {
      return Sesion.instance
    }

    Sesion.instance = this 
    this.id = id 
    this.nombreUsuario = nombreUsuario 
    this.nombre = nombre 
    this.email = email

    return this
  }

  recuperarDatos() {
    return [this.id, this.nombreUsuario, this.nombre, this.email]
  }

  finalizarSesion() {
    Sesion.instance = false
    this.id = null
    this.nombreUsuario = null
    this.nombre = null
    this.email = null
  }
}

const usuario = new Sesion(453289, 'Singleton', 'Keny', 'emailpromedio@gmail.com')
console.log(`${usuario.recuperarDatos().join(', ')}`)
usuario.finalizarSesion()
console.log(`${usuario}`)