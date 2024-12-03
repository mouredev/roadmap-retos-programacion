
import net.lingala.zip4j.ZipFile
import java.io.File

fun main() {
    val archive = File("") //dirección del archivo (hasta el propio archivo)
    val out = "" //dirección de destino (incluyyendo nombre que le pongamos al archivo comprimido)

    val archives = listOf(File(""), File(""))
    //Poner en la lista los distintos archivos a comprimir

    val folder = File("")
    //Dirección de la carpeta que vayamos a comprimir

    //Llamamos a una función y al ejecutar el programa ya comprime donde hayamos especificado
    
    /*
    Podríamos combinar y crear el archivo comprimiedo y posteriormente añadirle una carpeta o archivos
    con estas mismas funciones, pues además de crearlos, permite añadir archivos
     */
}

// función que comprime 1 archivo
fun archiveToZip(file: File, destiny: String) {
    val zip = ZipFile(destiny)
    zip.addFile(file)
}

// función que comprime varios archivos
fun someArchivesToZip(files: List<File>, destiny: String) {
    val zip = ZipFile(destiny)
    zip.addFiles(files)
}

// función que comprime una carpeta
fun archivesWithFolderToZip(folder: File, destiny: String) {
    val zip = ZipFile(destiny)
    zip.addFolder(folder)
}
