import java.util.Random;
import java.util.Scanner;

import static java.lang.Thread.sleep;

public class ArmentaAngel {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  // Create a Scanner object

        System.out.println("Enter Deadpool's life points:");
        Fighter deadpool = new Fighter(Hero.DEADPOOL, scanner.nextInt()) ;

        System.out.println("Enter Wolverine's life points:");
        Fighter wolverine = new Fighter(Hero.WOLVERINE, scanner.nextInt()) ;

        Game game = new Game(deadpool, wolverine);
        game.start();
    }
}

enum Hero {

    DEADPOOL("Deadpool", 10, 100, 25),
    WOLVERINE("Wolverine", 10, 120, 20);

    final String name;
    final int minDamage;
    final int maxDamage;
    final int defendAttackPercentage;

    Hero(String name, int minDamage, int maxDamage, int defendAttackPercentage) {
        this.name = name;
        this.minDamage = minDamage;
        this.maxDamage = maxDamage;
        this.defendAttackPercentage = defendAttackPercentage;
    }
}

class Fighter {

    public Hero hero;
    public int life;
    public String[] randomDefense = new String[100];

    private final String SUPER_DEFENSE = "SUPER_DEFENSE";
    private final String USED = "USED";
    private final String NOT_USED = "NOT_USED";

    private final Random rand = new Random();

    public Fighter(Hero hero, int life) {
        this.hero = hero;
        this.life = life;

        buildRandomDefense();
    }

    public int attack() {
        return randomBetween(hero.minDamage, hero.maxDamage);
    }

    public boolean defense() {
        int index;
        Boolean noDamage;

        do {
            index = rand.nextInt(100);
            if (randomDefense[index].equals(SUPER_DEFENSE)) {
                noDamage = true;
            } else if (randomDefense[index].equals(NOT_USED)) {
                noDamage = false;
            } else {
                // Only can be USED
                noDamage = null;
            }
        } while (noDamage == null);
        randomDefense[index] = USED;

        return noDamage;
    }

    protected int randomBetween(int minInclusive, int maxInclusive) {
        return rand.nextInt(maxInclusive - minInclusive + 1) + minInclusive;
    }

    private void buildRandomDefense() {
        // Place SUPER_DEFENSE positions
        int avoidAttackCount = hero.defendAttackPercentage;
        while (avoidAttackCount > 0) {
            int index = rand.nextInt(100);
            if (randomDefense[index] == null) {
                randomDefense[index] = SUPER_DEFENSE;
                avoidAttackCount--;
            }
        }

        fillNullIndexes(randomDefense, NOT_USED);
    }

    private void fillNullIndexes(String[] array, String filler) {
        for (int i = 0; i < array.length; i++) {
            if(array[i] == null) {
                array[i] = filler;
            }
        }
    }
}

class Game {
    private final Fighter[] fighters = new Fighter[2];
    private int turnCount;
    protected int turnOf;
    private boolean fightEnds = false;

    private final int TURN_TIME_IN_SECONDS = 1;

    public Game(Fighter fighter1, Fighter fighter2) {
        fighters[0] = fighter1;
        fighters[1] = fighter2;
    }

    public void start() {
        turnCount = 1;
        turnOf = chooseFirstFighterRandomly();

        while (!fightEnds) {
            playTurn();
        }

        fightBroadcastFightEnds();
    }

    protected int chooseFirstFighterRandomly() {
        Random rand = new Random();
        return rand.nextInt(2); // Only can return 0 or 1
    }

    protected void changeTurn() {
        turnOf = turnOf == 1 ? 0 : 1;
    }

    protected int fighterOnDefenseIndex() {
        return turnOf == 1 ? 0 : 1;
    }

    protected boolean fightEnds() {
        return fighters[0].life <= 0 || fighters[1].life <= 0;
    }

    protected int getWinnerIndex() {
        return fighters[0].life > fighters[1].life ? 0 : 1;
    }

    private void playTurn() {
        Fighter fighterOnAttack = fighters[turnOf];
        Fighter fighterOnDefense = fighters[fighterOnDefenseIndex()];

        fightBroadcastTurnBegins();

        dramaticPause();

        int attackPower = fighterOnAttack.attack();
        boolean defended = fighterOnDefense.defense();
        boolean maximumPower = attackPower == fighterOnAttack.hero.maxDamage;

        fightBroadcastTurnEnds(attackPower, maximumPower, defended);

        if (!defended) {
            fighterOnDefense.life -= attackPower;
        }

        if (!fightEnds()) {
            if (!maximumPower) {
                changeTurn();
            }
            turnCount++;
        } else {
            fightEnds = true;
        }
    }

    private void dramaticPause() {
        try {
            sleep(TURN_TIME_IN_SECONDS * 1000);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private void fightBroadcastTurnBegins() {
        System.out.printf("# This is turn %d ##############################################################%n", turnCount);
        System.out.printf("# %s life is %d%n", fighters[0].hero.name, fighters[0].life);
        System.out.printf("# %s life is %d%n", fighters[1].hero.name, fighters[1].life);
        System.out.printf("# %s's turn to attack, %s's turn to defend%n", fighters[turnOf].hero.name, fighters[fighterOnDefenseIndex()].hero.name);
        System.out.printf("%n");
    }

    private void fightBroadcastTurnEnds(int power, boolean maximumPower, boolean defended) {
        // Turn results
        System.out.printf("@ After turn %d%n", turnCount);
        if(maximumPower) {
            System.out.printf("@ %s attack is %d. It is a $$$ MAXIMUM POWER ATTACK $$$%n", fighters[turnOf].hero.name, power);
            System.out.printf("@ With this MAXIMUM POWER ATTACK, %s will strike again in the next turn%n", fighters[turnOf].hero.name);
        } else {
            System.out.printf("@ %s attack power is %d%n", fighters[turnOf].hero.name, power);
        }
        if(defended) {
            System.out.printf("@ %s dodges the attack with a --- SUPER DEFENSE ---%n", fighters[fighterOnDefenseIndex()].hero.name);
        } else {
            System.out.printf("@ %s receives an accurate hit and loses %d life points%n", fighters[fighterOnDefenseIndex()].hero.name, power);
        }
        System.out.printf("%n");
    }

    private void fightBroadcastFightEnds() {
        // Fight results
        System.out.printf("################################################################################%n");
        System.out.printf("#                                                                              #%n");
        System.out.printf("# %s is the WINNER after %d turns%n", fighters[getWinnerIndex()].hero.name, turnCount);
        System.out.printf("#                                                                              #%n");
        System.out.printf("# %s loses with %d life points%n", fighters[fighterOnDefenseIndex()].hero.name, fighters[fighterOnDefenseIndex()].life);
        System.out.printf("# %s wins with %d life points%n", fighters[turnOf].hero.name, fighters[turnOf].life);
        System.out.printf("#                                                                              #%n");
        System.out.printf("################################################################################%n");
    }
}
