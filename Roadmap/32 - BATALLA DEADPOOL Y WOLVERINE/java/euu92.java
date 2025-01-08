import java.util.Random;
import java.util.Scanner;

public class euudev {

    static Deadpool deadpool = new Deadpool();
    static Wolverine wolverine = new Wolverine();
    static Scanner scanner = new Scanner(System.in);
    static Random random = new Random();

    public static void main(String[] args) {

        AdministradorBatalla administradorBatalla = new AdministradorBatalla();

        administradorBatalla.setInitialHp();
        administradorBatalla.simBattle();

    }

    static class AdministradorBatalla {

        public void setInitialHp() {
            boolean deadpoolHpSet = false;
            boolean wolverineHpSet = false;

            while (!deadpoolHpSet || !wolverineHpSet) {
                if (!deadpoolHpSet) {
                    System.out.println("Selecciona un personaje:");
                    System.out.println("1. Deadpool");
                    System.out.println("2. Wolverine");

                    int action = scanner.nextInt();
                    scanner.nextLine();

                    switch (action) {
                        case 1:
                            setDeadpoolHp();
                            deadpoolHpSet = true;
                            break;
                        case 2:
                            setWolverineHp();
                            wolverineHpSet = true;
                            break;
                        default:
                            System.out.println("Acción no válida. Inténtalo de nuevo.");
                    }
                } else if (!wolverineHpSet) {
                    setWolverineHp();
                    wolverineHpSet = true;
                } else if (!deadpoolHpSet) {
                    setDeadpoolHp();
                    deadpoolHpSet = true;
                }
            }
        }

        public void simBattle () {
            int turn = 1;
            boolean deadpoolSkipTurn = false;
            boolean wolverineSkipTurn = false;

            while (deadpool.getHp() > 0 && wolverine.getHp() > 0) {
                System.out.println("Turno " + turn);
                if (!deadpoolSkipTurn) {
                    if (!evadeAttack(wolverine)) {
                        int damage = random.nextInt(91) + 10;
                        if (damage == 100) {
                            wolverineSkipTurn = true;
                        }
                        wolverine.setHp(wolverine.getHp() - damage);
                        System.out.println("Deadpool ataca a Wolverine con " + damage + " de daño.");
                    } else {
                        System.out.println("Wolverine evade el ataque de Deadpool.");
                    } 
                } else {
                    deadpoolSkipTurn = false;
                    System.out.println("Deadpool se está recuperando y no puede atacar.");
                }

                if (wolverine.getHp() <= 0) break;

                if (!wolverineSkipTurn) {
                    if(!evadeAttack(deadpool)) {
                        int damage = random.nextInt(111) + 10;
                        if (damage == 120) {
                            deadpoolSkipTurn = true;
                        }
                        deadpool.setHp(deadpool.getHp() - damage);
                        System.out.println("Wolverine ataca a Deadpool con " + damage + " de daño.");
                    } else {
                        System.out.println("Deadpool evade el ataque de Wolverine.");
                    }
                } else {
                    wolverineSkipTurn = false;
                    System.out.println("Wolverine se está recuperando y no puede atacar.");
                }

                System.out.println("Vida de Deadpool: " + deadpool.getHp());
                System.out.println("Vida de Wolverine: " + wolverine.getHp());

                turn++;
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } 

            if (deadpool.getHp() <= 0) {
                System.out.println("Wolverine gana la batalla!");
            } else {
                System.out.println("Deadpool gana la batalla!");
            }
        }

        public static boolean evadeAttack(Character character) {
            int chance = random.nextInt(100);
            if(character instanceof Deadpool) {
                return chance < 25;
            } else if (character instanceof Wolverine) {
                return chance < 20;
            }
            return false;
        }

        public void setDeadpoolHp() {
            System.out.println("Establece HP para Deadpool: ");
            int hp = scanner.nextInt();
            scanner.nextLine();
            deadpool.setHp(hp);
            System.out.println("HP de Deadpool establecida");
        }

        public void setWolverineHp() {
            System.out.println("Establece HP para Wolverine: ");
            int hp = scanner.nextInt();
            scanner.nextLine();
            wolverine.setHp(hp);
            System.out.println("HP de Wolverine establecida");
        }
    }
}

class Deadpool extends Character {
    public Deadpool() {
        super();
    }
}

class Wolverine extends Character {
    public Wolverine() {
        super();
    }
}

class Character {
    private int hp;

    public int getHp() {
        return hp;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }
}
