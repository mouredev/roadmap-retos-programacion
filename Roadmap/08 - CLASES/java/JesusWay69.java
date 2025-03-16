package roadmap.ejercicio_08;

import java.util.ArrayList;

/*
* EJERCICIO:
* Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
* atributos y una función que los imprima (teniendo en cuenta las posibilidades
* de tu lenguaje).
* Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
* utilizando su función.
*
*/


public class JesusWay69 {

  public static void main(String[] args) {

    Stack stack_instance = new Stack();
    Queue queue_instance = new Queue();
    Coche coche_instance = new Coche();

    stack_instance.add(1, 11);
    stack_instance.show();
    System.out.println("La lista tiene " + stack_instance.leight() + " números\n");
    System.out.println("Eliminamos el número " + stack_instance.unstack() + "\n");
    stack_instance.show();
    System.out.println("La lista tiene " + stack_instance.leight() + " números\n");
    
    queue_instance.add(1, 11);
    queue_instance.show();
    System.out.println("La lista tiene " + queue_instance.leight() + " números\n");
    System.out.println("Eliminamos el número " + queue_instance.dequeue()+ "\n");
    queue_instance.show();
    System.out.println("La lista tiene " + queue_instance.leight() + " números\n");
    

    coche_instance.setMarca("Alfa");
    coche_instance.setModelo("Giulietta");
    coche_instance.setMotorizacion("diesel");
    coche_instance.setCilindrada(2000);
    coche_instance.setPotencia(170);
    coche_instance.setTipo_cambio("manual 6v");
    coche_instance.setCarroceria("hachback");
    System.out.println(coche_instance.toString());
    
    coche_instance.setMarca("Toyota");
    coche_instance.setModelo("Corolla");
    coche_instance.setMotorizacion("híbrido");
    coche_instance.setCilindrada(1800);
    coche_instance.setPotencia(140);
    coche_instance.setTipo_cambio("variador cvt");
    coche_instance.setCarroceria("sedán");
    System.out.println(coche_instance.toString());
    
    

  }

}


class Coche {
    
    private String marca;
    private String modelo;
    private String motorizacion;
    private int cilindrada;
    private int potencia;
    private String tipo_cambio;
    private String carroceria;
    
    public Coche(){ 
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setMotorizacion(String motorizacion) {
        this.motorizacion = motorizacion;
    }

    public void setCilindrada(int cilindrada) {
        this.cilindrada = cilindrada;
    }

    public void setPotencia(int potencia) {
        this.potencia = potencia;
    }

    public void setTipo_cambio(String tipo_cambio) {
        this.tipo_cambio = tipo_cambio;
    }

    public void setCarroceria(String carroceria) {
        this.carroceria = carroceria;
    }
    


    @Override
    public String toString() {
        return "Objeto Coche:\nMarca = " + marca + "\nModelo = " + modelo + "\nMotorización = " + motorizacion+  "\nCilindrada = " 
      + cilindrada + "CC"+ "\nPotencia = " + potencia + "CV"+ "\nCambio = " + tipo_cambio + "\nCarrocería = " + carroceria + "\n";
    }
   
    
}

/*
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir todo su contenido.
*/

class Stack {

  public ArrayList my_stack_list;

  public Stack() {
    my_stack_list = new ArrayList<>();

  }

  public void add(int init_num, int end_num) {
    for (int i = init_num; i < end_num; i++)  my_stack_list.add(i);
  }

  public int unstack() {
    return Integer.parseInt(my_stack_list.remove(my_stack_list.size() - 1).toString());
  }

  public int leight() {
    return my_stack_list.size();
  }

  public void show() {
    System.out.println(my_stack_list);
  }

}

class Queue {

  public ArrayList my_stack_list;

  public Queue() {
    my_stack_list = new ArrayList<>();
  }

  public void add(int init_num, int end_num) {
    for (int i = init_num; i < end_num; i++)  my_stack_list.add(i);
  }

  public int dequeue() {
   return Integer.parseInt(my_stack_list.remove(0).toString());
  }

  public int leight() {
    return my_stack_list.size();
  }

  public void show() {
    System.out.println(my_stack_list);
  }

}