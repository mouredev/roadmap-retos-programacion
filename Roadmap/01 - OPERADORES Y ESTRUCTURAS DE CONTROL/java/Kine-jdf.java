public class Kine_jdf {
    public static void main(String args[]) {
     
     //Operadores Aritméticos:
     // Suma +
int suma = 5 + 3;          // suma = 8

// Resta -
int resta = 10 - 4;         // resta = 6

// Multiplicación *
int multiplicacion = 2 * 6; // multiplicacion = 12

// División  /
int division = 15 / 3;      // division = 5

// Módulo (resto de la división. siempre tengo que googlear que es) %
int modulo = 17 % 4;        // modulo = 1

int a = 5, b = 10;
System.out.println("Operadores Aritmeticos(ver codigo)");
System.out.println("Suma " + suma +"\nResta "+resta+"\nMultiplicacion "+multiplicacion+"\nDivision "+division);
      
//Operadores de Comparación:
// Igual a ==
boolean igual = (a == b);   // igual = false

// No igual a  !=
boolean noIgual = (a != b); // noIgual = true

// Mayor que    >
boolean mayorQue = (a > b);  // mayorQue = false

// Menor que  <
boolean menorQue = (a < b);  // menorQue = true

// Mayor o igual que >=
boolean mayorIgualQue = (a >= b); // mayorIgualQue = false

// Menor o igual que  <=
boolean menorIgualQue = (a <= b); // menorIgualQue = true
System.out.println("\nOperadores de Comparacion ");
System.out.println("A vale "+ a+"\nB vale "+b);
System.out.println("Igual "+igual+"\nNoIgual "+noIgual+"\nMayor que "+mayorQue+"\nMenor que "+menorQue
+"\nMayor o igual que "+mayorIgualQue+"\nMenor o igual que "+menorIgualQue);

int num = 5;
System.out.println("\nOperadores de Inc / Dec");
System.out.println("Numero inicial vale 5");
System.out.println("incremento ++ :" + num);
      
//Operadores de Incremento y Decremento:
// Incremento ++
num++;       // num = 6
System.out.println("incremento ++ :" + num);
// Decremento --
num--;       // num = 5
System.out.println("decremento -- :" + num);
      
//Operadores Lógicos:

boolean x = true, y = false;

// AND lógico &&
boolean andLogico = x && y;  // andLogico = false

// OR lógico  ||
boolean orLogico = x || y;   // orLogico = true

// NOT lógico !
boolean notLogico = !x;      // notLogico = false

System.out.println("\nOperadores Logivos ");
System.out.println("X es true, Y es false ");
System.out.println("x && y " +andLogico);
System.out.println("x || y " +orLogico);
System.out.println("x != y " +notLogico);

int c = 10;
      
//Operadores de Asignación:
// Asignación simple =
int d = c;    // d = 10
// Asignación con operación +=
a += 5;       // a = a + 5 (a ahora es 10)
System.out.println("\nOperadores de asignacion ");
System.out.println("Simple : c = 10, d=c");
System.out.println("Con operacion += (o -=)");
System.out.println("a +=5 :"+ a);
      
//Operadores de Identidad:
String str = "Hola";
int test = 0;
System.out.println("Es un String? " + (str instanceof String)); //true
System.out.println("Esto es un Integer?(wrapper obj para primitivo)" + (test instanceof Integer)); //CREO que deberia ser true, aunque use un wrapper


      
//Repeticion - Ciclos

 // Ciclo for
 for (int i = 1; i <= 5; i++) {
 System.out.println("Ciclo #" + i);
        }

// Ciclo while
  int j = 0;
  while (j < 5) {
  System.out.println("Ciclo en while #" + j);
       j++;
        }

// Ciclo do-while
 int k = 0;
   do {
  System.out.println("Ciclo en do-while #" + k);
     k++;
        } while (k < 5);


     
      
      elMetodo();
    }
    
    public static void elMetodo(){
      int start = 10;
      int end = 55;
      int count = start;
      System.out.println("\n             ||    EJERCICIO EXTRA    ||");
      System.out.println("○*:;;;:*○*: Fancy numeritos thing by Kine ○*:;;;:*○*:" +"\n");
          System.out.print(start+",");
          while(count <end) {
               
              if(count%2==0 && count !=16 && count%3!=0) {
                   
                    System.out.print(count+",");
                     
              }
              count+=2;
          }
            System.out.print(end);
      }
}
