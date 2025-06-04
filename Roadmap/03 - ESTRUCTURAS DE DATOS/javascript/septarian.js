// array
const arr = [1,2]
const arr2 = new Array(0,2,4,5,6)    //OTRA FORMA DE CREAR UN OBJETO
const arr3 = ["erick", "fernando"]
//actualizar
arr2[0] = "hola"
//agrega elemento al inicio
arr2.unshift("manzana") 
//borra el primer elemento del arr
arr2.shift()    
//agrega elemento al final 
arr2.push("adios")
//borra el ultimo elemento
arr2.pop()
//encuentra el indice de un elemento
arr2.indexOf(5)
//elimina elementos desde el index que le indiques y le dices cuantos elementos quieres eliminar
arr2.splice(2, 2)
const nuevoArr = arr2.splice(1,1)   //guardas lo que borraste en otro array
//copiar array
const copiaArray = arr2.slice()
//muestra los indices de los elementos del array
console.log(Object.keys(arr2))
//muestra el numero de elemntos que tiene el array
arr2.length
//crea una nueva instancia de array a partir de un objeto iterable o parecido a un array
console.log(Array.from("hola"))
//devuelve true si si es array o false si no es 
console.log(Array.isArray(arr2))
//Crea una nueva instancia de Array con un número variable de parámetros, independientemente del número y del tipo de dichos parámetros.
Array.of()
//concatena un array con otro
const arr4 = arr2.concat(arr)
//convierte en un string todos los elemntos de un array
arr2.join()
//devuelve true o false si el array contiene lo que se busca
arr2.includes(6)    //true
//invierte el orden del array
arr4.reverse()
//ordena los elementos del array
arr4.sort()


console.log(arr4)

//objetos
const obj = {}
const obj2 = new Object()   //OTRA FORMA DE CREAR UN OBJETO
const obj3 = {name: "erick", age: 23}

//diccionario / matriz
const dic = 
[
    [1,2,3]
    [4],
    [5],
    [6]
]
const dic2 = 
[
    {id: 1, name: "erick"},
    {id: 2, name: "johnny"},
    {id: 3, name: "gyro"}
]

//clases
class Articulo {
    constructor(title, author){
        this.title = title
        this.author = author
    }
}
let terror = new Articulo("cuentos de terror", "alan wake")
console.log(terror.title)
console.log(terror.author)

//set
const mySet = new Set()
mySet.add(1)
mySet.add(2)
console.log(mySet)

//EXTRA
const option = 1