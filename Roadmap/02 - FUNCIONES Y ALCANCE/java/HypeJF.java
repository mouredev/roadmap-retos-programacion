import java.util.function.Consumer;

public class HypeJF {
    public static void main(String[] args) {
        producto(2,5);
        saludo2();
        Variable miVariable = new Variable();
        miVariable.metodoVariableLocal();


    }
    //FUNCIONES
    //Funcion que no retorna nada
    public void saludo(){
        System.out.println("Saludo");
    }

    //Funcion con parametros y retorno
    public static int producto(int a, int b){
        return a*b;
    }

    //Funcion solo retorno
    public static String saludo2(){
        return "Saludo 2";
    }

    //FUNCION DENTRO DE OTRA FUNCION
    //Funcion compuesta usando un lambda y una interfaz Consumer que es void
    public void saludo3(){
        Consumer<String> saludoInterno = (saludo3) -> {
            System.out.println("Saludo 3" + saludo3);
        };
    }

    //EJEMPLO FUNCIONES CREADAS POR EL LENGUAJE
     //funcion aleatoria
    public static double numero_random = Math.random();

    //ALCANCE DE VARIABLES
    //Variable local (ella solo funciona solo dentro de un contexto) ej: Metodo
    static class Variable{
        public void metodoVariableLocal(){
            int variable_local = 10;
            System.out.println("Funcion numero aleatorio: " + numero_random);
            System.out.println("Variable local: " + variable_local);
            System.out.println("Variable global: " + variable_global);
            //la variable_global usa la variable static definida posteriormente
        }
    }


    //Variable global (static)
    //pertenecen a una clase, no a un objeto en concreto

    public static String variable_global = "Variable global";

    //DIFICULTAD EXTRA
    public static int Funcion_extra(String texto1, String texto2){
        int veces = 0;
        for (int i = 1; i < 101; i++) {
            if (i%3==0&& i%5==0){
                System.out.println(texto1+texto2);
            } else if (i%5==0){
                System.out.println(texto2);
            } else if (i%3==0){
                System.out.println(texto1);
            } else {
                veces++;
            }
        }
        return veces;
    }
}
