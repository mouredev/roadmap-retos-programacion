/* iteractors son una forma de recorrer una colección de datos
   en swift contamos con los protocolos IteratorProtocol y Sequence 
   para poder crear nuestros propios iteradores
 */


import Foundation


func examplesWithIterators() {
  let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  print("using for in")
  for number in numbers {
    print(number)
  }

  print("using forEach")
  numbers.forEach { number in
    print(number)
  }

  print("using repeat while")
  var index = 0
  repeat {
    print(numbers[index])
    index += 1
  } while index < numbers.count

}

examplesWithIterators()

// ejercicio extra

func examplesWithOtherIterators() {
  let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   print("usando while")
   var index = 0
   while index < numbers.count {
     print(numbers[index])
     index += 1
   }
    
   print("using custom struct")
   struct MyIterator: Sequence,IteratorProtocol {
       var current = 1
       mutating func next() -> Int? {
           defer { current += 1 }
           return current
       }
   }
   var i=0
   for number in MyIterator() {
       i+=1
       if i == 10 {break}
       print(number)
   }

   print("using for range ")
   for number in 1...10 {
       print(number)
   }
}

examplesWithOtherIterators()
