import com.sun.security.auth.UnixNumericUserPrincipal
import java.util.UUID

/*
 La herencia es la capacidad de crear una nueva clase a partir de otra al hacer esto la clase padre o super
 clase puede pasar sus atributos y metodos a la clase hija o sub clase

 ventajas principales de la herencia:

    -Organización de objetos: La herencia organiza los objetos en una jerarquía
     desde lo más general hasta lo más específico.

    -Relación entre clases: Representa la relación existente entre diferentes clases.

    -Reutilización de código: Permite reutilizar el código existente, evitando tener que escribir
     desde cero.

    -Jerarquía de clases: Conforma una jerarquía de clases cada vez más especializada.

    -Herencia múltiple: Algunos lenguajes permiten que una clase pueda heredar los atributos de varias superclases.
 */


//ejemplo de herencia

// nuestra superclase o clase padre en kotlin toso es final por defecto quiere decir que no espera
// para que una clase puede ser heredada esta debe incluir la palabra open
open class Animal(val name: String) {
    fun eat() = println("I'm eating")
    fun sound() = println("I'm making sound ${this.name}")
}

class Dog(name: String) : Animal(name) {
    fun bark() = println("I'm barking")
}

class Cat(name: String) : Animal(name) {
    fun meow() = println("I'm meowing")
}

//ejercicio adicional

enum class Role {
    MANAGER,PROYECT_MANAGER ,PROGRAMMER
}

// la keyword protected permite que solo las clases hijas accedan al metodo work otras clases no podran acceder
open class Employee(val id:UUID,val name:String,val role:Role){
    protected fun work():String="my name is $name and work as ${role.name.lowercase()}"
 }

class Programmer(id: UUID, name: String, role: Role, val tecnology: String) : Employee(id, name, role){
    fun code(){
        println(this.work())
        println("I'm coding in $tecnology")
    }
}

class ProyectManager(id: UUID, name: String,
                     role: Role, val projectName: String ,
                     val team: List<Programmer>) : Employee(id, name, role){
    fun manage(){
        println(this.work())
        println("I'm managing $projectName ")
    }
    fun manageTeam(){
        team.forEach { println("${it.id} -- ${it.name}" ) }
    }
}

class Manager(id: UUID, name: String,
              role: Role, val team: List<ProyectManager>,
              val department: String) : Employee(id, name, role){
    fun manage(){
        println(this.work())
        println("I'm managing $department")
    }
    fun manageTeam(){
        team.forEach { println("${it.id} -- ${it.name}" ) }
    }
}


fun main() {
    val dog = Dog("Max")
    val cat = Cat("Kitty")
    dog.eat()
    dog.sound()
    dog.bark()
    cat.eat()
    cat.sound()
    cat.meow()

    // ejercicio extra
    // creando objetos programadores
    val uuid=UUID.randomUUID()
    val p1=Programmer(uuid,"blackriper",Role.PROGRAMMER, "kotlin")
    val p2=Programmer(uuid,"miguelex",Role.PROGRAMMER, "kotlin")
    val p3 = Programmer(uuid,"allbertomd",Role.PROGRAMMER, "swift")
    val p4 = Programmer(uuid,"didacdev",Role.PROGRAMMER, "swift")

    // llamndo a metodos propios
    p1.code()
    p2.code()
    p3.code()
    p4.code()

    // creando listas de equipos a cargo del gerente de proyecto
    val teamKotlin = listOf(p1,p2)
    val teamSwift = listOf(p3,p4)

    // creando el objeto gerente de proyecto
    val pm1 = ProyectManager(uuid,"Roswell",Role.PROYECT_MANAGER, "kotlin app",teamKotlin)
    val pm2= ProyectManager(uuid,"Kontroldev",Role.PROYECT_MANAGER, "swift app",teamSwift)

    // llamando a metodos propios de encargado de proyecto
    pm1.manage()
    pm1.manageTeam()
    pm2.manage()
    pm2.manageTeam()
    // creando listas de los gerentes de proyectos
    val teamMoure = listOf(pm1,pm2)

    // creando el objeto gerente
    val m1 = Manager(uuid,"mouredev",Role.MANAGER,teamMoure,"Mobile development")

    // llamando a metodos propios de gerente
    m1.manage()
    m1.manageTeam()



}
