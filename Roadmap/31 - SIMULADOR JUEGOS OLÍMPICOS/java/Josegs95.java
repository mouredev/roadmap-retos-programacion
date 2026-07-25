import java.util.*;

public class Josegs95 {

    final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        new Josegs95().olympics();
    }

    public void olympics(){
        try(sc){
            Olympics olympics = new Olympics();
            app: while(true){
                String option = askOption();
                switch (option){
                    case "1":
                        olympics.registerEvent();
                        break;
                    case "2":
                        olympics.registerParticipant();
                       break;
                    case "3":
                        olympics.simulateEvent();
                        break;
                    case "4":
                        olympics.logCreation();
                        break;
                    case "5":;
                        break app;
                    default:
                        System.out.println("Opción incorrecta. Introduzca el número de la opción deseada");
                }
            }
            System.out.println("Terminando la aplicación. Gracias por usarla.");
        }
    }

    public enum Option{
        REG_EVENT("Registro de eventos"),
        REG_PARTICIPANT("Registro de participantes"),
        SIM_EVENT("Simulación de eventos"),
        LOG_CREATION("Creación de informes"),
        EXIT("Salir del programa");

        private String name;

        Option(String name){
            this.name = name;
        }

        @Override
        public String toString() {
            return name;
        }
    }

    private String askOption(){
        showOptions();
        System.out.print("Introduzca la opción deseada: ");
        return sc.nextLine();
    }

    private void showOptions(){
        System.out.println();
        System.out.println("---Opciones---");
        for (int i = 0; i < Option.values().length; i++)
            System.out.println((i + 1) + ". " + Option.values()[i]);
        System.out.println("--------------");
    }

    public class Olympics{
        private List<Event> eventList;
        private List<Event> activeEventList;
        private List<Nation> nationList;

        Olympics(){
            eventList = new ArrayList<>();
            activeEventList = new ArrayList<>();
            nationList = new ArrayList<>();
        }

        public void registerEvent(){
            System.out.print("Introduzca el nombre del evento: ");
            String name = sc.nextLine().strip();
            Event event = new Event(name);

            if (activeEventList.contains(event))
                System.out.println("El evento " + name + " ya existe");
            else{
                activeEventList.add(event);
                eventList.add(event);
                System.out.println("Evento " + name + " registrado correctamente");
            }

        }

        public void registerParticipant(){
            if (activeEventList.isEmpty()){
                System.out.println("No hay ningún evento activo para incribir a ningún participante");
                return;
            }

            System.out.print("Introduzca el nombre del participante: ");
            String name = sc.nextLine().strip();
            System.out.print("Introduzca la nacionalidad del participante: ");
            String nationality = sc.nextLine().strip();
            Nation nation = addNationtoList(nationality);
            Participant participant = new Participant(name, nation);

            Event event = askEvent();

            if (event.addParticipant(participant))
                System.out.println(name + " registrado correctamente");
            else
                System.out.println(name + " ya estaba registrado");
        }

        public void simulateEvent(){
            if (activeEventList.isEmpty()){
                System.out.println("No hay ningún evento activo para incribir a ningún participante");
                return;
            }

            Event event = askEvent();
            if (event.countParticipants() < 3){
                System.out.println("Solo se puede simular un evento si tiene mas de 3 participantes");
                return;
            }

            Random rnd = new Random();
            List<Participant> aux = new ArrayList<>(event.getParticipantList());
            Participant goldParticipant = aux.remove(rnd.nextInt(aux.size()));
            Participant silverParticipant = aux.remove(rnd.nextInt(aux.size()));
            Participant bronzeParticipant = aux.remove(rnd.nextInt(aux.size()));

            event.setGold(goldParticipant);
            event.setSilver(silverParticipant);
            event.setBronze(bronzeParticipant);
            goldParticipant.getNationality().addGoldMedal();
            silverParticipant.getNationality().addSilverMedal();
            bronzeParticipant.getNationality().addBronzeMedal();

            System.out.println("Evento: " + event);
            System.out.println("Oro: " + goldParticipant);
            System.out.println("Plata: " + silverParticipant);
            System.out.println("Bronce: " + bronzeParticipant);

            activeEventList.remove(event);
        }

        public void logCreation(){
            if (nationList.isEmpty()){
                System.out.println("No hay naciones registradas aún");
                return;
            }

            System.out.println();
            System.out.println("Ranking de naciones:");
            Collections.sort(nationList, Collections.reverseOrder());
            for (Nation nation : nationList)
                System.out.println(nation.getNationInfo());

            System.out.println();
            List<Event> aux = new ArrayList<>(eventList);
            aux.removeAll(activeEventList);
            for (Event event : aux){
                System.out.println(event + "-> Oro: " + event.getGold() + ", Plata: "
                    + event.getSilver() + ", Bronce: " + event.getBronze());
            }

        }

        private void showEvents(){
            System.out.println();
            System.out.println("---Eventos---");
            for (int i = 0; i < activeEventList.size(); i++){
                System.out.println((i + 1) + ". " + activeEventList.get(i));
            }
            System.out.println("-------------");
        }

        private Event askEvent(){
            showEvents();
            boolean validOption = false;
            int option = -1;
            do{
                System.out.print("Seleccione a qué evento quiere registrarlo: ");
                try{
                    option = Integer.parseInt(sc.nextLine()) - 1;
                    if (option < 0 || option >= activeEventList.size())
                        System.out.println("Opción inválida. Hay " + activeEventList.size() + " eventos disponibles.");
                    else
                        validOption = true;
                } catch (NumberFormatException e){
                    System.out.println("Opción inválida. Debe escribir un número");
                }
            }while(!validOption);

            return activeEventList.get(option);
        }

        private Nation addNationtoList(String name){
            for(Nation nation : nationList){
                if (nation.getName().toLowerCase().equals(name.toLowerCase()))
                    return nation;
            }

            Nation nation = new Nation(name);
            nationList.add(nation);
            return nation;
        }
    }

    public class Event{
        private String name;
        private List<Participant> participantList;
        private Participant gold = null;
        private Participant silver = null;
        private Participant bronze = null;

        Event(String name){
            this.name = name;
            participantList = new ArrayList<>();
        }

        public boolean addParticipant(Participant participant){
            return participantList.add(participant);
        }

        public int countParticipants(){
            return participantList.size();
        }

        public List<Participant> getParticipantList() {
            return participantList;
        }

        public Participant getGold() {
            return gold;
        }

        public Participant getSilver() {
            return silver;
        }

        public Participant getBronze() {
            return bronze;
        }

        public void setGold(Participant gold) {
            this.gold = gold;
        }

        public void setSilver(Participant silver) {
            this.silver = silver;
        }

        public void setBronze(Participant bronze) {
            this.bronze = bronze;
        }

        @Override
        public String toString() {
            return name;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Event event)) return false;
            return Objects.equals(name, event.name);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, participantList);
        }
    }

    public class Participant{
        private String name;
        private Nation nationality;

        public Participant(String name, Nation nationality) {
            this.name = name;
            this.nationality = nationality;
        }

        public String getName() {
            return name;
        }

        public Nation getNationality() {
            return nationality;
        }

        @Override
        public String toString() {
            return name + "(" + nationality + ")";
        }
    }

    public class Nation implements Comparable<Nation>{
        private String name;
        private int nGold = 0;
        private int nSilver = 0;
        private int nBronze = 0;

        private int medalValue = 0;

        Nation(String name){
            this.name = name;
        }

        public void addGoldMedal(){
            nGold++;
            medalValue += 4;
        }
        public void addSilverMedal(){
            nSilver++;
            medalValue += 2;
        }
        public void addBronzeMedal(){
            nBronze++;
            medalValue += 1;
        }

        public int getMedalValue(){
            return medalValue;
        }

        public String getName() {
            return name;
        }

        public String getNationInfo(){
            return name + ": " + nGold + " oros, " + nSilver
                    + " platas, " + nBronze + " bronces";
        }

        @Override
        public String toString() {
            return name;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Nation nation)) return false;
            return Objects.equals(name, nation.name);
        }

        @Override
        public int hashCode() {
            return Objects.hashCode(name);
        }

        @Override
        public int compareTo(Nation nation) {
            return this.medalValue - nation.getMedalValue();
        }
    }
}
