//clases
class Programmer {
    //constructor en mi inicio 
    constructor(nombre, experiencia, lenguajes){
        this.nombre = nombre,
        this.experiencia = experiencia,
        this.lenguajes = lenguajes

    }
    //funcion que imprima  console.log
    mortrarData (){
        console.log(this.nombre, this.experiencia, this.lenguajes + ' desde funcion mostrardata()')
    }

}
//créala y establece sus parámetros
let myProgramer = new Programmer('Dav', 2, ['javascript', 'java', 'python'])
myProgramer.mortrarData()
//modifícalos
myProgramer.experiencia = 5
myProgramer.mortrarData()
myProgramer.lenguajes.push('c#')
//imprímelos utilizando su función.
myProgramer.mortrarData()


// Extra 
// pila stack
class Pila {
    constructor(stack){
        this.stack = stack
    }
    añadir(num){
        this.stack.push(num)
    }
    eliminar(){
        this.stack.pop()
    }
    mostrar(){
        console.log('numero de elemtos en mi pila :' + this.stack.length , ', ' + this.stack )
    }
}

let myPila = new Pila([1,2,3])
myPila.añadir(10)
myPila.añadir(15)
myPila.mostrar()
myPila.eliminar()
myPila.mostrar()

// Cola queue 
class Cola {
    constructor(array){
        this.array = array
    }
    añadir(num){
        this.array.push(num)
    }
    eliminar(){
        this.array.shift()
    }
    mostrar(){
        console.log('numero de elemtos en mi pila :' + this.array.length , ', ' + this.array )
    }



}

let myCola = new Cola([])
 myCola.añadir('cliente')
 myCola.añadir('cliente1')
 myCola.añadir('cliente2')
myCola.eliminar()
 myCola.mostrar()
