fun main() {
    //Uso Incorrecto
    abstract class Aveh {
        abstract fun walk(): String
        abstract fun fly(): String
    }
    class Bird_: Aveh() {
        override fun walk() = "Estoy andando"
        override fun fly() = "Estoy volando"
    }
    class Penguin_: Aveh() {
        override fun walk() = "Estoy andando"
        override fun fly() = "Estoy volando"
    }
    val bird_ = Bird_()
    println(bird_.walk())
    val penguin_ = Penguin_()
    println(penguin_.fly())
    /*
    Es incorrecto porque los pingünos no vuelan. Para que se de este principio tienen que venir de una clase
    con métodos generales y cada subclase sus métodos específicos
     */

    //Uso correcto
    abstract class Ave {
        abstract fun walk(): String
    }
    class Bird: Ave() {
        override fun walk() = "Estoy andando"
        fun fly() = "Estoy volando"
    }
    class Penguin: Ave() {
        override fun walk() = "Estoy andando"
        fun swim() = "Estoy nadando"
    }
    val bird = Bird()
    println(bird.fly())
    val penguin = Penguin()
    println(penguin.swim())
    /*
    Así es correcto porque la interfaz tiene los métodos generales y ya las subclases hacen lo que
    sea específico de éstas más lo que herede.
     */

    println("\n${"*".repeat(7)} EJERCICIO EXTRA ${"*".repeat(7)}")
    class PrinterByW: Printer {
        override fun print(doc: String): String {
            return "Ha elegido impresión en blanco y negro. Imprimiendo '$doc'"
        }
    }
    class PrinterColor: Printer {
        override fun print(doc: String): String {
            return "Ha elegido impresión a color. Imprimiendo '$doc'"
        }
    }
    class MultiPrinter: PrinterFunctions {
        override fun print(doc: String): String {
            return "Imprimiendo $doc"
        }

        //scan y sendFax están definidas en la interface y si no van a tener
        //modificaciones, no es necesarios sobreescribirlas
    }

    val doc1 = PrinterByW()
    println(doc1.print("El Quijote"))
    val doc2 = PrinterColor()
    println(doc2.print("La Celestina"))
    val doc3 = MultiPrinter()
    println(doc3.scan("Apuntes Matemáticas"))
    println(doc3.sendFax("Documento_Secreto", 321456780))

}

interface Printer {
    fun print(doc: String): String
}

interface PrinterFunctions: Printer {
    fun scan(doc: String): String {
        return "Escaneando $doc"
    }
    fun sendFax(doc: String, fax: Int): String {
        return "Enviando $doc al fax $fax"
    }
}
