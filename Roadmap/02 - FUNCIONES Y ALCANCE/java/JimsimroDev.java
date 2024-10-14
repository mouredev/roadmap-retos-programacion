
public class JimsimroDev {

  // Funciones definidas pro el usuario
  // Funcion simple
  public static void saludar() {
    System.out.println("Hola, java");
  }

  // Funcion con retorno de caneda o texto
  public static String stringRetorno() {
    return "Hola, Java";
  }

  // Funcion con retorno de number
  public static int intRetorno() {
    return 30;
  }

  // Funcion con parametro el parametro que tiene la funcion en java se le conoce
  // como parametro formal o parametros
  // y cuando la funcion se llama y se le pasa el parametro se le conoce como
  // parametro actual o argumentos
  public static String argSaludo(String name) {
    return name;
  }

  // Funcion con parametros
  public static String argsSaludo(String saludo, String name) {
    return saludo + name;
  }

  // Funcion con número variables de argumentos
  public static void variosSaludos(String... names) {
    for (String name : names) {
      System.out.print(" Hola, " + name);
    }
    System.out.println();
  }

  // Funciones dentro de Funciones
  public static void funcionPrincipal() {
    saludar();
    System.out.println("Funcion interna");
  }

  // Variables globales y locales
  String variableGlobal = "Pyton";

  public void holaJava() {
    var variableLocal = "Hola, ";
    System.out.println(variableLocal + variableGlobal);
  }

  // Dificultad extra
  public static int mostrarNumeros(String str, String str1) {
    int contador = 0;
    for (int i = 0; i < 101; i++) {
      if (i % 3 == 0 && i % 5 == 0) {
        System.out.println(str + str1);
      } else if (i % 3 == 0) {
        System.out.println(str);
      } else if (i % 5 == 0) {
        System.out.println(str1);
      } else {
        System.out.println(i);
        contador++;
      }
    }
    return contador;
  }

  public static void main(String[] args) {
    // Funcion simple
    saludar();

    // Funcion con retorno cadena de texto
    System.out.println(stringRetorno());

    // Funcion con retorno cadena de texto
    System.out.println(intRetorno());

    // Funcion con parametro
    System.out.println(argSaludo("Jimmis"));

    // Funcion con parametros
    System.out.println(argsSaludo("Hola,", " Java"));

    // Funcion con número variables de argumentos
    variosSaludos("Jimmis", "Java", "Spring", "MySQL");
    variosSaludos("PHP", "Phyton", "GIT");

    funcionPrincipal();

    JimsimroDev principal = new JimsimroDev();
    principal.holaJava();

    System.out.println(mostrarNumeros("texto1 ", "texto2 "));
  }
}
