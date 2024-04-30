/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
// solucion con kotlin

fun main(){
    //firstWay(9)
    //secondWay(3)
    //thirtWay(6)
    //fourtWay(5)
    //fiftWay(3)
    //sixtWay(4)


}

fun firstWay(x:Int = 0):Int{
    var long = x
    var num = -1

    while (num < long){
        num++
        println(num)

    }
    return 0
}

fun secondWay(i:Int = 0):Int{
    for( i in 0..i){
        println(i)
    }

    return 0
}

fun thirtWay(z:Int = 0):Int {
    var lista1:ArrayList<Int> = arrayListOf()

    for (i in 0..z){
        lista1.add(i)
    }

    for (lista1 in lista1){
        println(lista1)
    }
    return 0
}

fun  fourtWay(a:Int = 0):Int{

    val list2:MutableList<Int> = mutableListOf()
    for(i in 0..a){
        list2.add(i)
    }

    list2.forEach{it -> println(it) }

    return 0
}

fun  fiftWay(w:Int = 0):Int{

    val list3:MutableList<Int> = mutableListOf()
    for(i in 0..w){
        list3.add(i)
    }

    list3.forEachIndexed { index, i -> println("${list3[i]}") }

    return 0
}

fun sixtWay(l:Int = 0):Int{
    val list4:MutableList<Int> = mutableListOf()
    for(i in 0..l){
        list4.add(i)
    }
    val it:ListIterator<Int> = list4.listIterator()

    while (it.hasNext()){
        var e:Int = it.next()
        println("$e")
    }
    return 0
}
