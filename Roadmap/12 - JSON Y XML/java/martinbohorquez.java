import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.TypeAdapter;
import com.google.gson.reflect.TypeToken;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * #12 JSON Y XML
 * <dependencies>
 * <dependency>
 * <groupId>com.fasterxml.jackson.dataformat</groupId>
 * <artifactId>jackson-dataformat-xml</artifactId>
 * <version>2.17.2</version>
 * </dependency>
 * <dependency>
 * <groupId>com.fasterxml.jackson.datatype</groupId>
 * <artifactId>jackson-datatype-jsr310</artifactId>
 * <version>2.17.2</version>
 * </dependency>
 * <dependency>
 * <groupId>com.google.code.gson</groupId>
 * <artifactId>gson</artifactId>
 * <version>2.10.1</version>
 * </dependency>
 * </dependencies>
 *
 * @author martinbohorquez
 */
public class martinbohorquez {

    private static final FileOperation operation = new FileOperation();

    public static void main(String[] args) {
        // Creación de objetos.
        Programmer programmer = new Programmer();
        programmer.setName("Martin B");
        programmer.setAge(29);
        programmer.setBirthDate(LocalDate.of(1994, 9, 26));
        programmer.setLanguages(new HashSet<>(Arrays.asList("Java", "Typescript", "Python")));

        // XML
        String stringXml = "data/martinDev.xml";
        File fileXml = operation.create(stringXml);
        // Serialización
        XMLManager<Programmer> xmlManager = new XMLManager<>(fileXml.toPath());
        xmlManager.serialize(programmer);
        // Deserialización
        TypeReference<Programmer> typeReference = new TypeReference<>() {
        };
        Programmer programmerFromXml = xmlManager.deserialize(typeReference);
        System.out.println(programmerFromXml);
//        operation.delete(fileXml);

        //JSON
        String stringJson = "data/martinDev.json";
        File fileJson = operation.create(stringJson);
        // Serialización
        JSONManager<Programmer> jsonManage = new JSONManager<>(fileJson.toPath());
        jsonManage.serialize(programmer);
        // Deserialización
        Programmer programmerFromJson = jsonManage.deserialize(TypeToken.get(Programmer.class));
        System.out.println(programmerFromJson);
//        operation.delete(fileJson);
    }

    private static class FileOperation {

        private static void printFileEmpty() {
            System.out.println("El archivo se encuentra vacío, no tiene registros!");
        }

        private static void printfException(IOException e, String process) {
            System.out.printf("Error al '%s' en el archivo: '%s'%n", process, e.getMessage());
        }

        private File create(String string) {
            File file = new File(string);
            if (file.getParentFile() != null) file.getParentFile().mkdirs();// Crear la carpeta si no existe
            return file;
        }

        private void write(File file, String string) {
            try (FileWriter writer = new FileWriter(file, true); Scanner reader = new Scanner(file)) {
                writer.append(string).append(System.lineSeparator());
                if (!reader.hasNext()) System.out.printf("Archivo '%s' creado!%n", file);
                else System.out.printf("Archivo '%s' modificado!%n", file);
            } catch (IOException e) {
                printfException(e, "escribir");
            }
        }

        private void read(File file) {
            if (file == null || file.length() == 0) printFileEmpty();
            else {
                try (Scanner reader = new Scanner(file)) {
                    System.out.println("Contenido del archivo: ");
                    while (reader.hasNext()) System.out.println(reader.nextLine());
                } catch (FileNotFoundException e) {
                    printfException(e, "leer");
                }
            }
        }

        private void delete(File file) {
            if (file != null && file.delete()) {
                if (file.getParentFile() != null && file.getParentFile().delete())
                    System.out.printf("Folder '\\%s' eliminado correctamente!%n", file.getParentFile().toString());
                System.out.printf("Archivo '%s' eliminado correctamente!%n", file);
            }
        }
    }

    private static class Programmer {
        private String name;
        private Integer age;
        private LocalDate birthDate;
        private Set<String> languages;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public Integer getAge() {
            return age;
        }

        public void setAge(Integer age) {
            this.age = age;
        }

        public LocalDate getBirthDate() {
            return birthDate;
        }

        public void setBirthDate(LocalDate birthDate) {
            this.birthDate = birthDate;
        }

        public Set<String> getLanguages() {
            return languages;
        }

        public void setLanguages(Set<String> languages) {
            this.languages = languages;
        }

        @Override
        public String toString() {
            return "Programmer : [name=" + name + ", age=" + age + ", birthDate=" + birthDate + ", languages=" + languages
                    + "]";
        }
    }

    private static class XMLManager<T> {
        private XmlMapper xmlMapper;
        private Path path;

        public XMLManager(Path path) {
            this.path = path;
            this.xmlMapper = XmlMapper.builder()
                    .enable(SerializationFeature.INDENT_OUTPUT)
                    .disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS)
                    .build();
            xmlMapper.registerModule(new JavaTimeModule());
        }

        public void serialize(T object) {
            try {
                this.xmlMapper.writeValue(this.path.toFile(), object);
            } catch (Exception e) {
                e.printStackTrace(System.out);
            }
        }

        public T deserialize(TypeReference<T> typeReference) {
            try {
                T objectDeserialize = this.xmlMapper.readValue(this.path.toFile(), typeReference);
                return objectDeserialize;
            } catch (Exception e) {
                e.printStackTrace(System.out);
            }
            return null;
        }
    }

    private static class JSONManager<T> {
        private Path path;
        private Gson gson;

        public JSONManager(Path path) {
            this.path = path;
            this.gson = new GsonBuilder()
                    .setPrettyPrinting() // This enables pretty printing
                    .registerTypeAdapter(LocalDate.class, new LocalDateTypeAdapter())
                    .create();
        }

        public void serialize(T object) {
            try {
                String jsonString = gson.toJson(object);
                Files.writeString(path, jsonString);
            } catch (IOException e) {
                e.printStackTrace(System.out);
            }
        }

        public T deserialize(TypeToken<T> typeToken) {
            try {
                byte[] data = Files.readAllBytes(path);
                T object = gson.fromJson(new String(data), typeToken.getType());
                return object;
            } catch (IOException e) {
                e.printStackTrace();
            }
            return null;
        }
    }

    // Type Adapter for LocalDate
    private static class LocalDateTypeAdapter extends TypeAdapter<LocalDate> {
        private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ISO_LOCAL_DATE;

        @Override
        public LocalDate read(JsonReader jsonReader) throws IOException {
            if (jsonReader.peek() == com.google.gson.stream.JsonToken.NULL) {
                jsonReader.nextNull();
                return null;
            } else {
                return LocalDate.parse(jsonReader.nextString(), FORMATTER);
            }
        }

        @Override
        public void write(JsonWriter jsonWriter, LocalDate localDate) throws IOException {
            if (localDate == null) {
                jsonWriter.nullValue();
            } else {
                jsonWriter.value(localDate.format(FORMATTER));
            }
        }
    }
}
