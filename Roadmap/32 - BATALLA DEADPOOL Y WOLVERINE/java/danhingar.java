import java.util.Random;

public class danhingar {

    public static void main(String[] args) throws InterruptedException {
        Player deepool = new Player(1000, 100, "Deadpool");
        Player wolverine = new Player(1000, 120, "Wolverine");
        Battle battle = new Battle(deepool, wolverine);
        battle.init();
    }

}

class Player {
    private String name;
    private Integer health;
    private Integer maxDamage;

    public Player(Integer health, Integer maxDamage, String name) {
        this.health = health;
        this.maxDamage = maxDamage;
        this.name = name;
    }

    public Integer getHealth() {
        return health;
    }

    public void setHealth(Integer health) {
        this.health = health;
    }

    public Integer getMaxDamage() {
        return maxDamage;
    }

    public void setMaxDamage(Integer maxDamage) {
        this.maxDamage = maxDamage;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer damage() {
        Random random = new Random();

        int min = 10;
        int max = this.maxDamage;

        return random.nextInt(max - min + 1) + min;
    }

}

class Battle {

    private Player player1;
    private Player player2;

    public Battle(Player player1, Player player2) {
        this.player1 = player1;
        this.player2 = player2;
    }

    public void init() throws InterruptedException {
        int shiftNumber = 1;
        Integer attackDeepool = 0;
        Integer attackWolverine = 0;
        Boolean regenerate = Boolean.FALSE;
        while (player1.getHealth() > 0 && player2.getHealth() > 0) {
            System.out.println("\nTurno " + shiftNumber);
            Double preventAttackWolverine = Math.random();
            if (regenerate) {
                System.out.println("Deadpool se está regenerando y no ataca.");
                regenerate = Boolean.FALSE;
            } else if (preventAttackWolverine > 0.2) {
                attackDeepool = attack(player1, player2);
                System.out.printf("%s ataca a %s con %d puntos de daño.\n", player1.getName(), player2.getName(),
                        attackDeepool);
                if (attackDeepool == 100) {
                    System.out.printf(
                            "¡Golpe crítico de %s! %s no atacará en el siguiente turno ya que tiene que regenerarse.\n",
                            player1.getName(), player2.getName());
                    regenerate = Boolean.TRUE;
                }

                if (player2.getHealth() <= 0) {
                    System.out.printf("La vida de %s ha llegado a cero.\n", player2.getName());
                    break;
                }
                System.out.printf("Vida restante de %s: %d\n", player2.getName(), player2.getHealth());

            } else {
                System.out.printf("¡%s esquiva el ataque de %s!\n", player2.getName(), player1.getName());
            }

            Double preventAttackDeepool = Math.random();
            if (regenerate) {
                System.out.println("Wolverine se está regenerando y no ataca.");
                regenerate = Boolean.FALSE;
            } else if (preventAttackDeepool > 0.25) {
                attackWolverine = attack(player2, player1);
                if (attackDeepool == 120) {
                    System.out.printf(
                            "¡Golpe crítico %s! %s no atacará en el siguiente turno ya que tiene que regenerarse.\n",
                            player2.getName(), player1.getName());
                    regenerate = Boolean.TRUE;
                }
                System.out.printf("%s ataca a %s con %d puntos de daño.\n", player2.getName(), player1.getName(),
                        attackWolverine);
                if (player1.getHealth() <= 0) {
                    System.out.printf("La vida de %s ha llegado a cero.\n", player1.getName());
                    break;
                }
                System.out.printf("Vida restante de %s: %d\n", player1.getName(), player1.getHealth());

            } else {
                System.out.printf("¡%s esquiva el ataque de %s!\n", player1.getName(), player2.getName());
            }
            shiftNumber++;
            Thread.sleep(1000);
        }
        finish(player1, player2);
    }

    public void turn(Player player1, Player Player2, Boolean regenerate) {

    }

    public Integer attack(Player attacker, Player defender) {
        Integer damage = attacker.damage();
        Integer newHealth = defender.getHealth() - damage;
        defender.setHealth(newHealth);
        return damage;
    }

    public void finish(Player player1, Player player2) {
        if (player1.getHealth() < 0) {
            System.out.printf("%s ha ganado la batalla!!!.\n", player2.getName());
        } else {
            System.out.printf("%s ha ganado la batalla!!!.\n", player1.getName());
        }
    }

}
