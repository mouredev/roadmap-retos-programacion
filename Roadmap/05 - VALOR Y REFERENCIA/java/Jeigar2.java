public class Jeigar2 {
    /*
     * EJERCICIO:
     * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
     *   su tipo de dato.
     * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
     *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
     * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
     *
     * DIFICULTAD EXTRA (opcional):
     * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
     * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
     *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
     *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
     *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
     *   Comprueba también que se ha conservado el valor original en las primeras.
     */

    private String nombre;
    private int edad;

    public Jeigar2(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public static void cambiarEdadValor(int edad) {
        edad = cambiarEdadValorRetorno(edad);
    }

    public static int cambiarEdadValorRetorno(int edad) {
        edad = edad * 2 + 1;
        return edad;
    }

    public static void cambiarNombreValor(String nombre) {
        nombre = cambiarNombreValorRetorno(nombre);
    }

    public static String cambiarNombreValorRetorno(String nombre) {
        nombre = "_" + nombre.toUpperCase() + "_";
        return nombre;
    }

    public static void cambiarEdadReferencia(Jeigar2 jeigar2) {
        cambiarEdadReferenciaRetorno(jeigar2);
    }

    public static int cambiarEdadReferenciaRetorno(Jeigar2 jeigar2) {
        jeigar2.setEdad(cambiarEdadValorRetorno(jeigar2.getEdad()));
        return jeigar2.getEdad();
    }

    public static void cambiarNombreReferencia(Jeigar2 jeigar2) {
        cambiarNombreReferenciaRetorno(jeigar2);
    }

    public static String cambiarNombreReferenciaRetorno(Jeigar2 jeigar2) {
        jeigar2.setNombre(cambiarNombreValorRetorno(jeigar2.getNombre()));
        return jeigar2.getNombre();
    }

    public static void main(String[] args) {
        Jeigar2 jeigar2 = new Jeigar2("Jesús", 33);

        System.out.println(String.format("# Antes: %s, %d", jeigar2.getNombre(), jeigar2.getEdad()));

        // Por valor no se modifica
        System.out.println("POR VALOR No cambia");
        cambiarEdadValor(jeigar2.getEdad());
        cambiarNombreValor(jeigar2.getNombre());
        System.out.println(String.format("- Después Valor 1: %s, %d", jeigar2.getNombre(), jeigar2.getEdad()));
        int edadCambio = cambiarEdadValorRetorno(jeigar2.getEdad());
        String nombreCambio = cambiarNombreValorRetorno(jeigar2.getNombre());
        System.out.println(String.format("- Después Valor 2: %s, %d", jeigar2.getNombre(), jeigar2.getEdad()));
        System.out.println(String.format("+ Después Retorno 2.1: %s, %d", nombreCambio, edadCambio));

        // Por referencia si se modifica
        System.out.println("POR REFERENCIA Sí cambia");
        cambiarEdadReferencia(jeigar2);
        cambiarNombreReferencia(jeigar2);
        System.out.println(String.format("+ Después Referencia 3 : %s, %d", jeigar2.getNombre(), jeigar2.getEdad()));
        cambiarEdadReferencia(jeigar2);
        edadCambio = cambiarEdadReferenciaRetorno(jeigar2);
        nombreCambio = cambiarNombreReferenciaRetorno(jeigar2);
        System.out.println(String.format("+ Después Referencia 4: %s, %d", jeigar2.getNombre(), jeigar2.getEdad()));
        System.out.println(String.format("+ Después Retorno 4.1: %s, %d", nombreCambio, edadCambio));

        System.out.println("\n ---- EXTRA ---- \n");

        Programa programa1 = new Programa("p1 Olivo", "p1 Palma");
        Programa programa2 = new Programa("p2 Getsemani", "p2 Tabor");
        System.out.println("# Antes " + programa1.toString("p1"));
        System.out.println("# Antes " + programa2.toString("p2"));

        System.out.println("POR VALOR No cambia");
        programa1.cambioValor(programa1.getParam1(), programa1.getParam2(), programa2.getParam1(), programa2.getParam2());
        System.out.println("- Después valor " + programa1.toString("p1"));
        System.out.println("- Después valor " + programa2.toString("p2"));

        System.out.println("POR REFERENCIA Sí cambia");
        programa1.cambioReferencia(programa1, programa2);
        System.out.println("+ Después referencia " + programa1.toString("p1"));
        System.out.println("+ Después referencia " + programa2.toString("p2"));
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
}
/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

class Programa {
    private String param1;
    private String param2;

    public Programa(String param1, String param2) {
        this.param1 = param1;
        this.param2 = param2;
    }

    public String getParam2() {
        return param2;
    }

    public void setParam2(String param2) {
        this.param2 = param2;
    }

    public String getParam1() {
        return param1;
    }

    public void setParam1(String param1) {
        this.param1 = param1;
    }

    public void cambioValor(String p11, String p12, String p21, String p22) {
        String aux = p11;
        p11 = p21;
        p21 = aux;
        aux = p12;
        p12 = p22;
        p22 = aux;
    }

    public void cambioReferencia(Programa p1, Programa p2) {
        String aux = p1.getParam1();
        p1.setParam1(p2.getParam1());
        p2.setParam1(aux);
        aux = p1.getParam2();
        p1.setParam2(p2.getParam2());
        p2.setParam2(aux);
    }

    public String toString(String sufijo) {
        return "Programa (" + sufijo + "){" +
                "param1='" + param1 + '\'' +
                ", param2='" + param2 + '\'' +
                '}';
    }
}


