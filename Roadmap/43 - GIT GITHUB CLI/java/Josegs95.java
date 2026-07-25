import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().gitCLI();
    }

    final private Scanner sc = new Scanner(System.in);
    private String workingDirectory = System.getProperty("user.dir");

    public void gitCLI(){
        try(sc) {
            app:
            while(true){
                printMenu();
                printWorkingDirectory();
                System.out.print("Selecciona una opción: ");
                String option = sc.nextLine();
                switch (option){
                    case "1":
                        setWorkingDirectory();
                        break;
                    case "2":
                        createNewRepository();
                        break;
                    case "3":
                        createNewBranch();
                        break;
                    case "4":
                        changeCurrentBranch();
                        break;
                    case "5":
                        checkUncommittedFiles();
                        break;
                    case "6":
                        commitFiles();
                        break;
                    case "7":
                        showCommits();
                        break;
                    case "8":
                        deleteBranch();
                        break;
                    case "9":
                        setRemoteRepository();
                        break;
                    case "10":
                        makePull();
                        break;
                    case "11":
                        makePush();
                        break;
                    case "12":
                        break app;
                    default:
                        System.out.println("Error. Opción no válida.");
                }
                System.out.println();
            }
        }
    }

    private void setWorkingDirectory(){
        System.out.print("Introduce la ruta absoluta del directorio de trabajo: ");
        String path = sc.nextLine().strip();

        if (!Files.isDirectory(Path.of(path))){
            System.out.println("La ruta introducida no corresponde con un directorio existente");
            return;
        }

        workingDirectory = path;
    }

    private void createNewRepository(){
        runCommand("git init");
        System.out.println("Repositorio creado en " + workingDirectory);
    }

    private void createNewBranch(){
        System.out.print("Introduzca el nombre de la rama: ");
        String branchName = sc.nextLine();
        runCommand("git branch " + branchName);
    }

    private void changeCurrentBranch(){
        System.out.print("Ramas: ");
        runCommand("git branch");

        System.out.print("Introduzca el nombre de la rama: ");
        String branchName = sc.nextLine();

        runCommand("git checkout " + branchName);
    }

    private void checkUncommittedFiles(){
        runCommand("git status");
    }

    private void commitFiles(){
        System.out.print("Introduzca el mensaje del commit: ");
        String commitMessage = sc.nextLine();
        runCommand("git add .");
        runCommand("git commit -m \"" + commitMessage + "\"");
    }

    private void showCommits(){
        runCommand("git log --oneline");
    }

    private void deleteBranch(){
        System.out.print("Ramas: ");
        runCommand("git branch");

        System.out.print("Introduzca el nombre de la rama: ");
        String branchName = sc.nextLine();

        runCommand("git branch -d " + branchName);
    }

    private void setRemoteRepository(){
        System.out.print("Introduce la URL del repositorio remoto: ");
        String repositoryURL = sc.nextLine();
        runCommand("git remote add origin " + repositoryURL);
    }

    private void makePull(){
        runCommand("git pull");
    }

    private void makePush(){
        runCommand("git push");
    }

    private void runCommand(String command){
        try {
            ProcessBuilder pb = new ProcessBuilder().redirectErrorStream(true);
            pb.command("cmd", "/c", command);
            pb.directory(new File(workingDirectory));
            Process process = pb.start();
            StringWriter result = new StringWriter();
            try (BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream())))
            {
                in.transferTo(result);
                System.out.print(result);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void printWorkingDirectory(){
        System.out.println("Ruta de trabajo: " + workingDirectory);
        System.out.println();
    }

    private void printMenu(){
        System.out.println("================== Menu ==================");
        System.out.println("1. Establecer el directorio de trabajo");
        System.out.println("2. Crear un nuevo repositorio");
        System.out.println("3. Crear una nueva rama");
        System.out.println("4. Cambiar de rama");
        System.out.println("5. Mostrar ficheros pendientes de hacer commit");
        System.out.println("6. Hacer commit (junto con un add de todos los ficheros)");
        System.out.println("7. Mostrar el historial de commits");
        System.out.println("8. Eliminar rama");
        System.out.println("9. Establecer repositorio remoto");
        System.out.println("10. Hacer pull");
        System.out.println("11. Hacer push");
        System.out.println("12. Salir");
        System.out.println("==========================================");
    }
}
