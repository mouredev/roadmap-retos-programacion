import java.util.Scanner;

public class VictorPolo28 {
    public static void main(String[] args) {

        //operadores arimeticos

        int numberA = 10;
        int numberB = 55;
        int suma = numberA + numberB;
        int resta = numberA -numberB ;
        int multiplicacion = numberA * numberB;
        int divisio = numberA /numberB;
        int sobrante = numberA % numberB ;

        //operadores  de asignación 
        numberA = 15;
        numberB += 25;
        numberA -= 10;
        numberB *= 25;
        numberA /= 2 ;
        numberB %= 5;

        //oepradores de Incremento  y  Decremento
        numberA ++;
        numberB --;

        //operadores Realcionles  o de  Comparacion 
          boolean  igualdad = (numberA == numberB );
          boolean   desigualdad = (numberB != numberA);
          boolean   mayorQue = (numberA > numberB); 
          boolean   menorQue = (numberA < numberB);
          boolean   mayorIgualQue = (numberA >= numberB);
          boolean   menorIgualQue = (numberB <= numberA);


        //operadores logicos

        boolean a =true ;
        boolean b = false;
        boolean resultado = a && b ;
        boolean resultado2 = a || b ;
        boolean resultado3 = a != true  ;

       

    //operadores  Bit a  Bit 
    int c = 5;
    int d = 85;
    int prueba = c & d;
    int prueba2 = c | d;
    int prueba3 = d  ^ c;
    int prueba4 = ~c;
    int prueba5 = d << 2;
    int prueba6 = c>> 2 ;
    int prueba7 = d >>> 2;
    

     //operador terniario
     if (numberA < numberB) {
        System.out.println( numberA + "es menor  que  " + numberB);
    } else {
        System.out.println( numberA + "es mayor que  " + numberB );
    }

    //Ejemplos de  los tipos de estructuras  de   control

    //Estructuras de Control de Selección (Condicionales)

    int ageM = 28  ;
    int ageF = 31 ;

    if (ageF > ageM ){
        System.out.println("La diferencia de edad es: " + (ageF -ageM)  + " años");
    }

    String  pokemon ="fuego";
    String pokemon2 = "planta";
    String  pokemon3  = "agua" ;
    

    if (pokemon == "fuego") {
        System.out.println("Yo soy de agua   y mela pelas ");
    } else {
        System.out.println("Ya  valiste verga perro...!");
    }
    
    

    if (pokemon == pokemon2){
        System.out.println("Quemado perro");
    } else if (pokemon != pokemon2) {
        System.out.println("F perdiste perro... ");
    }  else {
        System.out.println("Aqui que paso?");
    }

    Scanner menu = new Scanner (System.in);

    System.out.println("/n elija su opcion");
    System.out.println("1. pokemon de planta");
    System.out.println("2.pokemon de fuego");
    System.out.println("3 pokemon de agua");
    int opcion = menu.nextInt();
    menu.nextLine();
    

    switch (opcion) {
        case 1: 
        System.out.println("Soy  fugo  ya valiste");
            
            break;
        case 2: 
        System.out.println("Soy agua  ya valiste");
            
            break;
        case 3: 
        System.out.println( "Soy planta   ya valiste");
            
            break;
    
        default:
        System.out.println("Elieje  algo valido  pendejo");
            break;
    }


        // Estructuras de Control de Iteración (Bucles)

    for (int i= 0;  i < 1000; i++){
        System.out.println( "ahora  tu cantidad de sorinsas es:  " +  +i );
    }

    int smile = 0;

    while (smile < 10) {
       System.out.println( "Aun debese  sonreir  mas: " + smile + " Sonrisas no es  suficiente");
       smile++;
        
    }

    do {
        System.out.println( "Aun debese  sonreir  mas: " + smile + " Sonrisas no es  suficiente");
        smile++; 
    }while (smile < 10) ;


    // Estructuras de Control de Salto

    for (int i = 0; i < 101; i++){
        if ( i == 16) {
            break;
            
        }
        System.out.println(i);
    }

for (int i = 0; i < 101; i++){
        if ( i == 16 || i == 40) {
            continue;
            
        }
        System.out.println(i);
    }

 for (int i = 0; i <= 55; i ++){
    if (i == 16 || i%3 == 0){
        continue;
    }
    System.out.println(i);
 }

}




}