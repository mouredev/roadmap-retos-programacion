import kotlinx.serialization.ExperimentalSerializationApi
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.encodeToString
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder
import kotlinx.serialization.json.Json
import nl.adaptivity.xmlutil.serialization.XML
import java.io.File
import java.io.FileWriter
import java.io.PrintWriter
import java.util.*

/*
Al proceso de convertir la informacion  en un cierto formato se le conoce como serializacion
esto nos permite convertir alguna estructura  de kotlin en un formato de salida (json, xml, etc).

para sealizar kotlin utiliza una libreria auxilar llamada kotlinx.serialization.
este tambien nos provee de un modulo para poder serializar xml.

Serializar: proceso de convertir un objeto de kotlin a un formato de salida json o xml

Desializar: proceso de convertir un formato json o xml a un objeto de kotlin

para mas informacion visita:
https://kotlinlang.org/docs/serialization.html
https://github.com/rharter/kotlinx-serialization-xml

*/



@OptIn(ExperimentalSerializationApi::class)
fun jsonFile(){
val src="src/main/resources/blackriper.json"
// crear clase para serializar y deserealizar
@Serializable
data class User(val name: String, val age: Int, val birdday: String,val programingLenguages: List<String>)

// escribir file json
PrintWriter(FileWriter(src)).use {
    val prettyJson = Json {
        prettyPrint = true
        prettyPrintIndent = " "
    }
    val user=User("Rodolfo", 29, "20/05/1994", listOf("kotlin","go","python"))
    it.write(prettyJson.encodeToString(user))
}

// leer fichero json
File(src).readText().let {
    val user = Json.decodeFromString<User>(it)
    println(user)
}

// borrar fichero
File(src).delete()

}

fun xmlFile() {
  val src="src/main/resources/blackriper.xml"
  // crear data class
  @Serializable
  data class User(val name: String, val age: Int, val birdday: String,val programingLenguages: List<String>)
  // crear fichero xml
   PrintWriter(FileWriter(src)).use {
       val user=User("Rodolfo", 29, "20/05/1994", listOf("kotlin","go","swift"))
       it.write(XML.encodeToString(user))
    }

  // leer fichero xml
  File(src).readText().let {
      val user = XML.decodeFromString<User>(it)
      println(user)
  }

  // borrar fichero
  File(src).delete()

}

// reto extra con json  y xml

// crear custom serializer para UUID
object UUIDSerializer : KSerializer<UUID> {
    override val descriptor = PrimitiveSerialDescriptor("UUID", PrimitiveKind.STRING)

    override fun deserialize(decoder: Decoder): UUID {
        return UUID.fromString(decoder.decodeString())
    }

    override fun serialize(encoder: Encoder, value: UUID) {
        encoder.encodeString(value.toString())
    }
}


@Serializable
data class Product(
    @Serializable(with = UUIDSerializer::class)
    val sku: UUID,
    var name: String,
    var cant: Int,
    var price: Double)

@Serializable
data class StoreProducts(val products: List<Product>)

enum class FileType {
    JSON,
    XML
}

interface Store{
    fun addProduct(product: Product)
    fun removeProduct(name: String)
    fun updateProduct(sku: UUID, product:Product)
    fun showAllProducts()
    fun searchProductByName(name: String):Product
    fun calculateTotalSold()
    fun deleteFile()
}

class SoldSore(private val fileName:String,private val type:FileType):Store{
    private val products= mutableListOf<Product>()
    private val fileProduct=File("src/main/resources/$fileName")
    private val src="src/main/resources/$fileName"

    init {
        if (fileProduct.exists()){
           when(type){
               FileType.JSON -> fileProduct.readText().let {
                   val productsFile = Json.decodeFromString<StoreProducts>(it)
                   productsFile.products.forEach { product ->
                       products.add(product)
                   }
               }
               FileType.XML -> fileProduct.readText().let {
                   val productsFile = XML.decodeFromString<StoreProducts>(it)
                   productsFile.products.forEach { product ->
                       products.add(product)
                   }
               }
           }

        }
    }

    override fun addProduct(product: Product) {
        products.add(product)
        saveFile()
    }

    override fun removeProduct(name: String) {
        val product=products.first { it.name==name }
        val result=products.removeIf{it.sku==product.sku}
        if (result) {
            println("Product deleted successfully")
            saveFile()
        } else {
            println("Failed to delete the product")
        }
    }

