public class Rubioj17 {
    static String variableGlobal = "Global";

    public static void main(String[] args) {
        int numeroDeLetras, numDeVeces;
        String nombreEdad;
        saludo();
        saludoConParametros("Rubioj17");
        saludoConParametros("Rubioj17", "Alegre");
        System.out.println(edad(20));
        nombreEdad = saludoLLamandoFuncion("Rubioj17", 20);
        System.out.println(nombreEdad);
        numeroDeLetras = usandoFuncionesDelSistema(nombreEdad);
        System.out.println("En la anterior oracion hay " + numeroDeLetras + " carateres");
        localGlobal();
        numDeVeces = dificultadExtra("Primer Texto", "Segundo Texto");
        System.out.println("\nLos Numeros se Imprimieron " + numDeVeces);
    }
    //Sin parámetros ni retorno,
    static void saludo() {
        System.out.println("Hola");
    }

    //Con uno o varios parámetros
    static void saludoConParametros(String nombre) {
        System.out.println("Hola " + nombre);
    }

    static void saludoConParametros(String nombre, String estadoEmocional) {
        System.out.println("Hola " + nombre + ", hoy te encuentras " + estadoEmocional);
    }

    //Con retorno
    static int edad(int n) {
        return n;
    }

    //Comprueba si puedes crear funciones dentro de funciones.
    //* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    //*Por lo que tengo entendido no se pueden crear funciones*
    //*dentro de funciones a menos que se use lambda          *
    //* * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    //LLamar funciones dentro de otras funciones
    static String saludoLLamandoFuncion(String nombre, int n) {
        return "Hola " + nombre + " tienes " + edad(n) + " Años";
    }

    //Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    static int usandoFuncionesDelSistema(String palabra) {
        return palabra.length();
    }

    //Pon a prueba el concepto de variable LOCAL y GLOBAL.
    static void localGlobal() {
        String variableLocal = "Local";
        System.out.println(variableGlobal + " "+ variableLocal);
    }

    //* * * * * * * * * *
    //*DIFICULTAD EXTRA *
    //* * * * * * * * * *
    static int dificultadExtra(String texto1, String texto2) {
        int c = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) System.out.print(texto1+texto2);
            else if (i % 3 == 0) System.out.print(texto1);
            else if (i % 5 == 0) System.out.print(texto2);
            else {
                System.out.print(" "+ i + ",");
                c++;
            }
        }
        return c;
    }
}
