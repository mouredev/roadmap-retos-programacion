import kotlinx.coroutines.async
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import java.util.UUID

//1.-Definir entidades y comportamiento

data class Partner constructor(
    val uuid:UUID=UUID.randomUUID(),
    var name:String="",
    var sons : MutableList<UUID> = mutableListOf(),
 )

data class Person constructor(
    val uuid:UUID=UUID.randomUUID(),
    var name:String="",
    var partner: MutableList<Partner> = mutableListOf(),
    var sons : MutableList<Person> = mutableListOf(),
)


interface FamilyRecord{
 suspend fun registerPerson(person: Person)
 suspend fun deletePerson(uuid: UUID)
 suspend fun findMember(name: String):UUID?
 suspend fun updateOrDeletePartner(uuid: UUID,confirm:String)
}

interface PersonValidators{
  suspend fun maxNumofPartners(numWife: Int):Boolean
  suspend fun maxNumofSons(numSons: Int):Boolean
  suspend fun moreThanOneFather(son:Person):Boolean
}

//2.-Definir  un estado reactivo
typealias ListPerson=MutableList<Person>
val persons:ListPerson=mutableListOf()

class DragonRecord:FamilyRecord {

    override suspend fun registerPerson(person: Person) {
        persons.add(person)

    }


    override suspend fun deletePerson(uuid: UUID) {
        persons.removeIf { it.uuid == uuid }.run {
            if (this) println("The person was deleted")
            else println("The person was not found")
        }
    }


    override suspend fun findMember(name: String): UUID? =
        persons.firstOrNull { it.name.lowercase() == name }?.uuid


    override suspend fun updateOrDeletePartner(uuid: UUID, confirm: String) {
        val partner = persons.first { it.uuid == uuid }.partner
        when (confirm) {
            "D" -> {
                println("Name of the partner you want to delete")
                val partnerName = readLine()?.let { it.lowercase() } ?: ""

                partner.removeIf { it.name.lowercase() == partnerName }.run {
                    if (this) println("The partner $partnerName was deleted")
                    else println("The partner $partnerName was not found")
                }
            }

            "U" -> {
                println("Enter a partner name to update")
                val partnerName = readLine()?.let { it.lowercase() } ?: ""

                partner.firstOrNull { it.name.lowercase() == partnerName }.run {
                    if (this == null) println("partner name incorrect try again")
                    if (this != null) {
                        println("Enter new name (${this.name})")
                        this.name = readLine() ?: this.name
                    }
                }
            }
        }

    }
}

class Validator:PersonValidators{
    override suspend fun maxNumofPartners(numWife: Int): Boolean =numWife>2

    override suspend fun maxNumofSons(numSons: Int): Boolean =numSons>2

    override suspend fun moreThanOneFather(son :Person): Boolean =
        persons.contains(son)
}

context(PersonValidators,FamilyRecord)
class FamilyTree{

   suspend fun registerPerson():Unit= coroutineScope{
       val person= async {
           val father=Person()
           println("Enter a person name: ")
           father.name = readLine() ?: ""
           val patList= async { personPartners() }.await()
           val sonList = async {
               val sons:MutableList<Person> = mutableListOf()
               patList.forEach {
                   val patherSons=personSons(it.name)
                   it.sons.addAll(patherSons.map { it.uuid })
                   sons.addAll(patherSons)
               }
               sons
           }.await()
           father.apply {
               partner=patList
               sons=sonList
           }
       }
        registerPerson(person.await())
     }

    suspend  fun deletePerson():Unit= coroutineScope{
        println("Name of the person you want to delete")
        val name=readLine() ?: ""
        val uuid = findMember(name.lowercase())
        if (uuid==null) println("Person not found")
        if (uuid!=null) launch { deletePerson(uuid) }
    }


    suspend fun updateSonsOrWifes()= coroutineScope{
       println("Name of the person you want to update")
       val name=readLine() ?: ""
       val uuidFather = findMember(name.lowercase())
       if (uuidFather==null) println("Person not found")
       if (uuidFather!=null) launch { updateMenu(uuidFather) }
    }

  private suspend fun updateMenu(uuidFather:UUID){
      var operation = 0
      while (operation != 4) {
          println("1. Update/Delete wifes")
          println("2. Update/Delete sons")
          println("3. Add sons or wifes ")
          println("4. Exit")
          operation = readLine()!!.toInt()
          when (operation) {
              1-> deleteOrUpdatePartner(uuidFather)
              2-> deleteOrUpdateSon(uuidFather)
              3 -> with(Validator()){ addFamilyMember(uuidFather) }

          }
      }
  }


    private suspend fun deleteOrUpdateSon(uuid: UUID):Unit= coroutineScope{
        val sonList=persons.first { it.uuid == uuid }.sons
        println("Do you want to delete or update? (D/U)")
        val confirm = readLine()?.let { it.uppercase() } ?: "D"
        when(confirm){
            "D"->{
                println("Name of son you want to delete")
                val sonName = readLine()?.let { it.lowercase() } ?: ""
                sonList.removeIf { it.name.lowercase() == sonName }.run {
                    if (this) println("The son $sonName was deleted")
                    else println("The son $sonName was not found")
                }
            }
            "U"->{
                println("Name of son you want to update")
                val sonName = readLine()?.let { it.lowercase() } ?: ""
                sonList.firstOrNull { it.name.lowercase() == sonName }.run {
                    if (this == null) println("son name incorrect try again")
                    if (this != null) {
                        println("Enter new name (${this.name})")
                        val newName = readLine() ?: this.name
                        this.name= if (newName.isNotEmpty()) newName else this.name
                        val partnerList= async { personPartners() }.await()
                        val sonColl = async {
                            val sons:MutableList<Person> = mutableListOf()
                            partnerList.forEach {
                                val patherSons=personSons(it.name)
                                it.sons.addAll(patherSons.map { it.uuid })
                                sons.addAll(patherSons)
                            }
                            sons
                        }.await()
                        this.apply {
                            partner=partnerList
                            sons=sonColl
                        }
                    }
                }
            }
        }
    }

