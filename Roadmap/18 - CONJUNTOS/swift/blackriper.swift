import Foundation

/*
  un conjunto es la collecion de elementos  agrupados en algun objeto esta collecion no 
  necesariamente tiene un orden y a estas se les pueden aplicar varias operaciones 

  Uniòn : es cuando los elementos de un conjunto se combinan con otro  para dar como resultado 
  un nuevo conjunto de elementos conformados por los elementos de los dos conjuntos originales.

  Intersección :  operacion que como resultado da un conjuto cuyos elementos son los elementos
  comunes entre los dos conjuntos originales.

  Diferencia : es la operacion que da como resultado un conjunto de elementos que son los elementos
  que no son comunes entre los dos conjuntos originales

  Diferencia simétrica : es la operacion que da como resultado un conjunto cuyos elementos pertenecen a ambos 
  conjuntos originales pero no a ambos ala vez.

 */

 func OperationsWithCollections(){
    var numbers = [1,2,3,4,5,6,7,8,9,10]
    
    // agregar elementos a la lista 
    numbers.append(11)
    print(numbers)
    
    //agregar elementos al principio de la lista
    numbers.insert(0, at: 0)
    print(numbers)
    
   // agregar varios elemntos 
    numbers.append(contentsOf: [12,13,14,15,16])  
    print(numbers)

    // agregar varios elementos en un indice particular
    numbers.insert(contentsOf: [17,18,19,20], at: 2)
    print(numbers)

    // actualizar un elemento de la lista
    numbers[2] = 3
    print(numbers)

    // encontrar un elemento de la lista
     print(numbers.contains(21)) 

    //remover un elemento de la lista
    numbers.remove(at: 0)
    print(numbers)
    
    //remover todos los elementos de la lista
    numbers.removeAll()
    print(numbers)
        
 }
 
 OperationsWithCollections()

 func OperationsWithSets(){
     let characters: Set<String> = ["orochimaru","obito","madara","kisame","danzo","sasori","hidan","kakashi"]
     let charactersNaruto: Set<String> = ["naruto","sasuke","itachi","sakura","kakashi","sasori","danzo"]

     // union de conjunto 
     
     // forma declarativa
     print("union de conjuntos declarativa")
     let newCharacters = characters.union(charactersNaruto)
     print(newCharacters)

     // forma imperativa
     print("union de conjuntos imperativa")
     var unionCharacters: [String]=[]
     unionCharacters+=characters
     unionCharacters+=charactersNaruto
     print(unionCharacters)
 
      // intersección de conjuntos
      
      print("interseccion de conjuntos declarativa")
      let commonCharacters = characters.intersection(charactersNaruto)
      print(commonCharacters)

      print("interseccion de conjuntos imperativa")
      let commonCh = characters.filter{charactersNaruto.contains($0)}
      print(commonCh)
      
      // diferencia de conjuntos

      // forma declarativa
      print("diferencia de conjuntos declarativa")
      let differentCharacters = characters.subtracting(charactersNaruto)
      print(differentCharacters)

      // forma imperativa
      print("diferencia de conjuntos imperativa")
      let differentCh = characters.filter{!charactersNaruto.contains($0)}
      print(differentCh)
      
      // diferencia simétrica
     
      // forma declarativa
      print("diferencia simétrica de conjuntos declarativa")
      let symmetricDifference = characters.symmetricDifference(charactersNaruto)
      print(symmetricDifference)

      // forma imperativa
      print("diferencia simétrica de conjuntos imperativa")
      let different = characters.filter{!charactersNaruto.contains($0)}
      let different2 = charactersNaruto.filter{!characters.contains($0)}
      let symmetricDifferenceCh = Array(different.union(different2))
      print(symmetricDifferenceCh)

 }

 OperationsWithSets()

