//Importante ageragar en las dependencias de gradle "implementation("com.google.code.gson:gson:2.8.8")"
import com.google.gson.Gson
import java.io.File
import javax.xml.bind.annotation.XmlRootElement
import javax.xml.bind.JAXBContext
import javax.xml.bind.Marshaller
import org.w3c.dom.Document
import javax.xml.parsers.DocumentBuilderFactory

//JSON
//el ejercicio incluye ya la dificultad extra
data class programadorJson(val nombre: String, val edad: Int, val fechaNacimiento: String, val lenguajes: List<String>){
    fun mainProgramador(){

        //Iniciar objeto programador
        val dev = programadorJson(nombre, edad, fechaNacimiento, lenguajes)

        //Iniciar objeto Json de la libreria GSON
        val objetoGson = Gson()

        //Transorformar objeto Dev a Json
        val jsonDev = objetoGson.toJson(dev)

        //Creacion del archivo
        val archivo = File("C:\\Users\\vdsro\\Desktop\\dev.json")
        archivo.writeText(jsonDev)
        println("Se ha creado el archivo")

        //Mostrar informacion del archivo
        //Leer contenido del archivo
        val contenido = File("C:\\Users\\vdsro\\Desktop\\dev.json").readText()

        //Creacion del objeto Json con GSON
        val lecturaArchivo = Gson()

        //Convertir el archivo JSON al objeto "Programador"
        val lecturaDev = lecturaArchivo.fromJson(contenido, programadorJson::class.java)

        //Impresion
        println("Nombre: ${lecturaDev.nombre}")
        println("Edad: ${lecturaDev.edad}")
        println("Fecha de nacimiento: ${lecturaDev.fechaNacimiento}")
        println("Lenguajes de programacion: ${lecturaDev.lenguajes}")

        //Borrar archivo
        archivo.delete()
    }
}
@XmlRootElement //Importante agregar esta sentencia ya que es la que indica que la siguiente clase es un objeto XML
class programadorXml{
    var nombre: String = ""
    var edad: Int = 0
    var fechaNacimiento:String = ""
    var lenguajes: List<String> = listOf()
}

fun mainProgramadorXml(nombre: String, edad: Int, fechaNacimiento: String, lenguajes: List<String>){
    //Definicion de objeto
    val dev = programadorXml()
    dev.nombre = nombre
    dev.edad = edad
    dev. fechaNacimiento = fechaNacimiento
    dev.lenguajes = lenguajes

    //Creacion de objeto XML
    val contexto = JAXBContext.newInstance((programadorXml::class.java))

    //Crear objeto marshall -> marshall = describe el proceso de convertir datos en un fotmato que se pueda transmitir eje: de clase a XML
    val marshaller = contexto.createMarshaller()
    marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true)

    //Escribir en archivo XML
    val archivoXml = File("C:\\Users\\vdsro\\Desktop\\dev.xml")
    marshaller.marshal(dev, archivoXml)

    println("Archivo XML creado de forma correcta")

    //Mostrar contenido del archivo
    val contenido = archivoXml.path
    val documento = convertirXml(contenido)
    if(documento != null){
        println("Contendio file XML")
        println(documento.documentElement.textContent.trim())
    }else{
        println("No hay archivo")
    }
    archivoXml.delete()

}

fun convertirXml(ruta:String): Document?{
    //creacion de la instancia para convertir el archivo
    val conversor = DocumentBuilderFactory.newInstance()
    try{
        val constructor = conversor.newDocumentBuilder()
        return constructor.parse(ruta)
    } catch(excep: Exception){
        excep.printStackTrace()
    }
    return null
}

fun main(){
    val lenguajesProgram = listOf("Kotlin", "Java", "Python")
    val ejemploJson = programadorJson("Vincent", 24, "23/10/99", lenguajesProgram)

    ejemploJson.mainProgramador()
    mainProgramadorXml("Vincent", 24, "23/10/99", lenguajesProgram)

}