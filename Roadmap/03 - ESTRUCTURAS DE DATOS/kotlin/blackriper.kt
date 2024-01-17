import kotlin.math.sign

/*
 En kotlin existen tres estructuras de datos
 1. List
 2. Set
 3. Map
 estas estructuras pueden ser mutables o inmutables esto se tiene que especificar al crear
 la estructura
 */


fun examplesStructuredData(){
  //  listas
    val narutoCharacters= listOf("Naruto","Sasuke","Kakashi")
    val narutoJutsus= mutableListOf("Chidori","Rasegan","Edo tensei")

    print("lists\n")
    println(narutoCharacters)
    println(narutoJutsus)


    // set no pueden existir elemetos repetidos
   val narutoVillians= setOf("Orochimaru","Itachi","Kisame","Obito")
   val narutoGirls= mutableSetOf("Sakura","Hinata","Ino")
   print("sets\n")
   println(narutoVillians)
   println(narutoGirls)


  // map
  val narutoVilliansMap= mapOf("Orochimaru" to "Edo tensei","Itachi" to "Amaterasu","Kisame" to "samehada")
  val narutoVilliansMutable= mutableMapOf("Orochimaru" to "Edo tensei","Itachi" to "Amaterasu","Kisame" to "samehada")
  print("maps\n")
  println(narutoVilliansMap)
  println(narutoVilliansMutable)
}

fun examplesOperationStructuredData(){
  // solo las listas , mapas, sets mutables pueden ser modificadas
   val narutoJutsus= mutableListOf("Chidori","Rasegan","Edo tensei")
   val narutoGirls= mutableSetOf("Sakura","Hinata","Ino")
   val narutoVilliansMutable= mutableMapOf("Orochimaru" to "Edo tensei","Itachi" to "Amaterasu","Kisame" to "samehada")

  // insertion element
   println("insertion")
   narutoJutsus.add("Katon")
   println(narutoJutsus)
   narutoGirls.add("Temari")
   println(narutoGirls)
   narutoVilliansMutable["Madara"] = "Susano"
   println(narutoVilliansMutable)

   // remove element
   println("removal")
   narutoJutsus.remove("Chidori")
   println(narutoJutsus)
   narutoGirls.remove("Ino")
   println(narutoGirls)
   narutoVilliansMutable.remove("Itachi")
   println(narutoVilliansMutable)

   //update element solo aplicable a mapas
   println("update")
   narutoVilliansMutable["Orochimaru"] = "Soul reanimation"
   println(narutoVilliansMutable)

   // ordered
   println("ordered")
   println(narutoJutsus.sorted())
   println(narutoGirls.sorted())
   println(narutoVilliansMutable.values.sorted())

   }

// reto lista de contactos
val contacts:MutableMap<String,String> = mutableMapOf()

// crud de contactos
fun addContact(name:String,phone:String)=contacts.put(name,phone)
fun deleteContact(name:String)=contacts.remove(name)
fun updateContact(name:String,phone:String){
    contacts[name]=phone
}

// opraciones de contactos
fun readData() {
    println("name for new contact:")
    val name = readLine().toString()
    println("number phone  for new contact:")
    val phone = readLine()!!.filter { it.isDigit() }
    if (phone.length < 10) {
        println("invalid phone number")
    }
    addContact(name, phone)
}

fun deleteData(){
    println("name for delete contact:")
    val name = readLine()!!.toString()
    deleteContact(name)
}



fun showData(){
   for ((name,phone) in contacts){
       println("$name : $phone")
   }
}

fun updateData(){
    println("name for update number:")
    val name = readLine()!!.toString()
    println("number phone  for update contact:")
    val phone = readLine()!!.filter { it.isDigit() }
    if (phone.length < 10) {
        println("invalid phone number")
    }
    updateContact(name,phone)
}


fun contactAgent(){
 var option:Int=0
 while (option!=5) {
     println("contact agent menu")
     println("1. add contact")
     println("2. delete contact")
     println("3. update number contact")
     println("4. show contact list")
     println("5. exit")
     option = readLine()!!.toInt()
     when (option) {
         1 -> readData()
         2 -> deleteData()
         3 -> updateData()
         4 -> showData()
         5 -> break
         else -> println("invalid option")
     }
 }
}





fun main() {
   examplesStructuredData()
   examplesOperationStructuredData()
   contactAgent()
}