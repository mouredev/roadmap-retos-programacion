import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class danhingar {

    public static void main(String[] args) {

        simulateGame();

    }

    public static void simulateGame() {
        System.out.println("Simulador de Juegos Olimpicos");
        Olympics olympics = new Olympics();

        while (Boolean.TRUE) {
            System.out.println();
            String options = """
                    1. Registro de eventos.
                    2. Registro de participantes.
                    3. Simulación de eventos.
                    4. Creación de informes.
                    5. Salir.""";
            System.out.println(options);
            System.out.print("Selecciona una opción: ");
            Scanner sc = new Scanner(System.in);
            String option = sc.nextLine();
            switch (option) {
                case "1":
                    olympics.registerEvent();
                    break;
                case "2":
                    olympics.registerParticipant();
                    break;
                case "3":
                    olympics.simulateEvents();
                    break;
                case "4":
                    olympics.showReport();
                    break;
                case "5":
                    System.out.println("Saliendo del simulador...");
                    sc.close();
                    System.exit(0);
                    break;

                default:
                    System.out.println("Opción no válida");
                    break;
            }
        }

    }

}

class Participant {
    private String name;
    private String country;

    public Participant(String name, String country) {
        this.name = name;
        this.country = country;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
}

class Event {
    private String category;
    private List<Participant> participants;

    public Event(String category) {
        this.category = category;
        this.participants = new ArrayList<>();
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public List<Participant> getParticipants() {
        return participants;
    }

    public void setParticipants(List<Participant> participants) {
        this.participants = participants;
    }
}

interface EventInterface {

    List<Participant> simulate(Event event);

    Map<String, Participant> getPodium(Event event);

    void registerParticipantInEvent(Event event, Participant participant);

}

class EventService implements EventInterface {

    @Override
    public List<Participant> simulate(Event event) {
        Collections.shuffle(event.getParticipants());
        return event.getParticipants();

    }

    @Override
    public Map<String, Participant> getPodium(Event event) {
        return Map.of("gold", event.getParticipants().get(0), "silver", event.getParticipants().get(1), "bronze",
                event.getParticipants().get(2));
    }

    @Override
    public void registerParticipantInEvent(Event event, Participant participant) {
        event.getParticipants().add(participant);
    }

}

class Olympics {

    private List<Event> events;
    private EventService eventService;
    private Map<String, Map<String, Integer>> countryResults;
    private Map<Event, List<Participant>> eventResults;

    public Olympics() {
        this.events = new ArrayList<>();
        this.countryResults = new HashMap<>();
        this.eventResults = new HashMap<>();
        this.eventService = new EventService();
    }

    public void registerEvent() {

        System.out.print("Introduce la categoría del evento: ");
        Scanner sc = new Scanner(System.in);
        String category = sc.nextLine().trim();
        Event event = new Event(category);
        if (events.contains(event)) {
            System.out.printf(String.format("El evento %s ya está registrado.\n", category));
        } else {
            events.add(event);
        }
        System.out.printf(String.format("Evento %s registrado correctamente.\n", category));
    }

    public void registerParticipant() {
        if (events.isEmpty()) {
            System.out.println("No hay eventos registrados. Registre uno primero.");
        } else {

            System.out.print("Introduce el nombre del participante: ");
            Scanner sc = new Scanner(System.in);
            String name = sc.nextLine().trim();
            System.out.print("Introduce el país del participante: ");
            String country = sc.nextLine().trim();

            Participant participant = new Participant(name, country);

            System.out.println("Eventos disponibles:");
            for (int i = 0; i < events.size(); i++) {
                System.out.println(i + 1 + ". " + events.get(i).getCategory());
            }

            System.out.print("Selecciona el número del evento para asignar al participante: ");
            Integer index = sc.nextInt() - 1;

            if (index < 0 || index > events.size()) {
                System.out.println("Selección del evento deportivo inválido. El participante no se ha registrado.");
            } else {

                Event event = events.get(index);
                if (event.getParticipants().contains(participant)) {
                    System.out.printf("El participante %s de %s ya está registrado en el evento deportivo %s.\n",
                            participant.getName(), participant.getCountry(), event.getCategory());
                } else {
                    eventService.registerParticipantInEvent(event, participant);
                    System.out.printf("El participante %s de %s se ha registrado en el evento deportivo %s.\n",
                            participant.getName(), participant.getCountry(), event.getCategory());
                }
            }
        }
    }

