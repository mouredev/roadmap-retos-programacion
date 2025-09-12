import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;

public class miguelex{
    public static void main(String[] args){
        Stack<Integer> pila = new Stack<Integer>();
        Queue<Integer> cola = new LinkedList<Integer>();
        
        pila.push(1);

        System.out.println("Pila: " + pila);
        pila.push(2);
        pila.push(3);
        System.out.println("\nPila: " + pila);
        pila.pop();
        System.out.println("\nPila: " + pila);

        cola.add(1);
        System.out.println("\nCola: " + cola);
        cola.add(2);
        cola.add(3);
        System.out.println("\nCola: " + cola);
        cola.poll();
        System.out.println("\nCola: " + cola);

        Stack<String> pilaNavegacion = new Stack<String>();
        Queue<String> colaImpresion = new LinkedList<String>();

        Scanner sc = new Scanner(System.in);
        String url = "";

        System.out.println("Simulando navegador:");
        while(!url.equals("salir")){
            System.out.println("Ingrese la URL a visitar: ");
            url = sc.nextLine();
            switch (url){
                case "atras":
                    if(pilaNavegacion.size() > 1){
                        colaImpresion.add(pilaNavegacion.pop());
                        System.out.println("Se ha regresado a la página: " + pilaNavegacion.peek());
                    }else{
                        System.out.println("No hay páginas para regresar");
                    }
                    break;
                case "adelante":
                    if(colaImpresion.size() > 0){
                        pilaNavegacion.push(colaImpresion.poll());
                        System.out.println("Se ha avanzado a la página: " + pilaNavegacion.peek());
                    }else{
                        System.out.println("No hay páginas para avanzar");
                    }
                    break;
                case "salir":
                    System.out.println("Saliendo del navegador");
                    break;
                default:
                    pilaNavegacion.push(url);
                    System.out.println("Se ha visitado la página: " + pilaNavegacion.peek());
                    break;
            }
        }
        System.out.println("Simulando cola de impresion");
        String documento = "";

        while(!documento.equals("salir")){
            System.out.println("Ingrese el documento a imprimir: ");
            documento = sc.nextLine();
            if(!documento.equals("salir")){
                switch (documento){
                    case "imprimir":
                        if(colaImpresion.size() > 0){
                            System.out.println("Imprimiendo documento: " + colaImpresion.poll());
                        }else{
                            System.out.println("No hay documentos para imprimir");
                        }
                        break;
                    case "salir":
                        System.out.println("Saliendo de la cola de impresion");
                        break;
                    default:
                        colaImpresion.add(documento);
                        System.out.println("Se ha agregado el documento: " + documento + " a la cola de impresion");
                        break;
                }
            }
        }

    }
}