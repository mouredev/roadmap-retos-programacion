import java.util.*;
import java.util.function.Consumer;

/**
 * #35 REPARTIENDO LOS ANILLOS DE PODER
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    static List<Map<String, Race>> racesList = new LinkedList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce el número de anillos que deseas repartir:");

        try {
            Integer totalRings = Integer.valueOf(sc.nextLine());
            long duration1 = getDuration(martinbohorquez::distributeRings, totalRings);
            if (racesList.isEmpty()) System.out.println("No es posible distribuir los anillos de poder.");
            else {
                long duration2 = getDuration(martinbohorquez::displayDistributeRings, racesList);
                System.out.printf("La cantidad de posibles distribuciones es: %s%n", racesList.size());
                long duration3 = getDuration(martinbohorquez::bestDistributeRings, racesList);
                double duration = (double) (duration1 + duration2 + duration3) / 1000;
                System.out.printf("Execution time in seconds: %d (ms) + %d (ms) + %d (ms) = %.2f seconds.%n", duration1, duration2, duration3, duration);
            }
        } catch (NumberFormatException e) {
            System.out.println("Debe ingresar un número entero de anillos!");
        }
    }

    private static <T> long getDuration(Consumer<T> method, T parameter) {
        long startTime = System.currentTimeMillis();
        method.accept(parameter); // Run the passed method
        long endTime = System.currentTimeMillis();
        return endTime - startTime;
    }

    private static Map<String, Race> getRaceMap() {
        Map<String, Race> races = new LinkedHashMap<>();
        races.put("elves", new Race("Elfos"));
        races.put("dwarves", new Race("Enanos"));
        races.put("men", new Race("Hombres"));
        races.put("sauron", new Race("Sauron"));
        return races;
    }

    private static void distributeRings(Integer totalRings) {
        totalRings -= 1;
        for (int men = 2; men <= totalRings; men += 2)
            for (int elves = 1; elves <= (totalRings - men); elves += 2) {
                int dwarves = totalRings - men - elves;
                if (esPrimo(dwarves)) {
                    Map<String, Race> raceMap = getRaceMap();
                    raceMap.get("elves").setRings(elves);
                    raceMap.get("dwarves").setRings(dwarves);
                    raceMap.get("men").setRings(men);
                    raceMap.get("sauron").setRings(1);
                    racesList.add(raceMap);
                }
            }
    }

    private static void displayDistributeRings(List<Map<String, Race>> racesList) {
        racesList.stream()
                .map(Map::values)
                .forEach(System.out::println);
    }

    private static void bestDistributeRings(List<Map<String, Race>> racesList) {
        System.out.println("El conjunto de repartición mas equitativo es:");
        racesList.stream().map(Map::values)
                .min(Comparator.comparingDouble(martinbohorquez::calcularDesviacionEstandar))
                .ifPresent(System.out::println);
    }

    private static boolean esPrimo(Integer numero) {
        if (numero <= 1) return false;
        if (numero <= 3) return true;
        if (numero % 2 == 0) return false;
        for (int i = 3; i <= Math.sqrt(numero); i += 2) {
            if (numero % i == 0) return false;
        }
        return true;
    }

    private static double calcularDesviacionEstandar(Collection<Race> races) {
        if (races.isEmpty()) return 0.0;

        double media = races.stream()
                .mapToInt(Race::getRings)
                .average()
                .orElse(0.0);

        double sumaCuadrados = races.stream()
                .mapToDouble(race -> Math.pow(race.getRings() - media, 2))
                .sum();

        return Math.sqrt(sumaCuadrados / races.size());
    }

    private static class Race {
        private final String name;
        private Integer rings;

        public Race(String name) {
            this.name = name;
        }

        public Integer getRings() {
            return rings;
        }

        public void setRings(Integer rings) {
            this.rings = rings;
        }

        @Override
        public String toString() {
            return "'" + name + "': '" + rings + "'";
        }
    }
}

