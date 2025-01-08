import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class martinbohorquez {
    public static void main(String[] args) throws Exception {
        List<Suscriptor> subscribers = getSubscribers();
        List<Suscriptor> winners = selectWinners(subscribers);
        displayWinners(winners);
    }

    private static List<Suscriptor> getSubscribers() {
        List<String> lines;
        try {
            lines = Files.readAllLines(Paths.get("fichero.csv"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        // Devolver una lista modificable (para realizar luego el shuffle)
        return new ArrayList<>(lines.stream()
                .map(l -> l.split(",\\s*"))
                .filter(l -> l[2].trim().equals("activo"))
                .map(l -> new Suscriptor(Integer.parseInt(l[0].trim()), l[1].trim()))
                .toList());
    }

    private static List<Suscriptor> selectWinners(List<Suscriptor> subscribers) throws Exception {
        if (subscribers.size() < 3) throw new Exception("El número de suscriptores activos debe ser mínimo 3!");
        Collections.shuffle(subscribers); // Ordenar la lista aleatoriamente
        return subscribers.subList(0, 3); // Escoger los 3 primeros
    }

    private static void displayWinners(List<Suscriptor> suscriptors) {
        List<String> prizes = new LinkedList<>(List.of("Suscripción", "Descuento", "Libro"));
        for (int i = 0; i < 3; i++) {
            System.out.printf("%s: %s%n", prizes.get(i), suscriptors.get(i));
        }
    }

    private static class Suscriptor {
        Integer id;
        String email;

        public Suscriptor(Integer id, String email) {
            this.id = id;
            this.email = email;
        }

        @Override
        public String toString() {
            return email + " (ID=" + id + ")";
        }
    }
}