    public void simulateEvents() {
        if (events.isEmpty()) {
            System.out.println("No hay eventos registrados.");
        } else {
            for (Event event : events) {
                if (event.getParticipants().size() < 3) {
                    System.out.println(
                            "No hay participantes suficientes para simular el evento " + event.getCategory()
                                    + " (mínimo 3).");
                    return;
                }
                eventService.simulate(event);
                Map<String, Participant> result = eventService.getPodium(event);

                eventResults.put(event, List.of(result.get("gold"), result.get("silver"), result.get("bronze")));

                updateCountryResult("gold", result.get("gold").getCountry());
                updateCountryResult("silver", result.get("silver").getCountry());
                updateCountryResult("bronze", result.get("bronze").getCountry());

                System.out.printf("""
                        Resultados simulación del evento: %s
                        Oro: %s (%s)
                        Plata: %s (%s)
                        Bronce: %s (%s)\n""",
                        event.getCategory(), result.get("gold").getName(), result.get("gold").getCountry(),
                        result.get("silver").getName(), result.get("silver").getCountry(),
                        result.get("bronze").getName(), result.get("bronze").getCountry());
            }
        }
    }

    public void showReport() {

        System.out.println("Informe Juegos Olímpicos:");

        for (Event event : eventResults.keySet()) {
            System.out.printf("""
                    Evento: %s
                    Oro: %s (%s)
                    Plata: %s (%s)
                    Bronce: %s (%s)\n""",
                    event.getCategory(), eventResults.get(event).get(0).getName(),
                    eventResults.get(event).get(0).getCountry(),
                    eventResults.get(event).get(1).getName(), eventResults.get(event).get(1).getCountry(),
                    eventResults.get(event).get(2).getName(), eventResults.get(event).get(2).getCountry());
        }

        if (!countryResults.isEmpty()) {
            Map<String, Map<String, Integer>> sortedResults = countryResults.entrySet()
                    .stream()
                    .sorted((entry1, entry2) -> {
                        Map<String, Integer> medals1 = entry1.getValue();
                        Map<String, Integer> medals2 = entry2.getValue();

                        int compareOro = Integer.compare(medals2.get("gold"), medals1.get("gold"));
                        if (compareOro != 0)
                            return compareOro;

                        int comparePlata = Integer.compare(medals2.get("silver"), medals1.get("silver"));
                        if (comparePlata != 0)
                            return comparePlata;

                        return Integer.compare(medals2.get("bronze"), medals1.get("bronze"));
                    })
                    .collect(Collectors.toMap(
                            Map.Entry::getKey,
                            Map.Entry::getValue,
                            (e1, e2) -> e1,
                            LinkedHashMap::new));
            for (String country : sortedResults.keySet()) {
                System.out.printf("""
                        País: %s Oro %s, Plata: %s, Bronce %s\n""",
                        country, countryResults.get(country).get("gold"),
                        countryResults.get(country).get("silver"),
                        countryResults.get(country).get("bronze"));
            }
        } else {
            System.out.println("No hay medallas por país registradas");
        }

    }

    public void updateCountryResult(String medal, String country) {
        countryResults.putIfAbsent(country, new HashMap<>(Map.of("gold", 0, "silver", 0, "bronze", 0)));

        Map<String, Integer> countryMedals = countryResults.get(country);
        countryMedals.put(medal, countryMedals.get(medal) + 1);
    }

}