
public class Meir {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Alex" , 19);

        persona1.imprimir("Manzana");


        System.out.println("\n\n COLA");
        Cola cola = new Cola(5);
        cola.insertar("1");
        cola.insertar("2");
        cola.insertar("3");
        cola.insertar("4");
        cola.insertar("5");

        cola.contenido();
        cola.eliminar();
        cola.contenido();
        System.out.println("Numero de elementos: " + cola.numeroElementos() );



        System.out.println("\n\n PILA");

        Pila pila = new Pila(5);
        pila.añadir(2);
        pila.añadir(53);
        pila.añadir(70);


        pila.contenido();
        pila.eliminar();
        pila.contenido();
        System.out.println("Numero de elementos: " + pila.numeroElementos() );

    }
}

class Persona{
    String nombre;
    int edad;

    public Persona(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;
    }

    public void imprimir(String comida){
        System.out.println("Hola soy " + nombre + ", tengo " + edad + " y quiero comer " + comida);
    }
}

//Extra
class Cola{

    public String[] elementos;
    public int tamaño;

    public Cola(int capacidad) {
        elementos = new String[capacidad];
        this.tamaño = 0;
    }

    void insertar(String elemento){
        if( tamaño == elementos.length ){
            System.out.println("La cola esta llena");
            return;
        }
        elementos[tamaño] = elemento;
        tamaño ++;
    }

    void eliminar (){
        if(tamaño == 0 ){
            System.out.println("La cola esta vacia");
        }
        String aux = elementos[0];


        for ( int i = 0 ; i < tamaño -1 ; i++){
            elementos[i] = elementos[i+1];
        }
        elementos[tamaño -1] = null;
        tamaño --;
        System.out.println("Elemento eliminado: " + aux);

    }

    int numeroElementos(){
       return this.tamaño ;
    }

    void contenido(){
        for(int i = 0; i < tamaño; i++){
            System.out.println( elementos[i]);
        }
    }

}



class Pila{
    int[] elementos;
    int tamaño ;

    public Pila(int capacidad) {
        elementos = new int[capacidad];
        this.tamaño = 0;
    }

    void añadir ( int elemento){
        elementos[tamaño] = elemento;
        tamaño ++;
    }

    void contenido() {
        for (int i = tamaño - 1; i >= 0; i--) {
            System.out.println(elementos[i]);
        }
    }

    void eliminar() {
        if (tamaño == 0) {
            System.out.println("La pila esta vacia");
            return;
        }
        int aux = elementos[tamaño - 1];
        elementos[tamaño - 1] = 0;
        tamaño--;
        System.out.println("Elemento eliminado: " + aux);
    }
    int numeroElementos(){
        return tamaño;
    }
}
