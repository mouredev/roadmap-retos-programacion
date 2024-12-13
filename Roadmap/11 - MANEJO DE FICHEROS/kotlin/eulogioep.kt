import java.io.File

fun main() {
    // Nombre del archivo
    val fileName = "eulogioep.txt"

    // Crear el archivo y escribir la información
    File(fileName).writeText(
        """
        EulogioEP
        41
        Kotlin
        """.trimIndent()
    )

    // Imprimir el contenido
    println("Contenido del archivo:")
    File(fileName).forEachLine { println(it) }

    // Borrar el archivo
    File(fileName).delete()
    println("\nArchivo borrado.")

    // DIFICULTAD EXTRA
    gestionVentas()
}

fun gestionVentas() {
    val fileName = "ventas.txt"
    val file = File(fileName)

    while (true) {
        println("\n--- Gestión de Ventas ---")
        println("1. Añadir producto")
        println("2. Consultar productos")
        println("3. Actualizar producto")
        println("4. Eliminar producto")
        println("5. Calcular venta total")
        println("6. Calcular venta por producto")
        println("7. Salir")
        print("Seleccione una opción: ")

        when (readLine()) {
            "1" -> añadirProducto(file)
            "2" -> consultarProductos(file)
            "3" -> actualizarProducto(file)
            "4" -> eliminarProducto(file)
            "5" -> calcularVentaTotal(file)
            "6" -> calcularVentaPorProducto(file)
            "7" -> {
                file.delete()
                println("Archivo borrado. Saliendo del programa.")
                return
            }
            else -> println("Opción no válida.")
        }
    }
}

fun añadirProducto(file: File) {
    print("Nombre del producto: ")
    val nombre = readLine() ?: return
    print("Cantidad vendida: ")
    val cantidad = readLine()?.toIntOrNull() ?: return
    print("Precio: ")
    val precio = readLine()?.toDoubleOrNull() ?: return

    file.appendText("$nombre, $cantidad, $precio\n")
    println("Producto añadido.")
}

fun consultarProductos(file: File) {
    if (!file.exists()) {
        println("No hay productos registrados.")
        return
    }
    println("Lista de productos:")
    file.forEachLine { println(it) }
}

fun actualizarProducto(file: File) {
    print("Nombre del producto a actualizar: ")
    val nombre = readLine() ?: return

    val tempFile = File("temp.txt")
    var encontrado = false

    file.useLines { lines ->
        lines.forEach { line ->
            val parts = line.split(", ")
            if (parts[0] == nombre) {
                encontrado = true
                print("Nueva cantidad vendida: ")
                val cantidad = readLine()?.toIntOrNull() ?: return@forEach
                print("Nuevo precio: ")
                val precio = readLine()?.toDoubleOrNull() ?: return@forEach
                tempFile.appendText("$nombre, $cantidad, $precio\n")
            } else {
                tempFile.appendText("$line\n")
            }
        }
    }

    if (encontrado) {
        file.delete()
        tempFile.renameTo(file)
        println("Producto actualizado.")
    } else {
        tempFile.delete()
        println("Producto no encontrado.")
    }
}

fun eliminarProducto(file: File) {
    print("Nombre del producto a eliminar: ")
    val nombre = readLine() ?: return

    val tempFile = File("temp.txt")
    var eliminado = false

    file.useLines { lines ->
        lines.forEach { line ->
            if (line.split(", ")[0] != nombre) {
                tempFile.appendText("$line\n")
            } else {
                eliminado = true
            }
        }
    }

    if (eliminado) {
        file.delete()
        tempFile.renameTo(file)
        println("Producto eliminado.")
    } else {
        tempFile.delete()
        println("Producto no encontrado.")
    }
}

fun calcularVentaTotal(file: File) {
    var total = 0.0
    file.forEachLine { line ->
        val parts = line.split(", ")
        total += parts[1].toInt() * parts[2].toDouble()
    }
    println("Venta total: $%.2f".format(total))
}

fun calcularVentaPorProducto(file: File) {
    file.forEachLine { line ->
        val parts = line.split(", ")
        val ventaProducto = parts[1].toInt() * parts[2].toDouble()
        println("${parts[0]}: $%.2f".format(ventaProducto))
    }
}