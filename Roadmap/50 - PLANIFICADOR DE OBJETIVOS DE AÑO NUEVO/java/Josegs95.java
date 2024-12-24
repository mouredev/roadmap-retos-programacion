import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().newYearPlanner();
    }

    final private Scanner sc = new Scanner(System.in);
    private List<Plan> planList = new ArrayList<>();

    public void newYearPlanner(){

        try(sc){
            app:
            while(true){
                printMenu();
                System.out.print("Selecciona la opción que desees: ");
                String option = sc.nextLine();
                switch (option){
                    case "1" -> createGoal();
                    case "2" -> System.out.println(calculatePlanning());
                    case "3" -> savePlanningInAFile();
                    case "4" -> {
                        System.out.println("Saliendo de la aplicación...");
                        break app;
                    }
                    default -> System.out.println("Error, opción no válida.");
                }
            }
        }
    }

    private boolean createGoal(){
        if (planList.size() > 10){
            System.out.println("Solo puedes tener 10 objetivos de forma simultánea");
            return false;
        }

        System.out.print("Introduzca el objetivo: ");
        String goal = sc.nextLine();
        Integer amount = askIntegerToUser("Introduzca la cantidad: ");
        System.out.print("Introduzca las unidades: ");
        String unit = sc.nextLine();

        while(true){
            Integer deadline = askIntegerToUser("Introduzca el plazo (en meses): ");
            if (deadline > 12)
                System.out.println("El plazo máximo permitido son 12 meses.");
            else
                return planList.add(new Plan(goal, amount, unit, deadline));
        }
    }

    private String calculatePlanning(){
        String[][] planning = initPlanning();

        for (Plan plan : planList){
            int amountPerMonth = plan.getAmount() / plan.getDeadline();
            int rest = plan.getAmount() % plan.getDeadline();
            months:
            for (int i = 0; (rest > 0 || amountPerMonth > 0) && i < plan.getDeadline(); i++){
                for (int j = 0; j < planning[0].length; j++){
                    if (planning[i][j] != null)
                        continue;

                    int amount = amountPerMonth + (rest-- > 0 ? 1 : 0);
                    planning[i][j] = plan.getGoal() + "(" + amount + " " + plan.getUnit() +
                            "/mes). Total: " + plan.getAmount();
                    continue months;
                }
            }
        }

        return getPlanningAsString(planning);
    }

    private boolean savePlanningInAFile(){
        String planningString = calculatePlanning();
        Path filePath = Path.of("planning.txt");
        try {
            Files.writeString(filePath, planningString,
                    StandardOpenOption.CREATE,
                    StandardOpenOption.TRUNCATE_EXISTING);
            System.out.println("Planificación guardada exitosamente en: '" + filePath.toFile().getAbsolutePath() + "'");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return true;
    }

    private String[][] initPlanning(){
        String[][] matrix = new String[12][11];
        matrix[0][0] = "Enero";
        matrix[1][0] = "Febrero";
        matrix[2][0] = "Marzo";
        matrix[3][0] = "Abril";
        matrix[4][0] = "Mayo";
        matrix[5][0] = "Junio";
        matrix[6][0] = "Julio";
        matrix[7][0] = "Agosto";
        matrix[8][0] = "Septiembre";
        matrix[9][0] = "Octubre";
        matrix[10][0] = "Noviembre";
        matrix[11][0] = "Diciembre";

        return matrix;
    }

    private String getPlanningAsString(String[][] planning){
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < planning.length; i++){
            sb.append(planning[i][0] + ":" + System.lineSeparator());
            for (int j = 1; j < planning[0].length; j++){
                if (planning[i][j] == null){
                    if (j == 1)
                        sb.append("Nada." + System.lineSeparator());
                    break;
                }

                sb.append("[ ] " + j + ". " + planning[i][j] + System.lineSeparator());
            }
            sb.append(System.lineSeparator());
        }

        return sb.toString();
    }

    private Integer askIntegerToUser(String message){
        while(true){
            try{
                System.out.print(message);
                Integer userInput = Integer.parseInt(sc.nextLine());
                return userInput;
            } catch (NumberFormatException e) {
                System.out.println("Error, debes introducir un número entero");
            }
        }
    }

    private void printMenu(){
        System.out.println("===== Menu =====");
        System.out.println("1. Añadir objetivo al 'planning'");
        System.out.println("2. Calcular el plan detallado");
        System.out.println("3. Guardar la planificación");
        System.out.println("4. Salir de la aplicación");
        System.out.println("================");
    }

    public class Plan{
        private String goal;
        private Integer amount;
        private String unit;
        private Integer deadline;

        public Plan(String goal, Integer amount, String unit, Integer deadline) {
            this.goal = goal;
            this.amount = amount;
            this.unit = unit;
            this.deadline = deadline;
        }

        public String getGoal() {
            return goal;
        }

        public Integer getAmount() {
            return amount;
        }

        public String getUnit() {
            return unit;
        }

        public Integer getDeadline() {
            return deadline;
        }
    }
}
