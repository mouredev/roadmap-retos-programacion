public class Maynor06 {

    //function that salute
    public void hola (){
        System.out.println("Hola");
    }

    // with parameters
    public void suma(int a, int b){
        int c = a + b;
        System.out.println("la suma es: " + c);
    }

    // with parameters and return
    public String personalizedGreeting(String name, String lastName){
        return "Hola " + name + " " + lastName;
    }

    public int dobleOfAPlus(int a, int b){

        int suma = a + b;
        int resultado = suma *2;
        return resultado;
    }
    public int numGlobal1 = 50;
    public int numGlobal2 = 30;

    public int extra(String a, String b){
        int contador = 0;
        for (int i = 1; i <= 100; i++){
            if(i % 3 == 0 && i % 5 == 0){
                System.out.println("numero:" + i + a + b);
            } else if (i % 3 == 0 ) {
                System.out.println("numero:" + i + a);
            } else if (i % 5 == 0) {
                System.out.println("numero:" + i + b);
            }else {
                contador++;
            }
        }
        System.out.println("las veces que se a imprimido el numero son: " + contador);
        return contador;
    }

    public static void main(String[] args) {


        //variables locales

        int num1 = 10;
        int num2 = 20;

        Maynor06 ejemplo = new Maynor06();
        ejemplo.hola();
        ejemplo.suma(num1, num2);

        String salute = ejemplo.personalizedGreeting("John", "Doe");
        System.out.println(salute);
        System.out.println();

        // utilizamos la funcion valueOf para convertir un string a entero
        int casteo = Integer.valueOf("100");

        int resultado = casteo + ejemplo.numGlobal1  + ejemplo.numGlobal2;
        System.out.println("la suma del casteo mas las variables globales es: " +  resultado);

        Maynor06 ejemplo1 = new Maynor06();
        ejemplo1.extra("  este es el primer parametro", "  este es el segundo parametro");

    }
}
