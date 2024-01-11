public class nicoloboo02{


    public static void bucleWhile(int i,int y){
        while (i<y){
            System.out.println("Los números no son iguales");
            i++;
        }
        System.out.println("Los números ya son iguales");

    }

    public static void bucleIfElseFor(int i,int y){
        for (int z = 0;z<=5;z++){
            if(i>y){
                System.out.println("El primer numero es mayor que el segundo");
                y++;
            }else if(i<y){
                System.out.println("El segundo numero es mayor que el primero");
                i=i+3;
            }else{
                System.out.println("Los numeros son iguales");
                break;
            }
        }
    }

    public static void extra(){
        for(int i = 10;i<=55;i++){
            if (i%2==0 && i!=16 && !(i%3==0 )){
                System.out.println(i);
            }
        }
    }
       
    public static void main(String[] args) {
        int a = 5;
        int b = 6;
        int suma = a+b;
        int resta = a-b;
        int multipilcacion = a*b;
        int division = a/b;
        int modulo = a%b;
        int incremento = a++;
        int decremento = b--;
        boolean igual = a==b;
        boolean diferente = a!=b;
        boolean mayor = a>b;
        boolean menor = a<b;
        boolean mayorigual = a>=b;
        boolean menorigual = a<=b;
        boolean and = menor && mayor;
        boolean or = menor || mayor;
        System.out.println("Operadores Aritméticos");
        System.out.println("Suma: "+suma);
        System.out.println("Resta: "+resta);
        System.out.println("Multiplicacion: "+multipilcacion);
        System.out.println("Division: "+division);
        System.out.println("Módulo: "+modulo);
        System.out.println("Incremento: "+incremento);
        System.out.println("Decremento: "+decremento);
        System.out.println("\nOperadores relacionales");
        System.out.println("Son a y b iguales? " + igual);
        System.out.println("Son a y b diferentes? "+diferente);
        System.out.println("Es a mayor que b? "+mayor );
        System.out.println("Es a menor que b? "+menor );
        System.out.println("Es a mayor o igual que b? "+mayorigual );
        System.out.println("Es a menor o igual que b? "+menorigual );
        System.out.println("\nOperadores lógicos");
        System.out.println(and);
        System.out.println(or);
        System.out.println("\n Estructuras condicionales");
        int c = 5;
        int d = 7;
        System.out.println("Bucle while:");
        bucleWhile(c, d);
        System.out.println("Bucles for y if-else");
        bucleIfElseFor(c, d);
        System.out.println("\n Ejercicio extra");
        extra();

       


         

    }
}
