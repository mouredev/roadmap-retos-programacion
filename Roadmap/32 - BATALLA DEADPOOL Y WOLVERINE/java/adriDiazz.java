package Principal;

import java.util.Random;
import java.util.Scanner;

// INTERFACE PARA ESTRATEGIAS DE ATAQUE Y DEFENSA
interface AttackStrategy {
    int attack();
}

interface DefenseStrategy {
    boolean defend();
}

// CLASE ABSTRACTA PARA PERSONAJES
abstract class Character {
    protected int life;
    protected AttackStrategy attackStrategy;
    protected DefenseStrategy defenseStrategy;

    public Character(int life, AttackStrategy attackStrategy, DefenseStrategy defenseStrategy) {
        this.life = life;
        this.attackStrategy = attackStrategy;
        this.defenseStrategy = defenseStrategy;
    }

    public int getLife() {
        return life;
    }

    public void setLife(int life) {
        this.life = life;
    }

    public int attack() {
        return attackStrategy.attack();
    }

    public boolean defend() {
        return defenseStrategy.defend();
    }
}

// IMPLEMENTACIONES DE ESTRATEGIAS DE ATAQUE Y DEFENSA
class RandomAttackStrategy implements AttackStrategy {
    private final int minAttack;
    private final int maxAttack;
    private final Random random;

    public RandomAttackStrategy(int minAttack, int maxAttack) {
        this.minAttack = minAttack;
        this.maxAttack = maxAttack;
        this.random = new Random();
    }

    @Override
    public int attack() {
        return random.nextInt((maxAttack - minAttack) + 1) + minAttack;
    }
}

class RandomDefenseStrategy implements DefenseStrategy {
    private final int evadeChance; // porcentaje de evasión
    private final Random random;

    public RandomDefenseStrategy(int evadeChance) {
        this.evadeChance = evadeChance;
        this.random = new Random();
    }

    @Override
    public boolean defend() {
        return random.nextInt(100) < evadeChance;
    }
}

// CLASES DE PERSONAJES
class DeadPool extends Character {
    public DeadPool(int life) {
        super(life, new RandomAttackStrategy(10, 100), new RandomDefenseStrategy(25));
    }
}

class Wolverine extends Character {
    public Wolverine(int life) {
        super(life, new RandomAttackStrategy(10, 120), new RandomDefenseStrategy(20));
    }
}

// CONTROLADOR DE LA BATALLA
class BattleController {
    private final Character character1;
    private final Character character2;

    public BattleController(Character character1, Character character2) {
        this.character1 = character1;
        this.character2 = character2;
    }

    public void startBattle() {
        int turn = 0;
        while (character1.getLife() > 0 && character2.getLife() > 0) {
            turn++;
            System.out.println("Turno número " + turn);
            System.out.println("Vida " + character1.getClass().getSimpleName() + ": " + character1.getLife());
            System.out.println("Vida " + character2.getClass().getSimpleName() + ": " + character2.getLife());

            executeTurn(character1, character2);
            if (character2.getLife() <= 0) break;

            executeTurn(character2, character1);
        }

        declareWinner();
    }

    private void executeTurn(Character attacker, Character defender) {
        int attackValue = attacker.attack();
        if (!defender.defend()) {
            System.out.println(attacker.getClass().getSimpleName() + " ataca con " + attackValue);
            defender.setLife(defender.getLife() - attackValue);
        } else {
            System.out.println(defender.getClass().getSimpleName() + " esquiva el ataque");
        }
    }

    private void declareWinner() {
        if (character1.getLife() <= 0) {
            System.out.println(character2.getClass().getSimpleName() + " ha ganado!");
        } else if (character2.getLife() <= 0) {
            System.out.println(character1.getClass().getSimpleName() + " ha ganado!");
        }
    }
}

// CLASE PRINCIPAL
public class adriDiazz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Vida DeadPool:");
        int vidaDeadpool = scanner.nextInt();

        System.out.println("Vida Wolverine:");
        int vidaWolverine = scanner.nextInt();

        Character deadPool = new DeadPool(vidaDeadpool);
        Character wolverine = new Wolverine(vidaWolverine);

        BattleController battle = new BattleController(deadPool, wolverine);
        battle.startBattle();
    }
}
