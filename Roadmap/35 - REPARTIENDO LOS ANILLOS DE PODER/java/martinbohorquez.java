import java.util.*;

/**
 * #35 REPARTIENDO LOS ANILLOS DE PODER
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    static Random random = new Random();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce el número de anillos que deseas repartir:");

        try {
            Integer totalRings = Integer.valueOf(sc.nextLine());
            distributeRings(totalRings);
        } catch (NumberFormatException e) {
            System.out.println("Debe ingresar un número entero de anillos!");
        }
    }

    static class Race {
        private String name;
        private Integer rings;

        public Race(String name) {
            this.name = name;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
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

    private static Map<String, Race> getRaceMap() {
        Map<String, Race> races = new LinkedHashMap<>();
        races.put("elves", new Race("Elfos"));
        races.put("dwarves", new Race("Enanos"));
        races.put("men", new Race("Hombres"));
        races.put("sauron", new Race("Sauron"));
        return races;
    }

    static void distributeRings(Integer totalRings) {
        List<Map<String, Race>> racesList = new ArrayList<>();
        for (int men = 2; men < totalRings; men += 2)
            for (int elves = 1; elves < totalRings; elves += 2) {
                Map<String, Race> raceMap = getRaceMap();
                int dwarves = totalRings - men - elves - 1;
                if (dwarves > 1 && esPrimo(dwarves)) {
                    raceMap.get("elves").setRings(elves);
                    raceMap.get("dwarves").setRings(dwarves);
                    raceMap.get("men").setRings(men);
                    raceMap.get("sauron").setRings(1);
                    racesList.add(raceMap);
                }
            }
        if (racesList.isEmpty()) System.out.println("No es posible distribuir los anillos de poder.");
        else {
            racesList.stream()
                    .map(Map::values)
                    .forEach(System.out::println);

            System.out.println("El conjunto de repartición mas equitativo es:");
            racesList.stream().map(Map::values)
                    .min(Comparator.comparingDouble(martinbohorquez::calcularDesviacionEstandar))
                    .ifPresentOrElse(c -> {
                                System.out.println("La colección con menor desviación estándar tiene los siguientes valores:");
                                System.out.println(c);
                            },
                            () -> System.out.println("No hay colecciones disponibles."));
        }
    }

    static double calcularDesviacionEstandar(Collection<Race> races) {
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

    static boolean esPrimo(Integer numero) {
        if (numero <= 1) {
            return false;
        }
        if (numero <= 3) {
            return true;
        }
        if (numero % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= Math.sqrt(numero); i += 2) {
            if (numero % i == 0) {
                return false;
            }
        }
        return true;
    }
}

