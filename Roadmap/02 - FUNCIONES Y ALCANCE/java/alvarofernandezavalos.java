public class alvarofernandezavalos {

  public static int globalInt = 10;

  public static void main(String[] args) {
    funcionSinParametrosNiRetorno();
    System.out.println(funcionSinParametrosConRetorno());
    funcionConParemetroSinRetorno("alvarofernandezavalos");
    System.out.println(funcionConParametroConRetorno("alvarofernandezavalos"));
    System.out.println(funcionConDosParametrosConRetorno("alvarofernandez", "avalos"));
    System.out.println(funcionConNParametrosConRetorno(1,2,3,4,5,6,10));
    System.out.println("Java Home: "+getJavaHome());
    System.err.println("Operating System: "+getOS());
    variableGlobalyLocal();
    System.out.println("La función retorna el número de veces que se ha impreso el número en lugar de los textos: " + opcional("tortuga","grande"));
  }

  private static int opcional(String a, String b) {
    int numero=0;
    for(int i = 1; i <= 100 ; i++) {
      if (i%3==0) System.out.println(a);
      if (i%5==0) System.out.println(b);
      if (i%3==0 && i%5==0) System.out.println(a.concat(b));
      if (i%3!=0 && i%5!=0) {
        numero++;
        System.out.println(i);
      }
    }
    return numero;
  }

  private static void variableGlobalyLocal() {
    int globalInt;
    globalInt = 100;
    System.out.println("La variable local globalInt en esta funcion vale: " + globalInt);
    System.out.println("La variable global globalInt vale: " + alvarofernandezavalos.globalInt);
  }

  public static void funcionSinParametrosNiRetorno() {
    System.out.println("funcionSinParametrosNiRetorno");
  }

  public static String funcionSinParametrosConRetorno() {
    return "retorno";
  }

  public static void funcionConParemetroSinRetorno(String texto) {
    System.out.println("Parametro 1: "+texto);
  }

  public static String funcionConParametroConRetorno(String texto) {
    return texto;
  }

  public static String funcionConDosParametrosConRetorno(String texto, String texto2) {
    return texto.concat(texto2);
  }

  public static int funcionConNParametrosConRetorno (int ... numeros) {
    int suma = 0;
    for (int i : numeros) {
      suma += i;
    }
    return suma;
  }

  public static String getJavaHome() {
    return System.getProperty("java.home");
  }

  public static String getOS() {
    return System.getProperty("os.name");
  }

}
