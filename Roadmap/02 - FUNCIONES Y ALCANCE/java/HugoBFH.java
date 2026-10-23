import java.util.Arrays; //Mas adelante se usara el Arrrays
import java.util.Scanner; //Mas adelantense usara el scanner
public record RetonoDeVariosValores(int respuesta, boolean esExitoso){}
public class Ejersicio3 {
  static int variableGlobal = 100; // para usar variables globasles fuera del main
  public static void main(String [] args) {
    
    //HAY 4 TIPÓS DE FUNCIONES BASICAS
    
    //1 no recibe nada y no devuelve nada
    public static void saludar() {
      System.out.println("¡Hola!");
    }
    saludar(); // Imprime ¡Hola!

    //2 Recibe datos y no devuelve nada  
    public static void bienVenida(String nombre) {
      System.out.println("Te recibo con gusto " + nombre);
    }
    bienVenida("Hugo"); // Imprime Te recibo con gusto Hugo

    //3 no recibe nada y devuelve algo
    public static int recibirNumero() {
      return 7;
    }
    System.out.println("¡Felicidades! tu numero de la suete es el:" + recibirNumero()); 
    // Imprime ¡Felicidades! tu numero de la suete es el:7

    //4 Recives datos y devuelves algo (la mas usada)
    public static int sumar(int n1, int n2){
      return n1 + n2;
    }
    int total = sumar(10,5); //Aqui solo guarda la operacion pero no imprime
    System.out.println("El total es:" + total); // Aqi si imprime. Imprime El total es: 15
    // sepudo imprimir sin asignar la variable System.out.println(sumar(10,5));

    //SE PUEDEN COMBINAR OPERACIONES DE FUNCIONES
    public static int sum (int a, int b) {
      return a + b;
    }
    public static int multiplicar(int a, int b) {
      return a * b;
    }
    int resultado = multiplicar(sum(10,5),2);
    System.out.println("El resultado es: " + resultado); //Imprime El resultado es:30, primero suma y luego multiplica

    //TOMAR DESICIONES
    public static int restriccionDeEdad(int añoDeNacimiento) {
      return 2026 - añoDeNacimiento;
        }
    int edad = restriccionDeEdad(2001);
      if(edad >= 18) {
      System.out.prinln("Eres mayor de edad");
    } else {
      System.out.println("Eres menor de edad");
    } // hala resta y si el numerro restante es mayor o igual a 18 imprime if de lo contrario imprime elese

    //ENIARLO A OTRAS FUNCIONES
    public static int envio(int n) {
      return n * n;
    }
    public satic int dividir(int n, int m) {
      return n / m;
    }
    int num1 = envio(5); //multiplican 5*5 yu guarda el resultado (25)
    int num2 = envio(1); // multiplica 1*1 y guarda el resultado (1)
    int juntos = dividir(num1, num2); //divide los resultados anteriores 25/1 y guard el resultado (25)
    System.out.println("Resultado final: " + juntos);

    // Methodoverloading LO MAS CERCANO A FUMCIONES CON ARGUMENTO PREDETERMINADO
    public static void despedir(String nom) {
      System.out.println("Adios " + nom);
    }
    public static void despedir() {
      despedir ("amigo");
    }
    despedir(); //Imprime Adios amigo
    dfespedir("Hugo"); // Imprime Adios Hugo
    //Reacciona dependiendo si pones un valor o no

    // record ES PARA RETORNO CON VARIOS VALORES
    public static RetonoDeVariosValores calculo(int d1, int d2){
      int operacion = d1 + d2;
      boolean exito = true;
      return new RetonoDeVariosValores(oeperacion, exito);
    }
    RetonoDeVariosValores datos = calculo(10, 5);
    System.out.println("Resultado " + datos.respuesta); // Imprime resultado 15
    System.out.println("¿Fue exitoso? " + datos.esExitoso); //Imprime ¿Fue exitoso? true

    //varargs ES LO MAS SIMILAR A UNA FUNCION CON NUMEROS VARIABLES               
    public static int sumarTodos(int... num) {
      int total = 0;
      for(int n : num) {
        total += n;
      }
    int respuestaFinal = sumarTodos(10, 5, 1);
      System.out.println("Resultado: " + respuestaFinal); //Impime Resultado: 16

    //con void
    public static void multiplicarTodos(int... num) {
      int totalV = 1;
      for(int n : num) {
        totalV *= n;
      }
      System.out.println("El total es: " +totalV );
    }
    multiplicarTodos(1, 5, 3); //Sola llama la funcion y multiplica y imprime El total es: 15

    //NO HAY FUNCIONES DENTRO DE FUNCIONES SOLO SE PUEDEN LLAMAR ENTRE SI
    public static void segunda() {
      System.out.println("hola");
    }
    public static void base() {
      segunda();
      System.out.println("y adios");
    }
    base(); //Imprime hola y adios

    //FUNCIONES YA CREADAS DE JAVA

    //1 CLASE Math
    double resultado1 = Math.sqrt(25);
      System.out.println("La raiz cuadrada de 25 es: " + resultado1);
      // Imprime La raiz cuadrada de 25 es: 5.0
      //se pudo solo imprimir sin variable System.out.println(Math.sqrt(25));
      //int resultado1 = (int)Math.sqrt(25); con el int el resultado sale entero

    double resultado2 = Math.pow(2, 5);
      System.out.println("La potencia de 2 a la 5 es: " + resultado2);
      // Imprime La potencia de 2 a la 5 es: 32.0

    int resultado3 = Math.max(25, 15);
      System.out.println("El mayor es el: " + resultado3);
      // Imprime El mayor es el: 25

   int resultado4 = Math.min(25, 15);
      System.out.println("El maenor es el: " + resultado4);
      // Imprime El menor es el: 15

   double resultado5 = Math.abs(-25);
      System.out.println("El valor absoluto -25 es: " + resultado5);
      // Imprime El valor absoluto -25 es: 25

   double resultado6 = Math.random();
      System.out.println("El numero de hoy es: " + resultado6);
      // Imprime El numero de hoy es: (un numero entre 0.0 y 1.0 sin contar el 1.0) 
      //int resultado6 = (int)Math.random(); con el int el resultado sale entero pero solo sale 0
      //int resultado6 = (int)(Math.random()*10); con el int el resultado sale entero pero no llega al 10
      //int resultado6 = (int)(Math.random()*10)+1; ais si llega al 10, puede se 50,95,1000 etc.
   
   //2 CLASE Sting
   String mensaje1 = "hola";
     System.out.println("Hola tiene " + mensaje1.lengtn() + "letras");
      //Imprime Hola tiene 4 letras
      //Su funcion solo impime la cantidad de letras pero se agrego el texto

     System.out.println("Pasa a mayusculas " + mensaje1.toUpperCase());
      //Imprime Pasa a mayusculas HOLA

   String mensaje2 = "HOLA";
     System.out.println("Pasa a minusculas " + mensaje2.toLowerCase());
      //Imprime Pasa a minusculas hola
      
   String mensaje3 = "adios";
     System.out.println("¿Son iguales? " + mensaje3.equals("adios"));
      //Imprime ¿Son iguales? true

     System.out.println("¿Contiene eso? " + mensaje3.contains("dios"));
      //Imprime ¿Contiene eso? true

     System.out.println("La tercer letra es la " + mensaje1.charAt(3));
      //Imprime La tercer letra es la 'a'

     System.out.println("La l esta en el " + mensaje1.indexOf("l") +"lugar");
      //Imprime La l esta en el 2 lugar

   //3 CLASE Alrrays
   int[]numeros = {2, 1, 3, 5, 4};
   int[]numeros2 = {1, 2, 3, 4, 5};   
      Arrays.sort(numeros); //Acomoda los nuemeros 1, 2, 3, 4, 5
      System.out.println(Arrays.toString(numeros)); //Hace visible los nuemero anteriores porque sin esto imprimira algo raro
      int[]copia = Arrays.copyOf(numeros, 3); //Copia los 3 primeros numeros
      System.out.println(Arrays.toString(copia)); //Los hace visibles 1, 2, 3
      System.out.println(Arrays.equals(numeros, numeros2)); //Imprime true

   //4 CLASE Scanner
   Scanner teclado = new Scanner(System.in);
      System.out.println("Escibe tu nombre completo:");
      String nombreCompleto = teclado.nextLine(); //Aqui el usuario escribe

      System.out.println("Escibe tu edad:");
      int edad = teclado.nextInt();
      teclado.nextLine();

      System.out.println("Escibe tu altura:");
      double altura = teclado.nextDouble();
      teclado.nextLine();

      teclado.close();
      
   Scanner teclado2 = new Scanner(System.in); //Noe es recomendado hacer 2 teclados mejor solo 1 y cerrar al final
      System.out.println("Escibe la edad de tu mama:");
      int edadDeTuMama = teclado.nextInt();
      teclado.nextLine();

      teclado2.close();

   //VARIABLES Y LOCALES
      //Locales son las que estan dentodel main solo trabaja con lo que conoce del main
      //Globales estan fuera de pero trabaja con las variables de main y las que stan fuera de 
    } //Aqui cierro el main
  System.out.println(variableGlobal); // Imprime 100 
  //Aunque cerre el main lu puedo usar porque el la variable global esta arriba
} //Aqui cieero toda la clase


//EXTRA
public class EjercicioExtra {
  public static int contarImpreciones(String texto1, String texto2) {
    int contadorNumeros = 0;
    for(int i=1; i <= 100; i++) {
      if(i % 3 == 0 && i % 5 == 0) {
        System.out.println(texto1 + texto2);
      }
      else if(i % 3 == 0) {
        system.out.println(texto1);
      }
      }
      else if(i % 5 == 0) {
        system.out.println(texto2);
      }
    else {
      system.out.println(i);
      contadorNumeros++;
    }
  }
  return contadorNumeros;                          
  }
  public static void main(Strin[]args) {
    int cantidad = contarImpreciones("Fizz", "Buzz");
    System.out.println("Se imprimieron " + cantidad + " numeros.");
  }
  
      

  

      

      

      
      
  













  
      
    
  
  
