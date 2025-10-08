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
function agenda(){

    const contactos = [
        {name: "erick", tel: 3321904500},
        {name: "johnny", tel: 3321909000},
        {name: "gyro", tel: 3321908080},
    ]

    const option = 1
    const con = "johnny"

    console.log("1. buscar contacto")
    console.log("2. agregar contacto")
    console.log("3. actualizar contacto")
    console.log("4. eliminar contacto")
    console.log("5. salir")

    switch(option){
        case 1:
            console.log("cual contacto quiere buscar")
            let res = contactos.find(contacto => contacto.name === con) //compara que el nombre del contacto y el de la variable con sea el mismo
            if(res){    //si la variable es true (si encontro algo) ejecuta el codigo, si es false (no encontro coincidencias) hace lo del else
                console.log(res)
            } else{
                console.log("el contacto no existe")
            }
        break
        case 2:
            console.log("registre su contacto, primero el nombre")
            let newName = "funny valentine"
            console.log("nombre del contacto es: "+newName)
            console.log("ahora el numero, no puede ser mayor ni menor que 10 numeros")
            let newNumber = "3314111174"
            if(newNumber.length == 10){
                contactos.push({newName, newNumber})
                console.log("numero del contacto es: "+newNumber)
                console.log(contactos[3])
            } else {
                console.log("numero no valido")
                return
            }
        break
        case 3:
            console.log("escribe el nombre del contacto que  quieres actualizar")
            let act = "erick"
            let newAct = contactos.find(contacto => contacto.name === act)
            console.log("1. actualizar nombre")
            console.log("2. actualizar numero")

            let opt = 2

            switch(opt){
            case 1:
                console.log("escribe el nuevo nombre")
                let newNameAct = "diego"
                newAct.name = newNameAct
                console.log(newAct)
            break
            case 2:
                console.log("escribe nuevo numero")
                let newNumberAct = "3311444790"
                 if(newNumberAct.length == 10){
                    newAct.tel = newNumberAct
                    console.log(newAct)
            } else {
                console.log("numero no valido")
                return
            }
            break
            default:
                return
            }
        break
        case 4:
            console.log("nombre del contacto quieres borrar")
            let del = "gyro"
            let deleted = contactos.findIndex(contacto => contacto.name === del)
            if (deleted === -1){
                console.log("no existe el contacto")
            }else{
                contactos.splice(deleted, 1)
                console.log(contactos)
            }
        break
        case 5:
            console.log("hasta luego")
            return
        default:
            return
    }
}

agenda()