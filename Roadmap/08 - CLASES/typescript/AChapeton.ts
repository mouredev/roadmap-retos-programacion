class Todo {
  constructor(title: string, description: string, done: boolean, user: string, daysLeft: number){
    this.title = title,
    this.description = description,
    this.done = done,
    this.user = user,
    this.daysLeft = daysLeft
  }

  //Los Getters se utilizan para no interactuar directamente con las propiedades de la clase.
  //Tambien se evita para no dar a conocer todas sus propiedades, por seguridad.
  get finishTodo (){
    return this.toggleTodo()
  }

  //Metodos
  toggleTodo() {
    return !this.done
  }
}

const myTodo = new Todo('Finish roadmap', 'Finish exercise #08', false, 'Andres', 5)

console.log(myTodo)

console.log(myTodo.finishTodo)


/* DIFICULTAD EXTRA */

class Pila {
  constructor(data: Array<any>){
    this.data = data
  }

  addElementAction(element: any){
    return this.data.unshift(element)
  }

  deleteElementAction(){
    return this.data.shift()
  }

  sizeAction(){
    return this.data.length
  }

  get addElement() {
    return this.addElementAction
  }

  get deleteElement() {
    return this.deleteElementAction
  }

  get size(){
    return this.sizeAction
  }
}

const nuevaPila = new Pila([])

console.log('Pila vacia', nuevaPila)
nuevaPila.addElement(1)
nuevaPila.addElement(2)
nuevaPila.addElement(3)
console.log('Nuevos elementos agregados', nuevaPila)
console.log('Cantidad de elementos', nuevaPila.size())
nuevaPila.deleteElement()
console.log('Eliminado ultimo elemento', nuevaPila)

class Cola {
  constructor(data: Array<any>){
    this.data = data
  }

  addElementAction(element: any){
    return this.data.push(element)
  }

  deleteElementAction(){
    return this.data.shift()
  }

  sizeAction(){
    return this.data.length
  }

  get addElement() {
    return this.addElementAction
  }

  get deleteElement() {
    return this.deleteElementAction
  }

  get size(){
    return this.sizeAction
  }
}

const nuevaCola = new Cola([])

console.log('Cola vacia', nuevaCola)
nuevaCola.addElement(1)
nuevaCola.addElement(2)
nuevaCola.addElement(3)
console.log('Nuevos elementos agregados', nuevaCola)
console.log('Cantidad de elementos', nuevaCola.size())
nuevaCola.deleteElement()
console.log('Eliminado primer elemento', nuevaCola)