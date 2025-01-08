class Animal{
    final String name;
    final int peso;
    final int tamaño;

    public Animal(String name, int peso, int tamaño){
        this.name = name;
        this.tamaño = tamaño;
        this.peso = peso;
    }

    public void sound(){}
}

class Gato extends Animal{
    private final String sonido;

    public Gato(String name, int peso, int tamaño, String sonido){
        super(name, peso, tamaño);
        this.sonido = sonido;
    }

    @Override
    public void sound(){
        System.out.println("El" + name + "suena" + sonido);
    }
}

public class pguillo02 {

    public static void main(String args[]){
        Gato g = new Gato("Gato", 22, 22, "Miau");
        g.sound();
    }
}
