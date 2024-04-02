//Clase padre, debe estar en open para que sea accesible para las demas  clases
open class animal(val nombre: String, val edad:Int){
    open fun sonido(){
        println("Los animales pueden tener muchos tipos de sonidos diferentes")
    }
}

//Calse heradada, se heredan los datos de nombre y edad pero las clases traen un atributo de raza propio
class perro(nombre: String, edad:Int, val raza: String): animal(nombre,edad){
    //con Overide se demuestra el polimorfismo modificando por completo la funcionalidad del metodo llamado
    override fun sonido() {
        println("El perro hace Guau!")
    }
}

class gato(nombre: String, edad:Int, val raza: String): animal(nombre,edad){
    override fun sonido() {
        println("El gato hace Miau!")
    }
}

//funcion intermedia para demostrar polimofismo
fun hacerSonido(animal: animal){
    animal.sonido()
}

//Ejercicio Extra
open class employee(val id: Int, val name:String){
    var hierarchy = listOf("")
    open fun Id(){
        println("el empleado con nombre $name se identifica con el numero $id")
    }

    open fun labors(){
        println("Descripcion de labores las cuales pueden variar dependiendo del rol")
    }

    open fun inChargeEmployees(){
        println("El empleado $name tiene a su cargo las siguienets personas $hierarchy")
    }

    open fun shift(){
        println("El horario puede variar dependiendo de que empleado sea")
    }

}

class manager(name: String, id:Int): employee(id, name){
    override fun labors() {
        println("El gerente debe velar por el exito del proyecto orquestando todos los equipos necesarios para su desarrollo y asegurando una buena relacion y comunicacion con el cliente")
    }
    override fun shift() {
        println("El gerente peude trabajar en el horario que lo desee, debe estar disponible 24/7")
    }

}

class projectManager(name: String, id:Int): employee(id, name){
    override fun labors() {
        println("El PM es el puente de comunicaicon entre los equipos de desarrollo y la gerencia, encargandose de orquestar todos los equipos para el exito del proyecto")
    }
    override fun shift() {
        println("El gerente de proyectos debe asistir en un horario de 8:00 Am a 6:00 Pm, y debe estar disponible 24/7")
    }
}

class developer(name: String, id:Int): employee(id, name){
    override fun labors() {
        println("El desarrollador es el encargado de desarrollar todas las funciones requeridas por el cliente, es el encargado netamente de la parte tecnica del proyecto")
    }
    override fun shift() {
        println("El desarrollado peude trabajar en el horario que desee pero debe segurar su asistencia a las reuniones programadas, no debe estar disponible 24/7 a menos de que este asignado a disponibilidad del proyecto")
    }
    override fun inChargeEmployees() {
        println("Los desarrolladores no tienen personal a su cargo")
    }
}

//middle functions
fun showlabors(employee: employee){
    employee.labors()
}
fun showShift(employee: employee){
    employee.shift()
}
fun showHierarchy(employee: employee){
    employee.inChargeEmployees()
}

//al ejecutar la funcion intermedia que recibe un objeto de tipo animal se puede optimizar el codigo haciendo que una misma funcionalidad tenga comportamientos diferenets dependiendo de como se construya el objeto
fun main(){
    var nuevoPerro = perro("Zeus", 14, "schnauzer")
    hacerSonido(nuevoPerro)

    var nuevoGato = gato("Chopper", 7, "Criollo")
    hacerSonido(nuevoGato)

    //Ejecucion ejercicio extra

    //Objects definition
    //Manager
    var managerHierarchy = listOf("PM Juan", "PM Pedro", "PM Andres")
    var newManager = manager("Alberto", 314)
    newManager.hierarchy = managerHierarchy
    //Project Manager
    var projectMagaerHierarchy = listOf("Dev Carlos", "Dev Sergio", "Dev Sandra")
    var newProjectManager = projectManager("Juan", 480)
    newProjectManager.hierarchy = projectMagaerHierarchy
    //Developer
    var newDeveloper = developer("Carlos", 450)

    //Run processes
    //Manager
    newManager.Id()
    showlabors(newManager)
    showShift(newManager)
    showHierarchy(newManager)

    //Project Manager
    newProjectManager.Id()
    showlabors(newProjectManager)
    showShift(newProjectManager)
    showHierarchy(newProjectManager)

    //Developer
    newDeveloper.Id()
    showlabors(newDeveloper)
    showShift(newDeveloper)
    showHierarchy(newDeveloper)

}