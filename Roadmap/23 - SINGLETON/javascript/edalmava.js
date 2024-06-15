let contador = 0
let instancia

class Contador { 
    constructor() {
      if (instancia) {
        throw new Error('Solo se puede crear una sola instancia')
      }

      instancia = this
    }

    getInstancia() {
      return this
    }

    getContador() {
      return contador
    }

    incrementar() {
      return ++contador
    }

    decrementar() {
      return --contador
    }
}

const estado = Object.freeze(new Contador())
//const estado2 = new Contador() // Error: Solo se puede crear una sola instancia

estado.incrementar()  
estado.incrementar()
estado.incrementar()
estado.decrementar()
console.log(`Valor de contador: ${estado.getContador()}`)

// RETO EXTRA

let instanciaSesion = null

class Sesion {
  constructor(id, username, nombre, email) {
    if (instanciaSesion) {
      throw new Error('Solo se puede crear una sola instancia')
    }
  
    instanciaSesion = this
    this.id = id
    this.username = username
    this.nombre = nombre
    this.email = email
  }

  getSesion() {
    return instanciaSesion
           ?({ id: this.id, username: this.username, nombre: this.nombre, email: this.email })
           :null
  }

  delSesion() {
    instanciaSesion = null    
  }
}

const usuario = Object.freeze(new Sesion('1090', 'edalmava', 'Edwin Martinez', 'eamartinezv@gmail.com'))
console.log(JSON.stringify(usuario.getSesion()))
usuario.delSesion()
console.log(usuario.getSesion())
