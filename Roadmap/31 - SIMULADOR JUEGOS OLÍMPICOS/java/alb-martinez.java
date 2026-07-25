import java.util.*;

public class almartinez {

    private static final List<Event> events = new ArrayList<>();
    private static final Map<String, EnumMap<MedalType, Integer>> medalsByCountry = new HashMap<>();

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            displayMenu();
            int option = getOption(scanner);

            switch (option) {
                case 1 -> registerEvent(scanner);
                case 2 -> registerParticipant(scanner);
                case 3 -> simulateEvents();
                case 4 -> displayRanking();
                case 5 -> exit = true;
                default -> System.out.println("Invalid option.");
            }
        }

        scanner.close();
    }

    private static void displayMenu() {
        System.out.println("\nSelect an action:");
        System.out.println("1. Register event");
        System.out.println("2. Register participant");
        System.out.println("3. Simulate events");
        System.out.println("4. Create reports");
        System.out.println("5. exit");
    }

    private static int getOption(Scanner scanner) {
        while (!scanner.hasNextInt()) {
            System.out.println("Please enter a valid number.");
            scanner.next();
        }
        int option = scanner.nextInt();
        scanner.nextLine();
        return option;
    }

    private static void registerEvent(Scanner scanner) {
        System.out.println("Enter the event name: ");
        String eventName = scanner.nextLine();
        events.add(new Event(eventName));
        System.out.println("Event registered: " + eventName);
    }

    private static void registerParticipant(Scanner scanner) {
        if (events.isEmpty()) {
            System.out.println("No events registered. Plase register an event first");
            return;
        }

        System.out.println("Enter the participant's name: ");
        String participantName = scanner.nextLine();

        System.out.println("Enter the participant's country: ");
        String participantCountry = scanner.nextLine();

        Participant participan = new Participant(participantName, participantCountry);
        displayEvents();
        int eventIndex = getEventIndex(scanner);

        if (eventIndex == -1) return;

        events.get(eventIndex).addParticipant(participan);
        medalsByCountry.putIfAbsent(participantCountry, new EnumMap<>(MedalType.class));
        System.out.println("Participant registered: " + participantName + " from " + participantCountry);
    }

    private static void simulateEvents() {
        for (Event event : events) {
            System.out.println("Simulating event: " + event.name);

            if (event.participants.size() < 3) {
                System.out.println("Not enough participants to simulate this event.");
                continue;
            }

            List<Participant> winners = simulateEvent(event);
            assignMedals(winners);
            displayWinners(event, winners);
        }
    }

    private static void displayEvents() {
        System.out.println("Available events:");
        for (int i = 0; i < events.size(); i++) {
            System.out.println(i + ": " + events.get(i).name);
        }
    }

    private static int getEventIndex(Scanner scanner) {
        System.out.println("Select the event (0-" + (events.size() -1) + "): ");
        while (!scanner.hasNextInt()) {
            System.out.println("Please enter a valid number.");
            scanner.next();
        }
        int eventIndex = scanner.nextInt();

        if (eventIndex < 0 || eventIndex >= events.size()) {
            System.out.println("Invalid event.");
            return -1;
        }
        return eventIndex;
    }
    private static List<Participant> simulateEvent(Event event) {
        Collections.shuffle(event.participants);
        return event.participants.subList(0, 3);
    }

    private static void assignMedals(List<Participant> winners) {
        awardMedal(winners.get(0), MedalType.GOLD);
        awardMedal(winners.get(1), MedalType.SILVER);
        awardMedal(winners.get(2), MedalType.BRONZE);
    }

    private static void awardMedal(Participant participant, MedalType medalType) {
        EnumMap<MedalType, Integer> medals = medalsByCountry.get(participant.country);
        medals.put(medalType, medals.getOrDefault(medalType, 0) + 1);
    }

    private static void displayWinners(Event event, List<Participant> winners) {
        System.out.println("Winners of " + event.name + ":");
        System.out.println("Gold: " + winners.get(0).name + " from " + winners.get(0).country);
        System.out.println("Silver: " + winners.get(1).name + " from " + winners.get(1).country);
        System.out.println("Bronze: " + winners.get(2).name + " from " + winners.get(2).country);
    }

    private static void displayRanking() {
        System.out.println("\nRanking of countries by number of medals:");
        medalsByCountry.entrySet().stream()
                .sorted((a, b) -> {
                   int totalA = a.getValue().values().stream().mapToInt(Integer::intValue).sum();
                   int totalB = b.getValue().values().stream().mapToInt(Integer::intValue).sum();
                   return Integer.compare(totalB, totalA);
                })
                .forEach(entry -> {
                    String country = entry.getKey();
                    EnumMap<MedalType, Integer> medals = entry.getValue();
                    System.out.printf("%s: Gold=%d, Silver=%d, Bronze=%d%n",
                            country,
                            medals.getOrDefault(MedalType.GOLD, 0),
                            medals.getOrDefault(MedalType.SILVER, 0),
                            medals.getOrDefault(MedalType.BRONZE, 0));
                });
    }

    enum MedalType {
        GOLD, SILVER, BRONZE
    }

    static class Participant {
        String name;
        String country;

        public Participant(String name, String country) {
            this.name = name;
            this.country = country;
        }
    }

    static class Event {
        String name;
        List<Participant> participants = new ArrayList<>();

        public Event(String name) {
            this.name = name;
        }

        void addParticipant(Participant participant) {
            participants.add(participant);
        }
    }


}
