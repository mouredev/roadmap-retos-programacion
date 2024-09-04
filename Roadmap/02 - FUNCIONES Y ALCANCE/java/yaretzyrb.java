
// FUNCIÓN SIN RETORNO NI PARÁMETROS
static void  bienvenida (){
    System.out.println("Hola");
    System.out.println("Esto es una Calculadora");
}

// FUNCIÓN CON UN PARÁMETRO SIN RETORNO
static void personalizado (String nombre){
    System.out.println("Hola, " + nombre);
}

// FUNCIÓN CON DOS PARÁMETROS SIN RETORNO
static void numeros(int n1, int n2){
    System.out.println("El primer número es: " + n1);
    System.out.println("El segundo número es: " + n2);
}

// FUNCIÓN CON DOS PARÁMETROS Y RETORNO
static int calculadora(int num1, int num2){
    int resultado = num1 + num2;
    System.out.println("El resultado de la suma de los números es: ");
    return resultado;
}

//FUNCIÓN ESTÁTICA
public static void estatico(){
    System.out.println("Este es un ejemplo de un método estático");
}

/*
 * VARIABLES LOCALES Y GLOBALES
 */

//VARIABLE LOCAL
static void local(){
    String saludo = ("Hola, soy una variable local");
    System.out.println(saludo);
}

//VARIABLE GLOBAL
static String saludo = "Hola, soy una variable global";

/*
 * EJERCICIO EXTRA
 */

static int extra (String texto1, String texto2){
    int a = 0;
    int num = 1;
    for (num=1; num>=0 && num<=100;num++){
        if(num%3 == 0 && num%5 == 0){
            System.out.println(texto1 + " y " + texto2);
            a += 2;
        }
        else if(num%3==0){
            System.out.println(texto1);
            a += 1;
        }
        else if(num%5==0){
            System.out.println(texto2);
            a += 1;
        }
    }
    System.out.println(a);
    return a;
}


public static void main(String[] args) {
    
    //LLAMADO DE FUNCIONES
    bienvenida();
    personalizado("Usuario");
    numeros(4,5);
    calculadora(4,5);
    estatico();

    //FUNCIÓN YA CREADA EN JAVA
    String cadena = "Hola, te mostraré un método pre-construido en Java.";
    System.out.println(cadena);
    System.out.println("La cadena de texto anterior tiene " + cadena.length() + " caracteres.");

    //VARIABLE GLOBAL
    System.out.println(saludo);

    //LLAMADO EJERCICIO EXTRA
    extra("Multiplo de tres","Múltiplo de cinco");
        
}