    override fun updateProduct(sku: UUID, product: Product) {
        products.first { it.sku == sku }.apply {
            this.name = product.name
            this.cant = product.cant
            this.price = product.price
        }
        saveFile()
    }

    override fun showAllProducts() {
        val header="""
            -----------------------
            sku   name   cant  price
            -----------------------
        """.trimIndent()
        println(header)
        when(type){
            FileType.JSON -> {
                File(src).readText().let {
                    val products = Json.decodeFromString<StoreProducts>(it)
                    for (product in products.products) {
                        println("${product.sku} ${product.name} ${product.cant} ${product.price}")
                    }
                }
            }
            FileType.XML -> {
                File(src).readText().let {
                    val products = XML.decodeFromString<StoreProducts>(it)
                    for (product in products.products) {
                        println("${product.sku} ${product.name} ${product.cant} ${product.price}")
                    }
                }
            }
        }


    }

    override fun searchProductByName(name: String): Product =
        products.first { it.name==name }

    override fun calculateTotalSold() {
        val header="""
            ------------------------------------------------------------
            sku               name         cant       price     Subtotal
            -------------------------------------------------------------
        """.trimIndent()
        println(header)
        products.forEach {
            println("${it.sku} ${it.name} ${it.cant} ${it.price} ${"%.2f".format(it.cant*it.price)}")
        }
        val total=products.sumOf { it.cant*it.price }
        println("Total sold: $total")
    }

    override fun deleteFile() {
       val result= File(src).delete()
        if (result) {
            println("File deleted successfully")
        }else {
            println("Failed to delete the file")
        }
    }

    @OptIn(ExperimentalSerializationApi::class)
    private fun  saveFile(){
      when(type){
          FileType.JSON -> {
              PrintWriter(FileWriter(fileProduct)).use {
                  val prettyJson = Json {
                      prettyPrint = true
                      prettyPrintIndent = " "
                  }
                  val store=StoreProducts(products)
                  it.write(prettyJson.encodeToString(store))
              }
          }
          FileType.XML -> {
              PrintWriter(FileWriter(fileProduct)).use {
                  val store=StoreProducts(products)
                  it.write(XML.encodeToString(store))
              }
          }
      }
    }

}

fun oxxoStore() {
    // modificar si se quiere usar json o xml
    val oxxo = SoldSore("products.xml", FileType.XML)

    do {
        println("1. Add product")
        println("2. Remove product")
        println("3. Update product")
        println("4. Show all products")
        println("5. Search product by name")
        println("6. Calculate total sold")
        println("7. Exit")
        println("Choose an option:")
        val option = readLine()!!.toInt()
        when (option) {
            1 -> {
                println("Enter name:")
                val name = readLine()!!.lowercase()
                println("Enter cant:")
                val cant = readLine()!!.toInt()
                println("Enter price:")
                val price = readLine()!!.toDouble()
                val sku = UUID.randomUUID()
                val product = Product(sku, name, cant, price)
                oxxo.addProduct(product)
            }

            2 -> {
                println("Enter name:")
                val name = readLine()!!.lowercase()
                oxxo.removeProduct(name)
            }

            3 -> {
                println("Enter name product:")
                val oldname = readLine()!!.lowercase()
                val prod = oxxo.searchProductByName(oldname)
                println("update name (${prod.name}):")
                val name = if (readLine().isNullOrEmpty()) prod.name else readLine()!!.lowercase()
                println("update cat (${prod.cant}):")
                val cant = if (readLine().isNullOrEmpty()) prod.cant else readLine()!!.toInt()
                println("update price (${prod.price}):")
                val price = if (readLine().isNullOrEmpty()) prod.price else readLine()!!.toDouble()
                val product = Product(prod.sku, name, cant, price)
                oxxo.updateProduct(prod.sku, product)
            }

            4 -> oxxo.showAllProducts()

            5 -> {
                println("Enter name:")
                val name = readLine()!!.lowercase()
                val product = oxxo.searchProductByName(name)
                println("sku: ${product.sku} name: ${product.name} cant: ${product.cant} price: ${product.price}")
            }

            6 -> oxxo.calculateTotalSold()

        }
    } while (option != 7)

    oxxo.deleteFile()
}


    fun main() {
    //jsonFile()
    //xmlFile()
    oxxoStore()
}