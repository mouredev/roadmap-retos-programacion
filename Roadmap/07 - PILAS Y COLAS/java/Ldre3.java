import java.util.ArrayList;
import java.util.List;

public class Ldre3 {
    public static void main(String[] args) {
        /*
         * EJERCICIO:
         * Implementa los mecanismos de introducción y recuperación de elementos propios de las
         * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
         * o lista (dependiendo de las posibilidades de tu lenguaje).
         */



        /*
         * DIFICULTAD EXTRA (opcional):
         * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
         *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
         *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
         *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
         *   el nombre de una nueva web.
         * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
         *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
         *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
         *   interpretan como nombres de documentos.
         */
        Historial historial = new Historial();
        System.out.println(historial.atras());
        System.out.println(historial.adelante());
        historial.navegar("asd");
        historial.navegar("asasdd");
        historial.navegar("asasaaadd");
        System.out.println(historial.atras());
        System.out.println(historial.atras());
        System.out.println(historial.adelante());
        System.out.println(historial.adelante());

        Impresora impresora = new Impresora();
        impresora.agregar("2asdd");
        impresora.agregar("2asdsddd");
        impresora.agregar("2asddaaa");
        System.out.println(impresora.imprimir());
        System.out.println(impresora.imprimir());
        System.out.println(impresora.imprimir());





    }
    public class Fifo<E> {
        private List<E> list = new ArrayList<>();

        public void add(E element){
            list.add(element);
        }

        public E get (){
            return list.get(0);
        }

    }

    public class Lifo <E> {
        private List<E> list = new ArrayList<>();

        public void add (E element){
            list.add(0,element);
        }

        public E get (){
            return list.get(0);
        }
    }

    public static class Historial {
        private ArrayList<String> historial = new ArrayList<>();
        private int indice = -1;

        public void navegar (String pagina){
            historial.add(pagina);
            indice++;
        }
        public String atras(){
            if (indice > 0){
                String retorno = historial.get(indice-1);
                indice--;
                return retorno;
            }else {
                return null;
            }
        }

        public String adelante(){
            if (indice < historial.size()-1){
                String retorno = historial.get(indice+1);
                indice++;
                return retorno;
            }
            return null;
        }
    }

    public static class Impresora {
        private ArrayList<String> documentos = new ArrayList<>();

        public void agregar(String documento){
            documentos.add(documento);
        }

        public String imprimir(){
            return documentos.remove(0);
        }
    }
}