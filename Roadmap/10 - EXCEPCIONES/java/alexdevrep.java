package _10_Excepciones;

import java.util.ArrayList;

public class _10_Excepciones {



    /*
     * EJERCICIO:
     * Explora el concepto de manejo de excepciones según tu lenguaje.
     * Fuerza un error en tu código, captura el error, imprime dicho error
     * y evita que el programa se detenga de manera inesperada.
     * Prueba a dividir "10/0" o acceder a un índice no existente
     * de un listado para intentar provocar un error.
     *
     * DIFICULTAD EXTRA (opcional):
     * Crea una función que sea capaz de procesar parámetros, pero que también
     * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
     * corresponderse con un tipo de excepción creada por nosotros de manera
     * personalizada, y debe ser lanzada de manera manual) en caso de error.
     * - Captura todas las excepciones desde el lugar donde llamas a la función.
     * - Imprime el tipo de error.
     * - Imprime si no se ha producido ningún error.
     * - Imprime que la ejecución ha finalizado.
     */
    public static void main(String[] args){
        //Declaramos las variables necesarias
        int numero1= 10;
        int numero2= 0;
        //Creamos un listado y le insertamos los objetos que van en el
        ArrayList<String> listado = new ArrayList<String>();
        listado.add("Hola");
        listado.add("Java");
        listado.add("Mundo");
        listado.add("Alexdevrep");

        try{
            //Intentamos dividir ambos numeros
            int resultado= dividir(numero1,numero2);
            System.out.println(resultado);
        }
        catch(ArithmeticException e){ //Tipo de excepción predefinida para una división por 0
            System.out.println("No se puede dividir un número por cero");
        }
        finally{
            System.out.println("Programa finalizado");
        }

        try{
            //Intentamos acceder a un indice del array que no existe
            System.out.println(listado.get(5));
        }
        catch(IndexOutOfBoundsException e){ //Tipo de excepción predefinida para cuando no existe indice en el array
            System.out.println("Indice no existente");
        }
        finally {
            System.out.println("Cerrando el programa");
        }

        //Dificultad EXTRA
        //Declaramos una varible más
        int numero3= 2;

        try{
            int producto=multiplo (numero3);

            if (numero3 < 0) {
                throw new numeroNegativo("El número no puede ser negativo");
            }
            else if (String.valueOf(numero3).length()>1){
                throw new dosCifras("El número no puede tener más de una cifra");
            }
            else{
                System.out.println(producto);
            }

        }
        catch(NumberFormatException e){
            System.out.println("Debe de existir un número obligatorio");

        }
        catch(numeroNegativo e){
            System.out.println(e.getMessage());

        }
        catch(dosCifras e){
            System.out.println(e.getMessage());
        }
        finally{
            System.out.println("Cerrando el programa");
        }







    }

    public static int dividir (int numero1, int numero2) {
        return numero1 / numero2;
    }
    //Dificultad EXTRA
    public static int multiplo(int numero3){
        return 5 * numero3;
    }

    //Vamos a crear excepciones personalizadas
    static class numeroNegativo extends Exception{
        public numeroNegativo(String mensaje){
            super(mensaje);
        }

    }
    static class dosCifras extends Exception{
        public dosCifras(String mensaje1){
            super(mensaje1);
        }
    }




}
