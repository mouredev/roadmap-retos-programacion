/*
 * Principio de Segregación de Interfaces (ISP)
 * 
 * El ISP establece que ningún cliente debe ser forzado a depender de métodos
 * que no utiliza. Sugiere dividir interfaces grandes en otras más pequeñas
 * y específicas para que los clientes solo tengan que conocer los métodos
 * que realmente necesitan.
 */

// Interfaces segregadas
interface Impresora {
    fun imprimir(documento: String)
}

interface ImpresoraColor : Impresora {
    fun imprimirColor(documento: String)
}

interface Escaner {
    fun escanear(documento: String): String
}

interface Fax {
    fun enviarFax(documento: String)
}

// Implementaciones
class ImpresoraBasica : Impresora {
    override fun imprimir(documento: String) {
        println("Imprimiendo en blanco y negro: $documento")
    }
}

class ImpresoraAColor : ImpresoraColor {
    override fun imprimir(documento: String) {
        println("Imprimiendo en blanco y negro: $documento")
    }

    override fun imprimirColor(documento: String) {
        println("Imprimiendo en color: $documento")
    }
}

class ImpresoraMultifuncion : ImpresoraColor, Escaner, Fax {
    override fun imprimir(documento: String) {
        println("Imprimiendo en blanco y negro: $documento")
    }

    override fun imprimirColor(documento: String) {
        println("Imprimiendo en color: $documento")
    }

    override fun escanear(documento: String): String {
        println("Escaneando: $documento")
        return "Documento escaneado: $documento"
    }

    override fun enviarFax(documento: String) {
        println("Enviando fax: $documento")
    }
}

// Gestor de impresoras
class GestorImpresoras {
    fun imprimirDocumento(impresora: Impresora, documento: String) {
        impresora.imprimir(documento)
    }

    fun imprimirDocumentoColor(impresora: ImpresoraColor, documento: String) {
        impresora.imprimirColor(documento)
    }

    fun escanearDocumento(escaner: Escaner, documento: String): String {
        return escaner.escanear(documento)
    }

    fun enviarFax(fax: Fax, documento: String) {
        fax.enviarFax(documento)
    }
}

// Función principal para probar el sistema
fun main() {
    val gestorImpresoras = GestorImpresoras()
    val impresoraBasica = ImpresoraBasica()
    val impresoraColor = ImpresoraAColor()
    val multifuncion = ImpresoraMultifuncion()

    println("Prueba de Impresora Básica:")
    gestorImpresoras.imprimirDocumento(impresoraBasica, "Documento en blanco y negro")

    println("\nPrueba de Impresora a Color:")
    gestorImpresoras.imprimirDocumento(impresoraColor, "Documento en blanco y negro")
    gestorImpresoras.imprimirDocumentoColor(impresoraColor, "Documento en color")

    println("\nPrueba de Impresora Multifunción:")
    gestorImpresoras.imprimirDocumento(multifuncion, "Documento en blanco y negro")
    gestorImpresoras.imprimirDocumentoColor(multifuncion, "Documento en color")
    gestorImpresoras.escanearDocumento(multifuncion, "Documento para escanear")
    gestorImpresoras.enviarFax(multifuncion, "Documento para enviar por fax")
}