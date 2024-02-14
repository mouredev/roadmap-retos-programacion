
var hokage="Naruto"

print(hokage.contains("N"))

hokage.append(" Uzumaki")
print(hokage)

let upper=hokage.uppercased()
print(upper)

let lower=hokage.lowercased()
print(lower)

let rev=hokage.reversed()
print(String(rev))

let sp=hokage.split(separator: Character("-"))
print(sp)

let count=hokage.count
print(count)

hokage.remove(at: hokage.startIndex)
print(hokage)

print(hokage.hasPrefix("Naruto"))
print(hokage.hasSuffix("Uzumaki"))

print(hokage.isEmpty)

print("\(hokage) is the seventh hokage!!")


// ejercicio extra 

typealias Word=String

func isAnagram(text1:Word,text2:Word)->Bool{
    if text1.uppercased().sorted() == text2.uppercased().sorted(){
       return true
    }
    return false 
}

func isIsogram(_ word: Word) -> Bool {
  let lowercasedWord = word.lowercased()
  let characterSet = Set(lowercasedWord)

  // Devolver verdadero si el número de caracteres en la palabra es igual al número de caracteres en el conjunto.
  return characterSet.count == lowercasedWord.count
}


func analazingWord(text1:Word,text2:Word=""){
    
    if String(text1.uppercased().reversed()) == text2.uppercased(){
      print("\(text1) and \(text2) are palidrome")

    }else if isAnagram(text1: text1, text2: text2)==true{
       print("\(text1) and \(text2) are anagrams")
    }else if isIsogram(text1){
        print("\(text1) are isograms")
    }

}

analazingWord(text1: "Anna", text2: "anna")
analazingWord(text1: "Nacionalista", text2:"Altisonancia")
analazingWord(text1: "Taco")