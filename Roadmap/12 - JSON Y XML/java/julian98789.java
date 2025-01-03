package org.example;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

import java.io.File;
import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Datos de prueba
        List<String> lenguajesProgramacion = new ArrayList<>();
        lenguajesProgramacion.add("C++");
        lenguajesProgramacion.add("Java");
        lenguajesProgramacion.add("JavaScript");
        lenguajesProgramacion.add("Python");

        Persona persona = new Persona("Julian", 19, "12/11/2000", lenguajesProgramacion);


        crearArchivoJSON(persona, "persona.json");
        crearArchivoXML(persona, "persona.xml");

        Persona personaDesdeJSON = leerArchivoJSON("persona.json");
        Persona personaDesdeXML = leerArchivoXML("persona.xml");

        System.out.println("Datos leídos desde JSON:");
        System.out.println(personaDesdeJSON);
        System.out.println("Datos leídos desde XML:");
        System.out.println(personaDesdeXML);

        borrarArchivo("persona.json");
        borrarArchivo("persona.xml");
    }

    public static void crearArchivoJSON(Persona persona, String fileName) {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.registerModule(new JavaTimeModule());

        try {
            objectMapper.writeValue(new File(fileName), persona);
            System.out.println("Archivo JSON creado exitosamente.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void crearArchivoXML(Persona persona, String fileName) {
        XmlMapper xmlMapper = new XmlMapper();
        xmlMapper.registerModule(new JavaTimeModule());

        try {
            xmlMapper.writeValue(new File(fileName), persona);
            System.out.println("Archivo XML creado exitosamente.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static Persona leerArchivoJSON(String fileName) {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.registerModule(new JavaTimeModule());

        try {
            return objectMapper.readValue(new File(fileName), Persona.class);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static Persona leerArchivoXML(String fileName) {
        XmlMapper xmlMapper = new XmlMapper();
        xmlMapper.registerModule(new JavaTimeModule());

        try {
            return xmlMapper.readValue(new File(fileName), Persona.class);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void borrarArchivo(String fileName) {
        File file = new File(fileName);
        if (file.exists()) {
            boolean deleted = file.delete();
            if (deleted) {
                System.out.println("Archivo " + fileName + " borrado exitosamente.");
            } else {
                System.out.println("No se pudo borrar el archivo " + fileName + ".");
            }
        } else {
            System.out.println("El archivo " + fileName + " no existe.");
        }
    }

    public static class Persona {
        private String nombre;
        private int edad;

        @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd/MM/yyyy")
        private LocalDate fechaNacimiento;

        private List<String> lenguajesProgramacion;

        public Persona() {}

        public Persona(String nombre, int edad, String fechaNacimiento, List<String> lenguajesProgramacion) {
            this.nombre = nombre;
            this.edad = edad;
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
            this.fechaNacimiento = LocalDate.parse(fechaNacimiento, formatter);
            this.lenguajesProgramacion = lenguajesProgramacion;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public int getEdad() {
            return edad;
        }

        public void setEdad(int edad) {
            this.edad = edad;
        }

        public LocalDate getFechaNacimiento() {
            return fechaNacimiento;
        }

        public void setFechaNacimiento(LocalDate fechaNacimiento) {
            this.fechaNacimiento = fechaNacimiento;
        }

        public List<String> getLenguajesProgramacion() {
            return lenguajesProgramacion;
        }

        public void setLenguajesProgramacion(List<String> lenguajesProgramacion) {
            this.lenguajesProgramacion = lenguajesProgramacion;
        }

        @Override
        public String toString() {
            return "Persona{" +
                    "nombre='" + nombre + '\'' +
                    ", edad=" + edad +
                    ", fechaNacimiento=" + fechaNacimiento +
                    ", lenguajesProgramacion=" + lenguajesProgramacion +
                    '}';
        }
    }
}
