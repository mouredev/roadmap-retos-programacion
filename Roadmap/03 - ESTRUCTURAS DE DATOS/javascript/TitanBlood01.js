//Estructuras de datos en javascript

//Array
// Declaracion de Arrays

let miArray = [] //Un Array vacio

miArray = ['Gato','Perro','Liebre',45,78,8,8] //El array puede tener diferentes Tipos de datos dentro
//Tambien permite tener datos repetidos

let miArray2 = new Array(true, false) //Otra forma de poder declararlo y ponerle valores

miArray = [34, 53, 'FcBarcelona', 'Bayer Munich', 'Psg', true, false] //Se pueden cambiar los valores dentro del array

console.log(miArray[3]) //obtencion del valor mediante posicion en el array

miArray[2] = 47 //Cambio de un unico valor mediante posicion o indice


//metodos de los arrays

miArray.push('Real Madrid') //Insercion de nuevo dato al final
console.log(miArray)
miArray.pop() //Eliminacion del ultimo dato del array y lo devuelve
miArray.shift() //Elimina el primer elemento del array y lo devuelve
miArray.unshift('Nuevo elemento') //Adiciona en la primera posicion un nuevo elemento en el array y lo devuelve
console.log(miArray)
miArray.length //obtiene la longitud o tamaño de los datos del array

let slicedArray = miArray.slice(1,4) //Crea un nuevo array con la porcion de los datos especificados en el rango de posiciones entre parentesis
console.log(slicedArray) 
miArray.splice(1, 4, 'elemento') //Elimina los valores que estan incluidos en esos indices, el primer parametro
//es la posicion donde se empezara la eliminacio, el segundo parametro es el numero de elementos que se eliminaran a partir de ahi, y el tercer
//parametro es opcional, especifica un nuevo valor que ocupara el espacio de los valores que estan siendo eliminados
console.log(miArray)


//ESTRUCTURA DE DATO SET

let mySet = new Set() //Inicializacion de un set vacio
mySet = new Set(['primero','segundo','Tercero',45,78,8,9]) //Inicializacion de un set con valores, el set no permite valores repetidos, deben ser unicos

//Metodos de un set
mySet.add('cuarto') //Añade un nuevo elemento al final del set
console.log(mySet)
mySet.delete(78) //Elimina un elemento del set siempre y cuando exista dentro del set, no es necesario que sea el ultimo si o si
console.log(mySet)
console.log(mySet.has('quinto')) //Verifica que un elemento exista dentro del set y esto devuelve un true o false dependiendo el resultado
console.log(mySet.size) //Retorna el numero de elementos unicos que tiene un set
let arrayFromSet = Array.from(mySet) //conversion de un set a array
console.log(arrayFromSet)
let setFromArray = new Set(arrayFromSet)
console.log(setFromArray)

//ESTRUCTURA DE DATO MAP

let myMap = new Map() //Inicializacion de un map
myMap = new Map([
    ['City', 'Cochabamba'],
    ['Country', 'Bolivia'],
    ['Continent', 'America']
]) //Inicializacion con variables

//Metodos de los map
myMap.set('state', 'murillo') //Añade nuevo elemento al map con su correspondinte clave valor
console.log(myMap)
console.log(myMap.get('City'))//Obtiene el valor de un elemento del map si coincide con la clave pasada como parametro
console.log(myMap.has('Building')) //Devuelve true o false dependiendo si el valor existe con la clave que se esta pasando como parametro
console.log(myMap.delete('state')) //Sirve para eliminar devuelve true si el elemento existe y si fue correctamente eliminado, y false si no existe en el map
console.log(myMap)
console.log(myMap.keys()) //Devuelve una lista iterable de todas las claves que existen en el map
console.log(myMap.values()) //Devuelve una lista iterable de todos los valores que existen en el map
console.log(myMap.entries()) //Devuelve una lista iterable de todas las claves y valores que existen en el map

console.log(myMap.size) //Devuelve el tamaño que tiene el map con sus valores y claves

myMap.clear() //Elimina todos los elementos del map volviendolos vacios
console.log(myMap)

/*
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

let agendaContacto = new Map([
    ['Yo', 79710194],
    ['Daniela', 68858143],
    ['Daniel', 78714197],
    ['Giovanni', 79881842],
    ['Kelia', 79881852],
    ['Martha', 70521316]
])


function buscarContacto(target) {
    try {
        return agendaContacto.get(target)
    } catch (error) {
        window.alert('Ocurrio un error: ', error)
    }
}
function addContacto(key, value) {
    try {
        agendaContacto.set(key, value)
        window.alert(`Se añadio correctamente el contacto, su agenda es la siguiente: ${agendaContacto.entries()}`)
    } catch (error) {
        window.alert('Ocurrio un error: ', error)
    }
}
function modifyContacto(key, newKey, value) {
    try {
        agendaContacto.delete(key)
        agendaContacto.set(newKey, value)
        window.alert(`Se modifico correctamente el contacto, ${newKey}: ${agendaContacto.get(newKey)}`)
    } catch (error) {
        window.alert('Ocurrio un error: ', error)
    }
}
function deleteContacto(key) {
    try {
        agendaContacto.delete(key)
        window.alert(`Se elimino correctamente el contacto, ${key}`)
    } catch (error) {
        window.alert('Ocurrio un error: ', error)
    }
}

let exit = false

while(!exit){
    let opcionFuncion = prompt(`Bienvenido a su agenda, por favor 
        seleccione la accion que quiera realizar:
        1. Buscar
        2. Nuevo Contacto
        3. Actualizar contacto
        4. Eliminacion de contacto
        5. Salir`)
    

    switch(parseInt(opcionFuncion)){
        case 1:
            let busqueda = prompt('Digite el contacto que desea buscar: ')
            let resultado = buscarContacto(busqueda)
            window.alert(`Numero de ${busqueda}: ${resultado}`)
            console.log(agendaContacto)     
            break
        case 2:
            let newName = prompt('Digite el nombre del nuevo contacto que desea añadir: ')
            let newNumber = prompt('Digite el numero del nuevo contacto que desea añadir: ')
            if (/[^0-9]/.test(newNumber) || !(newNumber.length <= 11)){
                newNumber = prompt('Numero no valido, digite uno con menos o igual  11 caracteres numericos')
            }
            addContacto(newName, parseInt(newNumber))
            console.log(agendaContacto)     
            break
        case 3:
            let contact = prompt('Digite el nombre del contacto que desea modifcar: ')
            let modifyName = prompt('Digite el nombre modificado del contacto que desea modifcar: ')
            let modifyNumber = prompt('Digite el nuevo numero del contacto que desea modificar: ')
            if (!(modifyNumber.length <= 11) || /[^0-9]/.test(modifyNumber)){
                modifyNumber = prompt('Numero no valido, digite uno con menos o igual a 11 caracteres numericos')
            }
            modifyContacto(contact, modifyName, parseInt(modifyNumber))
            console.log(agendaContacto)     
            break
        case 4:
            let eliminar = prompt('Que contacto desea eliminar?:')
            deleteContacto(eliminar)
            console.log(agendaContacto)     
            break
        case 5:
            exit = true
            window.alert('Sales de la agenda')
            break
        default:
            exit = true
            window.alert('Accion no valida, saliendo...')
        }
    }

console.log(agendaContacto)     


