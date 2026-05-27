/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class JimsimroDev {
  // Filtra por pares imprime solo los numeros pares
  private static List<Integer> filtrarPares(List<Integer> numeros) {
    var pares = numeros.stream().filter(n -> n % 2 == 0).toList();
    return pares;
  }

  // Ordena de mayor a menor
  private static List<Integer> ordenardeMayorAmenor(List<Integer> numeros) {
    var numerosOrdenadosDescendente = numeros.stream().sorted(Comparator.reverseOrder()).toList();
    return numerosOrdenadosDescendente;
  }

  // Multiplicar * 2
  private static List<Integer> multiplicarPorDos(List<Integer> numeros) {
    var numerosMultiplicados = numeros.stream().map(n -> n * 2).toList();
    return numerosMultiplicados;
  }

  // Extra
  static class Alumno {
    private String nombre;
    private String fechaNacimiento;
    private List<Double> calificacion;

    Alumno(String nombre, String fechaNacimientos, List<Double> calificacion) {
      this.nombre = nombre;
      this.fechaNacimiento = fechaNacimientos;
      this.calificacion = calificacion;
    }

    // Inicializa la lista de esutiantes
    private static List<Alumno> obtenerAlumnos() {
      List<Alumno> estudiantes = Arrays.asList(
          new Alumno("Jhoan", "28/07/1995", Arrays.asList(7.7, 4.1, 3.9)),
          new Alumno("Juan", "05/08/1994", Arrays.asList(9.7, 9.1, 9.0)),
          new Alumno("Mario", "07/11/1990", Arrays.asList(8.0, 9.1, 9.9)),
          new Alumno("Keren", "20/12/2016", Arrays.asList(9.8, 9.9, 10.0)));
      return estudiantes;
    }

    @Override
    public String toString() {
      return String.format("{ Nombre: %s - Fecha Nacimiento: %s }", nombre, fechaNacimiento);
    }
  }

  static void print(Object... args) {
    for (Object s : args) {
      System.out.print(s + "\n");
    }
  }

  // Promedio calificaciones: Obtiene una lista de estudiantes por nombre y
  // promedio de sus calificaciones.
  private static void mostrarPromedioPorAlumnos() {
    List<String> promedioEstudiante = Alumno.obtenerAlumnos().stream()
        .map(s -> {
          double promedio = s.calificacion.stream()
              .mapToDouble(d -> d).average().getAsDouble();
          return String.format("Nombre: %s - Fecha Nacimiento: %s - Promedio:  %.2f%n ", s.nombre, s.fechaNacimiento,
              promedio);
        }).toList();
    print(promedioEstudiante);
  }

  // Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes que
  // tienen calificaciones con un 9 o más de promedio.
  private static void getMayorPromedio() {
    print("Estudiantes con Promedio >= 9");
    print(Alumno.obtenerAlumnos().stream()
        .filter(s -> s.calificacion.stream()
            .mapToDouble(d -> d).average().getAsDouble() >= 9)
        .map(estudiante -> {
          double promedio = estudiante.calificacion.stream()
              .mapToDouble(d -> d).average().getAsDouble();
          return String.format("Nombre: %s - Promedio:  %.2f%n ", estudiante.nombre, promedio);
        }).toList());
  }

  // Obtiene una lista de estudiantes ordenada desde el más joven.
  private static void mostrarAlumnoPorEdadDescendente() {
    print("Estudiantes ordenado por fecha nacimiento");
    Alumno.obtenerAlumnos().stream()
        .sorted(Comparator
            .comparing((Alumno e) -> LocalDate.parse(e.fechaNacimiento, DateTimeFormatter.ofPattern("dd/MM/yyyy")))
            .reversed())
        .forEach(System.out::println);
  }

  // Mayor calificación: Obtiene la calificación más alta de entre todas las de
  // los alumnos.
  private static void mostrarCalificacionMasAltaPorEstudiante() {
    print("La notas mas alta entre todos");
    Alumno.obtenerAlumnos().stream()
        .mapToDouble(d -> d.calificacion.stream()
            .mapToDouble(n -> n)
            .max().getAsDouble())
        .max().ifPresent(System.out::println);

  }

  // Mayor calificación: Obtiene la calificación más alta de entre todas las de
  // los alumnos.
  private static void mostrarCalificacionMasAltaGlobal() {
    double notaMaxima = Alumno.obtenerAlumnos().stream()
        .flatMapToDouble(e -> e.calificacion.stream()
            .mapToDouble(d -> d))
        .max().getAsDouble();
    print(notaMaxima);
  }

  public static void main(String[] args) {
    List<Integer> listaNumeros = Arrays.asList(8, 9, 12, 1, 4, 6, 7, 11, 5, 10, 2, 3);
    print("Números ordenados  de > a < " + ordenardeMayorAmenor(listaNumeros));
    print("Ordena e imprime solo los pares " + filtrarPares(ordenardeMayorAmenor(listaNumeros)));
    print("Multiplicar el resultado * 2 " + multiplicarPorDos(filtrarPares(ordenardeMayorAmenor(listaNumeros))));
    print("Numeros Impares " + listaNumeros.stream().filter(n -> n % 2 == 1).toList());
    print("Mayor " + listaNumeros.stream().max(Integer::compare).get());
    print("Menor " + listaNumeros.stream().min(Integer::compare).get());

    // Extra
    mostrarPromedioPorAlumnos();
    getMayorPromedio();
    mostrarAlumnoPorEdadDescendente();
    mostrarCalificacionMasAltaPorEstudiante();
    mostrarCalificacionMasAltaGlobal();

    List<Double> average = Alumno.obtenerAlumnos().stream()
        .map(estudiante -> estudiante.calificacion
            .stream()
            .mapToDouble(d -> d)
            .average().getAsDouble())
        .toList();
    print("Average " + average);
  }
}
