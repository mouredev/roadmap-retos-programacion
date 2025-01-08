import java.io.File
import java.io.FileWriter

class archivos(){
    fun creacionArchivo(){
        //Definicion de contenido
        val contenido = listOf("Nombre: Vincent Rodriguez", "Edad: 24", "Lenguaje favorito: Kotlin")

        //Definicion interna del archivo
        val archivo = File("C:\\Users\\vdsro\\Desktop\\VincentRodriguezR.txt")

        //Validacion de existencia del archivo
        if(!archivo.exists()){
            archivo.createNewFile()
        }

        //Escribir en el archivo
        val escritor = FileWriter(archivo)
        contenido.forEach{escritor.write(it + "\n")}
        escritor.close()
        println("Se ha creado el archivo de forma existosa")

        //Obtener contenido del archivo
        val nuevoContenido = archivo.readLines()
        println("Contenido del archivo:")
        nuevoContenido.forEach { println(it) }

        //eliminar archivo
        archivo.delete()
    }
}

//Ejercicio Extra
class salesManager() {

    var action = "None"
    var file: File = File("C:\\Users\\vdsro\\Desktop\\ventas.txt")

    fun showMenu() {
        if (action == "None") {
            newFile()
        } else {
            println("Seleccione la opcion que desea realizar")
            println("1. Agregar producto")
            println("2. Consultar productos")
            println("3. Actualizar productos")
            println("4. Eliminar productos")
            println("5. calcular venta total")
            println("6. calcular venta por producto")
            println("7. Salir")
            action = readLine()!!
            when (action.toInt()) {
                1 -> addItem()
                2-> getItems("continue")
                3-> updateItems()
                4-> deleteItems()
                5-> totalSales()
                6-> itemSales()
                7->{
                    file.delete()
                    return
                }
                else -> {
                    println("Selecciono una opcion no valida")
                    showMenu()
                }
            }
        }
    }

    fun newFile() {
        if (!file.exists()) {
            file.createNewFile()
            action = "with file"
        } else {
            file.delete()
            showMenu()
        }
        println("Se ha creado el archivo de forma existosa")
        showMenu()
    }

    fun writeItem(items: List<String>){
        val writer = FileWriter(file)

        items.forEach{ writer.write("$it \n") }
        writer.close()
    }

    fun addItem(){
        var content = buildContent()
        var tempContent = content.toMutableList()
        var tempList:MutableList<String> = mutableListOf()
        var tempItem = ""

        println("Digite el Nombre del producto")
        tempItem = readLine()!!
        tempList.add("[$tempItem]")
        println("Digite la cantidad vendida")
        tempItem = readLine()!!
        tempList.add("[$tempItem]")
        println("Digite el precio")
        tempItem = readLine()!!
        tempList.add("[$tempItem]")

        tempContent.add(tempList.joinToString (","))
        writeItem(tempContent)

        println("Se ha credo exitosamente el registro")
        showMenu()
    }

    fun buildContent(): MutableList<String>{
        var preContent = file.readLines()
        var content: MutableList<String> = preContent.toMutableList()
        return content
    }

    fun getItems(action: String){
        var content = buildContent()
        if(content.size == 0){
            println("No tiene registros creados, por favor cree uno nuevo")
            showMenu()
        }else{
            println("A continuacion se mostraran sus registros:")
            content.forEachIndexed{ index, value -> println("${index+1}. $value") }
        }
        if(action == "stop"){
            return
        }else{
            showMenu()
        }

    }

    fun updateItems(){
        var tempIndex = ""
        var content = buildContent()
        var tempAction = ""
        var tempConstructor: MutableList<String> = mutableListOf()
        var updatedItem = ""

        getItems("stop")

        println("Por favor seleccione el numero del item que desea editar")
        tempIndex = readLine()!!
        println("Que atributo del item desea actuializar?")
        println(" 1. Nombre")
        println(" 2. Cantidad vendida")
        println(" 3. precio")
        tempAction = readLine()!!

        tempConstructor = content[tempIndex.toInt()-1].split(",").toMutableList()
        println("Digite el nuevo valor")
        updatedItem = readLine()!!
        tempConstructor[tempAction.toInt()-1] = "[$updatedItem]"

        updatedItem = tempConstructor.joinToString(",")

        content[tempIndex.toInt()-1] = updatedItem

        action = "with File"
        writeItem(content)

        println("Se ha actualizado con exito su registro")

        showMenu()

    }

    fun deleteItems(){
        var content = buildContent()
        var tempIndex = ""

        getItems("stop")

        println("Seleccione el item que desea eliminar")
        tempIndex = readLine()!!

        content.removeAt(tempIndex.toInt()-1)
        writeItem(content)

        println("Se ha eliminado el item con exito")
        showMenu()
    }

    fun totalSales(){
        var content = buildContent()
        var total = 0

        for((id, value) in content.withIndex()){
            var tempList: List<String> = listOf()

            tempList = value.split(",").toList()
            total += tempList[2].replace("[","").replace("]","").replace(" ","").toInt() * tempList[1].replace("[","").replace("]","").replace(" ","").toInt()
        }

        println("El total de las ventas de todos los productos es de $$total")
        showMenu()
    }

    fun itemSales(){
        var content = buildContent()
        var tempIndex = ""
        var tempList: List<String> = listOf()
        var total = 0

        getItems("stop")
        println("Selecciona el numero del que deseas obtener el total vendido")
        tempIndex = readLine()!!

        tempList = content[tempIndex.toInt()-1].split(",")
        total = tempList[2].replace("[","").replace("]","").replace(" ","").toInt() * tempList[1].replace("[","").replace("]","").replace(" ","").toInt()
        println("el item ${tempList[0]} tiene un total de ${tempList[1]} sumando un total de $total vendido")
        showMenu()
    }
}

fun main(){
    var inicializador = archivos()
    inicializador.creacionArchivo()

    //Ejecucion punto extra
    var init = salesManager()
    init.showMenu()
}