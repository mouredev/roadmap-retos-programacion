import Foundation


var myArray = [1, 2, 3, 4, 5]
print(myArray)



// Insertar.
print("\nInserción.")

myArray.append(6)
print(myArray)

myArray.append(contentsOf: [7, 8, 9])
print(myArray)

myArray.insert(0, at: 0)
print(myArray)

myArray.insert(contentsOf: [-2, -1], at: 0)
print(myArray)



// Eliminar.
print("\nEliminación")

myArray.remove(at: 4)
print(myArray)



// Actualizar.
print("\nActualizar.")

myArray[7] = 400
print(myArray)



// Contiene.
print("\nContenido.")

print(myArray.contains(400))



// Eliminar todos.
print("\nElinar todas todo.")

myArray.removeAll()
print(myArray)




// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA.")




// Union.
print("\nUnión.")


var mySet: Set<Int> = [100, 44, 29, 71, -14, 999, 1, -4194]
var newSet: Set<Int> = [440, 71, 32, -18, 44, 4194, 12, 87]


let union = mySet.union(newSet)
print(union)

mySet.formUnion(newSet)
print(mySet)



// Intersección.
print("\nIntersección.")


mySet = [100, 44, 29, 71, -14, 999, 1, -4194]
newSet = [440, 71, 32, -18, 44, 4194, 12, 87]


let intersection = mySet.intersection(newSet)
print(intersection)

mySet.formIntersection(newSet)
print(mySet)



// Diferencia.
print("\nDiferencia.")


mySet = [100, 44, 29, 71, -14, 999, 1, -4194]
newSet = [440, 71, 32, -18, 44, 4194, 12, 87]


let subtracting = mySet.subtracting(newSet)
print(subtracting)



// Diferencia simetrica.
print("\nDiferencia Simetrica.")


mySet = [100, 44, 29, 71, -14, 999, 1, -4194]
newSet = [440, 71, 32, -18, 44, 4194, 12, 87]


let symmetricDiferene = mySet.symmetricDifference(newSet)
print(symmetricDiferene)

mySet.formSymmetricDifference(newSet)
print(mySet)

