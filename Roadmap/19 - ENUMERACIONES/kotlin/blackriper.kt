import java.util.UUID

/*
 Las Enumeraciones son un tipo de estructura que nos ayuda agrupar datos  los cuales rara vez cambian
 su valor por lo general son constantes.

 por ejemplo tenemos una opcion llamda direccion esta puede ser norte, sur ,oeste ,este
 si las evaluamos como  un  string este puede ser mayusculas o minusculas o incluso puede estar
 mal escrito. estas direcciones nuncan cambian asi que en un enum se resumira asi

 enum class Direccion{
     NORTE,SUR,OESTE,ESTE
 }
 cada enum en kotlin  consta de un objeto y cada valor son  constantes separadas por comas

gracias al enum evitamos errores por algun valor introducido y no es necesario escribir el
valor solo basta con poner Direccion.Norte esto indica que estamos usando el valor de norte
los enums en kotlin tiene varias aplicaciones para mas informacion.

https://kotlinlang.org/docs/enum-classes.html

*/

// creamos el enum
enum class WekendDay{
  MONDAY,
  TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
  SUNDAY
}



fun exampleWithEnums(numDay : Int){
  when(numDay){
      1 -> println(WekendDay.MONDAY)
      2 -> println(WekendDay.TUESDAY)
      3 -> println(WekendDay.WEDNESDAY)
      4 -> println(WekendDay.THURSDAY)
      5 -> println(WekendDay.FRIDAY)
      6 -> println(WekendDay.SATURDAY)
      7 -> println(WekendDay.SUNDAY)
  }

}

// ejercicio extra

// definir tipos de datos

enum class State{
  PENDING,SENDING,RECEIVED,CANCELED
}

data class Order( val id: Int,var state : State){
    fun showOrderState() = println("Order $id is $state")
}

interface OrderManager {
    fun createOrder(order: Order)
    fun updateState(id: Int, state: State)
    fun showOrders()
}

class OrderAdmin : OrderManager{
    private var orders = mutableListOf<Order>()

    override fun createOrder(order: Order) {
        orders.add(order)
    }

    override fun updateState(id: Int, state: State) {
        val order = orders.find { it.id == id }
        if (order != null) {
            if(validateOrder(order.state,state)){
                order.state = state
                order.showOrderState()
            }else{
                println("Order $id can not be updated to $state")
            }


        }else{
            println("Order not found")
        }
    }

    override fun showOrders() {
        orders.forEach { println("Order ${it.id} is ${it.state}") }
    }

}

fun validateOrder(currentState: State, newState: State):Boolean{
  // si la orden esta pediente no puede ser recibida
  if (currentState ==State.PENDING && newState == State.RECEIVED) {
      return false
  }

  // si la orden ya fue enviada no puede ser pendiente
  if (currentState == State.SENDING && newState == State.PENDING){
      return false
  }

  // si la orden ya fue recibida no puede ser enviada
  if (currentState == State.RECEIVED && newState == State.SENDING){
      return false
  }

  // si la orden ya fue cancelada no puede pasar a ningun otro estado
  if (currentState==State.CANCELED){
      return false
  }

  return true
}






fun main() {
  exampleWithEnums(3)
  val order1=Order(1,State.PENDING)
  val order2=Order(2,State.SENDING)
  val order3=Order(3,State.CANCELED)

  val orderAdmin = OrderAdmin()
  orderAdmin.createOrder(order1)
  orderAdmin.createOrder(order2)
  orderAdmin.createOrder(order3)

  orderAdmin.updateState(1,State.SENDING)
  orderAdmin.updateState(2,State.RECEIVED)
  orderAdmin.updateState(3,State.RECEIVED)

 orderAdmin.showOrders()

}
