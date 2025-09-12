import net.datafaker.Faker;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Faker faker = new Faker(); // Generador de datos falsos

        AdministradorEventos admin = new AdministradorEventos();
        Evento atletismo100MM = new Evento("Atletismo 100 metros masculino");
        Evento atletismo100MF = new Evento("Atletismo 100 metros femenino");

        Participante p1 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p2 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p3 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p4 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p5 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p6 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p7 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p8 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p9 = new Participante(faker.name().fullName(), faker.address().country());
        Participante p10 = new Participante(faker.name().fullName(), faker.address().country());

        atletismo100MM.agregarParticipante(p1);
        atletismo100MM.agregarParticipante(p2);
        atletismo100MM.agregarParticipante(p3);
        atletismo100MM.agregarParticipante(p4);
        atletismo100MM.agregarParticipante(p5);
        atletismo100MM.agregarParticipante(p6);
        atletismo100MM.agregarParticipante(p7);

        atletismo100MF.agregarParticipante(p8);
        atletismo100MF.agregarParticipante(p9);
        atletismo100MF.agregarParticipante(p10);
        atletismo100MF.agregarParticipante(p1);
        atletismo100MF.agregarParticipante(p2);
        atletismo100MF.agregarParticipante(p3);
        atletismo100MF.agregarParticipante(p4);

        admin.agregarEvento(atletismo100MM);
        admin.agregarEvento(atletismo100MF);

        admin.iniciarEventos();
        admin.mostrarRankingGeneralEventos();
        admin.mostrarRankingPorPais();
    }

    static class AdministradorEventos {
        private List<Evento> eventos;

        public AdministradorEventos() {
            this.eventos = new LinkedList<>();
        }

        public void iniciarEventos() {
            this.eventos.forEach(Evento::iniciarEvento);
        }

        public void agregarEvento(Evento evento) {
            this.eventos.add(evento);
        }

        public void mostrarRankingGeneralEventos() {
            this.eventos.forEach(Evento::mostrarRanking);
        }

        public void mostrarRankingPorPais() {
            Map<String, Integer> ranking = new HashMap<>();
            this.eventos.forEach(e -> e.getRanking().forEach(p -> {
                if (ranking.containsKey(p.getPais())) ranking.put(p.getPais(), ranking.get(p.getPais()) + 1);
                else ranking.put(p.getPais(), 1);
            }));

            System.out.println("Ranking por país");
            ranking.forEach((k, v) -> System.out.println("Pais: " + k + " - Cantidad de medallas: " + v));
        }
    }

    static class Evento {
        private String nombre;
        private List<Participante> participantes;
        private List<Participante> ranking;
        private final Random r;

        public Evento(String nombre) {
            this.nombre = nombre;
            this.participantes = new LinkedList<>();
            this.ranking = new LinkedList<>();
            this.r = new Random();
        }

        public void agregarParticipante(Participante participante) {
            this.participantes.add(participante);
        }

        public void mostrarParticipantes() {
            this.participantes.forEach(p -> System.out.println("Nombre: " + p.getNombre() + " - País: " + p.getPais()));
        }

        public int cantidadParticipantes() {
            return this.participantes.size();
        }

        public void iniciarEvento() {
            System.out.println("Iniciando evento: " + this.nombre);

            while (this.ranking.size() != 3) {
                int index = r.nextInt(this.participantes.size());
                Participante p = this.participantes.get(index);
                if (!this.ranking.contains(p)) this.ranking.add(p);
            }

            System.out.println("Evento finalizado");
        }

        public void mostrarRanking() {
            System.out.println("Ranking del evento: " + this.nombre);
            System.out.println("1er lugar: " + this.ranking.get(0).getNombre() + " - País: " + this.ranking.get(0).getPais());
            System.out.println("2do lugar: " + this.ranking.get(1).getNombre() + " - País: " + this.ranking.get(1).getPais());
            System.out.println("3er lugar: " + this.ranking.get(2).getNombre() + " - País: " + this.ranking.get(2).getPais());
        }

        public String getNombre() {
            return nombre;
        }

        public List<Participante> getRanking() {
            return ranking;
        }
    }

    static class Participante {
        private String nombre;
        private String pais;

        public Participante(String nombre, String pais) {
            this.nombre = nombre;
            this.pais = pais;
        }

        public String getNombre() {
            return nombre;
        }

        public String getPais() {
            return pais;
        }
    }
}
