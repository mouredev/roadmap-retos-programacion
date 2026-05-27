/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convención que debes de respetar para que el código se entienda.
 */
public class RodrigoGit87 {
        protected String nombre;

        public RodrigoGit87(String nombre) {
            this.nombre = nombre;
        }

    // Metodo sin retorno ni parametros
    public void metodoVacio(){
        System.out.println("Esto es un metodo void o vacio, y sin parametros");
    }
    //Metodo con un parametro, sin retorno
    public void metodoVacio2(int numero){
        System.out.println("ESto es un metodo void con parametro  int: " + numero );
    }
    // no se puede crear un metodo dentro de otro
//    public void metodoExterior(){
//        public void metodoInterior() {
//            System.out.println(" No se puede un metodo dentro de otro ");
//        }
//    }
    // Metodo con parametro y retorno tipo String
    public String validarEdad(int edad){
        String mensaje = "";
        if(edad<18){
            mensaje= "Eres menor de edad";
        }
        else {
            mensaje= "Eres mayor de edad";
        }
        return mensaje;
    }
    //Metodo con 2 parametros y retorno tipo Boolean
    public boolean encenderCalefaccion (int temperatura, String estacion) {
        if (temperatura < 20 || estacion.trim().equalsIgnoreCase("invierno")){
            System.out.println( " Hace un frio del carajo ");
            return true;
        } else return false;
    }
    // EXTRA
    public int vecesImpresion ( String texto1, String texto2){
            int contador = 0;
            int numero;
            //imprimir numeros del 1 al 100
            for (int i=1; i<= 100 ; i++){
                numero = i;
                // Condiciones

                if  ((numero % 3 == 0) && (numero % 5 == 0)){
                    System.out.println(numero + ": " + texto1 + " \n "+numero +": "+ texto2);
                }else if (numero % 5 == 0) {
                    System.out.println(numero +": "+ texto2);
                } else if ( numero % 3 == 0) {
                    System.out.println(numero + ": " + texto1);
                } else  {
                    System.out.println(numero);
                    contador ++;
                }
            }
            System.out.println( contador + " veces se han impreso números( sin contar múltiplos)");
            return contador;
    }

    //Campo de batalla :P
        public static void main (String[]args){

        var rodrigoGit87 = new RodrigoGit87("RodrigoGit87");
        rodrigoGit87.metodoVacio();
        rodrigoGit87.metodoVacio2(3);
        System.out.println(rodrigoGit87.validarEdad(38));
        rodrigoGit87.encenderCalefaccion(9, "primavera");
        rodrigoGit87.vecesImpresion(" es múltiplo de 3 :P ", " es múltiplo de 5 :) ");

        }
    }



