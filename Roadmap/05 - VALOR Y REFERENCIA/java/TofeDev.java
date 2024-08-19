public class TofeDev {
    public static void main(String[] args) {

        int valor = 20;
        String str = "String inmutable";
        Objeto obj1 = new Objeto();
        obj1.setNombre("Primero");


        //Asignación por valor
        int valorCopia = valor;
        valor = 25;

        //Asignaciones por referencia
        modificarObjeto(obj1);

        //Los Strings son inmutables
        moficicarString(str);

        System.out.println("Int modificado: " + valor); // 25
        System.out.println("Int sin modificar: " + valorCopia); // 20
        System.out.println("Objeto modificado por referencia: " + obj1.getNombre()); // "Segundo"
        System.out.println("String 'Modificado': " + str); // "String inmutable"
        
        /* DIFICULTAD EXTRA (opcional):
        * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
        * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
        *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
        *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
        *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
        *   Comprueba también que se ha conservado el valor original en las primeras.
        */

        //Modificación por valor
        int a = 5;
        int b = 10;
        System.out.println("a = " + a + " ; b = " + b);

        int[] modificacionValor = modificarPorValor(a, b);
        System.out.println("a = " + a + " ; b = " + b);
        System.out.println("a = " + modificacionValor[0] + " ; b = " + modificacionValor[1]);

        //Modificación por referencia
        Objeto objetoA = new Objeto();
        objetoA.setNombre("Caja Amarilla");
        objetoA.setNumero(12);

        Objeto objetoB = new Objeto();
        objetoB.setNombre("Caja Roja");
        objetoB.setNumero(26);

        System.out.println("Objeto A: " + objetoA.getNombre() + ", " + objetoA.getNumero() + " Objeto B: " + objetoB.getNombre() + ", " + objetoB.getNumero());


        modificarPorReferencia(objetoA, objetoB);

        System.out.println("Objeto A: " + objetoA.getNombre() + ", " + objetoA.getNumero() + " Objeto B: " + objetoB.getNombre() + ", " + objetoB.getNumero());
    }

    public static void moficicarString(String frase) {
        frase = "String modificada";
    }

    public static void modificarObjeto(Objeto mod) {
        mod.setNombre("Segundo");
    }

    public static int[] modificarPorValor(int uno, int dos) {
        int temp = uno;
        uno = dos;
        dos = temp;
        return new int[]{uno, dos};
    }

    public static void modificarPorReferencia(Objeto ref1, Objeto ref2) {
        Objeto hold = new Objeto();
        hold.setNombre("");
        hold.setNumero(0);

        hold.setNombre(ref1.getNombre());
        hold.setNumero(ref1.getNumero());

        ref1.setNombre(ref2.getNombre());
        ref1.setNumero(ref2.getNumero());

        ref2.setNombre(hold.getNombre());
        ref2.setNumero(hold.getNumero());
    }
}

class Objeto {
    private String nombre;
    private int numero;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }
}