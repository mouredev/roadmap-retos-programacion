public class Gerthai08 {

    public static void main(String[] arg) {

        //Instanciación del objeto para llamar a los procedimientos y metodos con retorno.
        Gerthai08 procedimiento = new Gerthai08();

        //Llamando función con retorno
        double resultado = retornaSuma(5, 2);
        System.out.println("======Función con retorno======");
        System.out.println(resultado);

        //Llamando función sin retorno
        System.out.println("======Función sin retorno======");
        texto();

        //llamando procedimiento
        System.out.println("======Llamado al procedimiento======");
        procedimiento.procedimiento(5,4);


        //En java no se puede crear una funcion dentro de otra, pero si llamar
        System.out.println("======Llamando a función dentro de otra======");
        double funcionDentroDeFuncion = retornaSuma(retornarMultiplicacion(2,3),5);
        System.out.println(funcionDentroDeFuncion);

        //llamada a la función del desafio extra
        System.out.println("======Desafio extra======");
        int cantidadNumeros = multiplo("Fizz","Buzz");
        System.out.println("se imprimieron números " + cantidadNumeros + " veces.");
    }

    //Funciones basicas
    //Función con retorno
    public static int retornaSuma(int a, int c) {
        return a + c;
    }

    public static int retornarMultiplicacion(int x, int p){
        return x * p;
    }

    //Función sin retorno
    public static void texto() {
        System.out.println("Este es un texto de una funcion sin retorno");
    }

    //Procedimiento
    void procedimiento(int n, int b){
        if (n > b){
            System.out.println(n + "es mayor que " + b);
            return;
        }
        System.out.println((n + "es menor que " + b));
    }

    //Desafio extra
    public static int multiplo(String palabra1, String palabra2){
        //Contador del bucle for para el reto extra
        int contador = 0;

        for (int i = 0; i <= 100 ; i++) {
            if (i % 3 == 0 && i % 5 == 0){
                System.out.println(palabra1 + palabra2);
            }else if (i % 3 == 0){
                System.out.println(palabra1);
            }else if (i % 5 == 0){
                System.out.println(palabra2);
            }else{
                System.out.println(i);
                contador++;
            }
        }
        return contador;
    }
}
