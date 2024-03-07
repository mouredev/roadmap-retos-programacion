open class Animal {
    val patas = 4
    val cola = true
    open fun talk() {
    }
}

class Perro : Animal() {
    override fun talk() {
        println("Guau")
    }
}

class Gato : Animal() {
    override fun talk() {
        println("Miau")
    }
}

open class Employee(
    val name: String, private val identif: Int, private val employment: String,
    private val employees: MutableList<Employee>
) {
    fun meetEmployee() {
        println("$name ($employment): id - $identif")
    }

    fun showEmployees() {
        println("$name está a cargo de:")
        for (employee in employees) {
            println("${employee.name} (${employee.employment}), identificador: ${employee.identif}")
        }
    }
}

class Programmer(
    name: String, identif: Int, employment: String, employees: MutableList<Employee>,
    private val language: String
) : Employee(name, identif, employment, employees) {

    fun work() {
        println("-> $name: Estoy programando en $language")
    }
}

class ProjectManager(
    name: String, identif: Int, employment: String, employees: MutableList<Employee>,
    private val project: String
) : Employee(name, identif, employment, employees) {
    fun supervise() {
        println("\n-> $name: Estoy \"supervisando\" $project. ¿Cómo vais muchachos?")
    }
}

class Manager(
    name: String, identif: Int, employment: String, employees: MutableList<Employee>,
    private val organization: String
) : Employee(name, identif, employment, employees) {
    fun organize() {
        println("\n-> $name: Estoy organizando en $organization")
    }
}


fun main() {
    val canino = Perro()
    canino.talk()
    println(canino.patas)

    val michi = Gato()
    michi.talk()
    println(michi.cola)

    println("${"\n" + "~".repeat(7)} EJERCICIO EXTRA ${"~".repeat(7)}")

    val employeeList = mutableListOf<Employee>()
    val victor = Programmer("Víctor", 11, "Programador", mutableListOf(), "Python")
    victor.work()
    val joel = Programmer("Joel", 12, "Programador", mutableListOf(), "Java")
    joel.meetEmployee()

    employeeList.add(victor)
    employeeList.add(joel)

    val giovanni = ProjectManager(
        "Giovanni", 13, "Project Manager",
        employeeList, "COBOL Multiplatform"
    )
    giovanni.supervise()
    giovanni.showEmployees()

    employeeList.add(giovanni)

    val jetbrains = Manager("JetBrains", 14, "Manager", employeeList, "Kotlin")
    jetbrains.organize()
    jetbrains.showEmployees()
}
