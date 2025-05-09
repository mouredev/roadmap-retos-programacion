public class TofeDev {
    public static void main(String[] args) throws Exception {
         
        int num1= 10, num2 = 0;
        int resultado;

        try {
            resultado = num1/num2;
            System.out.println(resultado);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            System.out.println("Se ha realizado la operación");
        }

        //Extra
        Calculadora calculadora = new Calculadora();
        
        try {
            resultado = calculadora.dividir(num1, num2);
            System.out.println(resultado);
            System.out.println("Se ha realizado la operación con éxito");
        } catch (CalcException e) {
            e.printStackTrace();
        } finally {
            System.out.println("Programa finalizado");
        }

        try {
            resultado = calculadora.resto(num1, num2);
            System.out.println(resultado);
            System.out.println("Se ha realizado la operación con éxito");
        } catch (CalcException e) {
            e.printStackTrace();
        } finally {
            System.out.println("Programa finalizado");
        }

        int[] array = new int[5];
        try {
            array[7] = 7;
        } catch (Exception e) {
            System.out.println("Index fuera de rango");
        } finally {
            System.out.println("Programa finalizado");
        }
    }

    /* DIFICULTAD EXTRA (opcional):
    * Crea una función que sea capaz de procesar parámetros, pero que también
    * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
    * corresponderse con un tipo de excepción creada por nosotros de manera
    * personalizada, y debe ser lanzada de manera manual) en caso de error.
    * - Captura todas las excepciones desde el lugar donde llamas a la función.
    * - Imprime el tipo de error.
    * - Imprime si no se ha producido ningún error.
    * - Imprime que la ejecución ha finalizado. 
    */

    public static class Calculadora {

        public int dividir(int dividendo, int divisor) throws CalcException {
            if (divisor == 0) throw new CalcException("No se puede dividir por cero");
            return dividendo/divisor;
        }

        public int resto(int dividendo, int divisor) throws CalcException {
            if (divisor == 0) throw new CalcException("No se puede sacar el resto si el divisor es 0");
            return dividendo%divisor;
        }

    }

    public static class CalcException extends Exception {

        String descripcion;
        
        public CalcException(String descripcion) {
            setDescripcion(descripcion);
        }
        
        @Override
        public String getMessage() {
            return getDescripcion();
        }
        
        //Getters y setters
        public String getDescripcion() {
            return descripcion;
        }
        
        public void setDescripcion(String descripcion) {
            this.descripcion = descripcion;
        }
    }
}
