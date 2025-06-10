import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import org.kohsuke.github.GHRepositoryStatistics
import org.kohsuke.github.GitHub
import org.kohsuke.github.GitHubBuilder

/**
 para simplificar el desarrollo vamos a utilizar una de las librerias recomendadas de github para java
 este ejercicio es kotlin pero hay que aprovechar su poder para usar cosas de java

 https://mvnrepository.com/artifact/org.kohsuke/github-api/1.326

 **/

//1.- definir estructuras y comportamiento

data class GitReport(
    var name: String,
    var language: String,
    var repoCount: Int,
    var follow: Int,
    var numCommits: Int
)

interface OctoverseInfo{
    suspend fun findGithubUser(): String
    suspend fun generateUserRepo(userName: String):GitReport
}



//2.- implementacion y modulo auxiliar

class GitHubReport:OctoverseInfo{

    private lateinit var userGit: GitHub

    override suspend fun findGithubUser(): String {
      println("Enter you github username ")
      val username=readLine()?:""
      println("Generate personal token access in your github account and copy them")
      var accessToken=readLine()?:""
      userGit= GitHubBuilder().withOAuthToken(accessToken).build()
      return username
    }

    override suspend fun generateUserRepo(userName: String): GitReport {
       val dataUser=userGit.getUser(userName).run {
           val language =
               countRepeatElements(this.repositories.map { it.value.language }.filter { it != null }) ?: ""
           return GitReport(
               userName,
               language,
               this.publicRepoCount,
               this.followersCount,
               GHRepositoryStatistics.CommitActivity().total
           )
       }
    }

}

//funcion para contar elementos repetidos
 private fun  GitHubReport.countRepeatElements(listE: List<String>): String? {
    val countMap = mutableMapOf<String, Int>()
     return listE.forEach { countMap[it] = countMap.getOrDefault(it, 0) + 1 }.let {countMap.maxByOrNull { it.value }?.key}

}
// funcion de extension para mostrar el reporte
fun GitReport.getReport(): String="""
    Octoverse Report
    Name: $name
    Language more use this year : $language
    Number of Repositories: $repoCount
    Number of Follows: $follow
    Number of Commits: $numCommits
    
""".trimIndent()


fun main() = runBlocking{
  val job= launch(Dispatchers.LOOM){
      val gitInfo=GitHubReport()
      val username= gitInfo.findGithubUser()
      gitInfo.generateUserRepo(username).run {
          println(this.getReport())
      }
  }
  job.join()

}