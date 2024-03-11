/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */ 

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

public class rantamhack01 {

    public static void main(String[] args){


    // OPERADORES ARITMETICOS
    //toman los operadores que se le indican y realizan un cálculo matemático
    
    int suma = 3 + 5;
    int resta = 5 - 3;
    int multiplicacion = 5 * 3; 
    double division = 5 / 2;
    double modulo = 10 % 3;  // Modulo es el resto que nos queda de la división en éste caso es 1
    
    // java no tiene sintaxis para elevar a una potencia. Lo hacemos usando la funcion math.pown

    double potencia = Math.pow(10, 3);

    System.out.println(suma);
    System.out.println(resta);
    System.out.println(multiplicacion);
    System.out.println(division);
    System.out.println(modulo);
    System.out.println(potencia);

    System.out.print("\n\n=======================================================================\n\n");

    // OPERADORES RELACIONALES
    // Son los que relacionan dos elementos entre sí
    
    boolean compara = (5 > 3);      // Devuelve True si es verdadero 
    boolean compara1 = (5 >= 3);    // Devuelve True si es verdadero
    boolean compara2 = (5 < 3);     // Devuelve True si es verdadero
    boolean compara3 = (5 <= 3);     // Devuelve True si es verdadero
    boolean compara4 = (5 == 3);     // Devuelve True solo si los dos operandos son iguales
    boolean compara5 = (5 != 3);     // Devuelve True solo si los dos operandos son diferentes

    System.out.println(compara);
    System.out.println(compara1);
    System.out.println(compara2);
    System.out.println(compara3);
    System.out.println(compara4);
    System.out.println(compara5);

    System.out.print("\n\n=======================================================================\n\n");

    // OPERADORES LOGICOS
    // Se usan basandonos en condiciones

    // El operando "and" devuelve True siempre que los dos operandos sean correctos
    
    System.out.println((3 + 2 == 5) && (7 * 2 == 14));
    
    // El operando "or" devuelve True siempre que uno de los dos operandos sea correcto
    
    System.out.println((3 + 2 == 5) || (7 * 2 == 10));
    
    // El operando "not" devuelve True siempre que uno de los dos operandos sea falso
    
    System.out.println(!(10 + 3 == 14));


    System.out.print("\n\n=======================================================================\n\n");


    // OPERADORES DE ASIGNACION
    // Son los que se usan para dar valor a una variable por ejemplo
    
   
    double my_variable = 5;        // Asignación    
    System.out.println(my_variable);

    my_variable += 1 ;       // Suma y Asignación
    System.out.println(my_variable);      

    my_variable -= 1;        // Resta y Asignación
    System.out.println(my_variable);      
    
    my_variable *= 2;        // Multiplicación y Asignación
    System.out.println(my_variable);      

    my_variable /= 2;        // División y Asignación
    System.out.println(my_variable);      
    
    my_variable %= 3;        // Mòdulo y aAsignación
    System.out.println(my_variable);    
    
    
    System.out.println("\n\n=======================================================================\n\n");


    // ESTRUCTURAS DE CONTROL 
    // CONDICIONALES 

    String my_name = "juan";

    if (my_name == "luis"){
        System.out.println("mi nombre es luis");
    }
    else if (my_name == "juan"){
        System.out.println("mi nombre es juan");
    }
    else{
        System.out.println("mi nombre no sale en el programa");
    }

    System.out.println("\n\n=======================================================================\n\n");

    // Condicional switch

    String login = "juan";

    switch(login) { 
        case "luis":
            System.out.println("mi nombre es luis");
            break;
        case "juan":
            System.out.println("mi nombre es juan");
            break;
        case "":
            System.out.println("Por favor escribe un nombre valido");
            break;
        default:
            System.out.println("respuesta no valida");
            break;
    }
    
    System.out.println("\n\n=======================================================================\n\n");

    // ESTRUCTURAS DE CONTROL 
    // ITERATIVAS

    for (int i = 0; i < 10; i++){
        System.out.println(i);
    }
    
    System.out.println("\n\n=======================================================================\n\n");

    int n = 0;

    while(n < 11){
        System.out.println(n);
        n++;
    }

    System.out.println("\n\n=======================================================================\n\n");

    int x = 0;
    
    do{
        System.out.println(x);
        x++;
    }

    while(x < 15);

    
    System.out.println("\n\n=======================================================================\n\n");   
    
    
    // ESTRUCTURAS DE CONTROL 
    // MANEJO DE EXCEPCIONES (simulacion dvision por cero)

    int numerador = 10;
    int denominador = 0;


    try{
        division = numerador / denominador;
    }
    catch (ArithmeticException ex){
        division = 0;
        System.out.println("Excepcion encontrada"+ ex.getMessage());
    }
    finally{
        System.out.println("No se puede hacer la division");
    }
 
    }
}
