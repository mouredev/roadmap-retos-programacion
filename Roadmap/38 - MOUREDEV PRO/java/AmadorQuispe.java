package com.amsoft.roadmap.example38;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Random;

public class Example38 {

    public static void main(String[] args) {

        List<Subscriptor> subs = getSubscribers();
        List<Subscriptor> winners = getWinners(subs, 3);
        System.out.println("Ganador suscripción : " + winners.get(0).id + " " + winners.get(0).email);
        System.out.println("Ganador Descuento : " + winners.get(1).id + " " + winners.get(1).email);
        System.out.println("Ganador Libro : " + winners.get(2).id + " " + winners.get(2).email);

    }

    static List<Subscriptor> getSubscribers() {
        var filePath = FileSystems.getDefault().getPath("");
        var fileDir = filePath.toAbsolutePath().toString();
        Path path = Path.of(fileDir.concat("/subs.csv"));
        List<String> lines;
        try {
            lines = Files.readAllLines(path);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return lines.subList(1, lines.size() - 1).stream()
                .map(l -> l.split(","))
                .map(l -> new Subscriptor(Integer.parseInt(l[0]), l[1], l[2]))
                .filter(s -> s.status.equals("activo"))
                .toList();
    }

    static List<Subscriptor> getWinners(List<Subscriptor> subs, int numWinners) {
        if (subs.size() < numWinners) {
            throw new RuntimeException("No hay suficientes subs para obtener ganadores");
        }
        Random random = new Random();
        return random.ints(0, subs.size())
                .distinct()
                .limit(numWinners)
                .mapToObj(subs::get)
                .toList();
    }

    private record Subscriptor(Integer id, String email, String status) {

        @Override
        public String toString() {
            return "Subscriptor{"
                    + "id=" + id
                    + ", email='" + email + '\''
                    + ", status='" + status + '\''
                    + '}';
        }
    }

}
