import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * #31 SIMULADOR JUEGOS OLÍMPICOS
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    private static final Scanner sc = new Scanner(System.in);
    private static boolean flag = true;

    public static void main(String[] args) {
        String option;
        while (flag) {
            option = menuOptions();
            switch (option) {
                case "1" -> Olympic.registerEvent();
                case "2" -> Olympic.registerCompetitor();
                case "3" -> Olympic.simulateEvents();
                case "4" -> {
                    Olympic.displayWinners();
                    Olympic.displayRankingByCountries();
                }
                case "5" -> {
                    System.out.println("Saliendo del programa...!");
                    flag = false;
                }
                default -> System.out.printf("Opción '%s' no valida! Ingresar una opción del 1 al 5.%n", option);
            }
        }
    }

    /*
     *  Requisitos:
     *  1. Registrar eventos deportivos.
     *  2. Registrar participantes por nombre y país.
     *  3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
     *  4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
     *  5. Mostrar los ganadores por cada evento.
     *  6. Mostrar el ranking de países según el número de medallas.
     */
    private static String menuOptions() {
        System.out.printf("%n<--- BIENVENIDO AL MENU \"JJOO PARIS 2024\" --->%n");
        System.out.println("""
                ------------------------------------------------
                Usted cuenta con las siguientes opciones:
                1. Registro de eventos.
                2. Registro de participantes.
                3. Simulación de eventos.
                4. Creación de informes.
                5. Salir del programa.
                """);
        System.out.print("Ingresar su número opción del menú (1, 2, 3, 4, 5): ");
        return sc.nextLine();
    }

    static class Competitor {
        String name;
        String country;

        public Competitor(String name, String country) {
            this.name = name;
            this.country = country;
        }

        public String getName() {
            return name;
        }

        public String getCountry() {
            return country;
        }

        @Override
        public boolean equals(Object object) {
            if (this == object) return true;
            if (object == null || getClass() != object.getClass()) return false;
            Competitor that = (Competitor) object;
            return Objects.equals(name, that.name) && Objects.equals(country, that.country);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, country);
        }

        @Override
        public String toString() {
            return "{name= '" + name + "', country= '" + country + "'}";
        }
    }

    static class CountryRank {
        private String country;
        private Map<Medal, Integer> medals;

        public CountryRank(String country) {
            this.country = country;
            medals = new LinkedHashMap<>();
            medals.put(Medal.GOLD, 0);
            medals.put(Medal.SILVER, 0);
            medals.put(Medal.BRONZE, 0);
        }

        public String getCountry() {
            return country;
        }

        public void setCountry(String country) {
            this.country = country;
        }

        public Map<Medal, Integer> getMedals() {
            return medals;
        }

        public void setMedals(Map<Medal, Integer> medals) {
            this.medals = medals;
        }

        @Override
        public String toString() {
            return "{country= '" + country + "', medals= '" + medals + "'}";
        }
    }

    enum Medal {
        GOLD, SILVER, BRONZE
    }

    static class EventCompetitor {
        private String event;
        private List<Competitor> competitors;

        public EventCompetitor(String event) {
            this.event = event;
            competitors = new LinkedList<>();
        }

        public String getEvent() {
            return event;
        }

        public void setEvent(String event) {
            this.event = event;
        }

        public List<Competitor> getCompetitors() {
            return competitors;
        }

        public void setCompetitors(List<Competitor> competitors) {
            this.competitors = competitors;
        }

        private void printWinner() {
            System.out.printf("{event= '%s', competitor= '%s'}%n", event, competitors.getFirst());
        }

        @Override
        public String toString() {
            return "{event='" + event + "', competitors=" + competitors + "}";
        }
    }

    private static class Olympic {
        static List<EventCompetitor> events = new LinkedList<>();
        static List<CountryRank> countriesRank = new LinkedList<>();

        private static void registerEvent() {
            System.out.print("Indicar el evento a registrar: ");
            String event = sc.nextLine().strip();

            if (event.isBlank())
                System.out.printf("El nombre del evento '%s' no debe estar en espacio en blanco!%n", event);
            else if (!events.isEmpty() && events.stream().anyMatch(e -> e.getEvent().equals(event)))
                System.out.printf("El evento '%s' ya se encuentra registrado!%n", event);
            else {
                EventCompetitor eventCompetitor = new EventCompetitor(event);
                events.add(eventCompetitor);
                System.out.printf("El evento '%s' registrado exitosamente!%n", event);
            }
        }

        private static void registerCompetitor() {
            if (events.isEmpty()) {
                System.out.println("No hay eventos registrados. Por favor, registra uno primero!");
                return;
            }

            System.out.println("Indicar los datos del competidor a registrar.");
            System.out.print("nombre: ");
            String name = sc.nextLine().strip();
            System.out.print("país: ");
            String country = sc.nextLine().strip();
            Competitor competitor = new Competitor(name, country);

            System.out.println("Eventos deportivos disponibles:");
            AtomicInteger index = new AtomicInteger(0);
            events.forEach(e -> System.out.printf("%d. %s%n", index.incrementAndGet(), e.getEvent()));

            System.out.println("Selecciona el número del evento para asignar al participante: ");
            int eventIndex = Integer.parseInt(sc.nextLine()) - 1;

            if (eventIndex >= 0 && eventIndex < events.size()) {
                EventCompetitor eventCompetitor = events.get(eventIndex);
                String event = eventCompetitor.getEvent();
                List<Competitor> competitors = eventCompetitor.getCompetitors();

                competitors.stream().filter(c -> c.equals(competitor))
                        .findFirst()
                        .ifPresentOrElse(c -> System.out.printf("El participante '%s' de '%s' ya está registrado en el evento deportivo '%s'.%n",
                                        c.getName(), c.getCountry(), event),
                                () -> {
                                    if (countriesRank.stream().noneMatch(cr -> cr.getCountry().equals(country))) {
                                        countriesRank.add(new CountryRank(country));
                                    }
                                    competitors.add(competitor);
                                    System.out.printf("El participante '%s' de '%s' se ha registrado en el evento deportivo '%s'.%n",
                                            name, country, event);
                                });
            } else System.out.println("Selección de evento deportivo inválido. El participante no se ha registrado!");
        }

        private static void simulateEvents() {
            if (events.isEmpty()) {
                System.out.println("No hay eventos registrados. Por favor, registra uno primero!");
                return;
            }
            events.forEach(ec -> {
                List<Competitor> competitors = ec.getCompetitors();
                if (competitors.size() < 3)
                    System.out.printf("%nNo hay participantes suficientes para simular el evento '%s' (mínimo 3).%n", ec.getEvent());
                else {
                    Collections.shuffle(competitors);
                    List<Competitor> rankCompetitor = competitors.subList(0, 3);

                    updateRankingByCountries(competitors);

                    System.out.printf("%nResultados de la simulación del evento '%s':%n", ec.getEvent());

                    System.out.printf("Oro: %s%n", rankCompetitor.getFirst());
                    System.out.printf("Plata: %s%n", rankCompetitor.get(1));
                    System.out.printf("Bronce: %s%n", rankCompetitor.get(2));
                }
            });
        }

        private static void updateRankingByCountries(List<Competitor> competitors) {
            for (Competitor c : competitors) {
                String country = c.getCountry();
                int index = competitors.indexOf(c);
                switch (index) {
                    case 0 -> assignMedal(country, Medal.GOLD);
                    case 1 -> assignMedal(country, Medal.SILVER);
                    case 2 -> assignMedal(country, Medal.BRONZE);
                }
            }
        }

        private static void assignMedal(String country, Medal medal) {
            countriesRank.stream().filter(cr -> cr.getCountry().equals(country))
                    .findFirst()
                    .ifPresent(cr -> cr.getMedals().put(medal,
                            cr.getMedals().get(medal) + 1));
        }

        private static void displayWinners() {
            System.out.printf("%nReporte de ganadores por evento:%n");
            events.stream().filter(ec -> ec.getCompetitors().size() >= 3)
                    .forEach(EventCompetitor::printWinner);
            events.stream().filter(ec -> ec.getCompetitors().size() < 3)
                    .forEach(ec -> System.out.printf("No hay resultado de simulación del evento '%s' " +
                            "(mínimo 3 participantes).%n", ec.getEvent()));
        }

        private static void displayRankingByCountries() {
            System.out.printf("%nReporte de medallas (Oro, Plata, Bronce) obtenidas por país:%n");
            countriesRank.forEach(System.out::println);
        }

    }
}

