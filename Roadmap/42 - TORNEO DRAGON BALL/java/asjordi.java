import java.util.*;

public class asjordi {

    private static final Random r = new Random();

    public static void main(String[] args) {
        Tournament tournament = new Tournament(
                new Fighter("Goku"), new Fighter("Vegeta"), new Fighter("Gohan"), new Fighter("Trunks"),
                new Fighter("Goten"), new Fighter("Picoro"), new Fighter("Krilin"), new Fighter("Yamcha"),
                new Fighter("Cell"), new Fighter("Freezer"), new Fighter("Buu"), new Fighter("Jiren"),
                new Fighter("Broly"), new Fighter("Kale"), new Fighter("Caulifla"), new Fighter("Hit")
        );

        var winner = tournament.start();
        System.out.println("Champion: " + winner.getName());
    }

    static class Tournament {

        private List<Fighter> fighters;

        public Tournament(Fighter... fighters) {
            if (!isAPowerOfTwo(fighters.length)) {
                throw new IllegalArgumentException("The number of fighters must be a power of two");
            }
            this.fighters = Arrays.asList(fighters);
            Collections.shuffle(this.fighters);
        }

        public Fighter start() {
            while (fighters.size() > 1) {
                fighters = startRound();
            }
            return fighters.get(0);
        }

        public List<Fighter> startRound() {
            var winners = new ArrayList<Fighter>();

            for (int i = 0; i < fighters.size(); i += 2) {
                var fighter1 = fighters.get(i);
                var fighter2 = fighters.get(i + 1);
                System.out.println("Fight: " + fighter1.getName() + " vs " + fighter2.getName());
                var battle = new Battle(fighter1, fighter2);
                var winner = battle.startRound();
                System.out.println("Winner of the fight: " + winner.getName());
                winners.add(winner);
            }

            return winners;
        }

        public void showFighters() {
            fighters.forEach(f -> System.out.println(f.getName()));
        }

        private boolean isAPowerOfTwo(int numero) {
            return numero > 0 && (numero & (numero - 1)) == 0;
        }

    }

    static class Battle {
        private Fighter fighter1;
        private Fighter fighter2;

        public Battle(Fighter fighter1, Fighter fighter2) {
            this.fighter1 = fighter1.getSpeed() > fighter2.getSpeed() ? fighter1 : fighter2;
            this.fighter2 = fighter1.getSpeed() > fighter2.getSpeed() ? fighter2 : fighter1;
        }

        public Fighter startRound() {
            Fighter winner = null;

            while (winner == null) {
                fight(fighter1, fighter2);
                if (fighter2.getHealth() <= 0) winner = fighter1;

                fight(fighter2, fighter1);
                if (fighter1.getHealth() <= 0) winner = fighter2;
            }

            return winner;
        }

        public void fight(Fighter a, Fighter b) {
            var damage = Math.abs(a.getAttack() - b.getDefense());

            if (getProbabilitySkipAttack() < 0.2) {
                System.out.println(b.getName() + " skip attack");
                return;
            }

            if (b.getDefense() > a.getAttack()) {
                damage = damage * 0.1;
            }

            b.setHealth(b.getHealth() - damage);
            System.out.println(a.getName() + " attack " + b.getName() + " with " + damage + " damage");
        }

        private double getProbabilitySkipAttack() {
            return r.nextDouble(0, 1);
        }
    }

    static class Fighter {
        private final String name;
        private double health;
        private double speed;
        private double attack;
        private double defense;

        public Fighter(String name) {
            this.name = name;
            this.health = 100;
            this.speed = getValue();
            this.attack = getValue();
            this.defense = getValue();
        }

        private double getValue() {
            return r.nextInt(50, 101);
        }

        public String getName() {
            return name;
        }

        public double getHealth() {
            return health;
        }

        public void setHealth(double health) {
            this.health = health;
        }

        public double getSpeed() {
            return speed;
        }

        public double getAttack() {
            return attack;
        }

        public double getDefense() {
            return defense;
        }
    }
}
