package es.armenta.roadmap;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class FighterTest {

    @Test
    public void testFighterConstructor() {
        Fighter deadpool = new Fighter(Hero.DEADPOOL, 200);
        assertEquals(deadpool.life, 200);
        assertEquals(deadpool.hero.minDamage, 10);
        assertEquals(deadpool.hero.maxDamage, 100);
        assertEquals(deadpool.hero.defendAttackPercentage, 25);

        Fighter wolverine = new Fighter(Hero.WOLVERINE, 100);
        assertEquals(wolverine.life, 100);
        assertEquals(wolverine.hero.minDamage, 10);
        assertEquals(wolverine.hero.maxDamage, 120);
        assertEquals(wolverine.hero.defendAttackPercentage, 20);
    }

    @Test
    public void randomDefenseMeetsPercentageCriteria() {
        Fighter deadpool = new Fighter(Hero.DEADPOOL, 200);
        int defendedCount = 0;
        for (int i = 0; i < 100; i++) {
            if (deadpool.defense()) {
                defendedCount++;
            }
        }
        assertEquals(deadpool.hero.defendAttackPercentage, defendedCount);

        Fighter wolverine = new Fighter(Hero.WOLVERINE, 200);
        defendedCount = 0;
        for (int i = 0; i < 100; i++) {
            if (wolverine.defense()) {
                defendedCount++;
            }
        }
        assertEquals(wolverine.hero.defendAttackPercentage, defendedCount);
    }

    @Test
    public void attackPowerIsBetweenLimits() {
        Fighter deadpool = new Fighter(Hero.DEADPOOL, 200);

        boolean minDamageUsed = false;
        boolean maxDamageUsed = false;

        for (int i = 0; i < 10000; i++) {
            int attackPower = deadpool.attack();
            assertTrue(attackPower >= deadpool.hero.minDamage && attackPower <= deadpool.hero.maxDamage);

            if (!minDamageUsed && attackPower == deadpool.hero.minDamage) {
                minDamageUsed = true;
            }
            if (!maxDamageUsed && attackPower == deadpool.hero.maxDamage) {
                maxDamageUsed = true;
            }
        }

        assertTrue(minDamageUsed);
        assertTrue(maxDamageUsed);
    }
}
