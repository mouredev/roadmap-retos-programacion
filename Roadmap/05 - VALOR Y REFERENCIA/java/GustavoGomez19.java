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

}