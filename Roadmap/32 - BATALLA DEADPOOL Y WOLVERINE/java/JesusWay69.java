package ejercicio32;

import java.util.Scanner;

/*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */
public class JesusWay69 {

    public static void main(String[] args) throws InterruptedException {
        boolean regenerateState = false;
        Deadpool deadpool = new Deadpool();
        Wolverine wolverine = new Wolverine();
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduzca los puntos de inicio de Deadpool: ");
        deadpool.lifePoints = sc.nextInt();
        System.out.print("Introduzca los puntos de inicio de Wolverine: ");
        wolverine.lifePoints = sc.nextInt();
        battle(wolverine.lifePoints, deadpool.lifePoints, regenerateState,
                wolverine.maxDamage, deadpool.maxDamage, wolverine.shield, deadpool.shield);

    }

    public static void battle(int wPoints, int dPoints, boolean regenerateState,
            int vMaxDamage, int dMaxDamage, int vShield, int dShield) throws InterruptedException {
        String name = "";
        int round = 1;
        while (wPoints > 0 && dPoints > 0) {
            System.out.println("\nRonda: " + round);
            
            /////////////////////////////////////ATACA DEADPOOL////////////////////////////////////////////////////////
            if (regenerateState) { //Comprobamos si en el turno del oponente ha generado ataque máximo y ha cambado el estado a true (empieza en false por defecto)
                System.out.println(name + " pierde su turno por haber recibido daño máximo y tiene que regenerarse ");
                regenerateState = false;//Tras perder el turno se vuelve a poner el estado en false
            } else if (Math.random() > (double) (vShield / 100)) {//En caso contrario generamos un número aleatorio entre 0 y 1 que sea mayor al porcentaje de la capacidad del escudo
                int dDamage = (int) (Math.random() * dMaxDamage + 10);//Y otro número random entre 10 y el máximo daño del atacante en caso de que la condición anterior se cumpla
                System.out.println(" El ataque de Deadpool le ha restado " + dDamage + " puntos de vida a Wolverine");
                if (dDamage == 100) { //Dentro del if del ataque comprobamos si el daño coincide con el ataque mçaximo
                    System.out.println("Ataque máximo de Deadpool");
                    regenerateState = true;//Cambiamos el estado a true para que en el turno del oponente salte el primer if y ceda turno
                    name = "Wolverine";
                }
                wPoints = wPoints - dDamage;// Le restamos los puntos generados en el ataque al saldo del oponente
                if (wPoints <= 0) {//Comprobamos si el oponente se ha quedado sin puntos de vida
                    System.out.println("Wolverine se ha quedado sin puntos de vida");
                } else {// Si no es así imprimimos el saldo de puntos del oponente
                    System.out.println("A Wolverine le quedan " + wPoints + " puntos");
                }
            } else {//En caso de que el número generado sea menor a la probabilidad de escudo del oponente no se genera ataque y se informa sobre la defensa del oponente
                System.out.println("Wolverine repele el ataque y no pierde puntos");
            }
            //Todas las anotaciones anteriores sirven para el siguiente bloque de código que sigue dentro del while

            /////////////////////////////////////ATACA WOLVERINE////////////////////////////////////////////////////////
            if (regenerateState) {
                System.out.println(name + " pierde su turno por haber recibido daño máximo y tiene que regenerarse ");
                regenerateState = false;
            } else if (Math.random() > (double) (dShield / 100)) {
                int vDamage = (int) (Math.random() * vMaxDamage + 10);
                System.out.println(" \nEl ataque de Wolverine le ha restado " + vDamage + " puntos de vida a Deadpool");
                if (vDamage == 120) {
                    System.out.println("Ataque máximo de Wolverine");
                    regenerateState = true;
                    name = "Deadpool";
                }
                dPoints = dPoints - vDamage;
                if (dPoints <= 0) {
                    System.out.println("Deadpoool se ha quedado sin puntos de vida");
                } else {
                    System.out.println("A Deadpool le quedan " + dPoints + " puntos");
                }
            } else {
                System.out.println("Deadpool repele el ataque y no pierde puntos");
            }
            Thread.sleep(1000);
            round++;
        }

        if (dPoints > 0) {//Una vez se quede uno de los contendientes a 0 o menos y se salga del while se comprueba cual de los 2 ha sido y se anuncia el ganador
            System.out.println("Deadpool gana con " + dPoints + " puntos de vida restantes");
        } else {
            System.out.println("Wolverine gana con " + wPoints + " puntos de vida restantes");
        }
    }

}

class Deadpool {

    int maxDamage = 100;
    int shield = 25;
    int lifePoints;
}

class Wolverine {

    int maxDamage = 120;
    int shield = 20;
    int lifePoints;

}
