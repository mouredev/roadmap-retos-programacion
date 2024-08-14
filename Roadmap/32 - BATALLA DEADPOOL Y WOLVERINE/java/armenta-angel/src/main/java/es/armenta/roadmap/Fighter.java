package es.armenta.roadmap;

import java.util.Random;

public class Fighter {
    public Hero hero;
    public int life;
    public String[] randomDefense = new String[100];

    private String SUPER_DEFENSE = "SUPER_DEFENSE";
    private String USED = "USED";
    private String NOT_USED = "NOT_USED";

    private Random rand = new Random();

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
