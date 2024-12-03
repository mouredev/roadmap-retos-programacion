import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    private String workingDirectory;
    private final Scanner scanner;

    public Main() {
        this.scanner = new Scanner(System.in);
        this.workingDirectory = System.getProperty("user.dir");
    }

    public void start() {
        int option;
        do {
            showMenu();
            option = getOption();
            executeOption(option);
        } while (option != 12);
    }

    private void showMenu() {
        System.out.println("\n=== Git CLI ===");
        System.out.println("Directorio actual: " + workingDirectory);
        System.out.println("1. Establecer directorio de trabajo");
        System.out.println("2. Crear nuevo repositorio");
        System.out.println("3. Crear nueva rama");
        System.out.println("4. Cambiar de rama");
        System.out.println("5. Mostrar ficheros pendientes");
        System.out.println("6. Hacer commit");
        System.out.println("7. Mostrar historial de commits");
        System.out.println("8. Eliminar rama");
        System.out.println("9. Establecer repositorio remoto");
        System.out.println("10. Hacer pull");
        System.out.println("11. Hacer push");
        System.out.println("12. Salir");
    }

    private int getOption() {
        System.out.print("\nSeleccione una opción: ");
        try {
            return Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            return 0;
        }
    }

    private void executeOption(int option) {
        try {
            switch (option) {
                case 1 -> setWorkingDirectory();
                case 2 -> initRepository();
                case 3 -> createBranch();
                case 4 -> checkoutBranch();
                case 5 -> showStatus();
                case 6 -> makeCommit();
                case 7 -> showLog();
                case 8 -> deleteBranch();
                case 9 -> setRemoteRepository();
                case 10 -> pull();
                case 11 -> push();
                case 12 -> System.out.println("Exiting...");
                default -> System.out.println("Opción no válida");
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private void setWorkingDirectory() {
        System.out.print("Introduce la ruta del directorio: ");
        String newPath = scanner.nextLine();
        File directory = new File(newPath);

        if (directory.exists() && directory.isDirectory()) {
            workingDirectory = newPath;
            System.out.println("Directorio establecido correctamente");
        } else {
            System.out.println("El directorio no existe");
        }
    }

    private void initRepository() throws Exception {
        executeCommand("git init");
        System.out.println("Repositorio inicializado correctamente");
    }

    private void createBranch() throws Exception {
        System.out.print("Nombre de la nueva rama: ");
        String branchName = scanner.nextLine();
        executeCommand("git branch " + branchName);
        System.out.println("Rama creada correctamente");
    }

    private void checkoutBranch() throws Exception {
        System.out.print("Nombre de la rama: ");
        String branchName = scanner.nextLine();
        executeCommand("git checkout " + branchName);
        System.out.println("Cambio de rama realizado");
    }

    private void showStatus() throws Exception {
        executeCommand("git status");
    }

    private void makeCommit() throws Exception {
        executeCommand("git add .");
        System.out.print("Mensaje del commit: ");
        String message = scanner.nextLine();
        executeCommand("git commit -m \"" + message + "\"");
        System.out.println("Commit realizado correctamente");
    }

    private void showLog() throws Exception {
        executeCommand("git log --oneline");
    }

    private void deleteBranch() throws Exception {
        System.out.print("Nombre de la rama a eliminar: ");
        String branchName = scanner.nextLine();
        executeCommand("git branch -d " + branchName);
        System.out.println("Rama eliminada correctamente");
    }

    private void setRemoteRepository() throws Exception {
        System.out.print("URL del repositorio remoto: ");
        String url = scanner.nextLine();
        executeCommand("git remote add origin " + url);
        System.out.println("Repositorio remoto establecido correctamente");
    }

    private void pull() throws Exception {
        executeCommand("git pull");
        System.out.println("Pull realizado correctamente");
    }

    private void push() throws Exception {
        System.out.print("¿Es el primer push? (s/n): ");
        String response = scanner.nextLine();
        if (response.toLowerCase().equals("s")) {
            executeCommand("git push -u origin master");
        } else {
            executeCommand("git push");
        }
        System.out.println("Push realizado correctamente");
    }

    private void executeCommand(String command) throws Exception {
        ProcessBuilder processBuilder = new ProcessBuilder();
        if (System.getProperty("os.name").toLowerCase().startsWith("windows")) {
            processBuilder.command("cmd.exe", "/c", command);
        } else {
            processBuilder.command("bash", "-c", command);
        }

        processBuilder.directory(new File(workingDirectory));
        Process process = processBuilder.start();

        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }

        BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
        while ((line = errorReader.readLine()) != null) {
            System.out.println("Error: " + line);
        }

        int exitCode = process.waitFor();
        if (exitCode != 0) {
            throw new Exception("Error ejecutando el comando. Código de salida: " + exitCode);
        }
    }

    public static void main(String[] args) {
        Main cli = new Main();
        cli.start();
    }
}
