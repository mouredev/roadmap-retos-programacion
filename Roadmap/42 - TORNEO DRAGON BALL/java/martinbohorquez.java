import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

public class martinbohorquez {
    public static void main(String[] args) throws InterruptedException {
        // 1. Mostrar luchadores a participar
        List<Figther> figthers = createFigthers();
        System.out.println("Los participan en el torneo de 'Dragon Ball: Sparking! ZERO!' son:");
        figthers.forEach(System.out::println);

        // 2. Simular torneo
        simulateTournament(figthers);
    }

    private static void simulateTournament(List<Figther> figthers) throws InterruptedException {
        printTittle("Torneo Dragon Ball: Sparking! ZERO");
        int rounds = (int) (Math.log(figthers.size())/Math.log(2));
        for (int i = 1; i <= rounds; i++) {
            if (i == rounds) printTittle("Ronda Final");
            else printTittle("Ronda número " + i);
            figthers = figthers.stream().filter(figther -> figther.getHealth().equals(100))
                    .collect(Collectors.toList());
            Collections.shuffle(figthers);
            for (int j = 0; j < figthers.size() / 2; j++) {
                Figther winner = battle(figthers.get(j), figthers.get(figthers.size() - 1 - j));
                winner.setHealth(100);
                System.out.printf("🌟 %s ha ganado la batalla!%n", winner.getName());
                if (i == rounds) printTittle("👑 " + winner.getName() + " es el ganador del torneo Dragon Ball: Sparking! ZERO!");
            }
        }
    }

    private static Figther battle(Figther f1, Figther f2) throws InterruptedException {
        printSubtitle(f1.getName().toUpperCase() + " 🆚 " + f2.getName().toUpperCase());
        Figther fa = f1.getSpeed() > f2.getSpeed()? f1: f2;
        Figther fb = fa == f1? f2: f1;
        System.out.printf("🏁 %s da el primer ataque.%n", fa.getName());
        int turn = 0;
        while (f1.getHealth() > 0 && f2.getHealth() > 0) {
            System.out.printf("▶️ Turno %s:%n", ++turn);
            if (fa.attack(fb)) break;
            if (fb.attack(fa)) break;
            TimeUnit.SECONDS.sleep(1);
        }
        return fb.getHealth().equals(0)? fa: fb;
    }

    private static void printTittle(String tittle) {
        int length = tittle.length();
        String blankSpaces = " ".repeat(Math.max(20 - length / 2, 0));
        System.out.println("\n" + blankSpaces + "╔" + "═".repeat(length + 2) + "╗");
        System.out.println(blankSpaces + "║ " + tittle + " ║");
        System.out.println(blankSpaces + "╚" + "═".repeat(length + 2) + "╝");
    }

    private static void printSubtitle(String subtitle) {
        int length = subtitle.length();
        System.out.println("╔" + "═".repeat(length + 2) + "╗");
        System.out.println("║ " + subtitle + " ║");
        System.out.println("╚" + "═".repeat(length + 2) + "╝");
    }

    private static List<Figther> createFigthers(){
        return new ArrayList<>(List.of(
            new Figther("Goku", 90, 95, 80),
            new Figther("Vegeta", 85, 100, 75),
            new Figther("Gohan", 80, 90, 70),
            new Figther("Frieza", 70, 85, 60),
            new Figther("Cell", 75, 88, 65),
            new Figther("Piccolo", 60, 80, 70),
            new Figther("Krillin", 65, 70, 60),
            new Figther("Majin Buu", 55, 75, 85)));
    }

    private static class Figther {
        private Integer id;
        private String name;
        private Integer speed;
        private Integer attack;
        private Integer defense;
        private Integer health;
        private static Integer count = 0;

        public Figther(String name, Integer speed, Integer attack, Integer defense) {
            this.id = ++count;
            this.name = name;
            this.speed = speed;
            this.attack = attack;
            this.defense = defense;
            this.health = 100;
        }

        public Integer getId() {
            return id;
        }

        public void setId(Integer id) {
            this.id = id;
        }

        public String getName() {
            return name;
        }

        public Integer getSpeed() {
            return speed;
        }

        public Integer getAttack() {
            return attack;
        }

        public Integer getDefense() {
            return defense;
        }

        public Integer getHealth() {
            return health;
        }

        public void setHealth(Integer health) {
            this.health = health;
        }

        public void decreseHealth(Integer damage) {
            this.health = Math.max(health - damage, 0);
        }

        public boolean attack(Figther f) {
            int damage = f.getDefense() > this.getAttack()
                    ? (int) (this.getAttack() * 0.1): this.getAttack() - f.getDefense();
            System.out.printf("⚔️ %s ataca a %s con una daño de %d.%n", this.name, f.name, damage);

            if (Math.random() < 0.2) System.out.printf("🌀 %s esquivó el ataque.%n", f.getName());
            else {
                f.decreseHealth(damage);
                System.out.printf("❤️ Salud de %s se reduce a %d.%n", f.name, f.getHealth());
            }
            return f.getHealth().equals(0);
        }

        @Override
        public String toString() {
            return "id: " + id + ", {name: '" + name + "', speed: " + speed + ", attack: " + attack
                    + ", defense: " + defense + ", health: " + health + "}";
        }
    }
}