public class danhingar {
    //variable global
    static int counter=10;
    
    public static void main(String[] args) {
        greet();
        System.out.println(returnGreet());
        argGreet("Daniel");
        argsGreet("Hi","Daniel");
        suma(2, 3);
        methodInside("Pepe");
        variable_arg_greet("Ramón","Curro","Alfonso");
        upperCase("hello java");
        localAndGlobalVar();
        counter--;
        System.out.println("Contador global: "+counter);
        System.out.println("Nº veces impreso el número: "+countPrints("zip","zap"));
        
    }

    //Función publica(accesible desde cualquier instancia de la clase), sin retorno(void) y sin parámetros 
    public static void greet(){
        System.out.println("¡Helloo!");
    }

    //Función privada(sólo accesible dentro de la clase), con retorno y sin parámetros
    private static String returnGreet(){
        return "Hello, Java!";
    }

    //Funcion privada, con argumentos y sin retorno
    private static void argGreet(String name){
        System.out.println("Hola ".concat(name));
    }

    //Con varios argumentos y sin retorno
    private static void argsGreet(String greet,String name){
        System.out.println(String.format("%s %s!", greet,name));
    }

    //Con varios argumentos y retorno
    private static Double suma(double num1, double num2){
        return num1+num2;
    }

    //Con un número variable de argumentos
    private static void variable_arg_greet(String... names){
        for (String name : names) {
            System.out.println(String.format("Hi, %s!",name));
        }
    }

    private static void upperCase(String word){
        System.out.println(word.toUpperCase());
    }

    //Funcion dentro de otra funcion
    private static void methodInside(String name){
        argsGreet("Hi",name);
    }

    private static void localAndGlobalVar(){
        int internalCounter = 0;
        counter--;
        internalCounter++;
        System.out.println(counter);
        System.out.println(internalCounter);
    }


    //EJERCICIO EXTRA
    private static int countPrints(String text1, String text2){
        int counter = 0;
        for(int i=1; i<=100;i++){
            if(i%3==0 && i%5==0){
                System.out.println(text1.concat(text2));
            }else if(i%3==0){
                System.out.println(text1);
            }else if(i%5==0){
                System.out.println(text2);
            }else{
                System.out.println(i);
                counter++;
            }
               
          
        }


        return counter;
    }


}
