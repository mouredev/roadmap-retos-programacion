package Principal;
import java.util.Random;

import Clases.*;
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
public abstract class Personajes {
	protected int vida;

    public Personajes() {
        this.setVida(100); 
    }

    public abstract int atacar();

    public abstract int defenderse();
    
    public abstract int regenerarse();

	public int getVida() {
		return vida;
	}

	public void setVida(int vida) {
		this.vida = vida;
	}
}
public class Wolverine extends Personajes {
	private boolean estaRegenerandose;
	public Wolverine() {
		 super();
		 this.estaRegenerandose = false;
	}

	@Override
	 public int atacar() {
        Random rand = new Random();
        return rand.nextInt((120 - 10) + 1) + 10;
    }

	@Override
	public int defenderse() {
		Random rand = new Random();
        int probabilidad = rand.nextInt(100);
        if (probabilidad < 20) {
            return 1; // Defensa exitosa
        } else {
            return 0; // Defensa fallida
        }
	}

	@Override
	public int regenerarse() {
        // Se regenera si recibe daño crítico, lo que le impide atacar
        if (this.vida <= 20) {
            this.estaRegenerandose = true;
            this.vida += 20; // Aumenta la vida en 20 puntos
        }
        return this.vida;
    }
	
	 public boolean estaRegenerandose() {
	        return this.estaRegenerandose;
	 }

}
public class Deadpool extends Personajes {
    private boolean estaRegenerandose;

    public Deadpool() {
        super(); // Llama al constructor de la clase padre para inicializar la vida
        this.estaRegenerandose = false; // Inicializa la variable de regeneración
    }

    @Override
    public int atacar() {
        Random rand = new Random();
        return rand.nextInt((100 - 10) + 1) + 10;
    }

    @Override
    public int defenderse() {
        // Tiene una probabilidad de defenderse del 25%
        Random rand = new Random();
        int probabilidad = rand.nextInt(100);
        if (probabilidad < 25) {
            return 1; // Defensa exitosa
        } else {
            return 0; // Defensa fallida
        }
    }
    @Override
    public int regenerarse() {
        // Se regenera si recibe daño crítico, lo que le impide atacar
        if (this.vida <= 20) {
            this.estaRegenerandose = true;
            this.vida += 20; // Aumenta la vida en 20 puntos
        }
        return this.vida;
    }

    public boolean estaRegenerandose() {
        return this.estaRegenerandose;
    }
}


public class Principal {

	public static void main(String[] args) throws InterruptedException{
		Personajes P1 = new Deadpool();
		Personajes P2 = new Wolverine();
		int turno = 1;
		Random rand = new Random();
		while (P1.getVida() > 0 && P2.getVida() > 0) {
			System.out.println("Turno: " + turno);
            System.out.println("Vida de Deadpool: " + P1.getVida());
            System.out.println("Vida del Wolverine: " + P2.getVida());
            boolean PrimerAtaqque = rand.nextBoolean();
            if (PrimerAtaqque) {
                // Deadpool ataca
                int ataque = P1.atacar();
                System.out.println("Deadpool ataca con un daño de " + ataque);
                if(P2.defenderse() == 0) {
                	int reducirvida = P2.getVida()-ataque;
                	System.out.println("Wolverine recibe daño");
                	P2.setVida(reducirvida);
                }else {
                	System.out.println("Wolverine Se defienden");
                } 
            } else {
                // Wolverine ataca
                int ataque = P2.atacar();
                System.out.println("Wolverine ataca con un daño de " + ataque);
                if(P2.defenderse() == 0) {
                	int reducirvida = P1.getVida()-ataque;
                	System.out.println("Deadpool recibe daño");
                	P1.setVida(reducirvida);
                }else {
                	System.out.println("Deadpool Se defienden");
                }                 
            }    
            // Cambiamos el turno
            
            PrimerAtaqque = !PrimerAtaqque;

            // Pausa de 1 segundo
            Thread.sleep(1000);
            turno++;
		}
		 if (P1.getVida() <= 0) {
	            System.out.println("Wolverine ha ganado la batalla.");
	        } else {
	            System.out.println("Deadpool ha ganado la batalla.");
	        }
	}

}