/*
 * 1
 * Natacion
 * 1
 * Salto largo
 * 1
 * Salto alto
 * 1
 * 100 metros planos
 * 1
 * Lanzamiento de bala
 * 1
 * Lanzamiento de jabilina
 * 2
 * Martin
 * Peru
 * 1
 * 2
 * Martin
 * Peru
 * 2
 * 2
 * Martin
 * Peru
 * 3
 * 2
 * Martin
 * Peru
 * 4
 * 2
 * Martin
 * Peru
 * 5
 * 2
 * Kath
 * Colombia
 * 1
 * 2
 * Kath
 * Colombia
 * 2
 * 2
 * Kath
 * Colombia
 * 3
 * 2
 * Kath
 * Colombia
 * 4
 * 2
 * Kath
 * Colombia
 * 6
 * 2
 * Piero
 * Peru
 * 1
 * 2
 * Piero
 * Peru
 * 2
 * 2
 * Piero
 * Peru
 * 4
 * 2
 * Piero
 * Peru
 * 6
 * 2
 * Marshall
 * Canada
 * 1
 * 2
 * Marshall
 * Canada
 * 2
 * 2
 * Marshall
 * Canada
 * 3
 * 2
 * Marshall
 * Canada
 * 6
 * 2
 * Kendall
 * Chile
 * 2
 * 2
 * Kendall
 * Chile
 * 4
 * 2
 * Kendall
 * Chile
 * 5
 */