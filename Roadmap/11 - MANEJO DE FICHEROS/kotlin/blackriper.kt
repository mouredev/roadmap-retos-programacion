import java.io.File
import java.util.UUID

fun writeFile(){
    val contentFile="""
        Name: blackriper
        Age: 29
    """.trimIndent()

    // crear instancia de la clase File con el path donde se guardara el fichero
    val file = File("src/main/resources/user.txt")
    //  escribir contenido en el fichero
    file.writeText(contentFile)
    // leer contenido del fichero
    file.forEachLine {
        println(it)
    }
    // borrar fichero
    val result= file.delete()

    if (result) {
        println("File deleted successfully")
    } else {
        println("Failed to delete the file")
    }
}

// ejercicio extra
data class Product(val sku: UUID,var name: String,var cant: Int, var price: Double)

interface Store{
    fun addProduct(product: Product)
    fun removeProduct(name: String)
    fun updateProduct(sku:UUID,product:Product)
    fun showAllProducts()
    fun searchProductByName(name: String):Product
    fun calculateTotalSold()
    fun deleteFile()
}



class SoldSore:Store{
    private val products= mutableListOf<Product>()
    private val fileProduct=File("src/main/resources/products.txt")

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
        fileProduct.forEachLine {
            println(it)
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
        val result=fileProduct.delete()
        if (result) {
            println("File deleted successfully")
        } else {
            println("Failed to delete the file")
        }
    }


    private fun  saveFile(){
        val productsContent=products.joinToString("\n"){"${it.sku}, ${it.name}, ${it.cant} ,${it.price}"}
        fileProduct.writeText(productsContent)
    }

}

fun oxxoStore(){
   val oxxo=SoldSore()

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
                val sku=UUID.randomUUID()
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
                val prod=oxxo.searchProductByName(oldname)

                println("update name (${prod.name}):")
                val name = if (readLine().isNullOrEmpty()) prod.name else readLine()!!.lowercase()
                println("update cat (${prod.cant}):")
                val cant = if (readLine().isNullOrEmpty()) prod.cant else readLine()!!.toInt()
                println("update price (${prod.price}):")
                val price = if (readLine().isNullOrEmpty()) prod.price else readLine()!!.toDouble()
                val product = Product(prod.sku, name, cant, price)
                oxxo.updateProduct(prod.sku, product)
            }

            4 ->  oxxo.showAllProducts()

             5 -> {
                println("Enter name:")
                val name = readLine()!!.lowercase()
                val product=oxxo.searchProductByName(name)
                println("sku: ${product.sku} name: ${product.name} cant: ${product.cant} price: ${product.price}")
            }

            6 ->  oxxo.calculateTotalSold()

        }

    } while (option != 7)

    oxxo.deleteFile()
}




fun main() {
 writeFile()
 oxxoStore()
}

