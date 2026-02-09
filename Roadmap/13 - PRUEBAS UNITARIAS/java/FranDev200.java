import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;

/*
    ------ POM.xml ------ [Partes añadidas]
    <dependencies>

        <!-- JUnit 5 -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.1</version>
            <scope>test</scope>
        </dependency>

    </dependencies>

    <build>
        <plugins>

            <!-- Plugin necesario para ejecutar JUnit 5 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.5</version>
            </plugin>

        </plugins>
    </build>


 */

public class FranDev200 {

    /*

    Crea una función que se encargue de sumar dos números y retornar su resultado.
    * Crea un test, utilizando las herramientas de tu lenguaje, que sea
    * capaz de determinar si esa función se ejecuta correctamente.

     */
    public static int Sumar(int a, int b){

        int resultado = a + b;
        return resultado;

    }

    @Test
    public void testSumar(){
        int sumar = Sumar(1,2);
        Assertions.assertEquals(sumar,1); // Da ERROR
        Assertions.assertEquals(sumar,3); // No da ERROR
        Assertions.assertEquals(sumar,2); // Da ERROR
    }

    /*

    DIFICULTAD EXTRA (opcional):
    * Crea un diccionario con las siguientes claves y valores:
    * "name": "Tu nombre"
    * "age": "Tu edad"
    * "birth_date": "Tu fecha de nacimiento"
    * "programming_languages": ["Listado de lenguajes de programación"]
    * Crea dos test:
    * - Un primero que determine que existen todos los campos.
    * - Un segundo que determine que los datos introducidos son correctos.

     */

    public static HashMap<String,Object> crearPersona(){

        ArrayList<String> lenguajesProgramacion = new ArrayList<>();
        lenguajesProgramacion.add("Java");
        lenguajesProgramacion.add("Python");
        lenguajesProgramacion.add("SQL");
        lenguajesProgramacion.add("C#");

        HashMap<String,Object> persona = new HashMap<>();
        persona.put("name","Fran");
        persona.put("age", 20);
        persona.put("birth_date", "13-12-2005");
        persona.put("programming_languages", lenguajesProgramacion);

        return persona;

    }

    @Test
    public void todosLosCampos(){

        HashMap<String,Object> persona = crearPersona();
        Assertions.assertTrue(persona.containsKey("name"));
        Assertions.assertTrue(persona.containsKey("age"));
        Assertions.assertTrue(persona.containsKey("birth_date"));
        Assertions.assertTrue(persona.containsKey("programming_languages"));

        System.out.println("Todos los campos están incluidos. [Test 1]");

    }

    @Test
    public void verificarDatos(){

        String nombre = "Fran";
        int edad = 20;
        String fechaNacimiento = "13-12-2005";
        ArrayList<String> lenguajesProgramacion = new ArrayList<>();
        lenguajesProgramacion.add("Java");
        lenguajesProgramacion.add("Python");
        lenguajesProgramacion.add("SQL");
        lenguajesProgramacion.add("C#");

        HashMap<String,Object> persona = crearPersona();

        Assertions.assertEquals(nombre,persona.get("name"));
        Assertions.assertEquals(edad,persona.get("age"));
        Assertions.assertEquals(fechaNacimiento,persona.get("birth_date"));
        Assertions.assertEquals(lenguajesProgramacion,persona.get("programming_languages"));

        System.out.println("Todos los campos coinciden. [Test 2]");

    }

}
