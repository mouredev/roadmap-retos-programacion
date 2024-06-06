import Foundation
import XMLCoder

/*
 Al proceso de convertir un objeto swift a un formato json o Xml 
 se le conoce como serialización.
 
 anteriormente se usaba la opcion JSONSerialization.dataWithJSONObject para serializar un objeto swift
 pero desde swift 4.0  se creo  un protocolo Codable para serializar un objeto swift.

 Codable es una composición de dos protocolos:  Encodable y Decodable

 Encondable: Permite serializar un objeto swift a un formato json o Xml
 Decodable: Permite deserializar un objeto json o Xml a un objeto swift

 codable por defecto no soporta xml por lo cual hay que agregar una libreria para ello 
 https://github.com/CoreOffice/XMLCoder

 */
 struct Person:Codable{
     let name:String
     let age:Int
     let birthDate:String
     let programmingLanguage:[String]
    }


func exampleWorkingWithJson(){
   let fileManager=FileManager.default
   let encoder=JSONEncoder()
   encoder.outputFormatting = .prettyPrinted
   
   // crear fichero
   let person=Person(name:"Rodolfo",age: 29,birthDate: "20/05/1994",programmingLanguage: ["swift","kotlin","go","python","typescript","java"])
   guard let encoded = try? encoder.encode(person)else{
        print("error to encode ")
        return 
    }
   fileManager.createFile(atPath: "/home/blackriper/Descargas/person.json", contents:encoded, attributes: nil)

   // leer fichero
   if let jsonData=fileManager.contents(atPath: "/home/blackriper/Descargas/person.json"){
        guard let decoded = try? JSONDecoder().decode(Person.self, from: jsonData)else{
                print("error to decode")
                return
            }
        let gretting="""
        Hello my name is \(decoded.name) and I am \(decoded.age) years old.
        I was born on \(decoded.birthDate) and 
        I am learning \(decoded.programmingLanguage)
        """
        print(gretting)
    }
    
    // borrar fichero
    do{
      try fileManager.removeItem(atPath: "/home/blackriper/Descargas/person.json")
    }catch{
        print("error to delete")
    } 

}

exampleWorkingWithJson()

func exampleWorkingWithXml(){
    let fileManager=FileManager.default
    let person=Person(name:"Rodolfo",age: 29,birthDate: "20/05/1994",programmingLanguage: ["swift","kotlin","go","python","typescript","java"])

    // crear fichero
    if let xmlDoc = try? XMLEncoder().encode(person,withRootKey: "person") {
      fileManager.createFile(atPath: "/home/blackriper/Descargas/person.xml", contents:xmlDoc, attributes: nil)
    }

    // leer fichero 
    if let xmlData=fileManager.contents(atPath: "/home/blackriper/Descargas/person.xml"){
        guard let decoded = try? XMLDecoder().decode(Person.self, from: xmlData)else{
                print("error to decode")
                return 
        }
        let gretting="""
        Hello my name is \(decoded.name) and I am \(decoded.age) years old.
        I was born on \(decoded.birthDate) and 
        I am learning \(decoded.programmingLanguage)
        """
        print(gretting)

    }

    // borrar fichero
    do{
      try fileManager.removeItem(atPath: "/home/blackriper/Descargas/person.xml")
    }catch{
        print("error to delete")
    } 
 }

exampleWorkingWithXml()

// ejercicio extra 

 struct Product:Codable {
    var name: String
    var cantity: Int
    var price: Int
}

 enum Formats {
    case xml
    case json
 }

struct FileOperations{
   let path: String 
   private let fileManager = FileManager.default   
    

    func createFile(_ contents: Data?) {
        fileManager.createFile(atPath:self.path,contents: contents)
    }

