public class DomingoAndres {

     //Funcion sin paramaetro ni retorno
        public static void saludo (){
            System.out.println("Hola, soy una funcion que solo saluda.");
        }

    //Funcion con 1 parametro pero sin retorno
    public static void unParametro (int paramtero1){
        System.out.println("El valor que recibi como parametro fue: " + paramtero1);
    }

    //Funcion con varios parametros pero sin retorno
    public static void variosParametros (int a, int b, int c){
        System.out.println("Recibi 3 parametros, y la suma de todos ellos es igual a: " + (a+b+c));
    }

    //Funcion con retorno pero sin retorno
    public static String conRetorno(){
        return "Soy una funcion con retorno, pero no tengo parametros.";
    }

    //Funcion con retorno y con 1 parametro
    public static String retornoConParametro(int a){
        return "El valor que me pasaron a mi fue: " + a;
    }

    //Funcion con retorno y varios parametros
    public static String retornoConParametros(int x, int y, int z){
        return "Soy una funcion con retorno y 3 parametros que suman: " + (x+y+z);
    }

    //En Java NO SE PUEDE crear o definir funciones dentro de otras funciones
    //Lo que si podemos hacer es usar funciones ya creadas anteriormente dentro de nuesvas funciones


    //Funcion ya creada de Java
    public static String raizCuadrada(int a){
        double resultado = Math.sqrt(a); //Math.sqrt es una funcion ya creada de java

        return "Me pasaron el numero " + a + " y su raiz cuadrada es: "+ resultado;
    }


    static int variableGlobal = 7;

    //Funcion para variable local
    public static String funcionVariableLocal(){
        int variableLocal = 5;

        return "Mi variable local es: " + variableLocal + " y mi variable global es: " + variableGlobal;
    }


    //-------------------DIFICULTAD EXTRA---------------------------

    public static int dificltadExtra(String a, String b){
        int contador = 0;
        for (int i = 1; i <= 100; i ++){
            if ( i % 3 == 0 && i % 5 == 0){
                System.out.println(a + ", " + b);
            }
            else if (i % 3 == 0){
                System.out.println(a);
            }
            else if (i % 5 == 0){
                System.out.println(b);
            }
            else{
                System.out.println(i);
                contador ++;
            }
        }
        return contador;
    }

    public static void main(String[] args) {
    
        saludo();
        unParametro(1);
        variosParametros(5, 8, 4);
        System.out.println(conRetorno());
        System.out.println(retornoConParametro(5));
        System.out.println(retornoConParametros(6, 12, 25));
        System.out.println(raizCuadrada(5));
        System.out.println(variableGlobal);
        System.out.println(funcionVariableLocal());
        // System.out.println(variableLocal); Esto va a marcar error porque va a decir que la variable no esta definida
        System.out.println(dificltadExtra("Hola", "Adios"));

    }

}
