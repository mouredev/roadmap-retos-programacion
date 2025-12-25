/*
Installar JUnit para las pruebas unitarias en
https://github.com/junit-team/junit4/wiki/Download-and-Install
Se puede usar el .jar para proyectos creados con ant
Para proyectos creados con Maven se puede usar el plugin
<dependency>
  <groupId>junit</groupId>
  <artifactId>junit</artifactId>
  <version>4.13</version>
  <scope>test</scope>
</dependency>
Agregando esto a las dependencias del proyecto en el pom.xml
*/

package com.jimsimrodev;

import java.util.Arrays;
import java.util.Collection;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import java.time.LocalDate;
import static java.time.format.DateTimeFormatter.ofPattern;
import static com.jimsimrodev.Suma.suma;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;

import static java.time.format.DateTimeFormatter.ofPattern;

import java.util.Arrays;
import java.util.Collection;
import java.time.LocalDate;

/**
 * Suma
 */
public class Suma {
  public static double suma(double a, double b) {
    return a + b;
  }

  /**
   * @return
   */
  public static Collection<String[]> data() {
    return Arrays.asList(
        new String[][] {
            { "Name: ", "JimsimroDev" },
            { "age: ", "28" },
            { "birthDate: ", LocalDate.now().format(ofPattern("dd/MM/yyyy")) },
            { "programinLenguages: ", "Java, Python, C++, C#" },
        });
  }

  public static void print(double resultado) {
    System.out.printf("La suma es: %s%n", resultado);
  }

  // Esta clase debe ir en el paquete de pruebas unitarias

  @RunWith(Parameterized.class)
  public class SumaTest {
    private final String key;
    private final String value;

    public SumaTest(String key, String value) {
      this.key = key;
      this.value = value;
    }

    @Test
    public void sumaTest() {

      // Para operaciones con decimales
      Assertions.assertEquals(6.0, suma(4.0, 2.0), 0.0001);
      assertEquals(-2.0, suma(5.0, -7.0), 0.0001);
      assertEquals(0.0, suma(0.0, 0.0), 0.0001);
      assertEquals(4.6, suma(2.5, 2.1), 0.0001);
      assertEquals(4.1, suma(2.1, 2.0), 0.0001);
      assertEquals(5.0, suma(2.5, 2.5), 0.0001);
      assertEquals(4.5, suma(2, 2.5), 0.0001);
      // assertEquals(5.0, suma("2.5", 2.5), 0.0001);//error
    }

    // Pruebas parametrizables
    @Parameterized.Parameters
    public static Collection<String[]> data() {
      return Arrays.asList(
          new String[][] {
              { "name: ", "jimsimrodev" },
              { "age: ", "28" },
              { "birthDate: ", LocalDate.now().format(ofPattern("dd/MM/yyyy")) },
              { "programinlenguages: ", "java, python, c++, c#" },
          });
    }

    @Test
    public void testfieldsexist() {
      assertNotNull("La clave no debe ser nula", key);
      assertFalse("La clave no debe estar vacía", key.trim().isEmpty());
      assertNotNull("El valor no debe ser nulo", value);
      assertFalse("El valor no debe estar vacío", value.trim().isEmpty());

    }

  }

  public static void main(String[] args) {
    print(suma(4, 2));
    print(suma(-4.0, 2.0));

    for (String[] data : data()) {
      for (String string : data) {
        System.out.print(string);
      }
      System.out.println(" ");
    }
  }
}
