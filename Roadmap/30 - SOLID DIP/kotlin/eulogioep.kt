/*
 * Principio de Inversión de Dependencias (DIP)
 * 
 * El Principio de Inversión de Dependencias es uno de los cinco principios SOLID
 * en programación orientada a objetos. Establece que:
 * 
 * 1. Los módulos de alto nivel no deben depender de módulos de bajo nivel.
 *    Ambos deben depender de abstracciones.
 * 2. Las abstracciones no deben depender de los detalles. Los detalles deben
 *    depender de las abstracciones.
 * 
 * En otras palabras, este principio nos ayuda a desacoplar los componentes de
 * software, haciendo que las clases de alto nivel dependan de interfaces o
 * clases abstractas en lugar de clases concretas. Esto mejora la flexibilidad,
 * la reutilización y la facilidad de prueba del código.
 */

// Ejemplo incorrecto (violando DIP)
class IncorrectExample {
    class LightBulb {
        fun turnOn() {
            println("LightBulb: Bulb turned on...")
        }
        
        fun turnOff() {
            println("LightBulb: Bulb turned off...")
        }
    }

    class ElectricPowerSwitch(private val bulb: LightBulb) {
        private var isOn = false
        
        fun press() {
            isOn = if (isOn) {
                bulb.turnOff()
                false
            } else {
                bulb.turnOn()
                true
            }
        }
    }
}

// Ejemplo correcto (aplicando DIP)
class CorrectExample {
    interface Switchable {
        fun turnOn()
        fun turnOff()
    }
    
    class LightBulb : Switchable {
        override fun turnOn() {
            println("LightBulb: Bulb turned on...")
        }
        
        override fun turnOff() {
            println("LightBulb: Bulb turned off...")
        }
    }
    
    class Fan : Switchable {
        override fun turnOn() {
            println("Fan: Fan started...")
        }
        
        override fun turnOff() {
            println("Fan: Fan stopped...")
        }
    }

    class ElectricPowerSwitch(private val device: Switchable) {
        private var isOn = false
        
        fun press() {
            isOn = if (isOn) {
                device.turnOff()
                false
            } else {
                device.turnOn()
                true
            }
        }
    }
}

// Sistema de notificaciones (Desafío extra)
interface NotificationService {
    fun send(message: String)
}

class EmailNotification : NotificationService {
    override fun send(message: String) {
        println("Sending Email: $message")
    }
}

class PushNotification : NotificationService {
    override fun send(message: String) {
        println("Sending Push Notification: $message")
    }
}

class SMSNotification : NotificationService {
    override fun send(message: String) {
        println("Sending SMS: $message")
    }
}

class NotificationSystem(private val services: List<NotificationService>) {
    fun notify(message: String) {
        services.forEach { it.send(message) }
    }
}

fun main() {
    println("Incorrect Example (Violating DIP):")
    val incorrectBulb = IncorrectExample.LightBulb()
    val incorrectSwitch = IncorrectExample.ElectricPowerSwitch(incorrectBulb)
    incorrectSwitch.press()
    incorrectSwitch.press()
    
    println("\nCorrect Example (Following DIP):")
    val correctBulb = CorrectExample.LightBulb()
    val correctSwitch1 = CorrectExample.ElectricPowerSwitch(correctBulb)
    correctSwitch1.press()
    correctSwitch1.press()
    
    val fan = CorrectExample.Fan()
    val correctSwitch2 = CorrectExample.ElectricPowerSwitch(fan)
    correctSwitch2.press()
    correctSwitch2.press()
    
    println("\nNotification System (Extra Challenge):")
    val notificationSystem = NotificationSystem(listOf(
        EmailNotification(),
        PushNotification(),
        SMSNotification()
    ))
    notificationSystem.notify("Hello, this is a test notification!")
}