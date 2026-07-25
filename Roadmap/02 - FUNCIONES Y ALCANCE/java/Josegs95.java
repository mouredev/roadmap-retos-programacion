import java.util.Calendar;
import java.util.GregorianCalendar;

public class Josegs95 {
    public static void main(String[] args) {
        //Como voy a trabajar en el main, todos los métodos que cree serán estáticos
        saludame();
        System.out.println(getSaludo());
        saludamePorMiNombre("Jose");
        System.out.println(getSaludoPorMiNombre("Jose"));
        System.out.println(getSaludoPorMiNombre("Jose", "Adiós"));
        System.out.println("La hora actual es: " + getHora());
        imprimeCadena();

        int n = retoFinal("Esta es la cadena 1", "Esta es la cadena 2");
        System.out.println("Veces que se ha impreso solo el número: " + n);
    }

    //Método sin argumentos ni retorno
    public static void saludame(){
        System.out.println("Hola!");
    }

    //Método sin argumentos pero con retorno
    public static String getSaludo(){
        return "Hola!";
    }

    //Método con argumentos pero sin retorno
    public static void saludamePorMiNombre(String nombre){
        System.out.println("Hola, " + nombre + "!");
    }

    //Método con argumentos y con retorno
    public static String getSaludoPorMiNombre(String nombre){
        return "Hola, " + nombre + "!";
    }

    //Ejemplo de método sobrecargado (mismo nombre), varios argumentos y retorno
    public static String getSaludoPorMiNombre(String nombre, String saludo){
        return saludo + ", " + nombre + "!";
    }

    //No se puede crear un método dentro de otro método en Java
//    public static void imprimeHora(){
//        public static String getHora(){
//            return "" + Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
//        }
//        System.out.println(getHora);
//    }

    //Ejemplo de métodos ya creados + concadenación de métodos
    public static String getHora(){
        return "" + Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
    }

    //Concepto de variable local y global
    static String cadena = "Global";
    public static void imprimeCadena(){
        String cadena = "Local";
        System.out.println("Variable local: " + cadena);
        System.out.println("Variable global: " + Josegs95.cadena);
        //Esto es así porque estoy trabajando en un entorno estático
        //Si fuera en un entorno no estático, se usaría this.cadena para referenciar a la
        //variable global.
    }

    public static int retoFinal(String cad1, String cad2){
        int contador = 0;

        for (int i = 1; i < 101; i++){
            if (i % 3 == 0){
                if (i % 5 == 0){
                    System.out.println(i + ": " + cad1 + ", " + cad2);
                    continue;
                }
                System.out.println(i + ": " + cad1);
            } else if (i % 5 == 0) {
                System.out.println(i + ": " + cad2);
            } else {
                System.out.println(i);
                contador++;
            }
        }

        return contador;
    }
}
