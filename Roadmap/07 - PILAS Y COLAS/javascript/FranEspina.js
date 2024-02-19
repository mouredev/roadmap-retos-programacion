import * as readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process'

//Implementación Pila (LIFO)
class Pila {

  constructor() {
    this.pila = []
  }

  encolar(value){
    this.pila.push(value)
  }

  desencolar(){
    return this.pila.pop()
  }

  numero(){
    return this.pila.length
  }

  valores(joinStr){
    let separator = '\r\n'
    if (joinStr){
      separator = joinStr
    }
    let valores = ""
    this.pila.forEach(item => valores += item + separator)
    return valores

  }

  actual () {
    if (this.pila.length === 0){
      return undefined
    }
    else{
      return this.pila[this.pila.length - 1]
    }
  }

  reiniciar(){
    this.pila = []
  }

}

//Implementación Cola (FIFO)
class Cola {

  constructor() {
    this.cola = []
  }

  encolar(value){
    this.cola.push(value)
  }

  desencolar(){
    return this.cola.shift()
  }

  numero(){
    return this.cola.length
  }

  valores(){
    let valores = ""
    this.cola.forEach(item => valores += "\r\n" + item)
    return valores
  }

}

//Implementación de una impresora que usa Colas
class Impresora {

  constructor(rl) {
    this.colaImpresion = new Cola()
    this.LogImpresion = new Cola()
    this.rl = rl
    this.intervalId = null;
  }

  async encender(){

    console.clear()
    console.log("Impresora activada")
    this.LogImpresion.encolar(`${new Date().toISOString()} Impresora conectada y lista para imprimir'`)    
    this.#impresionPeriodica(5) //Cada cierto tiempo se imprime todo lo que esté pendiente
    this.#escucharUsuario()

  }

  async #escucharUsuario() {
    
    const opcion = await this.rl.question('¿Qué desea hacer? [I]mprimir documento | [L]og Impresion | [D]ocumentos | [S]alir : ') 
    
    switch(opcion.toUpperCase()){

      case "I": 
        await this.#solicitarDocumentoUsuario()
        break

      case "L":
        console.log(this.LogImpresion.valores())
        await this.#escucharUsuario()
        break

      case "D":
        this.LogImpresion.encolar(`${new Date().toISOString()} Solicitado documentos en cola`)
        if (this.colaImpresion.length == 0){
          console.log("No existen documentos pendientes de imprimir")
        }
        else{
          console.log(this.colaImpresion.valores())
        }
        await this.#escucharUsuario()
        break

      case "S":
        this.#desconectarYSalir()
        break
         
      default: 
        await this.#escucharUsuario()
        break  
    }
  }

  //Imprime documentos encolados cada cierto tiempo para simular trabajo asíncrono (cada x tiempo imprime solo 1 documento )
  #impresionPeriodica(seconds) {
    this.intervalId = setInterval(() => {
      if (this.colaImpresion.numero() !== 0){
        var documento = this.colaImpresion.desencolar()
        this.LogImpresion.encolar(`${new Date().toISOString()} Imprimiendo documento: '${documento}'`)
      }
    }, seconds * 1000);
  } 

  async #solicitarDocumentoUsuario() {
    var opcion = await this.rl.question('Nombre del documento ([S]alir): ')    
    switch(opcion.toUpperCase()){
      case "S":
        await this.#escucharUsuario()
        break
      default:
        this.colaImpresion.encolar(opcion)
        this.LogImpresion.encolar(`${new Date().toISOString()} Documento encolado: '${opcion}'`)    
        await this.#solicitarDocumentoUsuario()
        break    
    }
  }

  #desconectarYSalir(){
    clearInterval(this.intervalId)
    console.log('Impresora desconectada')
    this.rl.close()
    globalThis.process.exit()
  }
  
}

//Implementación de un navegador Web que usa Pilas
class NavegadorWeb {
  constructor(rl){
    this.historial = new Pila() 
    this.paginasNavegadas = new Pila()
    this.rl = rl

    console.clear()
    console.log("Navegador Web inicializado")
  }

  async mostrarNavegador(){
    
    var pagina = this.historial.actual()
    if (pagina){
      console.log(`\r\nPágina actual : ${pagina}`)
    }
    else{
      console.log(`\r\nPágina en blanco`)
    }

    const navegacion = {
      "navegar": (pagina) => {
        this.historial.encolar(pagina)
      }, 
      "delante": () => {
        if (this.paginasNavegadas.numero() > 0 ){
          var pagina = this.paginasNavegadas.desencolar()
          this.historial.encolar(pagina)
        }
        else{
          console.log('No existe historial por delante\r\n')
        }  
      }, 
      "atras": () => {
        if (this.historial.numero() > 0){
          var pagina = this.historial.desencolar()
          this.paginasNavegadas.encolar(pagina)
        }
        else{
          console.log('No existe historial atrás\r\n')
        }
      }, 
      "salir": () => {
        console.log('Navegador cerrado por el usuario')
        this.rl.close()
        globalThis.process.exit() 
      }

    }

    var pagina = await this.rl.question(`¿a qué página desea navegar${this.#opcionesDeNavegacion()}?:  `)
    switch(pagina.toUpperCase()){
      case "A": 
        navegacion["atras"]()    
        break

      case "D": 
        navegacion["delante"]()      
        break

      case "S": 
        navegacion["salir"]()      
        break

      default:
        navegacion["navegar"](pagina)
        break
    }

    await this.mostrarNavegador()
  }

  #opcionesDeNavegacion () {
    let opctionesPosibles = []
    if (this.historial.numero() > 0){
      opctionesPosibles.push('[A]trás')
    }
    if (this.paginasNavegadas.numero() > 0 ){
      opctionesPosibles.push('[D]elante')
    }
    opctionesPosibles.push('[S]alir')


    return ` (${opctionesPosibles.join(" | ")}) `
  }
}


const mainUserQuestion = async () => {

  const rl = readline.createInterface({input, output})

  console.clear()

  var option = await rl.question('¿Qué programa desea probar? [I]mpresora | [N]avegador WEB| [S]alir: ')
  switch (option.toUpperCase()){
    case "I":
      console.clear()
      const impresora = new Impresora(rl)
      impresora.encender()
      break

    case "N": 
      console.clear()
      const navegador = new NavegadorWeb(rl)
      navegador.mostrarNavegador()
      break

    case "S": 
      rl.close()
      console.log('Operación cancelada por el usuario')
      globalThis.process.exit()
      break  

    default: 
      await mainUserQuestion()
  }
}

mainUserQuestion()