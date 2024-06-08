class valueReference{

    fun main(){

        //Asigancion por valores
        var value1 = "Las asignaciones por valores cambian el valor de la variable de forma independiente, en este caso value2 toma la forma de value1"
        var value2 = value1
        println(value1)
        println(value2)
        value2 = "En este caso si cambiamos el valor de value2 solo se cambiara para esta variable dejando value1 como se deifnio en el inicio, se comportan como variables independientes"
        println(value1)
        println(value2)
        val value3 = "estas asignaciones funcionan de esta manera para los tipos de datos primitivos incluyendo los arrays creados con arrayOf"

        //Asignacion por referencia
        var reference1 = mutableListOf(1, 2, 3)
        var reference2 = reference1
        println("En este caso reference2 toma la forma de reference1 pero no son valores independientes, ambas variables apuntan al mismo espacio en memoria")
        println("reference1: $reference1, reference2:$reference2")
        reference2.add(4)
        println("En este caso al agregar un valor a reference2 este valor extra lo veremos reflejado en reference1 ya que independientemente de que no lo agregamos en el original reference2 interactua como un puntero hacia reference1 ")
        println("reference1: $reference1, reference2: $reference2")

        //Funciones con asignacion por valores y referencias
        var number = 10
        fun value(num: Int){
            var innerNumber = 5
            println("En este caso si ceramos una variable en la funcion la podremos reasignar dentro de la misma, pero no podemos reasignar el parametro de entrada de la funcion")
            println("Numero original $innerNumber")
            innerNumber = 15
            println("Numero reasignado $innerNumber")
            //La siguente instruccion intenta reasignar el parametro num recibido por la funcion, esta con comentario ya que genera un error ya que esto no es permitido en Kotlin
            //num = 20
        }
        value(number)

        //Funciones por referencia
        fun reference(list: MutableList<Int>){
            println("En este caso al igual que las asignaciones por valor no se puede reasignar la variable, pero con las referencias si podemos añadir datos a los objetos desde las funciones")
            println("Lista Original: $list")
            list.add(4)
            println("Lista alterada: $list")
        }

        var list = mutableListOf(1, 2, 3)
        println("Aca comprobamos que la lista original tiene la siguiente forma antes de la adicion realizada en la funcion: $list")
        reference(list)
        println("Por ultimo ya que se ha realizado la adicion en la funcion queda de la siguiente forma la lista: $list")

        //Punto Extra
        //Por valor
        var newValue1 = 10
        var newValue2 = 20
        fun valueExchange(value1: Int, value2: Int): Pair<Int, Int>{
            //En kotlin los parametros de entrada son inmutables, por lo que para reasignarlos y cambiarlos debemos crear una variable nueva
            var newValue1 = value1
            var newValue2 = value2
            var temporalValue = value1
            newValue2 = newValue1
            newValue1 = temporalValue

            return Pair(newValue1, newValue2)
        }

        println("Primer valor inicial: $newValue1, Segundo valor inicial: $newValue2")
        var assignedPair = valueExchange(newValue1, newValue2)
        newValue1 = assignedPair.first
        newValue2 = assignedPair.second
        println("Primer valor final: $newValue1, Segundo valor final: $newValue2")

        //Por referencia
        var newList1 = mutableListOf(1, 2, 3)
        var newList2 = mutableListOf(4, 5, 6, 7)
        fun referenceExchange(list1: MutableList<Int>, list2: MutableList<Int>): Pair<MutableList<Int>, MutableList<Int>>{
            var newList1 = list1
            var newList2 = list2
            var temporalReference = list1
            newList1 = list2
            newList2 = temporalReference

            return Pair(newList1, newList2)
        }
        println("Primera Lista inicial: $newList1, Segunda Lista Inicial: $newList2")
        var assignedReference = referenceExchange(newList1, newList2)
        newList1 = assignedReference.first
        newList2 = assignedReference.second
        println("Primera Lista Final: $newList1, Segunda Lista Final: $newList2")
    }


    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val obj = valueReference()
            obj.main()
        }
    }
}