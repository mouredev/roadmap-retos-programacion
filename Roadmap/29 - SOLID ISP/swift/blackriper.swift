/*
Interface Segregation Principle

Este principio nos dice que una clase nunca debe extender de interfaces con métodos que no usa,
por el principio de segregación de interfaces busca que las interfaces sean lo más pequeñas
y específicas posible de modo que cada clase solo implemente los métodos que necesita.

errores comunes con este principio

- Estaremos violando este principio si Tenemos clases que implementan métodos de interfaces que no se usan.

- Definimos interfaces con parámetros que no se van a utilizar en todas las clases

-cuando tenemos interfaces muy grandes y métodos que no son genéricos y que otras clases que implementen esta interfaz no puedan usar

*/

//ejemplo de lo que no debe de hacerce

protocol Animal{
    func eat()
    func sleep()
    func run() throws->Void
}

enum ErrorAnimal:Error{
    case IcannotRun(name:String)
}

class Chicken:Animal{
   let name:String
   init(namePet:String){
       name=namePet
   }
   
   func eat(){
       print("\(name) is eating")
   }
   
   func sleep(){
       print("the chicken \(name) is sleeping") 
   }
   
   func run() throws->Void{
       print("the chicken \(name) is running")
   }
}

// como el pez no puede correr mandamos un error por lo cual violamos este principio


class Fish:Animal{
   let name:String
   init(namePet:String){
       name=namePet
   }
   
   func eat(){
       print("\(name) is eating")
   }
   
   func sleep(){
       print("the fish \(name) is sleeping") 
   }
   
   func run() throws->Void{
      throw ErrorAnimal.IcannotRun(name: name)
   }
}


let chicken=Chicken(namePet:"triki")
chicken.eat()
chicken.sleep()
try chicken.run()

let fish=Fish(namePet:"bandalo")
fish.eat()
fish.sleep()
do{
  try fish.run()
}catch ErrorAnimal.IcannotRun(let name) {
   print("the  fish \(name) cannot run ")
}

// la forma  correcta de cumplir el principio

protocol Specie{
  func eat()
  func sleep()
}

// como la gallina si puede correr creamos una interfaz derivada de la original
 protocol EarthSpecie:Specie{
     func run()
 }

// ahora las clases quedan de la siguiente manera 

class ChickenISP:EarthSpecie{
   let name:String
   init(namePet:String){
       name=namePet
   }
   
   func eat(){
       print("\(name) is eating")
   }
   
   func sleep(){
       print("the chicken \(name) is sleeping") 
   }
   
   func run() {
       print("the chicken \(name) is running")
   }
}

class FishISP:Specie{
   let name:String
   init(namePet:String){
       name=namePet
   }
   
   func eat(){
       print("\(name) is eating")
   }
   
   func sleep(){
       print("the fish \(name) is sleeping") 
   }
 }

let chick=ChickenISP(namePet:"blanquita")
chick.eat()
chick.sleep()
chick.run()

let fishing=FishISP(namePet:"guason")
fishing.eat()
fishing.sleep()

// ejercicio extra

enum Color{
    case black_and_white
    case color
}

// creamos una interfaz base de la cual haremos uns interface derivada 

protocol Printer{
    func print(_ document:String)->String
}


protocol MultiFunctionPrinter:Printer{
    func sendFax(_ fax:String)->String 
    func scanDocument(_ document:String)->String
}


struct NormalPrinter:Printer{
    let colorPrint:Color
    
    func print(_ document:String)->String{
        return "printing \(document) in \(colorPrint)"
    }
}


struct MultifunPrinter:MultiFunctionPrinter{
    let colorPrint:Color
    
    func sendFax(_ fax:String)->String{
        return "sending fax \(fax)"
    }
    
    func scanDocument(_ document:String)->String{
        return "scan \(document)"
    }
    
    func print(_ document:String)->String{
        return "printing \(document) in \(colorPrint)"
    }
}

func printingDocument(thermal:Printer,content:String){
    print(thermal.print(content))
}



let printer=NormalPrinter(colorPrint:.black_and_white)
let multi=MultifunPrinter(colorPrint:.color)

printingDocument(thermal:printer,content:"Swift is great")
printingDocument(thermal:multi,content:"Swift is embebed")

print(multi.sendFax("critical fail in system"))
print(multi.scanDocument("WWDC2024 photos"))
