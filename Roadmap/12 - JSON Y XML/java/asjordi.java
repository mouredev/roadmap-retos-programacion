import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

import java.io.File;
import java.io.IOException;
import java.time.LocalDate;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        crearJson();
        leerJson();
        crearXml();
        leerXml();
    }

    record Pojo(String nombre, Integer edad, LocalDate fechaNacimiento, List<String> lenguajes) {}

    static void crearJson() {
        Pojo pojo = new Pojo("Jordi", 25, LocalDate.of(1995, 8, 1), List.of("Java", "Kotlin", "Scala"));

        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());

        try {
            mapper.writeValue(new File("pojo.json"), pojo);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void leerJson() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());
        File jsonFile = new File("pojo.json");

        try {
            var pojo = mapper.readValue(jsonFile, Pojo.class);
            System.out.println(pojo);
            jsonFile.delete();
            System.out.println("Fichero eliminado");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void crearXml() {
        Pojo pojo = new Pojo("Jordi", 25, LocalDate.of(1995, 8, 1), List.of("Java", "Kotlin", "Scala"));
        ObjectMapper xmlMapper = new XmlMapper();
        xmlMapper.registerModule(new JavaTimeModule());
        xmlMapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);

        try {
            xmlMapper.writeValue(new File("pojo.xml"), pojo);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void leerXml() {
        ObjectMapper xmlMapper = new XmlMapper();
        xmlMapper.registerModule(new JavaTimeModule());
        File xmlFile = new File("pojo.xml");

        try {
            var pojo = xmlMapper.readValue(xmlFile, Pojo.class);
            System.out.println(pojo);
            xmlFile.delete();
            System.out.println("Fichero eliminado");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Maven dependencies:
     * jackson-databind
     * jackson-datatype-jsr310
     * jackson-dataformat-xml
     */

}
