import java.util.Random;
import java.util.Scanner;

public class asjordi {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numTurno = 0;

        System.out.println("Bienvenido a Deadpool vs Wolverine");
        System.out.println("Ingresa la vida de Deadpool: ");
        int vidaDeadpool = sc.nextInt();
        System.out.println("Ingresa la vida de Wolverine: ");
        int vidaWolverine = sc.nextInt();

        Personaje deadpool = new Personaje(TipoPersonaje.DEADPOOL, vidaDeadpool);
        Personaje wolverine = new Personaje(TipoPersonaje.WOLVERINE, vidaWolverine);

        while (deadpool.getVida() > 0 || wolverine.getVida() > 0) {
            numTurno++;
            System.out.println("Turno " + numTurno);
            System.out.println("Deadpool: " + deadpool.getVida() + " vida");
            System.out.println("Wolverine: " + wolverine.getVida() + " vida");

            System.out.println("Deadpool ataca a Wolverine");
            deadpool.atacar(wolverine);
            System.out.println("Wolverine ataca a Deadpool");
            wolverine.atacar(deadpool);

            if (deadpool.getVida() <= 0) {
                System.out.println("Wolverine ha ganado");
                break;
            } else if (wolverine.getVida() <= 0) {
                System.out.println("Deadpool ha ganado");
                break;
            }
        }
    }

    static class Personaje {
        private TipoPersonaje personaje;
        private double vida;
        private double ataque;
        private final Random r;
        private double ultimoAtaque;

        public Personaje(TipoPersonaje personaje, double vida) {
            this.personaje = personaje;
            this.vida = vida;
            this.r = new Random();
            definirPoderAtaque();
        }

        private void definirPoderAtaque() {
            this.ataque = r.nextInt(personaje.getMinAtaque(), personaje.getMaxAtaque() + 1);
        }

        public void recibirAtaque(double ataque) {
            if (r.nextInt(1, 101) > personaje.getPosEvitarAtaque()) {
                this.vida -= ataque;
            }
        }

        public void atacar(Personaje personaje) {
            personaje.recibirAtaque(this.ataque);
            System.out.println("Ataque de " + this.personaje + " a " + personaje.personaje + " con " + this.ataque + " de daño");
        }

        public double getVida() {
            return vida;
        }

        public void setVida(double vida) {
            this.vida = vida;
        }

        public double getAtaque() {
            return ataque;
        }

        public void setAtaque(double ataque) {
            this.ataque = ataque;
        }
    }

    enum TipoPersonaje {
        DEADPOOL(10, 100, 25),
        WOLVERINE(10, 120, 20);
        private final int minAtaque;
        private final int maxAtaque;
        private int posEvitarAtaque;

        TipoPersonaje(int minDamage, int maxAtaque, int posEvitarAtaque) {
            this.minAtaque = minDamage;
            this.maxAtaque = maxAtaque;
            this.posEvitarAtaque = posEvitarAtaque;
        }

        public int getMinAtaque() {
            return minAtaque;
        }

        public int getMaxAtaque() {
            return maxAtaque;
        }

        public int getPosEvitarAtaque() {
            return posEvitarAtaque;
        }
    }
}