    func readFile(format: Formats) {
        guard let data = fileManager.contents(atPath: self.path) else {
            print("File not found")
            return
        }
       switch format{
        case .xml:
            if let xmlDoc = try? XMLDecoder().decode([Product].self, from: data) {
              xmlDoc.forEach{ product in
                print("\(product.name)      |    \(product.cantity)       |     \(product.price)  |       \(product.price*product.cantity)")
              }

                }
            
        case .json:
            if let jsonData = try? JSONDecoder().decode([Product].self, from: data) {
              jsonData.forEach{ product in
                print("\(product.name)      |    \(product.cantity)       |     \(product.price)  |       \(product.price*product.cantity)")
            }
        }
       }  
    }
   
    func deleteFile() {
        do {
            try fileManager.removeItem(atPath: self.path)
        }catch let error{
            print("Error deleting file: \(error)")
       }
    }
}


class Cart { 
    private var products: [Product] = []
    let fileManager:FileOperations
    let format:Formats

    init(src:String,fmt:Formats) {
        self.fileManager = FileOperations(path: src)
        self.format = fmt
    }

    func addProduct(product: Product) {
        products.append(product)
        self.saveFile()
    
    }
    func removeProduct(name:String) {
        products.removeAll(where: { $0.name == name.uppercased() })
        self.saveFile()
    }

      func updateProduct(name:String){
       guard var product=products.first(where: { $0.name == name.uppercased() })else {
          print("Product not found")
          return
       }
       print("update name \(product.name):")
       let newName=readLine() ?? product.name

       print("update cantity \(product.cantity):")
       let newCantity = Int(readLine() ?? "\(product.cantity)")

       print("update price \(product.price):")
       let newPrice = Int(readLine() ?? "\(product.price)")

       product.name=newName.uppercased()
       product.cantity=newCantity ?? product.cantity
       product.price=newPrice ?? product.price
       saveFile()
    }

    func listProducts(){
        let header="""
            Name     | cantity | Price
          """      
        print(header)  
        fileManager.readFile(format: format)   
     }

    func totalSold(){
        let total=products.reduce(0) { $0 + $1.price }
        let header="""
            Name       |    cantity   |    Price      |   Total Product
          """      
       print(header)
       products.forEach { product in
        print("\(product.name)      |    \(product.cantity)       |     \(product.price)  |       \(product.price*product.cantity)")
       }
       print("Total sold: \(total)")
    }
    

    func exitApp(){
      fileManager.deleteFile()
    }
  
   private func saveFile() {
       switch format {
           case .xml:
           if let xmlDoc = try? XMLEncoder().encode(products,withRootKey: "products") {
              fileManager.createFile(xmlDoc)
           }
           case .json:
           if let jsonData = try? JSONEncoder().encode(products) {
              fileManager.createFile(jsonData)
           }
       } 
   }
}
            

            

 func marketPlace(format:Formats) {
   let src = switch format {
      case .xml:
         "/home/blackriper/Descargas/products.xml"
      case .json:
         "/home/blackriper/Descargas/products.json"   
    }
     let cart = Cart(src: src, fmt: format)
  marketloop:
     while true {
        print("1. Add product")
        print("2. Remove product")
        print("3. Update product")
        print("4. List products")
        print("5. Total sold")
        print("6. Exit")
        let option = Int(readLine() ?? "0") ?? 0
        switch option {
           case 1:
              print("Name of product:")
              let name = readLine() ?? ""
              print("Cantity:")
              let cantity = Int(readLine() ?? "0") ?? 0
              print("Price:")
              let price = Int(readLine() ?? "0") ?? 0
              let product=Product(name: name.uppercased(), cantity: cantity, price: price)
              cart.addProduct(product: product)
           
           case 2:
              print("Name of product:")
              let name = readLine() ?? ""
              cart.removeProduct(name: name.uppercased())

           case 3: 
              print("Name of product:")
              let name = readLine() ?? ""
              cart.updateProduct(name: name.uppercased())
           case 4:
              cart.listProducts()
           
           case 5:
              cart.totalSold()

           case 6:
              cart.exitApp()
              break marketloop
            
           default:
             print("Invalid option")
        }
    }    
 }

 marketPlace(format: Formats.json)
