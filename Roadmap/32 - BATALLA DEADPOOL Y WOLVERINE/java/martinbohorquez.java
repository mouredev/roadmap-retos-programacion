import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class martinbohorquez {
    static Random random = new Random();

    public static void main(String[] args) throws InterruptedException {
        Hero deadpool = new Hero("Deadpool");
        Hero wolverine = new Hero("Wolverine");
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresar la vida de Deadpool (número de 1 a 1000):");
        deadpool.setHealth(Integer.parseInt(sc.nextLine()));
        deadpool.setMinDamage(10);
        deadpool.setMaxDamage(100);
        deadpool.setEvasionRate(0.25f);

        System.out.println("Ingresar la vida de Wolverine (número de 1 a 1000):");
        wolverine.setHealth(Integer.parseInt(sc.nextLine()));
        wolverine.setMinDamage(10);
        wolverine.setMaxDamage(120);
        wolverine.setEvasionRate(0.2f);

        int turn = 0;

        while (deadpool.getHealth() > 0 && wolverine.getHealth() > 0) {
            System.out.printf("%nTurno %s:%n", ++turn);
            if (deadpool.attack(wolverine)) break;
            if (wolverine.attack(deadpool)) break;
            TimeUnit.SECONDS.sleep(1);
        }

        if (deadpool.getHealth() > 0)
            System.out.printf("Deadpool gana la batalla con %s de vida restante!%n", deadpool.getHealth());
        else System.out.printf("Wolverine gana la batalla con %s de vida restante!%n", wolverine.getHealth());
    }

    static class Hero {
        private String name;
        private int health;
        private int minDamage;
        private int maxDamage;
        private float evasionRate;
        private boolean regenerate;

        public Hero(String name) {
            this.name = name;
            regenerate = false;
        }

        public String getName() {
            return name;
        }

        public boolean isRegenerate() {
            return regenerate;
        }

        public void setRegenerate(boolean regenerate) {
            this.regenerate = regenerate;
        }

        public int getHealth() {
            return health;
        }

        public void setHealth(int health) {
            this.health = health;
        }

        public int getMinDamage() {
            return minDamage;
        }

        public void setMinDamage(int minDamage) {
            this.minDamage = minDamage;
        }

        public int getMaxDamage() {
            return maxDamage;
        }

        public void setMaxDamage(int maxDamage) {
            this.maxDamage = maxDamage;
        }

        public float getEvasionRate() {
            return evasionRate;
        }

        public void setEvasionRate(float evasionRate) {
            this.evasionRate = evasionRate;
        }

        private int getDamage() {
            return random.nextInt(this.getMinDamage(), this.getMaxDamage() + 1);
        }

        public void decreaseHealth(int damage) {
            this.health -= damage;
        }

        private boolean attack(Hero hero) {
            if (isRegenerate()) {
                System.out.printf("%s se está regenerando y no ataca!%n", getName());
                setRegenerate(false);
            } else if (random.nextFloat() > getEvasionRate()) {
                int damage = getDamage();
                System.out.printf("%s ataca a %s con %d de daño!%n"
                        , getName(), hero.getName(), damage);
                if (damage == getMaxDamage()) {
                    System.out.printf("%s da un golpe crítico! %s no atacará en el siguiente turno.%n"
                            , getName(), hero.getName());
                    hero.setRegenerate(true);
                }

                hero.decreaseHealth(damage);

                if (hero.getHealth() <= 0) {
                    System.out.printf("La vida de %s ha llegado a 0!%n", hero.getName());
                    return true;
                } else {
                    System.out.printf("Vida restante de %s: %d%n", hero.getName(), hero.getHealth());
                }
            } else System.out.printf("¡%s esquiva el ataque!%n", hero.getName());
            return false;
        }
    }
}
