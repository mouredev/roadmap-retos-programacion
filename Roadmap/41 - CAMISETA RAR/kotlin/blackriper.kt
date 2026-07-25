import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import net.lingala.zip4j.ZipFile
import net.lingala.zip4j.model.ZipParameters
import net.lingala.zip4j.model.enums.AesKeyStrength
import net.lingala.zip4j.model.enums.EncryptionMethod
import net.lingala.zip4j.progress.ProgressMonitor
import java.io.File

// libreria para comprimir
//https://github.com/srikanth-lingala/zip4j

//1.- crear una factoria para simplificar la liberia opcional
class ZipFactory{
   var password: String=""
   var folder:File?=null
   var files:List<File> = emptyList()
   var dirOut: String=""


   private val zipParamaters=ZipParameters().apply {
       isEncryptFiles=true
       encryptionMethod= EncryptionMethod.AES
       aesKeyStrength= AesKeyStrength.KEY_STRENGTH_256
   }

    internal fun buildZip():ZipFile{

       if (password.isNotEmpty() && folder!=null) {
           return ZipFile("$dirOut",password.toCharArray()).apply {
               addFolder(folder,zipParamaters)
           }
       }
       if (files.isNotEmpty() && password.isNotEmpty()){
           return ZipFile("$dirOut",password.toCharArray()).apply {
               if (files.size==1) addFile(files.first(),zipParamaters) else addFiles(files,zipParamaters)
           }
       }

       if (folder!=null) return  ZipFile("$dirOut").apply {addFolder(folder)}

       return ZipFile("$dirOut").apply {
           if (files.size==1) addFile(files.first()) else addFiles(files)
        }
      }

}

fun zipFactory(block: ZipFactory.()-> Unit):ZipFactory= ZipFactory().apply(block)


//1.- definir comportamiento

interface Compress {
    suspend fun compressZipFolder(folderName: File, pass: String?): ZipFile
    suspend fun compressZipFiles(filesCompress: List<File>, pass: String?,nameZip: String): ZipFile
}

interface FactoryCompress{
    suspend fun readFiles()
    suspend fun compressData(): ZipFile
}

//2.- Crear implementaciones

class ZipCompress:Compress{
    override suspend fun compressZipFolder(folderName: File, pass: String?): ZipFile {
       if (pass!=null) return  zipFactory {
           folder=folderName
           password=pass
           dirOut="src/main/resources/${folderName.name}.zip"
       }.buildZip()

      return zipFactory {
          folder=folderName
          dirOut="src/main/resources/${folderName.name}.zip"
      }.buildZip()

    }

    override suspend fun compressZipFiles(
        filesCompress: List<File>,
        pass: String?,
        nameZip: String
    ): ZipFile {
        if (pass!=null) return  zipFactory {
            files=filesCompress
            password=pass
            dirOut="src/main/resources/${nameZip}.zip"
        }.buildZip()

        return zipFactory {
            files=filesCompress
            dirOut="src/main/resources/${nameZip}.zip"
        }.buildZip()
   }

}

class Factory(private val zip:ZipCompress):FactoryCompress{
    private var filesReading:MutableList<File> =mutableListOf()
    private var folderName: String=""

     override suspend fun readFiles() {
        println("you are going to compress a folder o file ?")
        val option= readLine().toString().lowercase()

        when(option){
            "folder"-> {
                println("Enter the path value where the folder is located")
                folderName=readLine().toString()
            }
            "file"-> readMultipleFiles()
        }
    }

    override suspend fun compressData(): ZipFile {
        val password =addEncrpty()
        if (folderName.isEmpty()) return zip.compressZipFiles(filesReading,password,"files")
        return zip.compressZipFolder(File(folderName),password)

    }

    private fun  readMultipleFiles(){
        var option=""
        while (option!="N"){
            println("Enter the path value where the file is located")
            val path= readLine().toString()
            if (path.isEmpty()){
                println("the path is empty")
                continue
            }
            val file= File(path)
            filesReading.add(file)
            println("there is another file to add (Y/N)")
            option=readLine().toString().uppercase()
        }
    }

    private fun addEncrpty(): String?{
        println("you want to add a key to your compress file password(optional)")
        return readlnOrNull()
     }
}




fun main() = runBlocking{
  val zip=ZipCompress()
  val factory=Factory(zip)
  val job= launch(Dispatchers.IO) {
      factory.readFiles()
      val zipFile = factory.compressData().run {
          val progressMonitor = this.progressMonitor
          this.isRunInThread = true
          if (progressMonitor.result == ProgressMonitor.Result.SUCCESS) println("Successfully added folder to zip")
          if (progressMonitor.result == ProgressMonitor.Result.ERROR) println("Error occurred. Error message: " + progressMonitor.exception.message);
          else if (progressMonitor.result == ProgressMonitor.Result.CANCELLED) println("Task cancelled")
      }
  }
   job.join()
}