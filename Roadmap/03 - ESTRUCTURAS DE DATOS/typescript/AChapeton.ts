// **** TIPOS DE ESTRUCTURAS ****

// ** ARRAYS **
// Tiene dos formas distintas de tiparlo pero ambas dan el mismo resultado
// Se pueden combinar los tipos de datos que se permiten almacenar o incluso personalizarlos, a estos elementos se les llama Tuplas
let numbers: number[] = [2, 4, 6, 8]
let letters: string[] = ['p', 'b', 'd', 'q']
let combined: Array<string | boolean> = ['abc', true, 'def', false] //No se permite otro tipo de dato que no sea String o Boolean

interface User {
  id: number, 
  name: string,
  subscribed: boolean
}

let users: User[] = [
  {
    id: 1, 
    name: 'Andres',
    subscribed: true
  },
  {
    id: 2, 
    name: 'Brais',
    subscribed: false
  },
  {
    id: 3, 
    name: 'Chape',
    subscribed: false
  },
  {
    id: 4, 
    name: 'Jesus',
    subscribed: true
  },
  {
    id: 5, 
    name: 'Midudev',
    subscribed: true
  },
  {
    id: 6, 
    name: 'Teffcode',
    subscribed: false
  }
]
console.log('users', users)

// Operaciones en Arrays

//Push - Agregar elementos al final
const pushUser = {
    id: 11, 
    name: 'Moure',
    subscribed: true
}
users.push(pushUser)
console.log('push', users)

//Unshift - Agregar elementos al inicio
const unshiftUser = {
    id: 0, 
    name: 'Mouredev',
    subscribed: false
}
users.unshift(unshiftUser)
console.log('unshift', users)

//Splice - Agregar elementos en cualquier posicion
//El primer parametro es para indicar en que posicion agregarlo
//El segundo parametro es para indicar cuantos elementos se reemplazarian (0 es ningun elemento)
//El tercer parametro es el elemento a agregar
const spliceUser = {
    id: 12, 
    name: 'Chape',
    subscribed: false
}
users.splice(2, 0, spliceUser)
console.log('splice', users)

//Pop - Eliminar el ultimo elemento
users.pop()
console.log('pop', users)

//Shift - Eliminar el primer elemento
users.shift()
console.log('shift', users)

//Splice - Eliminar un elemento en cualquier posicion
//El primer parametro es la posicion del elemento
//El segundo parametro es la cantidad de elementos a eliminar desde la posiocion indicada
users.splice(2, 1)
console.log('splice', users)

//Filter - Crea un nuevo array con los elementos que cumplan el criterio
const fiteredUsers = users.filter(user => user.id < 10)
console.log('filter', fiteredUsers)

//Sort - Metodo para ordenar datos
let unorderedArray = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];

// Ordenar el array
unorderedArray.sort((a, b) => a - b);
console.log('sort', unorderedArray)


// ** SETS **
let mySet: Set<number> = new Set()

//Add - Agregar un valor
mySet.add(1)
mySet.add(2)
mySet.add(3)
// mySet.add('string') - No se permite porque el Set fue tipado de solo numeros
console.log('add', mySet)

//Has - Verificar si un valor existe dentro del Set
mySet.has(1) //true
mySet.has(3) //false

//Delete - Elimina un valor
mySet.delete(1)
console.log('delete', mySet)

//Size - Devuelve el tama;o del set
console.log('size', mySet.size)

//Clear - Eliminar todos los elementos
mySet.clear()
console.log('clear', mySet)


// ** OBJETOS **
//En TypeScript, se suele declarar la estructura de un objeto por medio de Interface
//Para agregar o eliminar una nueva propiedad, no se podria directamente crer un objeto y a ese colocarle la nueva propiedad, ya que este objeto iria en base al tipado de la interfaz

interface Person{
  name: string,
  age: number,
  genre: string
}



// *** EJERCICIO EXTRA *** 

interface Contact {
  nombre: string | null,
  telefono: number | null,
}

const contacts: Contact[] = []

const agregarContacto = () => {
  let newName: string | null = null;
  let newPhone: string | null = null;

  do {
    newName = prompt('Nombre: ');
    if (!newName) {
      console.log('Por favor, ingresa un nombre válido.');
    }
  } while (!newName);

  do {
    newPhone = prompt('Telefono: ');
    if (!newPhone) {
      console.log('Por favor, ingresa un número de teléfono válido.');
    }
  } while (!newPhone);

  const newContact = {
    nombre: newName,
    telefono: parseInt(newPhone)
  };
  
  contacts.push(newContact)
}

const buscarContacto = () => {
  let searchedName : string | null = null;
  do {
    searchedName = prompt('Buscar por nombre: ')
  } while (!searchedName);
  const searchedResult : Contact | undefined = contacts.find(contact => contact.nombre.toLowerCase() === searchedName.toLowerCase())
  if(searchedResult === undefined){
    alert(searchedName + ' no existe') 
  }else{
    alert(JSON.stringify(searchedResult, null, 2)) 
  }
}

const actualizarContacto = () => {
  let searchedName: string | null = null
  do{
    searchedName = prompt('Buscar por nombre: ')
  }while(!searchedName)
  const searchedResult: number | undefined = contacts.findIndex(contact => contact.nombre.toLowerCase() === searchedName.toLowerCase())
  if(searchedResult === undefined){
    alert(searchedName + ' no existe') 
  }else{
    let newName : string | null = null;
    let newPhone : string | null = null;
    do{
      newName = prompt('Nuevo nombre', contacts[searchedResult]?.nombre || '')
      contacts[searchedResult].nombre = newName
    }while(newName === null)
    do{
      newPhone = prompt('Nuevo telefono', contacts[searchedResult]?.telefono.toString() || '')
      contacts[searchedResult].telefono = parseInt(newPhone)
    }while(newPhone === null)
    alert(searchedName + ' fue actualizado a ' + newName) 
  }
}

const eliminarContacto = () => {
  let searchedName : string | null = null;
  do {
    searchedName = prompt('Nombre de contacto a eliminar: ')
  } while (!searchedName);
  const searchedResult: number | undefined = contacts.findIndex(contact => contact.nombre.toLowerCase() === searchedName.toLowerCase())
  if(searchedResult === undefined){
    alert(searchedName + ' no existe') 
  }else{
    if (searchedResult >= 0 && searchedResult < contacts.length) {
      contacts.splice(searchedResult, 1);
      alert(searchedName + ' fue eliminado')
    } else {
      console.log('Índice inválido');
    }
  }
}

const listarContactos = () => {
  const contactsString = JSON.stringify(contacts, null, 2);
  alert(contactsString);
}

const agendaApp = () => {
  let option: string | null = ''
  const menu: string = 'MENU: \n 1. Agregar nuevo contacto \n 2. Buscar contacto \n 3. Actualizar contact \n 4. Eliminar un contacto \n 5. Listar todos los contactos \n 6. Salir'

  while (option !== '6') {
    option = prompt(menu)

    switch (option) {
      case '1':
        agregarContacto()
        break;
      case '2':
        buscarContacto()
        break;
      case '3':
        actualizarContacto()
        break;
      case '4':
        eliminarContacto()
        break;
      case '5':
        listarContactos()
        break;
      case '6':
        break;
      default:
        console.log('Opcion no valida. Intentar de nuevo.')
        break;
    }
  }
}

agendaApp()