    private suspend fun deleteOrUpdatePartner(uuid: UUID) {
        println("Do you want to delete or update? (D/U)")
        val confirm = readLine()?.let { it.uppercase() } ?: "D"
        updateOrDeletePartner(uuid,confirm)
    }


    private suspend  fun personSons(partnerName:String):MutableList<Person> {
        println("The person have sons with $partnerName ? (Y/N)")
        val confirmSons = readLine()?.let { it.uppercase() } ?: "N"
        if (confirmSons == "Y") return registerSons(::maxNumofSons, ::moreThanOneFather)
        else return mutableListOf()
    }

    private suspend fun personPartners(): MutableList<Partner>  {
        println("The person have a partner? (Y/N)")
        val confirm = readLine()?.let { it.uppercase() } ?: "N"
        if (confirm == "Y")  return registerPartner(::maxNumofPartners)
        else return mutableListOf()
    }


}

class RecordTree(private val record: FamilyTree){

  suspend fun showMenu()= coroutineScope{
      var option=0
      while (option!=5){
          println("1. Add person")
          println("2. Delete person")
          println("3. Update sons or partners")
          println("4.-Print family tree")
          println("5. Exit")
          option=readLine()!!.toInt()
          when(option){
              1->record.registerPerson()
              2->record.deletePerson()
              3->record.updateSonsOrWifes()
              4->printTree()
          }
      }
  }

  private suspend fun printTree(){
      println("Name of the person you want to print the family tree")
      val name=readLine()?.let { it.lowercase() } ?: ""
      val person=persons.first { it.name.lowercase() == name }
      val familyTree="""
          
               ${person.name}
      __________________________________
            ${person.name}  Partners    
      __________________________________                 
      ${person.partner.forEach { "${it.name}\n" }}
      ___________________________________
      ${printSons(person.uuid,person.partner)}
      
      
      """.trimIndent()

      println(familyTree)
  }

  private fun printSons(uuidFather: UUID,parthers:MutableList<Partner>):String{
      var result=""
      if (parthers.isEmpty()) return result
       parthers.forEach {
          it.sons.forEach {uuid->
              val person = persons.first { it.uuid == uuidFather }.sons.first {it.uuid == uuid }
              result += """
                       ${it.name} sons
              __________________________________    
                       ${person.name}
              __________________________________
                    ${person.name}  Partners    
              __________________________________                 
             ${person.partner}
              ___________________________________
                      
              """.trimIndent()
            }

      }
      return result
  }


}





//4.-Vamos a usar programacion funcional para modularizar algunas acciones de la clase FamilyTree
context(PersonValidators)
suspend fun addFamilyMember(uuid: UUID)= coroutineScope{
    val person = persons.first { it.uuid == uuid }
    println("Who do you want to add? (P or S)")
    val confirm = readLine()?.let { it.uppercase() } ?: "P"
    if (confirm == "P") {
        launch {
            val newPartners = registerPartner(::maxNumofPartners, person.partner.size)
            person.partner.addAll(newPartners)
        }
    }

    if (confirm == "S") {
        launch {
            val newSons = registerSons(::maxNumofSons, ::moreThanOneFather, person.sons.size)
            person.sons.addAll(newSons)
        }
    }
}


suspend fun registerPartner(maxPartner: suspend (Int)->Boolean, partnersSize:Int=0): MutableList<Partner>{
    val partnerList = mutableListOf<Partner>()
    var option = ""
    while (option != "N") {
        println("Enter partner name: ")
        val wifeName = readLine() ?: ""
        val partner = Partner(name = wifeName)
        val numPartner=if (partnersSize>0) partnerList.size+partnersSize else partnerList.size
        if (maxPartner(numPartner)) {
            println("The person not have more than 3 partner")
            break
        }
        partnerList.add(partner)
        println("The person have another partner ? (Y/N)")
        option = readLine()?.let { it.uppercase() } ?: "N"

    }
    return partnerList
}

suspend fun registerSons(
    
    maxNumofSons: suspend (Int) -> Boolean,
    moreThanOneFather: suspend (Person) -> Boolean,
    oldSon:Int=0

):MutableList<Person>{
    val sonList = mutableListOf<Person>()
    var option = ""
    while (option != "N") {
        println("Enter son name: ")
        val sonName = readLine() ?: ""
        val son=Person(name = sonName)
        if (moreThanOneFather(son)) {
            println("Your son have more than one father. please try again")
            continue
        }
        val numSons=if (oldSon>0) sonList.size+oldSon else sonList.size
        if (maxNumofSons(numSons)){
            println("The person not have more than 3 sons")
            break
        }
        sonList.add(son)
        println("The person have another son? (Y/N)")
        option = readLine()?.let { it.uppercase() } ?: "N"

    }
    return sonList
    
}


fun main() = runBlocking {
    with(Validator()) {
        with(DragonRecord()) {
            val recordTree = RecordTree(FamilyTree())
            recordTree.showMenu()
       }

    }
}

