console.log('/* ESTRUCTURA DE DATOS */')
console.log('/* ----- ***** ----- ***** ----- ***** ----- */')

console.log('/* ARRAYS */')
const myList = ['Marcos', 'Estefanía', 'Izan', 'Gael', 'Olivia']
console.log(myList)

console.log('Añadir elemento al final de la lista')
myList.push('Slash')
console.log(myList)

console.log('Añadir elemento al principio de la lista')
myList.unshift('Mushu')
console.log(myList)

console.log('Añadir elemento a ubicación específica de la lista')
myList.splice(3, 0, 'Neo') // splice => el primer argumento es la posición, el segundo argumento cuántos elementos quiero borrar (en este caso 0), el tercer argumento lo que inserto
console.log(myList)

console.log('Eliminar el último elemento de la lista')
myList.pop()
console.log(myList)

console.log('Eliminar el primer elemento de la lista')
myList.shift()
console.log(myList)

console.log('Eliminar elemento elegido en de la lista')
myList.splice(2, 1)
console.log(myList)


console.log('/* ----- ***** ----- ***** ----- ***** ----- */')


console.log('/* Acceder a un elemento del array */')
console.log(myList[3])

console.log('/* Actualizar un elemento del array */')
myList[2] = 'Z'
console.log(myList)


console.log('/* ----- ***** ----- ***** ----- ***** ----- */')


console.log('/* Ordenar un array */')
console.log(myList.sort())


console.log('/* ----- ***** ----- ***** ----- ***** ----- */')


console.log('/* Tuple */') // Son elementos inmutables, en javascript existe esta opción
const myTuple = Object.freeze(['Marcos', 'Pérez', '@socramdev', 46])
console.log(myTuple)


console.log('/* ----- ***** ----- ***** ----- ***** ----- */')


console.log('/* SETS */')
const mySet = new Set()
console.log(typeof(mySet))

console.log('/* Añadir al set */')
mySet.add('Marcos')
console.log(mySet)
mySet.add('Pérez')
console.log(mySet)
mySet.add('@socramdev')
console.log(mySet)
mySet.add(46)
console.log(mySet)

console.log('/* Añadir al set un mismo valor */') // Si os datos son iguales, no se duplican
mySet.add('Marcos')
console.log(mySet)

console.log('/* Eliminar del set */')
mySet.delete('Pérez')
console.log(mySet)


console.log('/* ----- ***** ----- ***** ----- ***** ----- */')


console.log('/* OBJETOS / DICCIONARIOS */')
const myDict = {
    'name': 'Marcos',
    'surname': 'Pérez',
    'alias': '@socramdev',
    'age': 46
}
console.log(myDict)

console.log('/* Acceder al diccionario */')
console.log(myDict['name'])

console.log('/* Añadir al diccionario */')
myDict.email = 'socram@socram.com'
console.log(myDict)

console.log('/* Actualizar al diccionario */')
myDict.age = 47
console.log(myDict)

console.log('/* Eliminar del diccionario */')
delete myDict.age
console.log(myDict)


console.log('/* ----- ***** ----- ***** ----- ***** ----- */')


console.log('/* DIFICULTAD EXTRA - AGENDA */')
// Pendiente ya que no se usar aplicaciones en Terminal