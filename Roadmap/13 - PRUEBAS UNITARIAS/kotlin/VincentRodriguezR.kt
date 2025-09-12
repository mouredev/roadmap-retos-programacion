//Estos imports deben ir en el archivo del test
import org.junit.Test
import org.junit.Assert.*

//Clases que debe de ir en un archivo en la carpeta main
class calculadora(){
    fun sum(num1:Int, num2:Int): Int{
        var res = num1 + num2
        return  res
    }
}

//Ejercicio Extra
class developer(){
    fun androidDeveloper(name:String, age: Int, birthDate: String, programmingLanguages: List<String>): MutableMap<String, String>{
        val developerMap: MutableMap<String, String> = mutableMapOf()

        developerMap.put("Name", name)
        developerMap.put("Age", age.toString())
        developerMap.put("BirthDate", birthDate)
        developerMap.put("ProgramminLanguages", programmingLanguages.joinToString(", "))

        return  developerMap
    }
}

//Clases que deben ir en unarchivo en la carpeta de test
class calculadoraTest(){

    val testeo = calculadora()

    @Test
    fun sumTest(){
        val resultado = testeo.sum(2,3)
        assertEquals(5,resultado)
    }
}

//Dificultad Extra
class developerTest(){
    val developerTest = developer()

    @Test
    fun androidDeveloperTest(){
        val languages = listOf("Kotlin", "Java", "Python")

        val developerMap: MutableMap<String, String> = mutableMapOf()
        developerMap.put("Name", "Vincent Rodriguez")
        developerMap.put("Age", "24")
        developerMap.put("BirthDate", "23/10/99")
        developerMap.put("ProgramminLanguages", languages.joinToString (", "))

        val res = developerTest.androidDeveloper("Vincent Rodriguez", 24, "23/10/99", languages)
        assertEquals(developerMap, res)
    }

    @Test
    fun androidDeveloperTestNullValidation(){
        val languages = listOf("Kotlin", "Java", "Python")
        var nullValidator = false

        val developerMap: MutableMap<String, String> = mutableMapOf()
        developerMap.put("Name", "Vincent Rodriguez")
        developerMap.put("Age", "24")
        developerMap.put("BirthDate", "23/10/99")
        developerMap.put("ProgramminLanguages", languages.joinToString (", "))

        for(i in developerMap){
            if(i == null){
                nullValidator = true
            }
        }

        val res = developerTest.androidDeveloper("Vincent Rodriguez", 24, "23/10/99", languages)
        assertEquals(false, nullValidator)
    }
}