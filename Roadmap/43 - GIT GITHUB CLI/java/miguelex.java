import java.io.*;
import java.util.Scanner;

public class miguelex {
    private String workingDirectory;

    public void setWorkingDirectory(String dir) {
        File file = new File(dir);
        if (file.isDirectory()) {
            workingDirectory = file.getAbsolutePath();
            System.out.println("Directorio de trabajo establecido en: " + workingDirectory);
        } else {
            System.out.println("Error: El directorio no existe.");
        }
    }

    public void createRepository(String name) {
        if (workingDirectory == null) {
            System.out.println("Error: Debe establecer un directorio de trabajo primero.");
            return;
        }
        executeCommand("cd " + workingDirectory + " && git init " + name);
    }

    public void createBranch(String branchName) {
        executeCommand("cd " + workingDirectory + " && git checkout -b " + branchName);
    }

    public void changeBranch(String branchName) {
        executeCommand("cd " + workingDirectory + " && git checkout " + branchName);
    }

    public void showPendingCommits() {
        executeCommand("cd " + workingDirectory + " && git status");
    }

    public void commitChanges(String message) {
        executeCommand("cd " + workingDirectory + " && git add . && git commit -m \"" + message + "\"");
    }

    public void showCommitHistory() {
        executeCommand("cd " + workingDirectory + " && git log");
    }

    public void deleteBranch(String branchName) {
        executeCommand("cd " + workingDirectory + " && git branch -d " + branchName);
    }

    public void setRemoteRepository(String url) {
        executeCommand("cd " + workingDirectory + " && git remote add origin " + url);
    }

    public void pull() {
        executeCommand("cd " + workingDirectory + " && git pull");
    }

    public void push() {
        executeCommand("cd " + workingDirectory + " && git push origin HEAD");
    }

    private void executeCommand(String command) {
        try {
            Process process = Runtime.getRuntime().exec(new String[]{"cmd.exe", "/c", command});
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error al ejecutar el comando: " + e.getMessage());
        }
    }

    public void run() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nSelecciona una opción:");
            System.out.println("1. Establecer el directorio de trabajo");
            System.out.println("2. Crear un nuevo repositorio");
            System.out.println("3. Crear una nueva rama");
            System.out.println("4. Cambiar de rama");
            System.out.println("5. Mostrar ficheros pendientes de hacer commit");
            System.out.println("6. Hacer commit");
            System.out.println("7. Mostrar el historial de commits");
            System.out.println("8. Eliminar rama");
            System.out.println("9. Establecer repositorio remoto");
            System.out.println("10. Hacer pull");
            System.out.println("11. Hacer push");
            System.out.println("12. Salir");

            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (option) {
                case 1:
                    System.out.print("Introduce el directorio de trabajo: ");
                    String dir = scanner.nextLine();
                    setWorkingDirectory(dir);
                    break;
                case 2:
                    System.out.print("Introduce el nombre del repositorio: ");
                    String name = scanner.nextLine();
                    createRepository(name);
                    break;
                case 3:
                    System.out.print("Introduce el nombre de la nueva rama: ");
                    String branchName = scanner.nextLine();
                    createBranch(branchName);
                    break;
                case 4:
                    System.out.print("Introduce el nombre de la rama a la que deseas cambiar: ");
                    String changeBranch = scanner.nextLine();
                    changeBranch(changeBranch);
                    break;
                case 5:
                    showPendingCommits();
                    break;
                case 6:
                    System.out.print("Introduce el mensaje del commit: ");
                    String message = scanner.nextLine();
                    commitChanges(message);
                    break;
                case 7:
                    showCommitHistory();
                    break;
                case 8:
                    System.out.print("Introduce el nombre de la rama a eliminar: ");
                    String deleteBranch = scanner.nextLine();
                    deleteBranch(deleteBranch);
                    break;
                case 9:
                    System.out.print("Introduce la URL del repositorio remoto: ");
                    String url = scanner.nextLine();
                    setRemoteRepository(url);
                    break;
                case 10:
                    pull();
                    break;
                case 11:
                    push();
                    break;
                case 12:
                    System.out.println("Saliendo...");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Opción no válida.");
            }
        }
    }

    public static void main(String[] args) {
        GitHubCLI cli = new GitHubCLI();
        cli.run();
    }
}
