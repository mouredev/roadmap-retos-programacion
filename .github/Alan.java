
import java.util.Scanner;

/**
 *
 * @author PrettyBoyDirtyBoy
 */
public class RetosDeProgramacion002 {
      
    public static int medida1;
    public static int medida2; 
    public static int Saldo = 0;
    
    
  public static void main(String[] args) {

   Scanner A = new Scanner(System.in);     
     
    Saludar("Hola Alan");
    Sumar(14,12);
    Mayor(20);
    Tabla(29);
    Saludar();
    mostrarNumeros();
    comprobarNumero(); 
    table();
    int r = suma(4,4);
    System.out.println(r);
    boolean b = MayorNo(40);
    System.out.println(b);
    int c = Cuadrado(2);
    System.out.println(c);
    int m = mayor(2,9);
    System.out.println(m);
    System.out.println("Ingrese la primera medida");
    medida1 = A.nextInt();
    System.out.println("Ingrese la segunda medida");
    medida2 = A.nextInt();
    System.out.print("El area calculada es : ");
    int a = calcularArea(medida1,medida2);
    System.out.println(a);
    System.out.println("Cuanto quiere depositar");
    int deposito = A.nextInt();
    depositar(deposito); 
    System.out.println("Saldo total es : " + Saldo);
    System.out.println("Ingrese el precio Original");
    double pre = A.nextDouble();
    System.out.println("Ingrese el descuento a realizar"); 
    double des = A.nextDouble();
    double cpf = calcularPrecioFinal(pre,des);
    System.out.println("Precio final"); 
    System.out.println(cpf);
    System.out.println("Introduce la Primera Palabra");
    String N1 = A.nextLine();
    System.out.println("Introduce la Segunda Palabra");
    String N2 = A.nextLine(); 
    int n1a100 = numeros1al100(N1,N2);    
    System.out.println("Resultado");
    System.out.println(n1a100);  
    String nombre = A.nextLine();
    int edad = A.nextInt();
    System.out.println("Hola " + nombre +","+ "tienes " + edad +" años" );
    System.out.println("ejercico 2" );
    double numero1 = A.nextDouble();
    double numero2 = A.nextDouble();
    double numero3 = A.nextDouble();
    double resultado = (numero1 + numero2 + numero3) /3;
    System.out.println(resultado);  
    System.out.println("ejercico 4" ); 
    String entrada = A.nextLine(); 
    System.out.println(entrada.length());
    System.out.println("ejercico 5" );
    String frase = A.nextLine();
    System.out.println(frase.toUpperCase());
    System.out.println(frase.toLowerCase());
    System.out.println("ejercico 6");
    String frase1 = A.nextLine();
    System.out.println(frase1.charAt(0));
    System.out.println("ejercico 7");
    String frase2 = A.nextLine();
    String frase3 = A.nextLine();
    System.out.println(frase2.equals(frase3));
    System.out.println("ejercico 8");
    System.out.println("Ingrese la cantidad a la que equivale la base");
    double base = A.nextDouble();
    System.out.println("Ingrese la cantidad a la que equivale el exponente");
    double exponente = A.nextDouble();
    System.out.println("Resultado");
    double palabra = Math.pow(base, exponente);
    System.out.println(palabra);
    System.out.println("ejercico 9");
    System.out.println("Ingresar cantidad calcular raiz cuadrada");
    double numero = A.nextDouble();
    double result = Math.sqrt(numero);
    System.out.println("la raiz cuadrada de " + numero + " es igual a : " + result);
    System.out.println(result);
    String Palabras = A.nextLine();
    System.out.println(Palabras.length());
    System.out.println(Palabras.toUpperCase());
    System.out.println(Palabras.toLowerCase());
    System.out.println(Palabras.charAt(0));
    System.out.println(Palabras.equals("La temperatura"));
    
    
   }
   public static void Saludar(){
       System.out.println("Hola,Bienvenido al programa!");
   } 
    public static void mostrarNumeros (){
     for (int t = 1; t<= 10; t++){
       System.out.println(t);
         
     }
   }
     
    public static void comprobarNumero (){
      int numero = 12; 
      if (numero %2 == 0){
       System.out.println("El numero " + numero + " es par");
      }else{
         System.out.println("El numero " + numero + " es impar"); 
      }
    }

         public static void table (){
          int number = 7;
         for (int t = 1; t<= 10; t++){
           System.out.println(t * number);
         
     }
   }
   
   public static void Saludar(String Saludo){
       System.out.println(Saludo);
   } 
   
  public static void Sumar (int n , int m){
             System.out.println(n + m);
   
  }
  
  public static void Mayor (int edad) {
   if (edad >= 18){
     System.out.println("Genial si es mayor de edad");
   }else{
     System.out.println("eres muy joven");
    } 
  }
  
   public static void Tabla (int multiplicador){
     for (int t = 1; t<= 10; t++){
       System.out.println(t * multiplicador );
         
     }
   }
           
   
   public static int suma (int n1,int n2){
       int resultado = n1 + n2;
       return resultado;
   }
   
   public static boolean MayorNo (int numero){
    if (numero > 10){
       return true; 
    }else{
       return false;  
    }
   }
   
   public static int Cuadrado (int numero){
   int resultado = numero * numero;
      return resultado;
   }      
      
   public static int mayor (int n1,int n2){
       if (n1 > n2){
       return n1; 
     }else{
        return n2;     
     }  
   }
   
      public static int calcularArea(int media1, int media2){
         int Area = media1 * media2;
         return Area; 
      }
   
      public static void depositar(int cantidad){
     
     Saldo = Saldo + cantidad;
     
     
 }
   
    public static double calcularPrecioFinal(double precio, double descuento){
      
      double guardar =(precio * descuento)/100.0;
      double guardarFinal = precio - guardar;
      
      return guardarFinal;

  }
  
    public static int numeros1al100(String n1,String n2){
       int numeroVeces = 0; 
      for (int i = 1; i<= 100; i++){
          if((i%5==0) && (i%3==0)){
             System.out.println(n1 + n2);
          }else if(i%5 == 0){
             System.out.println(n2);
          }else if ( i%3==0){
             System.out.println(n1);  
          }
          else{
             System.out.println(i);  
             numeroVeces++;

          }
      }
        
      return numeroVeces;
        
        
    }
   
   
   
   
   
   
 }  
       
       
