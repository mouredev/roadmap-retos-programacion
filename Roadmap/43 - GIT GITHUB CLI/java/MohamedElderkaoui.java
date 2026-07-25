import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class MohamedElderkaoui {

    // Directorio de trabajo actual. Por defecto, es el directorio desde donde se ejecuta el programa.
    private static File workingDirectory = new File(System.getProperty("user.dir"));

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true; // Controla si el programa sigue activo

        // Bucle principal del menú
        while (running) {
            System.out.println("\nGitHub CLI - GitHub Universe 2024");
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
            System.out.print("Seleccione una opción: ");
            
            // Capturamos la opción del usuario
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consumimos el salto de línea

            try {
                // Evaluamos la opción elegida por el usuario
                switch (choice) {
                    case 1 -> setWorkingDirectory(scanner);
                    case 2 -> createRepository();
                    case 3 -> createBranch(scanner);
                    case 4 -> switchBranch(scanner);
                    case 5 -> showStatus();
                    case 6 -> commitChanges(scanner);
                    case 7 -> showCommitHistory();
                    case 8 -> deleteBranch(scanner);
                    case 9 -> setRemote(scanner);
                    case 10 -> pullChanges();
                    case 11 -> pushChanges();
                    case 12 -> running = false; // Salimos del bucle
                    default -> System.out.println("Opción no válida, intente de nuevo.");
                }
            } catch (IOException | InterruptedException e) {
                // Captura y muestra errores de entrada/salida o interrupciones
                System.err.println("Error: " + e.getMessage());
            }
        }
        scanner.close(); // Cerramos el escáner al salir del programa
        System.out.println("Saliendo del CLI de Git.");
    }

    // Método para establecer el directorio de trabajo
    private static void setWorkingDirectory(Scanner scanner) {
        System.out.print("Ingrese la ruta del nuevo directorio de trabajo: ");
        String path = scanner.nextLine();
        File newDir = new File(path);

        // Verificamos si la ruta ingresada es válida
        if (newDir.exists() && newDir.isDirectory()) {
            workingDirectory = newDir;
            System.out.println("Directorio de trabajo actualizado a: " + workingDirectory.getAbsolutePath());
        } else {
            System.out.println("Ruta no válida.");
        }
    }

    // Método para inicializar un nuevo repositorio Git
    private static void createRepository() throws IOException, InterruptedException {
        executeCommand("git init");
    }

    // Método para crear una nueva rama en el repositorio actual
    private static void createBranch(Scanner scanner) throws IOException, InterruptedException {
        System.out.print("Ingrese el nombre de la nueva rama: ");
        String branchName = scanner.nextLine();
        executeCommand("git branch " + branchName);
    }

    // Método para cambiar a una rama existente
    private static void switchBranch(Scanner scanner) throws IOException, InterruptedException {
        System.out.print("Ingrese el nombre de la rama a la que desea cambiar: ");
        String branchName = scanner.nextLine();
        executeCommand("git checkout " + branchName);
    }

    // Método para mostrar el estado de los archivos pendientes de hacer commit
    private static void showStatus() throws IOException, InterruptedException {
        executeCommand("git status");
    }

    // Método para añadir todos los archivos y hacer un commit con un mensaje proporcionado
    private static void commitChanges(Scanner scanner) throws IOException, InterruptedException {
        System.out.print("Ingrese el mensaje del commit: ");
        String message = scanner.nextLine();
        executeCommand("git add ."); // Añadimos todos los archivos al área de staging
        executeCommand("git commit -m \"" + message + "\""); // Hacemos commit con el mensaje
    }

    // Método para mostrar el historial de commits en formato breve
    private static void showCommitHistory() throws IOException, InterruptedException {
        executeCommand("git log --oneline");
    }

    // Método para eliminar una rama especificada por el usuario
    private static void deleteBranch(Scanner scanner) throws IOException, InterruptedException {
        System.out.print("Ingrese el nombre de la rama a eliminar: ");
        String branchName = scanner.nextLine();
        executeCommand("git branch -d " + branchName);
    }

    // Método para configurar un repositorio remoto (URL proporcionada por el usuario)
    private static void setRemote(Scanner scanner) throws IOException, InterruptedException {
        System.out.print("Ingrese la URL del repositorio remoto: ");
        String remoteUrl = scanner.nextLine();
        executeCommand("git remote add origin " + remoteUrl);
    }

    // Método para hacer pull desde el repositorio remoto
    private static void pullChanges() throws IOException, InterruptedException {
        executeCommand("git pull origin main"); // Nota: Especificar la rama 'main' o la rama predeterminada del repositorio
    }

    // Método para hacer push de los cambios al repositorio remoto
    private static void pushChanges() throws IOException, InterruptedException {
        executeCommand("git push origin main"); // Nota: Especificar la rama 'main' o la rama predeterminada del repositorio
    }

    // Método auxiliar que ejecuta un comando del sistema en el directorio de trabajo actual
    private static void executeCommand(String command) throws IOException, InterruptedException {
        ProcessBuilder builder = new ProcessBuilder(command.split(" ")); // Dividimos el comando en partes
        builder.directory(workingDirectory); // Establecemos el directorio de trabajo
        Process process = builder.start(); // Iniciamos el proceso

        // Lectura de la salida estándar del proceso
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        // Lectura de la salida de errores del proceso
        BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));

        // Imprimimos la salida del comando línea por línea
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }

        // Imprimimos cualquier error que ocurra durante la ejecución del comando
        while ((line = errorReader.readLine()) != null) {
            System.err.println(line);
        }

        // Esperamos a que el proceso termine
        process.waitFor();
    }
}
