import org.eclipse.jgit.api.Git
import org.eclipse.jgit.api.RemoteAddCommand
import org.eclipse.jgit.lib.Repository
import org.eclipse.jgit.storage.file.FileRepositoryBuilder
import org.eclipse.jgit.transport.RefSpec
import org.eclipse.jgit.transport.URIish
import org.eclipse.jgit.transport.UsernamePasswordCredentialsProvider
import java.io.File
import kotlin.io.path.Path

/*
para no depender del cliente del http client y tener mejor modularizacion
usaremos la siguiente libreria:

  -Git : https://git-scm.com/book/es/v2/Ap%C3%A9ndice-B:-Integrando-Git-en-tus-Aplicaciones-JGit
*/


data class GithubAuth(val  username: String, val  password: String)


// acciones que se pueden realizar desde el repositorio remoto y con las diferentes operaciones con las branches
enum class BranchOptions{
    NEW,
    CHANGE,
    DELETE
}
enum class GitAction{
    PULL,
    PUSH
}

// definir funcionamiento de la aplicacion
interface CliRepository{
    fun workDirectory(src: String)
    fun actionBranch(nameBranch: String, option:BranchOptions)
    fun gitStatus()
    fun createCommit(message : String)
    fun addingRemoteRepo(url: String)
    fun actionRemote(action:GitAction,remoteBranchName: String,user:GithubAuth)
    fun existRemoteRepository(): Boolean
}

// implementar logica con jgit y kotlin

class GitRespository:CliRepository{

    private lateinit var git: Git
    private lateinit var uriRemote: String


    override fun workDirectory(src: String) {
       val aboslutePath= Path(src)
       val result= runCatching { File("${aboslutePath.toAbsolutePath()}") }
       if (result.isFailure) println("directory not found ${result.exceptionOrNull()}")
       if (result.isSuccess){
           git= Git.init().apply { setDirectory(result.getOrNull())}.call()
           println("created a new repository at ${git.repository.directory}")
       }
     }

    override fun actionBranch(nameBranch: String,option: BranchOptions) {

     val result= runCatching {
         when (option) {
             BranchOptions.NEW -> git.branchCreate().apply {
                 setName(nameBranch)
             }.call()

             BranchOptions.CHANGE -> git.checkout().apply {
                 setName(nameBranch)
             }.call()

             BranchOptions.DELETE -> git.branchDelete().apply {
                 setBranchNames(nameBranch)
                 setForce(true)
             }.call()
         }
     }

       if (result.isSuccess)  println("the ${nameBranch} executed operation ${option.name}")
       if (result.isFailure)  println("branch operation error ${result.exceptionOrNull()}")
    }

    override fun gitStatus() {
        var status=""
        git.status().call().run {
            status="""
                Git Status  branch ${git.repository.branch}
                Added: ${this.added}
                Changed: ${this.changed}
                Conflicting: ${this.conflicting}
                Missing:   ${this.missing}
                Modified:  ${this.modified}
                Removed:   ${this.removed}
                Untracked:   ${this.untracked}
                UntrackedFolders:  ${this.untrackedFolders}
            """.trimIndent()
            println(status)
        }
    }

    override fun createCommit(message: String) {
       git.run {
           val result= runCatching {
               add().apply { addFilepattern(".") }.call()
               commit().apply { setMessage(message) }.call()
           }

           if (result.isSuccess) println("commit added sucessfully")
           if (result.isFailure) println("error to create commit ${result.exceptionOrNull()}")
       }

    }

    override fun addingRemoteRepo(url: String) {
      val result= runCatching {
          git.remoteAdd().apply {
              setName("origin")
              setUri(URIish(url))
          }.call()
      }
       if (result.isSuccess) {
           println("remote repo ${url} added sucessfully")
           uriRemote=url
       }
        if (result.isFailure) println("error to adding remote repository ${result.exceptionOrNull()}")
    }

    override fun actionRemote(action: GitAction,remoteBranchName: String,user:GithubAuth) {

        val result= runCatching {
            when (action) {
                GitAction.PULL -> git.pull().apply {
                    setRemoteBranchName(remoteBranchName)
                    setRebase(true)
                }.call()

                GitAction.PUSH -> git.push().apply {
                    setCredentialsProvider(UsernamePasswordCredentialsProvider(user.username,user.password))
                    setRefSpecs(RefSpec(remoteBranchName))
                    setForce(true)
                }.call()
            }
        }
        if (result.isSuccess) println("operation ${action.name}  execute sucessfully")
        if (result.isFailure) println("error to execute ${action.name} ${result.exceptionOrNull()}")
    }

    override fun existRemoteRepository(): Boolean = git.remoteList().call().isNotEmpty()

}

class CliApp(private  val repository: CliRepository){
   private lateinit var userGithub:GithubAuth

   fun showMenuOptions(){
       var option=0
       while (option!=6){
           println("KGit App")
           println("""
               1.- Create new Repository
               2.- Create Commit
               3.- Repo Status
               4.- Actions Branch
               5.- Actions Remote
               6.- Exit
               
           """.trimIndent())
           option= readLine()?.toInt() ?:0
           when(option){
               1-> createRepository()
               2-> createCommit()
               3-> repository.gitStatus()
               4-> operationsBranch()
               5-> operationsRemote()
               6-> break

           }

       }
   }

    private fun createRepository(){
        println("introduce path  where the project is located:  ")
        val src= readLine().toString()
        repository.workDirectory(src)
    }

    private fun operationsBranch(){
        println("Select operation branch to execute 1.-New, 2.-Change , 3.-Delete")
        var action= readLine()?.toInt() ?:0
        println("name the branch to ${if (action==1) "New" else if (action==2) "Change" else "Delete"} ?")
        var nameBranch= readLine()?:""
        val actionBranch= when(action){
            1-> BranchOptions.NEW
            2->BranchOptions.CHANGE
            3->BranchOptions.DELETE
            else -> BranchOptions.NEW
        }
        repository.actionBranch(nameBranch,actionBranch)
    }

    private fun operationsRemote(){
        if (repository.existRemoteRepository().not()){
            println("There is no remote repository copy the url of one")
            val remoteUrl= readLine().toString()
            repository.addingRemoteRepo(remoteUrl)

        }
        println("selected operation remote to execute 1.-Pull , 2.-Push")
        val action=readLine()?.toInt()?:0

        println("name the remote branch to work ")
        var remoteBranch= readLine()?:""

        println("username to use in github")
        val name=readLine()?:""

        println("generate github token  and paste this ")
        val password=readLine()?:""

        userGithub=GithubAuth(username = name,password=password)

        val actionRemote= when(action){
            1 -> GitAction.PULL
            2 -> GitAction.PUSH
            else -> GitAction.PUSH
        }
        repository.actionRemote(actionRemote,remoteBranch,userGithub)

    }


    private fun createCommit(){
        println("Adding message commit ")
        val message= readLine()?:"first commit".let { if (it.isEmpty()) "first commit" else it }
        repository.createCommit(message)
    }
}




fun main() {
    val repoGit =GitRespository()
    val appCli= CliApp(repoGit)
    appCli.showMenuOptions()
}