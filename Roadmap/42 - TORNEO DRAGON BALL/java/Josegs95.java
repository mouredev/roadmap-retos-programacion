import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().DragonBallTournament();
    }

    private double delay = 1;

    public void DragonBallTournament(){
        List<Fighter> participantList = getFighters();

        if (!checkParticipantCount(participantList.size())){
            System.out.println("No se puede empezar el torneo porque no hay suficientes participantes");
            return;
        }
        System.out.print("Introduzca el delay para las peleas (en segundos): ");
        delay = Double.parseDouble(new Scanner(System.in).nextLine());

        System.out.println("¡¡ Comienza el torneo de artes marciales !!");
        System.out.println();

        Fighter winner = tournament(new ArrayList<>(participantList));

        System.out.println("\n");
        System.out.println("¡¡" + winner.getNAME() + " ha ganado el torneo de artes marciales!!");
    }

    private Fighter tournament(ArrayList<Fighter> participants){
        int nParticipants = participants.size();
        switch (nParticipants){
            case 2:
                System.out.println("¡ Empieza la final !");
                break;
            case 4:
                System.out.println("¡ Empieza las semifinales !");
                break;
            case 8:
                System.out.println("¡ Empieza los cuartos de final !");
                break;
            case 16:
                System.out.println("¡ Empieza los octavos de final !");
                break;
            default:
                System.out.println("¡ Empieza la ronda de " + nParticipants + " !");
                break;
        }
        Collections.shuffle(participants);
        System.out.print("COMBATES: ");
        for (int i = 0; i < nParticipants; i += 2){
            System.out.print("[" + participants.get(i).getNAME() + " vs " + participants.get(i + 1).getNAME() + "] ");
        }
        System.out.println();

        System.out.println("Pulse INTRO para continuar la simulación");
        new Scanner(System.in).nextLine();

        List<Fighter> loserList = new ArrayList<>();
        for (int i = 0; i < nParticipants; i += 2){
            battle(participants.get(i), participants.get(i + 1), loserList);
            System.out.println();
        }

        participants.removeAll(loserList);

        if (participants.size() == 1)
            return participants.get(0);
        else
            return tournament(participants);
    }

    private void battle (Fighter fighter1, Fighter fighter2, List<Fighter> loserList){
        Fighter first, last;
        if (fighter1.getSPD() > fighter2.getSPD()) {
            first = fighter1;
            last = fighter2;
        } else if (fighter1.getSPD() < fighter2.getSPD()) {
            first = fighter2;
            last = fighter1;
        } else {
            first = Math.random() < 0.5 ? fighter1 : fighter2;
            last = first == fighter1 ? fighter2 : fighter1;
        }

        try {
            int round = 1;
            while(first.isAlive()){
                System.out.print("Ronda " + round++ + ". ");
                System.out.print(first.getNAME() + "(" + first.getHp() + "/100) ");
                System.out.println(last.getNAME() + "(" + last.getHp() + "/100)");

                attack(first, last);
                if (!last.isAlive())
                    break;
                attack(last, first);

                if (round < 20)
                    Thread.sleep((long) (delay * 1000));
                System.out.println();
            }
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }


        if (first.isAlive()) {
            System.out.println(first.getNAME() + " ha ganado el combate.");
            first.heal();
            loserList.add(last);
        } else {
            System.out.println(last.getNAME() + " ha ganado el combate.");
            last.heal();
            loserList.add(first);
        }
    }

    private void attack(Fighter attacker, Fighter defender){
        if (Math.random() < 0.2){
            System.out.println(defender.getNAME() + " ha esquivado el ataque de " + attacker.getNAME());
            return;
        }

        int attackerATK = attacker.getATK();
        int defenderDEF = defender.getDEF();
        double damageDealt = Math.max(attackerATK - defenderDEF, 10);

        if (attackerATK < defenderDEF)
            damageDealt *= 0.1;

        defender.takeDamage(damageDealt);
        System.out.println(attacker.getNAME() + " ha hecho " + damageDealt + " puntos de daño a "
                + defender.getNAME());
    }

    private boolean checkParticipantCount(int nParticipants){
        for (int i = 1, participantLimit; (participantLimit = (int) Math.pow(2, i)) <= nParticipants; i++){
            if (participantLimit == nParticipants)
                return true;
        }

        return false;
    }

    private List<Fighter> getFighters(){
        Fighter goku = new Fighter("Goku", 80, 50, 60);
        Fighter vegeta = new Fighter("Vegeta", 70, 60, 55);
        Fighter piccolo = new Fighter("Piccolo");
        Fighter gohan = new Fighter("Gohan");
        Fighter krilin = new Fighter("Krilin");
        Fighter yamcha = new Fighter("Yamcha");
        Fighter tien = new Fighter("Tien");
        Fighter jackie = new Fighter("Jackie Chun");

        return Arrays.asList(goku, vegeta, piccolo, gohan,
                krilin, yamcha, tien, jackie);
    }

    public class Fighter{
        final private String NAME;
        final private int ATK;
        final private int DEF;
        final private int SPD;
        private int hp = 100;

        public Fighter(String name, int attack, int defense, int speed) {
            this.NAME = name;
            this.ATK = attack;
            this.DEF = defense;
            this.SPD = speed;
        }
        
        public Fighter(String name){
            this.NAME = name;
            Random rnd = new Random();
            ATK = rnd.nextInt(0, 101);
            DEF = rnd.nextInt(0, 101);
            SPD = rnd.nextInt(0, 101);
        }

        public void takeDamage(double amount){
            hp -= amount;
            hp = (hp < 0) ? 0 : hp;
        }

        public void heal(){
            hp = 100;
        }

        public boolean isAlive(){
            return hp > 0;
        }

        public String getNAME() {
            return NAME;
        }

        public int getATK() {
            return ATK;
        }

        public int getDEF() {
            return DEF;
        }

        public int getSPD() {
            return SPD;
        }

        public int getHp() {
            return hp;
        }
    }
}
