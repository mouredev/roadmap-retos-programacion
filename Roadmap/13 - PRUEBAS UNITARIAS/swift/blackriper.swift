import Foundation
import XCTest
/*
 El testing es la manera de probar diferentes fragmentos de codigo
 para ver si el resultado es el que se esperaba.

en swift se realiza el testing mediante la libreria XCTest
para probar los diferentes test se debe contar con el package.swift 

asi que aqui solo se muestran los ejemplos de testing 

 */

struct Calculator{
    let num1 : Int 
    let num2 : Int

    func add() -> Int{
        return num1 + num2
    }
  }

 typealias DictProgrammer = [String:Any]

  struct Programmer{
      let name:String
      let age : Int
      let birthDate:String
      let programmingLanguage: [String]

     static func toDictionary(programmer: Programmer) -> DictProgrammer {
          return [
              "name": programmer.name,
              "age": programmer.age,
              "birthDate":programmer.birthDate,
              "programmingLanguage": programmer.programmingLanguage
          ]
      }

    }

// ejemplo clase testing  al tenerla en el folder test correr el comando swift test 

//nombre de la libreria donde esta el codigo a probar
//@testable import testing


final class testingTests: XCTestCase {
     func testAdd(){
        let calculator = Calculator(num1: 1, num2: 2)
        XCTAssertEqual(calculator.add(), 3)
    }

    func testProgrammerSucessCases(){
        let black = Programmer(name: "blackiper", age: 30, birthDate: "20/05/1994", programmingLanguage: ["swift", "go"])
        let dictionary = Programmer.toDictionary(programmer: black )
        let dictionaryMock: [String:Any] = [
            "name": "blackiper",
            "age": 30,
            "birthDate": "20/05/1994",
            "programmingLanguage": ["swift", "go"]
        ]

       // comparar campos de diccionario 
       XCTAssertTrue(dictionary.keys == dictionaryMock.keys) 

      
      // comprobrar tipos de dictionary  pendiente ver si es la mejor forma
       XCTAssertTrue(dictionary["name"] as! String == dictionaryMock["name"] as! String)
       XCTAssertTrue(dictionary["age"] as! Int == dictionaryMock["age"] as! Int) 
       XCTAssertTrue(dictionary["birthDate"] as! String == dictionaryMock["birthDate"] as! String) 
       XCTAssertTrue(dictionary["programmingLanguage"] as! [String] == dictionaryMock["programmingLanguage"] as! [String])
   
    }

   func testProgrammerErrorCases(){
       let black = Programmer(name: "blackiper", age: 30, birthDate: "20/05/1994", programmingLanguage: ["swift", "go"])
       let dictionary = Programmer.toDictionary(programmer: black )
       let dictionaryMockError: [String:Any] = [
           "age": 30,
           "birthDate": "20/05/1994",
           "programmingLanguage": ["swift"]
       ]

       XCTAssertFalse(dictionary.keys == dictionaryMockError.keys)

       XCTAssertFalse(dictionary["programmingLanguage"] as! [String] == dictionaryMockError["programmingLanguage"] as! [String])

   }

