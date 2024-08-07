package Clases;

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
