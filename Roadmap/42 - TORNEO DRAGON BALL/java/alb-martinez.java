import java.util.*;

public class AlbMartinez {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Fighter> fighters = createFighters();

        while (true) {
            showMenu();
            int choice = -1;

            try {
                choice = scanner.nextInt();
                scanner.nextLine();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input! Please enter a valid number");
                scanner.nextLine();
                continue;
            }

            switch (choice) {
                case 1 -> listFighters(fighters);
                case 2 -> startTournament(fighters);
                case 3 -> {
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                }
                default -> System.out.println("Invalid option. Please try again.");
            }
        }
    }

    private static List<Fighter> createFighters() {
        List<Fighter> fighters = new ArrayList<>();
        fighters.add(new Fighter("Goku", 90, 95, 80));
        fighters.add(new Fighter("Vegeta", 85, 100, 75));
        fighters.add(new Fighter("Gohan", 80, 90, 70));
        fighters.add(new Fighter("Frieza", 70, 85, 60));
        fighters.add(new Fighter("Cell", 75, 88, 65));
        fighters.add(new Fighter("Piccolo", 60, 80, 70));
        fighters.add(new Fighter("Krillin", 65, 70, 60));
        fighters.add(new Fighter("Majin Buu", 55, 75, 85));
        return fighters;
    }

    private static void showMenu() {
        System.out.println("--- Dragon Ball Tournament Menu ---");
        System.out.println("1. List Fighters");
        System.out.println("2. Start Tournament");
        System.out.println("3. Exit");
        System.out.println("Choose an option: ");
    }

    private static void addFighter(Scanner scaner, List<Fighter> fighters) {
        System.out.println("Enter fighter name: ");
        String name = scaner.nextLine();

        System.out.println("Enter speed (0-100): ");
        int speed = getValidInput(scaner);

        System.out.println("Enter attack (0-100): ");
        int attack = getValidInput(scaner);

        System.out.println("Enter defense (0-100): ");
        int defense = getValidInput(scaner);

        fighters.add(new Fighter(name, speed, attack, defense));
        System.out.println(name + " has been added.");
    }

    private static int getValidInput(Scanner scanner) {
        int value;
        while (true) {
            value = scanner.nextInt();
            if (value >= 0 && value <= 100) {
                break;
            } else {
                System.out.println("Please enter a value between 0 and 100");
            }
        }
        scanner.nextLine();
        return value;
    }

    private static void listFighters(List<Fighter> fighters) {
        System.out.println("--- Fighters List ---");
        for (Fighter figther : fighters) {
            System.out.println("Name " + figther.name + ", Speed: " + figther.speed +
                    ", Attack: " + figther.attack + ", Defense: " + figther.defense +
                    ", Health: " + figther.health);
        }
    }

    private static void startTournament(List<Fighter> fighters) {
        if (fighters.size() == 0 || (fighters.size() & (fighters.size() - 1)) != 0) {
            System.out.println("Number of fighters must be a power of 2!");
            return;
        }
        List<Fighter> roundWinners = new ArrayList<>();
        int round = 1;

        while (fighters.size() > 1) {
            System.out.println("\n=== 🥋 Round " + round + " 🥋 ===");
            System.out.println("Fighters in this round: " + fighters.size() + "\n");

            for (int i = 0; i < fighters.size(); i += 2) {
                Fighter fighter1 = fighters.get(i);
                Fighter fighter2 = fighters.get(i + 1);

                System.out.println(">>> Battle " + ((i / 2) + 1) + ": " + fighter1.name + " 🆚 " + fighter2.name);
                battle(fighter1, fighter2);

                // Determinar el ganador
                roundWinners.add(fighter1.health > 0 ? fighter1 : fighter2);

                fighter1.resetHealth();
                fighter2.resetHealth();
            }
            fighters = roundWinners;
            roundWinners = new ArrayList<>();
            round++;
        }

        System.out.println("\n🏆 The champion of the tournament is: " + fighters.get(0).name + "! 🏆");

        System.exit(0);
    }

    public static void battle(Fighter fighter1, Fighter fighter2) {
        Fighter attacker = fighter1.speed >= fighter2.speed ? fighter1 : fighter2;
        Fighter defender = attacker == fighter1 ? fighter2 : fighter1;

        System.out.println("🔽 " + attacker.name + " starts attacking.");

        while (fighter1.health > 0 && fighter2.health > 0) {
            // Verificar si el defensor esquiva
            if (Math.random() < 0.2) {
                System.out.println("💨 " + defender.name + " dodged the attack!");
            } else {
                int damage;

                // Calcular daño según la defensa y el ataque
                if (defender.defense > attacker.attack) {
                    // Defensa mayor que ataque, recibe 10% del daño de ataque
                    damage = (int) (attacker.attack * 0.1);
                } else {
                    // Daño normal
                    damage = attacker.attack - defender.defense;
                    damage = Math.max(damage, 0); // Asegurarse de que no sea negativo
                }

                defender.health -= damage;

                if (defender.health < 0) {
                    defender.health = 0;
                }

                System.out.println("⚔️ " + attacker.name + " attacks " + defender.name + " for " + damage + " damage.");
                System.out.println("❤️ " + defender.name + "'s health is now " + defender.health);
            }

            // Cambiar turno
            Fighter temp = attacker;
            attacker = defender;
            defender = temp;
        }

        if (fighter1.health <= 0) {
            System.out.println("🎉 " + fighter2.name + " wins the battle!\n");
        } else {
            System.out.println("🎉 " + fighter1.name + " wins the battle!\n");
        }
    }

    static class Fighter {
        String name;
        int speed;
        int attack;
        int defense;
        int health;
        int initialHealth;

        public Fighter(String name, int speed, int attack, int defense) {
            this.name = name;
            this.speed = speed;
            this.attack = attack;
            this.defense = defense;
            this.health = 100;
            this.initialHealth = 100;
        }

        public void resetHealth() {
            this.health = this.initialHealth;
        }

    }
}
