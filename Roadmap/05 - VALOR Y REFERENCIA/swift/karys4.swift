//Value Types (A copy) -> Struct, Enum, tuples
//Awesome explanation in the following link: https://www.swift.org/documentation/articles/value-and-reference-types.html

struct Document {
    var text: String
}

var myDocument = Document(text: "Kary's document")
var friendDocument = myDocument

friendDocument.text = "I am kary's friend and this is my own document"

print(myDocument.text) //Kary's document
print(friendDocument.text) //I am kary's friend and this is my own document



//Reference Types -> Class, closure
class Car {
    var color: String
    
    init(color: String) {
        self.color = color
    }
}


var myCar = Car(color: "White")
var friendCar = myCar

friendCar.color = "Yellow" //This assignation affected "myCar" because it is a reference to the instance that is assigned.

print(myCar.color) //Yellow
print(friendCar.color) //Yellow




