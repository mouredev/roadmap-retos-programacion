import Foundation
/*
 Decorator es un patron de diseño estructural que permite añadir 
 dinamicamente  nuevos comportamientos a un objeto  colocandolo
 dentro de objetos que los envuelven.(wrapper)

 para mas informacion https://refactoring.guru/es/design-patterns/decorator


 */

 // 1.- creamos un protocolo(interface) para las operaciones que vamos a modificar 
 protocol MacComputer{
     func getDataComputer() -> String
 }

 //2.- creamos una clase que implemente el protocolo
 class MacbookPro: MacComputer{
     func getDataComputer() -> String {
         return "MackbookPro has "
     }
 }

 //3.- creamos la clase que va a ser el wrapper de la clase MacbookPro
 class MacDecorator: MacComputer{
     private var macbookPro: MacComputer

     init(_ macbookPro: MacComputer){
         self.macbookPro = macbookPro
     }
     func getDataComputer() -> String {
         return macbookPro.getDataComputer()
     }
    }

   //4.-creamos los diferentes objetos  que va envolver nuestro wrapper 
 class MacDecoratorCpu: MacDecorator{
     override func getDataComputer() -> String {
         return super.getDataComputer() + "M3 pro processor"
     }
 }

 class MacDecoratorRam: MacDecorator{
     override func getDataComputer() -> String {
         return super.getDataComputer() + " and 16 GB ram"
     }
 }

 //5.- creamos una instancia de la clase MacDecorator
 let macbookPro = MacbookPro()
 let macDecoratorCpu = MacDecoratorCpu(macbookPro)
 let macDecoratorRam = MacDecoratorRam(macDecoratorCpu)
 print(macDecoratorRam.getDataComputer())

// reto extra

protocol Count{
    func getCount() -> Int
}

class CountExucution: Count{
    private var count = 0
    func getCount() -> Int {
        count += 1
        return count
    }
}

class CountDecorator: Count{
    private var countExucution: Count
    init(_ countExucution: Count){
        self.countExucution = countExucution
    }
    func getCount() -> Int {
        return countExucution.getCount()
    }
}

class SwiftVersion: CountDecorator{

   func getSwiftVersion() -> String {
      print("function invoke \(getCount()) times")
      return "5.10.1"
    }

    override  func getCount() -> Int {
        return super.getCount() 
    }
}

let swiftVersion = SwiftVersion(CountExucution())
print(swiftVersion.getSwiftVersion())
print(swiftVersion.getSwiftVersion())
