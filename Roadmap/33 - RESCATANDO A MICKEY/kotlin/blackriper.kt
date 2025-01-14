
//1.-Declaracion de varibles auxiliares e interfaces
typealias ObstacleList=MutableList<Pair<Int,Int>>

interface Drawable{
    fun drawLaberit(mickeyLoc:Pair<Int,Int>)
    fun searchObstacle(location:Pair<Int,Int>):Boolean
}

interface Move{
    fun moveMickey(y: Int,x: Int):Pair<Int,Int>
    fun mickeyIsFree(mickeyPosition: Pair<Int, Int>):Boolean
}

//2.-implementar clases y interfaces

class DrawableLaberit:Drawable{
    private  var laberit: String=""
    private var listObstacle:ObstacleList = mutableListOf()
    private var completed=false

    override fun drawLaberit(mickeyLoc: Pair<Int, Int>) {
        for (x in 1..6){
            for (y in 1..6) {
                laberit += if (x==mickeyLoc.first && y==mickeyLoc.second) "🐭"
                else if (y==6 && x==6) "🚪"  else drawObstacle(x,y)
                if (y%6==0) laberit+="\n"

            }
         }
        completed=true
        println(laberit)
        laberit=""

    }

    override fun searchObstacle(location: Pair<Int, Int>): Boolean {
       if(listObstacle.count { it.first == location.first && it.second == location.second } == 1){
           println("Mickey found obstacle he need move to another way")
           return true
       }
       return false
    }

   private fun drawObstacle(x:Int,y:Int):String=
       if (completed) generateExistObstacle(x,y)
       else generateNewObstacles(x,y)


   private fun  generateNewObstacles(x: Int,y: Int):String{
       val generator=(1..10).random()
       if (x==generator || y==generator) {
           listObstacle.add(Pair(x,y))
           return "⬛️"
       }
       return "⬜️"
   }

  private fun  generateExistObstacle(x: Int,y: Int):String{
      if (listObstacle.count { x==it.first && y==it.second }==1) return "⬛️"
      return "⬜️"
  }

}

class Mickey(
   val blockObs:(Pair<Int,Int>)->Boolean
  ):Move{

    override fun moveMickey(y: Int,x: Int):Pair<Int,Int> {
       println("Select direction to move Mickey 1 [Up], 2 [Down] , 3 [Left], 4 [Right] ")
       val position= readlnOrNull()?.toInt()?:0
       val oldPosition=Pair(y,x)

        return when(position){
           1->if(isLimit(Pair(y-1,x))) oldPosition else isObstacle(Pair(y-1,x),oldPosition)
           2->if(isLimit(Pair(y+1,x))) oldPosition else isObstacle(Pair(y+1,x),oldPosition)
           3->if(isLimit(Pair(y,x+1))) oldPosition else isObstacle(Pair(y,x+1),oldPosition)
           4->if(isLimit(Pair(y,x-1))) oldPosition else isObstacle(Pair(y,x-1),oldPosition)
           else -> oldPosition
       }
    }

    override fun mickeyIsFree(mickeyPosition:Pair<Int,Int>): Boolean {
       if (mickeyPosition.first == 6 && mickeyPosition.second == 6){
           println("Mickey found exit of laberit")
           return true
       }
      return false
    }

 private fun isLimit(newPosition: Pair<Int, Int>):Boolean {
    if(newPosition.first == 0 || newPosition.first>=7|| newPosition.second>6){
        println("Mickey can't go any further, he has reached a wall in the maze ")
        return true
    }
    return false
 }

   private fun isObstacle(newPosition:Pair<Int,Int>,position:Pair<Int,Int>):Pair<Int,Int> =
       if (blockObs(newPosition)) position else newPosition

}

fun laberitD23(){
    val laberit= DrawableLaberit()
    val mickey= Mickey(laberit::searchObstacle)
    var mickeyPosition=Pair(1,1)


    while (!mickey.mickeyIsFree(mickeyPosition)){
        laberit.drawLaberit(mickeyPosition)
        mickeyPosition=mickeyPosition.let { mickey.moveMickey(it.first,it.second) }
    }

}



fun main() {
  laberitD23()
}