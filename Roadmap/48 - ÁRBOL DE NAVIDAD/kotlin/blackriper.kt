import kotlin.random.Random

// al seleccionar una vez se ponen o quitan adornos eso evita llenar el arbol

class ChrismasTree {

    private var height=0
    private var addStar=false
    private var addSpheres=false
    private var addFocus=false
    private var focusOn=true
    private var lisOfSpheres= mutableListOf<Int>()

    fun createTree(){
        println("Introduce la altura del arbol: ")
        height = readLine()!!.toInt()
    }

    fun actionsUser(){
        while (true){
           drawChristmasTree()
            println("selecciona una accion")
            println("1. Añadir o eliminar estrella en la copa (@)")
            println("2. Añadir o eliminar bolas de dos en dos (O) aleatoriamente")
            println("3. Añadir o eliminar luces de tres en tres (+) aleatoriamente")
            println("4. Apagar (*) o encender (+) las luces")
            println("5.- exit")
            var option= readLine()!!.toInt()
            when(option){
                1->{
                    addStar=!addStar
                    if (addStar) println("se ha agregado la estrella al arbol")
                    else println("se ha quitado la estrella del arbol")
                }
                2->{
                    addSpheres=!addSpheres
                    if (addSpheres) println("se han agregado esferas al arbol")
                    else println("se ha quitado las esferas del arbol")


                }
                3->{
                    addFocus=!addFocus
                    if (addFocus) println("se han agregado luces al arbol ")
                    else println("se han quitado las luces del arbol")
                }
                4->{
                    focusOn=!focusOn
                    if (focusOn) println("se han prendido las  luces del  arbol ")
                    else println("se han apagado las luces del arbol")
                }
                5->break
            }
        }
    }

   private  fun drawChristmasTree() {
        if (lisOfSpheres.size>0) lisOfSpheres.clear()

        //dibujar arbol
        for (i in 0..<height) {
            for (j in 0..<height - i - 1) {
                print(" ")
            }
            for (k in 0..<2 * i + 1) {
                if (addStar && i==0)print("@")
                else if (k%2==0 && addSpheres){
                    print("O")
                    lisOfSpheres.add(k)
                }
                else if (k%3==0 && addFocus && !lisOfSpheres.contains(k)){
                    if (focusOn) print("+") else print("*")
                }
                else print("*")

            }
            println()
        }
        //dibujar el tronco
        for (i in 0..<2) {
            for (j in 0..<height - 2) {
                print(" ")
            }
            println("|||")
        }
    }




}

fun main() {
  val tree=ChrismasTree()
  tree.createTree()
  tree.actionsUser()
}