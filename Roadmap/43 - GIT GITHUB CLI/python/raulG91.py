import os
import subprocess
class GitClient:
    def __init__(self) -> None:
        self._directory = ""
    def setDirectory(self,path:str):
        path = path.strip()
        try:
            os.chdir(path)
            self._directory = path 
            print(f'Directorio cambiado a : {self._directory}')   
        except Exception as err:
            print(f'Error cambiando directorio: {err}')
    def _isDirectorySet(self):
        if self._directory != "":
            return True
        else:
            return False        
    def createNewRepo(self):
        try:
            if self._isDirectorySet():
                subprocess.run("git init",shell=True,check=True,capture_output=True)
                print(f'Repositorio inicializado en {os.getcwd()}')
            else:
                print("Debe indicar directorio de trabajo")    
        except:
            print("Error inicializando el repositorio") 
    
    def createBranch(self,branch_name):

        if self._isDirectorySet():

            #Check if there is any branch 

            result = subprocess.run("git branch",shell=True,check=True,capture_output=True)
            branches = result.stdout.splitlines()
            
            if len(branches) == 0:
                #There is not branch, so create main one first and commit it
                try:
                    result = subprocess.run("git checkout -b main",shell= True, capture_output=True,check=True)
                    subprocess.run("git add .",shell=True,capture_output=True,check=True)
                    subprocess.run("git commit -m \"Initial commit\"",shell=True,capture_output=True,check=True)  
                except:
                    print("Error creando la rama principal")
            

            try:  
                subprocess.run(f'git branch {branch_name}',shell=True,check=True,capture_output=True)
                print(f'Branch {branch_name} ha sido creada')
            except:
                print(f'Error creando la rama {branch_name}')
        else:
            print("Debe establecer un directorio de trabajo")    
    def changeBranch(self,branch_name):
        if self._isDirectorySet():
            try:
                subprocess.run(f'git checkout {branch_name}',shell=True,capture_output=True,check=True)
                print(f'Rama actual es: {branch_name}')  
            except:
                print(f'Error cambiando a rama {branch_name}')   
        else:
            print("Debe establecer un directorio de trabajo")                       
    def getPendingFiles(self):
        if self._isDirectorySet():
            try:
                result = subprocess.run("git status",shell=True,check=True,capture_output=True)       
                pending = result.stdout.splitlines()       
                print(pending)
            except:
                print("Error obteniendo ficheros pendientes")   
        else:
            print("Debe establecer un directorio de trabajo")  
    def commitChanges(self,message):
        if self._isDirectorySet():
            try:
                subprocess.run("git add .",check=True,shell=True,capture_output=True)
                subprocess.run(f'git commit -m "{message}"',shell=True,capture_output=True,check=True)
                print("Commit ha sido realizado")
            except:
                print("Error haciendo commit") 
        else:
            print("Debe establecer un directorio de trabajo")             
    def getCommitHistory(self):
        if self._isDirectorySet():
            try:
                result = subprocess.run("git log",shell=True,check=True,capture_output=True)
                commit_history = result.stdout.splitlines()    
                print(commit_history)
            except:
                print("Error obteniendo lista de commits")    
        else:
            print("Debe establecer un directorio de trabajo")                  
    def deletebranch(self,branch_name:str):

        branch_name = branch_name.strip()
        try:
            subprocess.run(f'git branch -d {branch_name}',shell=True,check=True,capture_output=True)
            print(f'Rama {branch_name} borrada')
        except:
            print(f'Error borrando rama {branch_name}')    
    def addRemoteRepo(self,repo):
        
        if self._isDirectorySet():
            try:
                subprocess.run(f'git remote add origin {repo}',check=True,shell=True,capture_output=True)
                print(f'Repositorio {repo} ha sido establecido')
            except:
                print("Error añadiendo repositorio remoto")    
        else:
            print("Debe establecer directorio de trabajo")    
    def push(self):
        if self._isDirectorySet():
            try:
                result = subprocess.run("git push -u origin main",check=True,shell=True,capture_output=True)
                print(result)
                print("Cambios enviados al repositorio remoto")
            except:
                print("Error enviando cambios al repositorio remoto")  
        else:
            print("Debe establecer el directorio de trabajo")     
    def pull(self):
        if self._isDirectorySet():
            try:
                subprocess.run("git pull",check=True,shell=True,capture_output=True)
                print("Pull ejecutado corectamente")        
            except:
                print("Error obteniendo cambios del repositorio remoto")            
        else:  
            print("Debe establecer el directorio de trabajo")           
client = GitClient()

while True:
    print("Pulsa 1 para establecer directorio de trabajo")
    print("Pulsa 2 para crear un nuevo repositorio")
    print("Pulsa 3 para crear una rama")
    print("Pulsa 4 para cambiar de rama")
    print("Pulsa 5 para mostrar ficheros pendientes")
    print("Pulsa 6 para hacer un commit")
    print("Pulsa 7 para motrar el historial de commit")
    print("Pulsa 8 para eliminar una rama")
    print("Pulsa 9 para establecer el repositorio remoto")
    print("Pulsa 10 para hacer un pull del repositorio remoto")
    print("Pulsa 11 para hacer un push al repositorio remoto")
    print("Pulsa 12 para salir")

    option = int(input('Introduzca opcion: '))

    match option:
        case 1:     
            path = input("Introduzca directorio de trabajo ")
            client.setDirectory(path)
        case 2: client.createNewRepo()   
        case 3: 
            branch = input("Introduzca el nombre para la nueva rama ")
            client.createBranch(branch_name=branch)
        case 4: 
            branch = input("Introduzca la rama a moverse ")
            client.changeBranch(branch_name=branch)    
        case 5:
            client.getPendingFiles()   
        case 6:
            message = input("Intorduzca el mensaje para el commit ")
            message = message.strip()
            client.commitChanges(message)    
        case 7: client.getCommitHistory()    
        case 8: 
            branch = input("Introduzca la rama a eliminar ")
            client.deletebranch(branch)
        case 9:
            repo = input("Introduzca el repositorio remoto ")
            client.addRemoteRepo(repo)   
        case 10:
            client.pull()    
        case 11:
            client.push()    
        case 12: break


        