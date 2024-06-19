public class juanca2805 {

    private static int variableGlobal = 10;
    //Variable creada a nivel global a la que se podrá acceder desde toda la clase

    public static void main(String[] args) {
        /*Funciones y alcance */
        Saludar();
        Sumar();
        Extra();
    }

    private static void buenosDias() {
        System.out.println("Buenos días");
    }

    private static void Nombre() {
        String Nombre = "pepe";
       if (Nombre == "camilo") {
        System.out.println("señor camilo");
       }
       else{
        System.out.println("Quien es usted");
       }
    }
        private static void Saludar() {
            // Llamamos a buenosDias y a Nombre
            buenosDias();
            Nombre();
        }

        private static void Sumar(){
            int variableLocal = 22;
            System.out.println(variableGlobal+variableLocal);
        }

         //Funcion con parametros
    public static void suma(int num1, int num2){
        int suma;
        suma = num1 + num2;
        System.out.println("La suma es: " + suma);
    }
      //extra

      public static void Extra(){
        for(int i = 1; i < 101; i++){
            String Texto1 = "fizz";
            String Texto2 = "buzz";
            if (i %3 == 0 && i %5 == 0) {
                System.out.println(Texto1 + Texto2);
            } 
            else if(i %3 == 0){
                System.out.println(Texto1 );
            }
            else if(i %4 == 0){
                System.out.println(Texto2 );
            }
            else {
                System.out.println(i);
               
            }
        }
      }
    }


