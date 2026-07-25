const myList: (number | number[])[] = [1,2,3,4]

myList.push(5)
myList.unshift(0)
myList.push([10, 11, 12])
myList[2] = [20, 21, 23]
myList.splice(0, 1)
myList[0] = 3
myList.includes(3)
myList.length = 0

/*
  Extra
*/

const mySet1: Set<number> = new Set([1, 3, 5, 7, 9])
const mySet2: Set<number> = new Set([1, 4, 9])

// Unión
console.log(mySet1.union(mySet2))

// Intersección
console.log(mySet1.intersection(mySet2))

// Diferencia
console.log(mySet1.difference(mySet2))

// Diferencia simétrica
console.log(mySet1.symmetricDifference(mySet2))

/*
  * Referencia: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
*/