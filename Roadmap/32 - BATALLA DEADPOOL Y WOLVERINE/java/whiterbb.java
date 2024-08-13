import java.util.Random;
import java.util.Scanner;

//GlobalConstants
interface GlobalConstants{
    static final int DEADPOOL_MIN_DAMAGE = 10;
    static final int DEADPOOL_MAX_DAMAGE = 100;
    static final int WOLVERINE_MIN_DAMAGE = 10;
    static final int WOLVERINE_MAX_DAMAGE = 120;
    static final double DEADPOOL_DODGE_PROBABILITY = 0.25;
    static final double WOLVERINE_DODGE_PROBABILITY = 0.20;
}

public class whiterbb implements GlobalConstants{

    /* Global Variables (I know that we shouldn't do it. But in this case it doesn't matter.)
    *  We can create a helper class to return object with values like isRegenerating boolean.
    */
    static Random random = new Random();
    static boolean isDeadpoolRegenerating = false;
    static boolean isWolverineRegenerating = false;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to this Epic Battle");

        System.out.println("Deadpool's life points (LP): ");
        int deadpoolLP = scanner.nextInt();
        System.out.println("Wolverine's life Points (LP): ");
        int wolverineLP = scanner.nextInt();

        simulateCombat(deadpoolLP, wolverineLP);
    }

    public static void simulateCombat(int deadpoolLP, int wolverineLP) {
        int turn = 1;

        //Loop until anyone's lifepoints is 0
        while (deadpoolLP > 0 && wolverineLP > 0) {
            System.out.println("Turn: " + turn);

            // Deadpool attacks if he is not regenerating
            
            //Parameters: attack(Enemy's name, Enemy's LP, AttackerMinDamage, AttackerMaxDamage, Enemy's DodgeProbability)
            if (!isDeadpoolRegenerating) {
                wolverineLP = attack("Wolverine", wolverineLP, DEADPOOL_MIN_DAMAGE, DEADPOOL_MAX_DAMAGE,
                        WOLVERINE_DODGE_PROBABILITY);
            } else {
                System.out.println("Deadpool is regenerating, cannot attack!");
            }
            //Reset Regenerating Status
            isDeadpoolRegenerating = false;

            if (wolverineLP > 0 && !isWolverineRegenerating) {
                deadpoolLP = attack("Deadpool", deadpoolLP, WOLVERINE_MIN_DAMAGE, WOLVERINE_MAX_DAMAGE,
                        DEADPOOL_DODGE_PROBABILITY);
            } else {
                System.out.println("Wolverine is regenerating, cannot attack!");
            }
            
            //Reset Regenerating Status
            isWolverineRegenerating = false;

            System.out.println("Remaining Deadpool's Life Points: " + deadpoolLP);
            System.out.println("Remaining Wolverine's Life Points: " + wolverineLP);

            turn++;
            waitOneSecond();
        }

        displayWinner(deadpoolLP);
    }

    public static int attack(String enemyname, int enemyLP, int minDamage, int maxDamage, double dodgeProbability) {
        
        if (random.nextDouble() <= dodgeProbability) {
            System.out.println(enemyname + " dodge the attack!");
            return enemyLP;
        } else {
            int damage = generateRandomDamage(minDamage, maxDamage);

            //Attacker
            String attacker = (enemyname.equals("Deadpool")) ? "Wolverine" : "Deadpool";
            
            if (damage == maxDamage) {
                if (enemyname.equals("Deadpool")) {
                    System.out.println("Wolverine does an amazing attack!");
                    enemyLP -= damage;
                    isDeadpoolRegenerating = true;
                } else {
                    System.out.println("Deadpool does an amazing attack!");
                    enemyLP -= damage;
                    isWolverineRegenerating = true;
                }

                return enemyLP;
            }

            System.out.println(attacker + " attacks with " + damage + " damage!");
            enemyLP -= damage;

            return enemyLP;
        }

    }

    public static int generateRandomDamage(int minDamage, int maxDamage){
        return random.nextInt(maxDamage - minDamage + 1) + minDamage;
    }

    public static void displayWinner(int deadpoolLP){
        if(deadpoolLP <= 0){
            System.out.println("Wolverine wins!");
        }else{
            System.out.println("Deadpool wins!");
        }
    }

    static void waitOneSecond() {
        try {
            Thread.sleep(1000);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}