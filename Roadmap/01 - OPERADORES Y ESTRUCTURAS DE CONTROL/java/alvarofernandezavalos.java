public class alvarofernandezavalos {
  public static final int START=10;
  public static final int END=55;
  public static void main(String[] args) {
    System.out.println("Operadores Aritméticos");
    int suma=0;
    for(int x=0;x<3;x++) suma=suma+x;
    System.out.println("Suma Total: "+suma);
    while (suma<END) suma++;
    System.out.println("Suma Total: "+suma);
    do {
      suma++;
    } while (suma<END*2);
    System.out.println("Suma Total: "+suma);
    int array[] = {1,2,3,4,5};
    for (int x : array) System.out.println(x);
    try {
      Integer.parseInt("S");
    } catch (Exception e) {
      System.err.println("No se puede convertir a Integer");
    }
    System.out.println("Operadores Lógicos");
    int a = 10; int b = 20; int c = 15; int d = 23;
    System.out.println(a+" es menor que "+b+" AND "+c+" es mayor que "+d+" ? "+ (a<b && c>d));
    System.out.println(a+" es menor que "+b+" OR "+c+" es mayor que "+d+" ? "+ (a<b || c>d));
    System.out.println(a+" es menor que "+b+" NOT "+c+" es mayor que "+d+" ? "+ !(a<b && c>d));
    System.out.println("Operadores Comparación");
    System.out.println("A es mayor que B "+(a>b));
    System.out.println("A es igual a B "+(a==b));
    System.out.println("A es mayor o igual a B " + (a>=b));
    System.out.println("A es diferente a B "+(a!=b));
    System.out.println("Operadores Asignación");
    System.out.println("El valor de suma es "+suma);
    suma=suma+1;
    System.out.println("He sumado 1 a suma, su nuevo valor es"+suma);
    suma+=1;
    System.out.println("He sumado 1 a suma, su nuevo valor es "+suma);
    suma-=1;
    System.out.println("He restado 1 a suma, su nuevo valor es "+suma);
    suma*=2;
    System.out.println("He multiplicado el valor de suma por 2, su nuevo valor es "+suma);
    suma/=2;
    System.out.println("He dividido el valor de suma entre 2, su nuevo valor es "+suma);
    System.out.println("Operadores Identidad");
    //cosultamos si el objeto apunta al mismo puntero.
    //no estamos comprobando si las cadena son iguales.
    String string1 = new String("Alvaro");
    String string2 = new String("Alvaro");
    System.out.println(string1==string2);
    System.out.println("Operador Ternario");
    suma = (a>b ? 10: 20);
    System.out.println("El Valor de suma es "+suma);
    System.out.println("Operadores Bits");
    int puerta1 = 6; //(0110)
    int puerta2 = 5; //(0101)
    int result = puerta1|puerta2;
    System.out.println("Puerta 1 OR Puerta 2 "+result+" Binary: " + Integer.toString(result,2));
    result = puerta1 & puerta2;
    System.out.println("Puerta 1 AND Puerta 2 "+result+" Binary: " + Integer.toString(result,2));
    result = puerta1 ^ puerta2;
    System.out.println("Puerta 1 XOR Puerta 2 "+result+" Binary: " + Integer.toString(result,2));
    System.out.println("Parte Opctional:");
    for(int x=START;x<=END;x++) {
      if(x%2==0 && x!=16 && x%3!=0) System.out.println(x);
    }
  }
}