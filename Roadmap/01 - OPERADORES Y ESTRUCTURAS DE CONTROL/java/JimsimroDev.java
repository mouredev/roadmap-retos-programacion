public class JimsimroDev {
  public static void main(String[] args) {

    // Operadores aritmeticos
    System.out.println("Operadores aritmeticos");
    System.out.printf("Suma 12 + 12 = %d", (12 + 12));
    System.out.printf("\n Resta 12 - 10 = %d", (12 - 10));
    System.out.printf("\n Multiplicación 2 * 5 = %d", (2 * 5));
    System.out.printf("\n División 24 / 2 = %d", (24 / 2));
    System.out.println("\nResiduo 10 % 6 = " + (10 % 6));
    System.out.println("Residuo 10^6 = " + (10 ^ 2));

    // Operadores De Asignacion
    System.out.println("Operadores de asignación");
    int numero = 20;// asignacion
    System.out.println(numero);
    numero += 1; // suma y asignacion
    System.out.println(numero);
    numero -= 1; // resta y asignacion
    System.out.println(numero);
    numero *= 2; // Multiplicación y asignacion
    System.out.println(numero);
    numero %= 1; // modulo y asignacion
    System.out.println(numero);
    numero /= 2;// División y asignacion
    System.out.println(numero);

    // Operadores de comparacion
    System.out.println("Operadores de comparacion");
    System.out.println("Igualdad: 10 == 3" + (10 == 3));
    System.out.println("Desigualdad 10 != 3 " + (10 != 3));
    System.out.println("Mayor que 10 > 3 " + (10 > 3));
    System.out.println("Menor que 10 < 3 " + (10 < 3));
    System.out.println("Menor igual que 10 <= 10 " + (10 <= 10));
    System.out.println("Mayor igual que 10 >= 3 " + (10 >= 3));

    // Operadore de pertenencia
    System.out.println("Operador de pertenencia");
    System.out.println("jimsimroDev".contains("j"));
    System.out.println(!"jimsimroDev".contains("a"));

    // Operadores logicos
    System.out.println("Operadores Lógicos");
    // Operador "and" se representa pro && ambas afirmaciones deben ser verdaderas
    int num = 10;
    int num1 = 12;
    if (num == 10 && num1 == 12) {
      System.out.println(true);
    } else {
      System.out.println(false);
    }
    // Operador "or" se representa por || y se evalua como tru si alguna de las
    // afirmaciones es verdadera es decir que solo es falso si ambas afirmaciones
    // son falsas
    if (num == 10 || num1 == 23) {
      System.out.println(true);
    } else {
      System.out.println(false);
    }

    // Operador Lógico "not" se representa ! es la espresion negada es decir si la
    // exprexion es true
    // el Operador devuelve false
    boolean a = true;
    boolean b = false;
    System.out.println(!a);// devuelve false
    System.out.println(!b);// devuelve true

    // Operadores Lógicos binarios
    System.out.println("Operadores binarios");
    // Operador "and binaro" se representa por &

    System.out.println("10 & 12 " + (num & num1));// salida 8 por que analiza bit por bit

    // Operador "or binario" se representa por |
    System.out.println("10 | 12 " + (num | num1));// salida 14 por que analiza bit por bit

    // Operador "not binario" se representa por ~
    System.out.println("not ~ " + ~num);

    // Corrimiento de bits
    // << shift left Corrimiento a l izquierda
    System.out.println(-15 >> 3);
    System.out.println(-15 >>> 3);
    // >> shift right Corrimiento al a derecha

    // Condicinales
    String name = "JimsimroDev";
    if (name.equals("JimsimroDev")) {
      System.out.println("Mi nombre es JimsimroDev ");
    } else if (name.equals("jhoan")) {
      System.out.println("My nombre es Jhoan");
    } else {
      System.out.println("Mu nombre no es JimsimroDev ni jhoan");
    }

    // Iterativas
    for (int i = 0; i < 15; i++) {
      System.out.println(i);
    }
    int i = 0;
    while (i <= 10) {
      System.out.println(i);
      i++;
    }
    // Manejo de excepcines
    try {
      System.out.println(10 / 0);
    } catch (Exception e) {
      System.out.println("Se ha producido un error");
    } finally {
      System.out.println("Ha finalizado correctamente");
    }
    int inicio = 10;
    int fin = 55;
    while (inicio <= fin) {
      if (inicio % 3 != 0 && inicio % 2 == 0 && inicio != 16) {
        System.out.println(inicio);
      }
      inicio++;
    }
  }
}
