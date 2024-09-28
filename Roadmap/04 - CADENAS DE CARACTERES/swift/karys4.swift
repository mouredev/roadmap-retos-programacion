import Foundation

//Concatenating two strings
 var firstString = "All we hear is radio ga ga"
 var secondString = "Radio goo goo"
 var chorus = firstString + " " + secondString


 //String interpolation
 var radioSong = "You had your time, you had the power, you've yet to have your finest hour Radio (radio) \(chorus)."


 //Counting characters
 var songCharacters = radioSong.count


 //Insert a character
 radioSong.insert("!", at: radioSong.endIndex)

//Insert a word
radioSong.insert(contentsOf: "hello", at: radioSong.index(before: radioSong.endIndex))

//Remove a single character (the last character)
radioSong.remove(at: radioSong.index(before: radioSong.endIndex))

//Remove a substring
let range = radioSong.index(radioSong.endIndex, offsetBy: -25)..<radioSong.endIndex
radioSong.removeSubrange(range)

//Substring
var bohemianSong = """
Is this the real life? Is this just fantasy?
Caught in a landslide, no escape from reality
Open your eyes, look up to the skies and see
I'm just a poor boy, I need no sympathy
"""

//append() method
bohemianSong.append(radioSong)

//elementsEqual() method
var compare = radioSong.elementsEqual(bohemianSong)

//replacingOcurrences() method
var championsSong = """
 I've paid my dues
Time after time
I've done my sentence
But committed no crime
And bad mistakes
I've made a few
"""

championsSong.replacingOccurrences(of: "my", with: "your")

//trimmingCharacters() method removes whitespace from both ends of a string.
var underPressureSong = " Under pressure that burns a building down Splits A FAMILY in two "
var songWithOutSpaces = underPressureSong.trimmingCharacters(in: .whitespaces)

//dropFirst() method removes the first character of the string.
songWithOutSpaces.dropFirst()

//dropLast() method removes the last character of the string.
songWithOutSpaces.dropLast()

//lowercased() method converts all uppercase characters in a string into lowercase characters.
songWithOutSpaces.lowercased()

//uppercased() method converts all lowercase characters in a string into lowercase characters.
songWithOutSpaces.uppercased()

//hasPrefix() method checks whether the string begins with the specified string or not.
songWithOutSpaces.hasPrefix("Und")

//hasSuffix() method checks whether the string ends with the specified string or not (is case-sensitive).
songWithOutSpaces.hasSuffix("xyz")

//contains() method checks whether the specified string (sequence of characters) is present in the string or not.
championsSong.contains("time")

//joined() method returns a new string with the given elements joined with the specified delimiter.
var str = ["I","Love","Swift"]
str.joined(separator: " ")

//split() method breaks up a string at the specified separator and returns an array of strings.
championsSong.split(separator: " ")

//reversed() method reverses the given string.
String(championsSong.reversed())


/*
 DIFICULTAD EXTRA (opcional):
  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
  * para descubrir si son:
  * - Palíndromos
  * - Anagramas
  * - Isogramas (palabra que no contiene valores repetidos)
*/

func comparingWords(word1:String, word2: String) {
    if word1 == String(word1.reversed()) && word2 == String(word2.reversed()) {
        print("Both words are Palindrome.")
    } else if word1.sorted() == word2.sorted() {
    print("Both words are anagram")
    } else {
        print("I still don't know how to validate an isogram, pending to complete this in the future.")
    }
}

comparingWords(word1: "narran", word2: "seres") //Palindrome
comparingWords(word1: "ecuador", word2: "acuerdo") //Anagram











