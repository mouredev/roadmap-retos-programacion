public class Jeigar2 {
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

    public static void main(String[] args) {
        boolean errores = false;
        try {
            int i = 10/0;
        }catch (ArithmeticException e) {
            System.out.println(e.toString());
        }

        try {
//            recibeParametros("123456789", "Jorge Lopez Borrego", "Texto");// error de tiempo
//            recibeParametros("123456789", "Jorge", "23"); // error de titular no tiene nombre compleo
//            recibeParametros("bb-3456789", "Jorge Lopez Borrego", "23"); // error de telefono mal formato
            recibeParametros("123456789", "Jorge Lopez Borrego", "23"); // sin errores
        } catch (NumberFormatException e) {
            System.err.println("el parametro no está bien inicializado " + e.getMessage());
            errores = true;
        } catch (IndexOutOfBoundsException e){
            System.err.println("El valor es demasiado corto debe poner nombre y apellido " + e.getMessage());
            errores = true;
        } catch (TelefonoMalFormadoException e) {
            System.err.println("El telefono está mal expresado " + e.getMessage());
            errores = true;
        }
        if(!errores) {
            System.out.println("No se ha producido ningun tipo de error");
        }
        System.out.println("La ejecución ha finalizado");

    }

    public static void recibeParametros(String telefono, String titular, String tiempo) throws NumberFormatException, IndexOutOfBoundsException, TelefonoMalFormadoException{
        int tempo = Integer.parseInt(tiempo);
        String nombreTroceado[] =  titular.split(" ");
        String apellido1 = nombreTroceado[1];
        if(telefono.length() != 9 || telefono.toUpperCase() != telefono.toLowerCase()){
            throw new TelefonoMalFormadoException(telefono);
        }

    }

}
class TelefonoMalFormadoException extends Exception {
    public TelefonoMalFormadoException(){
        super();
    }
    public TelefonoMalFormadoException(String telefono){
        super(telefono);
    }
}
