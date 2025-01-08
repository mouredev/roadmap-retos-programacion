public class GustavoGomez19 {
    /* MANEJO DE EXCEPCIONES
     * EJERCICIO:
     * Explora el concepto de manejo de excepciones según tu lenguaje.
     * Fuerza un error en tu código, captura el error, imprime dicho error
     * y evita que el programa se detenga de manera inesperada.
     * Prueba a dividir "10/0" o acceder a un índice no existente
     * de un listado para intentar provocar un error. */
    public static void main(String[] args){
        ArrayList<Integer> array = new ArrayList<>();
        for (int i = 0; i < 7; i++){
            array.add(i);
        }
        try {
            array.add(8, 9);
        } catch (Exception e){
            System.out.println("Indice fuera del rango: " + e);
        }
        System.out.println(array);

        try {
            int resultado = 10 / 0;
            System.out.println("Resultado: " + resultado);
        } catch (Exception e){
            System.out.println("No se puede divir por 0!!!. " + e);
        }
        System.out.println("Finalización del programa.");

        /* DIFICULTAD EXTRA (opcional):
         * Crea una función que sea capaz de procesar parámetros, pero que también
         * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
         * corresponderse con un tipo de excepción creada por nosotros de manera
         * personalizada, y debe ser lanzada de manera manual) en caso de error.
         * - Captura todas las excepciones desde el lugar donde llamas a la función.
         * - Imprime el tipo de error.
         * - Imprime si no se ha producido ningún error.
         * - Imprime que la ejecución ha finalizado. */
        try {
            procesarParametros(-7);
            procesarParametros(0);
            procesarParametros(51);
        } catch (MiExcepcionPersonalizada e){
            System.out.println("Error personalizada: " + e.getMessage());
        }
        finally {
            System.out.println("Ejecución finalzada!.");
        }

    }
    // Extra
    static class MiExcepcionPersonalizada extends Exception{
        public MiExcepcionPersonalizada(String mensaje) {
            super(mensaje);
        }
    }

    public static void procesarParametros(int parametro) throws MiExcepcionPersonalizada{
        try {
            if (parametro < 0){
                throw  new IllegalArgumentException("El parámetro no puede ser negativo.");
            } else if (parametro == 0) {
                throw new ArithmeticException("No se puede dividir por 0.");
            } else if (parametro > 50) {
                throw new MiExcepcionPersonalizada("El parámetro es muy grande");
            }
            System.out.println("No se ha producido ningún error.");
        } catch (IllegalArgumentException e){
            System.out.println("Error: " + e.getMessage());
        } catch (ArithmeticException e){
            System.out.println("Error: " + e.getMessage());
        }

    }
}
