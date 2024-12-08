import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.*;

public class miguelex {
    public static List<Suscriptor> obtenerSuscriptoresActivos(String archivoCsv) throws IOException {
        List<Suscriptor> suscriptores = new ArrayList<>();

        List<String> lines = Files.readAllLines(Paths.get(archivoCsv));
        lines.remove(0); 

        for (String line : lines) {
            String[] data = line.split(",");
            if (data[2].trim().equalsIgnoreCase("activo")) {
                suscriptores.add(new Suscriptor(data[0].trim(), data[1].trim()));
            }
        }

        return suscriptores;
    }

    public static List<Suscriptor> seleccionarGanadores(List<Suscriptor> suscriptores, int numeroGanadores) {
        if (suscriptores.size() < numeroGanadores) {
            return null;
        }

        Collections.shuffle(suscriptores);
        return suscriptores.subList(0, numeroGanadores);
    }

    public static void main(String[] args) throws IOException {
        String archivoCsv = "suscriptores.csv";
        List<Suscriptor> suscriptoresActivos = obtenerSuscriptoresActivos(archivoCsv);

        if (suscriptoresActivos.size() > 0) {
            List<Suscriptor> ganadores = seleccionarGanadores(suscriptoresActivos, 3);
            if (ganadores != null) {
                System.out.println("Ganador de la suscripción: " + ganadores.get(0));
                System.out.println("Ganador del descuento: " + ganadores.get(1));
                System.out.println("Ganador del libro: " + ganadores.get(2));
            } else {
                System.out.println("No hay suficientes suscriptores activos para seleccionar 3 ganadores.");
            }
        } else {
            System.out.println("No hay suscriptores activos.");
        }
    }
}

class Suscriptor {
    String id;
    String email;

    public Suscriptor(String id, String email) {
        this.id = id;
        this.email = email;
    }

    @Override
    public String toString() {
        return "ID: " + id + " | Email: " + email;
    }
}
