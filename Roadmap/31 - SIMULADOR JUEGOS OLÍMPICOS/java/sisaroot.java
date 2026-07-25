// #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

import java.util.*;
import java.util.stream.*;

public class SisaRoot {

    record Participant(String name, String country) {}

    static class Event {
        String name;
        List<Participant> participants = new ArrayList<>();
        Event(String name) { this.name = name; }
    }

    static class CountryMedals {
        String country; int gold, silver, bronze;
        CountryMedals(String c) { country = c; }
        int total() { return gold + silver + bronze; }
    }

    private final List<Event> events = new ArrayList<>();
    private final Map<String, CountryMedals> medalTable = new LinkedHashMap<>();
    private final Scanner scanner = new Scanner(System.in);
    private final Random rng = new Random();

    void registerEvent() {
        System.out.print("Nombre del evento: ");
        String name = scanner.nextLine().trim();
        if (name.isEmpty()) { System.out.println("Invalido."); return; }
        if (events.stream().anyMatch(e -> e.name.equalsIgnoreCase(name)))
        { System.out.println("Ya existe."); return; }
        events.add(new Event(name));
        System.out.println("Evento '" + name + "' registrado.");
    }

    void registerParticipant() {
        if (events.isEmpty()) { System.out.println("No hay eventos."); return; }
        for (int i=0; i<events.size(); i++) System.out.println("  "+(i+1)+". "+events.get(i).name);
        System.out.print("Selecciona numero: ");
        int idx; try { idx = Integer.parseInt(scanner.nextLine().trim()); } catch (Exception e) { System.out.println("Invalido."); return; }
        if (idx<1 || idx>events.size()) { System.out.println("Invalido."); return; }
        var ev = events.get(idx-1);
        System.out.print("Nombre: "); String pname = scanner.nextLine().trim();
        System.out.print("Pais: ");   String country = scanner.nextLine().trim();
        ev.participants.add(new Participant(pname, country));
        System.out.println("'" + pname + " (" + country + ")' añadido a '" + ev.name + "'.");
    }

    void simulateEvents() {
        if (events.isEmpty()) { System.out.println("No hay eventos."); return; }
        for (var ev : events) {
            System.out.println("\n=== Simulando: " + ev.name + " ===");
            if (ev.participants.size() < 3) { System.out.println("  Necesita >=3. Saltando."); continue; }
            var s = new ArrayList<>(ev.participants);
            Collections.shuffle(s, rng);
            System.out.println("  🥇 Oro:    " + s.get(0).name() + " (" + s.get(0).country() + ")");
            System.out.println("  🥈 Plata:  " + s.get(1).name() + " (" + s.get(1).country() + ")");
            System.out.println("  🥉 Bronce: " + s.get(2).name() + " (" + s.get(2).country() + ")");
            addMedal(s.get(0).country(), "gold"); addMedal(s.get(1).country(), "silver"); addMedal(s.get(2).country(), "bronze");
        }
    }

    void addMedal(String country, String type) {
        medalTable.putIfAbsent(country, new CountryMedals(country));
        var cm = medalTable.get(country);
        switch (type) { case "gold" -> cm.gold++; case "silver" -> cm.silver++; default -> cm.bronze++; }
    }

    void showReport() {
        System.out.println("\n== INFORME FINAL ==");
        if (medalTable.isEmpty()) { System.out.println("Sin resultados."); return; }
        var ranking = new ArrayList<>(medalTable.values());
        ranking.sort((a,b) -> b.gold!=a.gold ? b.gold-a.gold : b.silver!=a.silver ? b.silver-a.silver : b.bronze-a.bronze);
        for (int i=0; i<ranking.size(); i++) {
            var c = ranking.get(i);
            System.out.printf("%d. %-20s Oro:%d Plata:%d Bronce:%d Total:%d%n", i+1, c.country, c.gold, c.silver, c.bronze, c.total());
        }
    }

    void run() {
        while (true) {
            System.out.println("\n====== SIMULADOR JJOO ======\n1. Registrar evento\n2. Registrar participante\n3. Simular\n4. Informe\n5. Salir");
            System.out.print("Opcion: ");
            switch (scanner.nextLine().trim()) {
                case "1" -> registerEvent(); case "2" -> registerParticipant();
                case "3" -> simulateEvents(); case "4" -> showReport();
                case "5" -> { System.out.println("Hasta luego!"); return; }
                default -> System.out.println("Invalido.");
            }
        }
    }

    public static void main(String[] args) { new SisaRoot().run(); }
}
