import java.util.Random;
import java.util.Scanner;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().battleSim();
    }

    private Superhero deadpool;
    private Superhero wolverine;
    final Scanner sc = new Scanner(System.in);
    private Random rnd = new Random();

    public void battleSim(){
//        System.out.println("---Opciones---");
//        System.out.println("1. Empezar la batalla");
//        System.out.println("2. Salir del programa");

        try(sc){
//            app: while(true){
//                System.out.print("Introduzca la opción que desee: ");
//                String option = sc.nextLine().strip();
//                switch (option){
//                    case "1":
//                        initSuperheros();
//                        battle();
//                        break;
//                    case "2":
//                        System.out.println("Saliendo de la aplicación...");
//                        break;
//                    default:
//                        System.out.println("Opción inválida.");
//                }
//            }

            initSuperheros();
            battle();
        }
    }

    private void initSuperheros(){
        deadpool = new Superhero("Deadpool", askSuperheroHp("Deadpool"),
            10, 100, 25);
        wolverine = new Superhero("Wolverine", askSuperheroHp("Wolverine"),
                10, 120, 20);
    }

    private void battle(){
        Random rnd = new Random();
        Superhero first;
        Superhero last;
        int turn = 1;
        while(true){
            System.out.println();
            System.out.println("Turno: " + turn++);
            System.out.println(deadpool);
            System.out.println(wolverine);

            if (rnd.nextBoolean()){
                first = deadpool;
                last = wolverine;
            } else{
                first = wolverine;
                last = deadpool;
            }

            if (attack(first, last) || attack(last, first))
                break;

            try{
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

    private boolean attack(Superhero attacker, Superhero defender){
        if (attacker.isStunned()){
            System.out.println(attacker.getName() + " está regenerandose y no puede atacar");
            attacker.setStunned(false);
            return false;
        }

        Integer damage = rnd.nextInt(attacker.getATK_MIN(), attacker.getATK_MAX() + 1);

        if (rnd.nextInt(100) <= defender.getEvasion()){
            System.out.println(defender.getName() + " esquivó el ataque de " + attacker.getName());
            return false;
        }

        System.out.println(attacker.getName() + " hizo " + damage + " puntos de " +
                "daño a " + defender.getName());
        defender.takeDamage(damage);

        if (!defender.isAlive()){
            System.out.println("\n" + attacker);
            System.out.println(defender);
            System.out.println("¡" + attacker.getName() + " es el ganador!");
            return true;
        }

        if (damage == attacker.getATK_MAX()){
            defender.setStunned(true);
        }

        return false;
    }

    private Integer askSuperheroHp(String name){
        boolean validOption = false;
        Integer value = -1;
        while (!validOption){
            System.out.print("Introduzca la vida inicial de " + name + ": ");
            String input = sc.nextLine();
            try{
                value = Integer.parseInt(input);
                validOption = true;
            } catch (NumberFormatException e){
                System.out.println("Error. Introduzca un número entero por favor");
            }
        }
        return value;
    }

    public class Superhero{
        final private Integer HP_MAX;
        final private Integer ATK_MIN;
        final private Integer ATK_MAX;
        final private Integer EVASION;

        private String name;
        private Integer hp;
        private boolean stunned;

        public Superhero(String name, Integer hp, Integer atkMin, Integer atkMax, Integer evasion){
            HP_MAX = hp;
            ATK_MIN = atkMin;
            ATK_MAX = atkMax;
            EVASION = evasion;

            this.name = name;
            this.hp = HP_MAX;
            stunned = false;
        }

        public void takeDamage(Integer damage){
            if (damage > hp)
                hp = 0;
            else
                hp -= damage;
        }

        public String getName() {
            return name;
        }

        public Integer getHp() {
            return hp;
        }

        public Integer getEvasion() {
            return EVASION;
        }

        public Integer getATK_MIN() {
            return ATK_MIN;
        }

        public Integer getATK_MAX() {
            return ATK_MAX;
        }

        public boolean isStunned() {
            return stunned;
        }

        public void setStunned(boolean stunned) {
            this.stunned = stunned;
        }

        public boolean isAlive(){
            return hp > 0;
        }

        @Override
        public String toString() {
            return name + "(" + hp + "/" + HP_MAX + ")";
        }
    }
}
