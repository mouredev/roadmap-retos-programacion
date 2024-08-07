public class GustavoGomez19 {

   /*
    * Asignación de varialbles por valor: La asignación de una variable por valor
    * es el proceso de copiar el valor
    * de una variable original a una nueva ubicación en memoria, cualquier
    * modificación en la variable copiada
    * no afectará la variable original. En Java los tipos de datos primitivos se
    * asignan por valor
    */

   /*
    * Asignación de valor por referencia: En Java las variables de tipo objeto se
    * asignan por referencia, lo que quiere
    * decir que cuando se asigna un objeto a una variable, se asigna una referencia
    * al objeto en lugar del objeto mismo.
    * La referencia es esencialmente una dirección en memoria donde se encuentra
    * almacenado el objeto.
    * Cuando se pasa una variable de objeto por parámetro a un método, también se
    * pasa la referencia al objeto, no el objeto
    * en si mismo, cualquier modificación del objeto dentro del método se reflejará
    * en el objeto original.
    */

   // Ejemplo de asignación por valor
   static int original = 10;
   static int copia = original;

   // Ejemplo paso por referencia
   static class Persona {
      String nombre;

      public Persona(String nombre) {
         this.nombre = nombre;
      }
   }

   public static void main(String[] args) {
      // Impresión de los valores de las variables asignadas por valor
      System.out.println("Valor de la variable original: " + original);
      System.out.println("Valor de la variable copia: " + copia);

      cmabioValorCopia(copia);

      System.out.println("El valor dela variable original se mantiene sin modificaciones. " + original);

      // Creación de los objetos de la clase "Persona"
      Persona persona1 = new Persona("Gustavo"); // Se asigna el valor al objeto persona1
      Persona persona2 = persona1; // Se asigna por referencia al objeto persona2 el objeto persona1

      // Impresión por terminal de los objetos
      System.out.println("Nombre persona 1: " + persona1.nombre);
      System.out.println("Nombre persona 2: " + persona2.nombre);

      // Modificación del nombre de persona2
      persona2.nombre = "Katerine";
      System.out.println("Nombre persona 1 modidifado : " + persona1.nombre);
      System.out.println("Nombre persona 2 modidifado : " + persona2.nombre);

      persona1.nombre = cambioDeValorPorReferencia("María José");
      System.out.println("Nombre persona 1 modidifado por método: " + persona1.nombre);
      System.out.println("Nombre persona 2 modidifado por método: " + persona2.nombre);

      // Por valor
      int num1 = 10;
      int num2 = 7;
      System.out.println("Valores originales: ");
      System.out.println("num1: " + num1 + ", num2: " + num2);
      int[] cambio = cambioPorValor(num1, num2);
      System.out.println("Variables intercambiadas: ");
      System.out.println("num1: " + cambio[0] + " - num2: " + cambio[1]);

      // Por referencia
      int[] c = {17};
      int[] d = {19};
      System.out.println("Variables originales");
      System.out.println("c[0] " + c[0] + " | " + "d[0] " + d[0]);
      int[] e = cambioPorReferencia(c, d);
      System.out.println("Variables intercambiadas");
      System.out.println("c[0] " + e[0] + " | " + "d[0] " + e[0]);

   }

   // Método para cambiar el valor de la variable copia
   public static void cmabioValorCopia(int copia) {
      copia = 20;
      System.out.println("Nuevo valor de la variable copia: " + copia);
   }

   // Método para cambiar el valor por referencia
   public static String cambioDeValorPorReferencia(String nombre) {
      return nombre;
   }

   /* Desafio dificultad extra: Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
    * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
        Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
        se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
        variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
        Comprueba también que se ha conservado el valor original en las primeras.
    */

    // Por valor
    

    public static int[] cambioPorValor(int num1, int num2){
      int aux = num1;
      num1 = num2;
      num2 = aux;
      return new int[] {num1, num2};
    }

    // Por referencia
    public static int[] cambioPorReferencia(int[]a, int[]b){
      int aux = a[0];
      a[0] = b[0];
      b[0] = aux;
      return new int[] {a[0], b[0]};
    }

}