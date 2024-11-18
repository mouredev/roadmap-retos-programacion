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

public class Alextc35 {
    public static void main(String[] args) {
        // Asignación de variables "por valor"
        System.out.println("\n--- Asignación de variables por valor ---");
        int x = 10;
        System.out.println("- Antes de llamar a la función: x = " + x);
        modificarPrimitivo(x);
        System.out.println("\n- Después de llamar a la función: x = " + x);
        System.out.println("-----------------------------------------");

        // Asignación de variables "por referencia"
        System.out.println("\n------- Asignación por referencia -------");
        Persona persona = new Persona("Alejandro");
        System.out.println("- Antes de llamar a la función:\npersona.nombre = "
                + persona.nombre);
        modificarObjeto(persona);
        System.out.println("\n- Después de llamar a la función:\npersona.nombre = "
                + persona.nombre);
        System.out.println("-----------------------------------------");

        // Modificación de Referencia de Objeto
        System.out.println("\n------- Modificación de Referencia -------");
        Persona persona2 = new Persona("Barry Allen");
        System.out.println("- Antes de llamar a la función:\npersona2.nombre = " + persona2.nombre);
        cambiarReferencia(persona2);
        System.out.println("\n- Después de llamar a la función:\npersona2.nombre = " + persona2.nombre);
        System.out.println("-----------------------------------------");

        // Opcional
        // Intercambio por valor
        System.out.println("\n--- Intercambio de valores por valor ---");
        int a = 5;
        int b = 10;
        System.out.println("\n- Antes de llamar a la función:\na = " + a + "\nb = " + b);
        // Llamada al método para intercambiar valores
        int[] resPorValor = swapPorValor(a, b);
        // Resultados después de la llamada
        int nuevoA = resPorValor[0];
        int nuevoB = resPorValor[1];
        System.out.println("\n- Después de intercambiar por valor:\na = " + a
                + "\nb = " + b + "\nnuevoA = " + nuevoA + "\nnuevoB = " + nuevoB);
        System.out.println("-----------------------------------------");

        // Intercambio por referencia
        System.out.println("\n- Intercambio de valores por referencia -");
        Par par1 = new Par(5);
        Par par2 = new Par(10);
        System.out.println("\n- Antes de llamar a la función:\npar1.valor = " + par1.valor
                + "\npar2.valor = " + par2.valor);
        // Llamada al método para intercambiar valores
        Par[] resPorReferencia = swapPorReferencia(par1, par2);
        // Resultados después de la llamada
        Par nuevoPar1 = resPorReferencia[0];
        Par nuevoPar2 = resPorReferencia[1];
        System.out.println("\n- Después de intercambiar por referencia:\npar1.valor = " + par1.valor
                + "\npar2.valor = " + par2.valor + "\nnuevoPar1.valor = " + nuevoPar1.valor
                + "\nnuevoPar2.valor = " + nuevoPar2.valor);
    }

    // Opcional MÉTODO 1
    public static int[] swapPorValor(int x, int y) {
        int temp = x;
        x = y;
        y = temp;
        return new int[] { x, y };
    }

    // Opcional MÉTODO 2
    public static Par[] swapPorReferencia(Par p1, Par p2) {
        int temp = p1.valor;
        p1.valor = p2.valor;
        p2.valor = temp;
        return new Par[] { p1, p2 };
    }

    // Asignación de variables "por valor"
    public static void modificarPrimitivo(int a) {
        a = 20; // Modifica la copia local, no afecta a la variable original
    }

    // Asignación de variables "por referencia"
    public static void modificarObjeto(Persona p) {
        p.nombre = "Alex"; // Modifica el objeto al que p apunta
    }

    // Modificación de Referencia de Objeto
    public static void cambiarReferencia(Persona p) {
        p = new Persona("The Flash"); // Cambia la referencia local, no afecta a la variable original
    }
}

// Clase Persona
class Persona {
    String nombre;

    Persona(String nombre) {
        this.nombre = nombre;
    }
}

// Opcional
// Clase que representa un par de valores
class Par {
    int valor;

    Par(int valor) {
        this.valor = valor;
    }
}