
fun operationsWithStrings(){
 val villain="freezer"

  // substring
  println(villain.substring(0,3))
  // length
  println(villain.length)
  // uppercase
  println(villain.uppercase())
  // lowercase
  println(villain.lowercase())
  // repeat
  println(villain.repeat(3))
  // trim
  println(villain.trim())
  //replace
  println(villain.replace("free",""))
  // interpolation
  println("$villain use kienzan technique")
 // union
 val example="$villain use kienzan technique"
 println(example +"and Goku use kamehameha")
 // verify
 println(villain.startsWith("free"))
 println(villain.endsWith("zer"))
 // split
 println(villain.split("e"))
 // compare
 println(villain.compareTo("cell"))
// reversed
 println(villain.reversed())

}

fun isAnagram(str1: String, str2: String): Boolean {
    val array1=str1.uppercase().toCharArray()
    val array2=str2.uppercase().toCharArray()
    array1.sort()
    array2.sort()
    return array1.contentEquals(array2)
}

fun isIsogram(word: String): Boolean {
    if (word.length == 1) return true // las letras individuales son un isogram

    val charCounts = IntArray(26) // Crear un arrgle de 26 enteros

    // hacer un ciclo para contar los caracteres
    for (char in word) {
        charCounts[char - 'a']++ // Increment the count for that character
       }

    // checar si los cacteres contados son mas de uno
    for (count in charCounts) {
        if (count > 1) return false // si count es mayor que 1, no es un isogram
    }

    return true //  si todos los caracteres contados son 1 o cero, es un isogram
}


fun analyzingWord(word:String,word2:String=""){
    when {
      word.uppercase().reversed() == word2.uppercase() -> println("palindrome")
      isAnagram(word,word2) -> println("anagram")
      isIsogram(word) -> println("isogram")
      else-> println("not category")
    }
}


fun main() {
    operationsWithStrings()
    analyzingWord("Anna","anna")
    analyzingWord("Nacionalista","Altisonancia")
    analyzingWord("murcielago")
}