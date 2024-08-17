package com.amsoft.roadmap.example31;

import java.util.*;

public class Example31 {
    public static void main(String[] args) {
        System.out.println("""
                SIMULADOR JUEGOS OLÍMPICOS:
                --------------------------------------------------
                | 1. Registrar evento        | 4. Crear informes |
                | 2. Registrar participante  | 5. Salir          |
                | 3. Simulación de eventos   |                   |
                --------------------------------------------------        \s
                """);
        ManagerOlympic managerOlympic = new ManagerOlympic();
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.print("Ingresa el número de la opción:");
            String option = sc.nextLine();
            switch (option) {
                case "1":
                    System.out.print("Ingresa el nombre del evento:");
                    String event = sc.nextLine();
                    System.out.println(managerOlympic.addEvent(event));
                    break;
                case "2":
                    System.out.println("Registrar participante");
                    System.out.print("Ingresa el nombre del evento:");
                    String eventParticipant = sc.nextLine();
                    System.out.print("Ingresa el nombre del participante:");
                    String name = sc.nextLine();
                    System.out.print("Ingresa el país del participante:");
                    String country = sc.nextLine();
                    Participant participant = new Participant(name, country);
                    System.out.println(managerOlympic.registerParticipant(eventParticipant, participant));
                    break;
                case "3":
                    System.out.println("Simulación de eventos");
                    managerOlympic.simulateEvents();
                    break;
                case "4":
                    managerOlympic.createReports();
                    break;
                case "5":
                    System.out.println("Saliendo");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Saliendo");
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

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Participant that = (Participant) o;
        return Objects.equals(name, that.name) && Objects.equals(country, that.country);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, country);
    }
}

class ManagerOlympic {
    private final HashMap<String, List<Participant>> events;
    private final HashMap<String, List<Participant>> eventResults;

    ManagerOlympic() {
        this.events = new HashMap<>();
        this.eventResults = new HashMap<>();
    }

    public String addEvent(String eventName) {
        if (this.events.containsKey(eventName)) {
            return "El evento " + eventName + " ya está registrado";
        }
        List<Participant> participants = new ArrayList<>();
        this.events.put(eventName, participants);
        return "El evento " + eventName + " fué registrado correctamente";
    }

    public String registerParticipant(String eventName, Participant participant) {
        if (!this.events.containsKey(eventName)) {
            return "El evento " + eventName + " no está registrado aún, registralo!!";
        }
        List<Participant> participantsEvent = this.events.get(eventName);
        if (participantsEvent.contains(participant)) {
            return String.format(
                    "El participante %s de %s ya está registrado en el evento deportivo %s.",
                    participant.getName(),
                    participant.getCountry(),
                    eventName
            );
        }
        participantsEvent.add(participant);
        return String.format(
                "El participante %s de %s se ha registrado en el evento deportivo %s.",
                participant.getName(),
                participant.getCountry(),
                eventName
        );
    }

    public void simulateEvents() {
        if (this.events.isEmpty()) {
            System.out.println("No hay eventos para iniciar simulación, registra una!!");
            return;
        }
        this.events.forEach((event, participants) -> {
            if (participants.size() < 3) {
                System.out.println("No hay participantes suficientes para simular el evento " + event + " (mínimo 3)");
                return;
            }
            Random r = new Random();
            List<Participant> winners = new ArrayList<>();
            while (winners.size() < 3) {
                Participant winner = participants.get(r.nextInt(participants.size()));
                if (winners.contains(winner)) {
                    continue;
                }
                winners.add(winner);
            }
            this.eventResults.put(event, winners);
        });
        System.out.println("Simulación de eventos finalizada");
        System.out.println("Resultados:");
        this.eventResults.forEach((event, winners) -> {
            System.out.println("Evento: " + event);
            System.out.println("Ganadores:");
            String gold = winners.get(0).getName() + " de " + winners.get(0).getCountry();
            String silver = winners.get(1).getName() + " de " + winners.get(1).getCountry();
            String bronze = winners.get(2).getName() + " de " + winners.get(2).getCountry();
            System.out.println("Oro: " + gold);
            System.out.println("Plata: " + silver);
            System.out.println("Bronce: " + bronze);
        });

    }

    public void createReports() {
        System.out.println("INFORME JUEGOS OLÍMPICOS");
        System.out.println("------------------------");
        if (this.eventResults.isEmpty()) {
            System.out.println("No hay eventos para mostrar resultados");
            return;
        }
        System.out.println("Informe por eventos");
        System.out.println("-------------------");
        this.eventResults.forEach((event, winners) -> {
            System.out.println("Evento: " + event);
            System.out.println("Ganadores:");
            String gold = winners.get(0).getName() + " de " + winners.get(0).getCountry();
            String silver = winners.get(1).getName() + " de " + winners.get(1).getCountry();
            String bronze = winners.get(2).getName() + " de " + winners.get(2).getCountry();
            System.out.println("Oro: " + gold);
            System.out.println("Plata: " + silver);
            System.out.println("Bronce: " + bronze);
        });

        System.out.println("Informe por países");
        System.out.println("-------------------");
        HashMap<String, List<Integer>> rankingMedals = new HashMap<>();
        this.eventResults.forEach((event, winners) -> {
            var gold = winners.get(0).getCountry();
            var silver = winners.get(1).getCountry();
            var bronze = winners.get(2).getCountry();
            rankingMedals.putIfAbsent(gold, new ArrayList<>(Arrays.asList(0, 0, 0)));
            rankingMedals.putIfAbsent(silver, new ArrayList<>(Arrays.asList(0, 0, 0)));
            rankingMedals.putIfAbsent(bronze, new ArrayList<>(Arrays.asList(0, 0, 0)));
            rankingMedals.get(gold).set(0, rankingMedals.get(gold).getFirst() + 1);
            rankingMedals.get(silver).set(1, rankingMedals.get(silver).get(1) + 1);
            rankingMedals.get(bronze).set(2, rankingMedals.get(bronze).get(2) + 1);

        });
        System.out.println("Ranking de medallas");
        rankingMedals.entrySet()
                .stream()
                .sorted((e1, e2) -> {
                    int compareGold = e2.getValue().get(0) - e1.getValue().get(0); // Oro
                    if (compareGold != 0) return compareGold;
                    int compareSilver = e2.getValue().get(1) - e1.getValue().get(1); // Plata
                    if (compareSilver != 0) return compareSilver;
                    return e2.getValue().get(2) - e1.getValue().get(2); // Bronce
                })
                .forEach(entry -> {
                    System.out.println("País: " + entry.getKey());
                    String result = String.format("Oro: %d, Plata: %d, Bronce: %d",
                            entry.getValue().get(0),
                            entry.getValue().get(1),
                            entry.getValue().get(2));
                    System.out.println(result);
                });


    }


}
