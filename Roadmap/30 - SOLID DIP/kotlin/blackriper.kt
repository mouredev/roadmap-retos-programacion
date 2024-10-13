import java.util.*

/*
   Inversion Dependency  Principle
   Inversión de Dependencias, el cual nos dice que las clases de alto nivel no deben depender
   de las clases de bajo nivel,sino que ambas deben depender de abstracciones.

   El principio se establece en dos partes

   1. La clase de alto nivel no debe de depender de la clase de bajo nivel
   2.  Las abstracciones no deberían depender de los detalles, los detalles deben depender de las abstracciones.

*/

//ejemplo de lo que no debe de hacerce

data class ProductTick(val sku: UUID, var name: String, var cant: Int, var price: Double)
data class ServiceTick(val sku: UUID, var name: String, var price: Double)

// la clase PrinterTicket solo depende de ProductTick y ServiceTick y al modificar o agregar mas tipos de tickets el codigo crece demasiado
class PrinterTicket{
    fun printTicketProduct(product: ProductTick){
        val ticket="""
            Ticket sold 
            sku: ${product.sku}
            name: ${product.name}
            cant: ${product.cant}
            price: ${product.price}
            _________________________
            Total: ${product.price*product.cant}
        """.trimIndent()
        println(ticket)
    }

    fun printTicketService(service: ServiceTick){
        val ticket="""
            Ticket sold 
            sku: ${service.sku}
            name: ${service.name}
            price: ${service.price}
            _________________________
            Total: ${service.price}
        """.trimIndent()
        println(ticket)
    }
}

// abstrayendo la logica  de la clase PrinterTicket usando genericos experimiento

//1.- extraemos la logica en una interfaz en este caso la T representa un tipo generico
interface Ticket<in T>{
    fun printTicket(t: T)
}

//2.-implementamos la  interface  en la clase al requerir un solo tipo separamos la logica de los diferentes tickets

class PrinterProduct: Ticket<ProductTick>{
    override fun printTicket(t: ProductTick) {
        val ticket="""
            Ticket sold 
            sku: ${t.sku}
            name: ${t.name}
            cant: ${t.cant}
            price: ${t.price}
            _________________________
            Total: ${t.price*t.cant}
        """.trimIndent()
        println(ticket)
    }
}

class PrinterService: Ticket<ServiceTick>{
    override fun printTicket(t: ServiceTick) {
        val ticket="""
            Ticket sold 
            sku: ${t.sku}
            name: ${t.name}
            price: ${t.price}
            _________________________
            Total: ${t.price}
        """.trimIndent()
        println(ticket)
    }
}

//3.- ahora podemos crear una clase builder para la impresion de tickets
class ThermalPrinter<T>{
   var dataTicket: T? = null

    fun print(){
        when(dataTicket){
            is ProductTick -> PrinterProduct().printTicket(dataTicket as ProductTick)
            is ServiceTick -> PrinterService().printTicket(dataTicket as ServiceTick)
        }

    }
}
//4.-kotlin builder opcional
fun <T>printerBuilder(block: ThermalPrinter<T>.() -> Unit):ThermalPrinter<T>{
   return ThermalPrinter<T>().apply(block)

}


fun exampleDip(){

     printerBuilder<ProductTick> {
        dataTicket = ProductTick(UUID.randomUUID(), "Laptop", 1, 2000.0)
     }.run { this.print() }


    printerBuilder<ServiceTick> {
        dataTicket = ServiceTick(UUID.randomUUID(), "Internet Isp", 100.0)
    }.run { this.print() }

}

// ejercicio opcional
interface ForNotification{
    fun sendNotification():String
}


class EmailNotification(private  val subject:String,
                        private  val cc:String,
                        private  val body:String):ForNotification{
    override fun sendNotification(): String {
        return """
            Subject: $subject
            cc: $cc
            body: $body
        """.trimIndent()
    }
}


class SmsNotification(
    private  val to:String,
    private  val body:String
):ForNotification{
    override fun sendNotification(): String {
        return """
            To: $to
            body: $body
        """.trimIndent()
    }
}

class PushNotification(
    private  val title:String,
    private  val appName:String,
    private  val content:String
):ForNotification{
    override fun sendNotification(): String {
        return """
            $appName
          _____________________
             $title
             $content
        """.trimIndent()
    }
}
// creamos una factoria para construir notificaciones lo mejor seria que cada tipo de notificacion tuviera sus propios builders
class NotificationFactory{
      var subject:String=""
      var cc:String=""
      var to:String=""
      var body:String=""
      var title:String=""
      var appName:String=""
      var content:String=""

      inline fun<reified T:ForNotification> buildNotification():T {
          return when(T::class){
              EmailNotification::class -> EmailNotification(subject,cc,body)
              SmsNotification::class -> SmsNotification(to,body)
              PushNotification::class -> PushNotification(title,appName,content)
              else -> throw IllegalArgumentException("Not supported")
          } as T
     }
}
// estas funciones se consideran avanzadas puedes ignorarlas y usar las otras clases en un manager comun
inline fun <reified T:ForNotification>buildNotification(block: NotificationFactory.() -> Unit):String{
    return NotificationFactory().apply(block).buildNotification<T>().sendNotification()
}

fun showNotification(){
   buildNotification<EmailNotification> {
       subject="correo@example.com"
       cc="microsoft@azure.com"
       body="Expiro licencia microsoft 365"
    }.let { it+"\n" }.run { println(this) }

    buildNotification<SmsNotification> {
        to="4111145678"
        body="Tu saldo se ha expirado"
    }.let { it+"\n" }.run { println(this) }

    buildNotification<PushNotification> {
        title="Brais moure curso javascript"
        appName="youtube"
        content="nuevo video del curso de javascript con ejercicios"

    }.let { it+"\n" }.run { println(this) }
}



fun main(){
    exampleDip()
    showNotification()
}