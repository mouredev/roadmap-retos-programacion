import java.io.IOException;
import java.nio.file.Path;
import java.util.List;
import java.nio.file.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class LogicaJava12 {

    public static void main(String[] args) {

        // XML
        
        String nombre = "Lautaro";
        int edad = 21;
        String fechaNacimiento = "2004-11-11";
        List<String> lenguajes = List.of("Java", "Python", "Go");

        Path xmlPath = Path.of("persona.xml");

        String xml =
                """
                <?xml version="1.0" encoding="UTF-8"?>
                <data>
                  <nombre>""" + nombre + "</nombre>\n" +
                "  <edad>" + edad + "</edad>\n" +
                "  <fechaNacimiento>" + fechaNacimiento + "</fechaNacimiento>\n" +
                "  <lenguajes>\n";

        for (String lang : lenguajes) {
            xml += "    <lenguaje>" + lang + "</lenguaje>\n";
        }

        xml +=
                """
                  </lenguajes>
                </data>""";

        try {
            Files.writeString(xmlPath, xml);
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava12.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        System.out.println("=== XML ===");
        try {
            Files.readAllLines(xmlPath).forEach(System.out::println);
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava12.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        try {
            Files.delete(xmlPath);
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava12.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        // JSON
                Path jsonPath = Path.of("persona.json");

        String json =
                "{\n" +
                "  \"nombre\": \"" + nombre + "\",\n" +
                "  \"edad\": " + edad + ",\n" +
                "  \"fechaNacimiento\": \"" + fechaNacimiento + "\",\n" +
                "  \"lenguajes\": [\n";

        for (int i = 0; i < lenguajes.size(); i++) {
            json += "    \"" + lenguajes.get(i) + "\"";
            if (i < lenguajes.size() - 1) json += ",";
            json += "\n";
        }

        json +=
                "  ]\n" +
                "}";

        try {
            Files.writeString(jsonPath, json);
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava12.class.getName()).log(Level.SEVERE, null, ex);
        }

        System.out.println("\n=== JSON ===");
        try {
            Files.readAllLines(jsonPath).forEach(System.out::println);
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava12.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        try {
            Files.delete(jsonPath);
        } catch (IOException ex) {
            Logger.getLogger(LogicaJava12.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
