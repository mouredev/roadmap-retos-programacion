public class LogicaJava02 {
    
    // 1.
    public static void saludar() {
            System.out.println("Hola");
        }

    public static void saludarA(String nombre) {
        System.out.println("Hola, " + nombre);
    }

    public static void saludarALautaro(String nombre, String apellido) {
        System.out.println("Hola, " + nombre + " " + apellido);
    }

    public static int edad() {
        return 21;
    }

    public static String nombreCompleto (String nombre, String apellido) {
        return nombre + apellido;
    }
    
    /*
        2.
        En Java no se pueden anidar funciones.
        Y los métodos siempre van a nivel de clase.
    */
    
    // 4.
    static String nombre = "Lautaro";
    static String apellido = "Risso";
    
    // EXTRA
    public static int imprimirNumeros(String texto1, String texto2) {
        int cont = 0;
        for (int i=1;i<101;i++) {
            if (i%15 == 0) {
                System.out.println(texto1 + texto2);
            } else if (i%3==0) {
                System.out.println(texto1);
            } else if (i%5==0) {
                System.out.println(texto2);
            } else {
                System.out.println(i);
                cont++;
            }
        }
        return cont;
    }
    
    public static void main(String[] args) {
        // 3.
        // 4.
        int longitud = nombre.length();
        
        // 5.
        System.out.println(longitud);
        saludar();
        saludarA(nombre);
        saludarALautaro(nombre, apellido);
        edad();
        nombreCompleto(nombre, apellido);
        
        // EXTRA
        imprimirNumeros("Hola, soy texto 1","Hola, soy texto 2");
    }
}
