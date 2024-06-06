package com.amsoft;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.util.Set;

import com.amsoft.jsonandxml.LocalDateTypeAdapter;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

/*
 *    --- dependencies----
 *     <dependency>
            <groupId>com.fasterxml.jackson.dataformat</groupId>
            <artifactId>jackson-dataformat-xml</artifactId>
            <version>2.11.1</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.datatype</groupId>
            <artifactId>jackson-datatype-jsr310</artifactId>
            <version>2.14.1</version>
        </dependency>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.10.1</version>
        </dependency>
 */

public class Main {
    public static void main(String[] args) throws IOException {
        // Creación de objetos.
        Programmer programmer = new Programmer();
        programmer.setName("Amador Quispe Huaycho");
        programmer.setAge(31);
        programmer.setBirthDate(LocalDate.of(1992, 7, 13));
        programmer.setLanguages(Set.of("Go", "Java"));

        // JSON
        Path pathJson = Path.of("AmadorQuispe.json");
        if (!Files.exists(pathJson)) {
            Files.createFile(pathJson);
        }
        JSONManage<Programmer> jsonManage = new JSONManage<>(pathJson);
        jsonManage.serialize(programmer);
        Programmer programmerFromJson = jsonManage.deserialize(TypeToken.get(Programmer.class));
        System.out.println(programmerFromJson);
        Files.delete(pathJson);

        // XML
        Path pathXml = Path.of("AmadorQuispe.xml");
        if (!Files.exists(pathXml)) {
            Files.createFile(pathXml);
        }
        XMLManager<Programmer> xmlManager = new XMLManager<>(pathXml);
        TypeReference<Programmer> typeReference = new TypeReference<Programmer>() {
        };
        xmlManager.serialize(programmer);
        Programmer programmerFromXml = xmlManager.deserialize(typeReference);
        System.out.println(programmerFromXml);
        Files.delete(pathXml);
    }
}

class Programmer {
    private String name;
    private Integer age;
    private LocalDate birthDate;
    private Set<String> languages;

    public Programmer() {
    }

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

class XMLManager<T> {
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

class JSONManage<T> {
    private Path path;
    private Gson gson;

    public JSONManage(Path path) {
        this.path = path;
        this.gson = new GsonBuilder()
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