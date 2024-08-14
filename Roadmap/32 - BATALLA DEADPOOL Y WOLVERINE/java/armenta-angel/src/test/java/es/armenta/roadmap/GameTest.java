package es.armenta.roadmap;

import org.junit.Test;

import static org.junit.Assert.*;

public class GameTest {

    @Test
    public void firstFighterShouldBeZeroOrOne() {
        Game game = new Game(null, null);
        boolean zeroUsed = false;
        boolean oneUsed = false;
        for (int i = 0; i < 100; i++) {
            int firstFighter = game.chooseFirstFighterRandomly();
            assertTrue(firstFighter == 0 || firstFighter == 1);
            if (!zeroUsed && firstFighter == 0) {
                zeroUsed = true;
            }
            if (!oneUsed && firstFighter == 1) {
                oneUsed = true;
            }
        }

        assertTrue(zeroUsed);
        assertTrue(oneUsed);
    }

    @Test
    public void whenTurnOfIsZeroChangeTurnWillReturnOne() {
        Game game = new Game(null, null);
        game.turnOf = 0;
        game.changeTurn();
        assertEquals(1, game.turnOf);
    }

    @Test
    public void whenTurnOfIsOneChangeTurnWillReturnZero() {
        Game game = new Game(null, null);
        game.turnOf = 1;
        game.changeTurn();
        assertEquals(0, game.turnOf);
    }

    @Test
    public void whenTurnOfFighterZeroFighterOnDefenseIsOne() {
        Game game = new Game(null, null);
        game.turnOf = 0;
        assertEquals(1, game.fighterOnDefenseIndex());
    }

    @Test
    public void whenTurnOfFighterOneFighterOnDefenseIsZero() {
        Game game = new Game(null, null);
        game.turnOf = 1;
        assertEquals(0, game.fighterOnDefenseIndex());
    }

    @Test
    public void whenFighterZeroOrFighterOneLifeIsZeroOrLessFightEnds() {
        Fighter deadpool = new Fighter(Hero.DEADPOOL, 1) ;
        Fighter wolverine = new Fighter(Hero.WOLVERINE, 1) ;
        Game game = new Game(deadpool, wolverine);

        assertFalse(game.fightEnds());

        deadpool.life = 1;
        wolverine.life = 0;
        assertTrue(game.fightEnds());

        deadpool.life = 0;
        wolverine.life = 1;
        assertTrue(game.fightEnds());

        deadpool.life = -20;
        wolverine.life = 1;
        assertTrue(game.fightEnds());

        deadpool.life = 1;
        wolverine.life = -12;
        assertTrue(game.fightEnds());
    }

    @Test
    public void whenFighterZeroLifeIsZeroOrLessFighterOneIsTheWinner() {
        Fighter deadpool = new Fighter(Hero.DEADPOOL, 1) ;
        Fighter wolverine = new Fighter(Hero.WOLVERINE, 1) ;
        Game game = new Game(deadpool, wolverine);

        deadpool.life = 1;
        wolverine.life = 0;
        assertEquals(0, game.getWinnerIndex());

        deadpool.life = 1;
        wolverine.life = -12;
        assertEquals(0, game.getWinnerIndex());
    }

    @Test
    public void whenFighterOneLifeIsZeroOrLessFighterZeroIsTheWinner() {
        Fighter deadpool = new Fighter(Hero.DEADPOOL, 1) ;
        Fighter wolverine = new Fighter(Hero.WOLVERINE, 1) ;
        Game game = new Game(deadpool, wolverine);

        deadpool.life = 0;
        wolverine.life = 1;
        assertEquals(1, game.getWinnerIndex());

        deadpool.life = -20;
        wolverine.life = 1;
        assertEquals(1, game.getWinnerIndex());
    }

    @Test
    public void runGameWorksWithoutErrors() {
        Fighter deadpool = new Fighter(Hero.DEADPOOL, 100) ;
        Fighter wolverine = new Fighter(Hero.WOLVERINE, 80) ;
        Game game = new Game(deadpool, wolverine);

        try {
            game.start();
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }
}
