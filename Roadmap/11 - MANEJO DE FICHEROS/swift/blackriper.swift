import Foundation

struct User {
    let name: String
    let age: Int

    func getUserString() -> String {
        return """
         Name: \(name)
         Age: \(age)
        """
    }
}

func WriteFileExample(){
    let fileManager = FileManager.default
    let user = User(name: "blackriper", age: 29)

    // write file 
     fileManager.createFile(atPath:"/home/blackriper/Descargas/blackriper.txt", contents: user.getUserString().data(using: .utf8))

    // read file
     guard let data = fileManager.contents(atPath: "/home/blackriper/Descargas/blackriper.txt") else{
          print("File not found")
          return
    }
     let string = String(data: data, encoding: .utf8) ?? user.getUserString()
     print(string)
     
    // delete file
    do {
        try fileManager.removeItem(atPath: "/home/blackriper/Descargas/blackriper.txt")
    } catch {
        print("Error deleting file: \(error)")
    }
    
 }
 WriteFileExample()

 // ejercicio extra 

 struct Product {
    var name: String
    var cantity: Int
    var price: Int
}

struct FileOperations{
   private let fileManager = FileManager.default   
   private let path = "/home/blackriper/Descargas/products.txt"

    func createFile(_ contents: Data?) {
        fileManager.createFile(atPath:self.path,contents: contents)
    }

    func readFile(defaultValue: String) {
        guard let data = fileManager.contents(atPath: self.path) else {
            print("File not found")
            return
        }
        let string = String(data: data, encoding: .utf8) ?? defaultValue
         print(string)
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
    private let fileManager = FileOperations()

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
        fileManager.readFile(defaultValue:"No products")  
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
        let contents = products.map { "\($0.name), \($0.cantity), \($0.price)" }.joined(separator: "\n")
        fileManager.createFile(contents.data(using: .utf8))
   }
}
            

 func superMarket(){
     let cart = Cart()
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

 superMarket()
