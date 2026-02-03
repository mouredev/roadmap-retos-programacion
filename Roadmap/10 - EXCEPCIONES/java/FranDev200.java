public class FranDev200 {

    static void main() {

        /*
            EJERCICIO:
            * Explora el concepto de manejo de excepciones según tu lenguaje.
            * Fuerza un error en tu código, captura el error, imprime dicho error
            * y evita que el programa se detenga de manera inesperada.
            * Prueba a dividir "10/0" o acceder a un índice no existente de un listado para intentar provocar un error.
         */

        String[] miArray = new String[3];
        miArray[0] = "Hola";
        miArray[1] = "Mundo";
        miArray[2] = "Java";

        System.out.println("Tamaño de elementos del array: " + miArray.length);
        System.out.println("Valor numero 1: " + miArray[0]);

        try {
            System.out.println("Valor numero 4: " + miArray[3]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("\nERROR:");
            System.out.println(e.getMessage());
        }

        int a = 20;
        int b = 4;
        int c = 0;

        System.out.println("\nCUENTAS MATEMÁTICAS");
        System.out.println("-------------------");
        System.out.println("20 + 4 = " + (20 + 4));
        System.out.println("0 - 4 = " + (0 - 4));
        System.out.println("20 * 0 = " + (20 * 0));
        System.out.println("0 / 4 = " + (0 / 4));

        try {
            System.out.println("20 / 0 = " + (20 / 0));
        } catch (ArithmeticException e) {
            System.out.println("\nERROR:");
            System.out.println(e.getMessage());
        }

        System.out.println("\n----------------------");
        System.out.println("Finalizando el programa.");

    /*

        DIFICULTAD EXTRA (opcional):
        * Crea una función que sea capaz de procesar parámetros, pero que también
        * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
        * corresponderse con un tipo de excepción creada por nosotros de manera
        * personalizada, y debe ser lanzada de manera manual) en caso de error.
        * - Captura todas las excepciones desde el lugar donde llamas a la función.
        * - Imprime el tipo de error.
        * - Imprime si no se ha producido ningún error.
        * - Imprime que la ejecución ha finalizado.

     */

        System.out.println("\n\nEJERCICIO EXTRA");
        System.out.println("===============");

        // EDAD CORRECTA NO SALTAN EXCEPCIONES
        try {

            if(comprobarMayoriaDeEdad(18)){
                System.out.println("Es mayor de edad");
            }else{
                System.out.println("Es menor de edad");
            }

        } catch (NullPointerException e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }catch (IllegalArgumentException e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }catch (EdadExcesiva e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }

        System.out.println("--------------\n");
        // EDAD ELEVADA SALTA EXCEPCION PERSONALIZADA
        try {

            if(comprobarMayoriaDeEdad(230)){
                System.out.println("Es mayor de edad");
            }else{
                System.out.println("Es menor de edad");
            }

        } catch (NullPointerException e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }catch (IllegalArgumentException e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }catch (EdadExcesiva e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }

        System.out.println("--------------\n");
        // EDAD NEGATIVA SALTA EXCEPCION DE ILLEGALARGUMENT
        try {

            if(comprobarMayoriaDeEdad(-20)){
                System.out.println("Es mayor de edad");
            }else{
                System.out.println("Es menor de edad");
            }

        } catch (NullPointerException e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }catch (IllegalArgumentException e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }catch (EdadExcesiva e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }

        System.out.println("--------------\n");
        // EDAD NULL SALTA LA EXCEPCION DE NULLPOINTER
        try {

            if(comprobarMayoriaDeEdad(null)){
                System.out.println("Es mayor de edad");
            }else{
                System.out.println("Es menor de edad");
            }

        } catch (NullPointerException e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }catch (IllegalArgumentException e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }catch (EdadExcesiva e) {
            System.out.println(e.getClass().getSimpleName() + ": " + e.getMessage());
            System.out.println("Edad no valida");
        }

        System.out.println("--------------\n");
        System.out.println("Saliendo del programa...");
        System.out.println("- - - - ");

    }

    public static boolean comprobarMayoriaDeEdad(Integer edad) {

        boolean resultado = false;

        if( edad == null){
            throw new NullPointerException("La edad no puede ser nula.");
        } else if( edad < 0){
            throw new IllegalArgumentException("La edad no puede ser negativa.");
        }else if( edad > 120){
            throw new EdadExcesiva("La edad no puede ser mayor a 120.");
        }else {
            resultado = edad >= 18;
        }

        return resultado;

    }

    static class EdadExcesiva extends RuntimeException {

        public EdadExcesiva(String mensaje) {
            super(mensaje);
        }

    }

}
