package _08_Clases;
import java.util.LinkedList;
import java.util.Stack;
import java.util.Queue;
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */


public class _08_Clases {
    public String Nombre;
    public String Saludo;

    //Creamos el constructor de la clase
    public _08_Clases(){
        this.Nombre= "";
        this.Saludo="";

    }
    //Vamos a crear una función que nos imprima el Saludo
    public void saludar(){
        System.out.println(this.Saludo+","+this.Nombre);
    }
    public static void main(String[] args){
        //Creamos una nueva instancia
        _08_Clases saludo1 = new _08_Clases();

        //Asignamos valores a los atributos
        saludo1.Nombre="Java";
        saludo1.Saludo="Hola";

        //Llamamos a la función saludar
        saludo1.saludar();

        //Modificamos los atributos
        saludo1.Nombre="ALexdevrep";
        saludo1.saludar();

        //Dificultad EXTRA Pilas

        Pila miPila = new Pila();

        //Añadimos elementos a la pila
        miPila.anadirElemento("Objeto 1");
        miPila.anadirElemento("Objeto 2");
        miPila.anadirElemento("Objeto 3");

        //Imprimimos los elementos que tenemos en la pila
        miPila.imprimirelementos();

        //Eliminamos el último elemento en entrar a la pila
        miPila.borrarElemento();

        //Imprimimos el resultado
        miPila.imprimirelementos();

        //Comprobamos que el número de elementos es el correcto
        int numero= miPila.numeroelementos();
        System.out.println("El número de elementos de la pila es: "+numero);

        //Dificultad EXTRA Colas

        Colas miCola = new Colas();

        //Añadimos objetos a la cola
        miCola.insertarObjetos("Objeto 1");
        miCola.insertarObjetos("Objeto 2");
        miCola.insertarObjetos("Objeto 3");

        //Imprimimos el resultado
        miCola.imprimirObjetos();

        //Elimimamos el primer objeto en entrar a la cola
        miCola.borrarObjetos();
        miCola.imprimirObjetos();

        //Comprobamos que el número de objetos es el correcto
         int numeroObjetos=miCola.numeroObjetos();
         System.out.println("El número de objetos que hay en la cola es: "+numeroObjetos);







    }


}

class Pila {

    private Stack<String> pilaelementos ;

    public Pila(){

        this.pilaelementos= new Stack<>();

    }
    //Añadimos un elemento a la pila
    public void anadirElemento(String ELemento){
        this.pilaelementos.push(ELemento);

    }
    //Borramos el último elemento de la pila
    public void borrarElemento(){
        this.pilaelementos.pop();
    }
    //Método para imprimir los elementos que hay en la pila
    public void imprimirelementos(){
        System.out.println("Contenido de la pila");
        for(String elemento : this.pilaelementos){
            System.out.println(elemento);
        }
    }
    //Método para saber el número de elementos que hay en la pila
    public int numeroelementos(){
        return this.pilaelementos.size();
    }


}

class Colas {
    private Queue<String> colaObjetos;

    public Colas(){
        this.colaObjetos= new LinkedList<>();

    }
    public void insertarObjetos(String Objeto){
        this.colaObjetos.add(Objeto);
    }
    public void borrarObjetos(){
        this.colaObjetos.poll();
    }
    public void imprimirObjetos(){
        System.out.println("Contenido de la cola");
        for(String Objeto : this.colaObjetos) {
            System.out.println(Objeto);
        }

    }
    public int numeroObjetos(){
        return this.colaObjetos.size();
    }

}
