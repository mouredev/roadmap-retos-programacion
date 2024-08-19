/**
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 * 
 * @version v1.0
 * 
 * @since 01/07/2024
 * 
 * @author GlossyPath
 */

public class GlossyPath {
    
    /*
     * Descripción: mètodo para cambiar notas por referencia.
     */
    public static void nuevaNotaReferencia(double[] notas){

        notas[0] = 8.5d;
    }
    /*
     * Descripción: método para cambiar nota por valor.
     */
    public static void nuevaNota(double nota){

        nota = 9d;
        System.out.println(String.format("Nota dentro del método = %s",nota));

    }


    public static void main(String[] args) {
        
        System.out.println("\n----------Por valor------------");
        //los tipos primitivos se pasan por valor (copia del dato)
        double nota = 7.5d;
        System.out.println(String.format("Nota antes de pasar por valor = %s ",nota));

        nuevaNota(nota);

        System.out.println(String.format("Nota después de pasar por el método por valor = %s", nota));

        //los arreglos y objetos se pasan por referencia.

        System.out.println("\n----------Por referencia------------");
        double[] notaReferencia = {5.5};

        for(double notaRef: notaReferencia){
            System.out.println( "Antes de pasar por referencia = " + notaRef);
        }

        nuevaNotaReferencia(notaReferencia);

        for(double notaRef: notaReferencia){
            System.out.println("Despues de pasar al método por referencia = " +notaRef);
        }


        System.out.println("\n------DIFICULTAD EXTRA------");

        Programa p1 = new Programa("Sheila", "Laura");  
        Programa p2 = new Programa("Carlos", "Lorenzo");

        System.out.println("CAMBIO POR VALOR");
        p1.cambioPorValor(p1.getParametro1(), p1.getParametro2(), p2.getParametro1(), p2.getParametro2());
        System.out.println(p1.toString("p1"));
        System.out.println(p2.toString("p2"));

        System.out.println("CAMBIO POR REFERENCIA");
        p1.cambioPorReferencia(p1, p2);
        System.out.println(p1.toString("p1"));
        System.out.println(p2.toString("p2"));

        }
    }

    class Programa {

        private String parametro1;
        private String parametro2;

        public Programa(String parametro1, String parametro2){

            this.parametro1 = parametro1;
            this.parametro2 = parametro2;
        }

        public String getParametro1() {
            return parametro1;
        }

        public void setParametro1(String parametro1) {
            this.parametro1 = parametro1;
        }

        public String getParametro2() {
            return parametro2;
        }

        public void setParametro2(String parametro2) {
            this.parametro2 = parametro2;
        }

        public void cambioPorValor(String s1, String s2, String s3, String s4){

            String aux = s1;
            s1 = s3;
            s3 = aux;
            aux = s2;
            s2 = s4;
            s4 = aux;

            System.out.println(s1);
        }

        public void cambioPorReferencia(Programa p1,  Programa p2){

            String aux = p1.getParametro1();
            p1.setParametro1(p2.getParametro1());
            p2.setParametro1(aux);
            aux = p1.getParametro2();
            p1.setParametro2(p2.getParametro2());
            p2.setParametro2(aux);

        }

        public String toString(String programa){

            return ("Programa: " + programa +
            "\nparametro1: " + parametro1 +
            "\nparametro2: " + parametro2
            );
        }
    }

