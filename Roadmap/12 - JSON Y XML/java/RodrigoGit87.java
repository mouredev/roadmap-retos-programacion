import java.io.IOException;
import java.nio.file.*;
import java.util.*;

public class RodrigoGit87 {
    private static final String ARCHIVO_JSON = "RodrigoGit87.json";
    private static final String ARCHIVO_XML = "RodrigoGit87.xml";

    public static void main(String[] args){
        Usuario nuevoUsuario;
        nuevoUsuario = new Usuario("Rodrigo", 38, "24-05-1987",
                List.of(
                "java",
                "javascript",
                "HTML",
                "CSS",
                "SQL"));

        // Crear builders
        StringBuilder json = new StringBuilder();
        StringBuilder xml = new StringBuilder();

        //Añadir el texto en JSON
        json.append("{\n");
        json.append("  \"nombre\": \"").append(nuevoUsuario.getNombre()).append("\",\n");
        json.append(" \"edad\": ").append(nuevoUsuario.getEdad()).append(",\n");
        json.append(" \"fecha_nacimiento\": \"").append(nuevoUsuario.getFecha_nacimiento()).append("\",\n ");
        json.append("\"lenguajes\": [ \"");
        json.append(String.join("\", \"",nuevoUsuario.getLenguajes()));
        json.append("\" ]\n");
        json.append("}\n");

        System.out.println(json.toString());


        //Añadir el texto en XML
        xml.append("<usuario>\n");
        xml.append(" <nombre>"+nuevoUsuario.getNombre()+"</nombre>\n");
        xml.append(" <edad>"+nuevoUsuario.getEdad()+"</edad>\n");
        xml.append(" <fecha_nacimiento>"+nuevoUsuario.getFecha_nacimiento()+"</fecha_nacimiento>\n");
        xml.append(" <lenguajes>");
        for (String key: nuevoUsuario.getLenguajes()) xml.append(" <lenguaje>").append(key).append("</lenguaje>\n");
        xml.append(" </lenguajes>\n");
        xml.append("</usuario>\n");


        //RUTAS
        Path rutaJson = Paths.get(ARCHIVO_JSON);
        Path rutaXML = Paths.get(ARCHIVO_XML);

        //ESCRIBIR LOS DATOS EN UN ARCHIVO
        try {
            Files.writeString(rutaJson, json.toString());
            Files.writeString(rutaXML, xml.toString());
            System.out.println("Archivos creados\n");
        } catch (Exception e) {
            System.err.println ("Error al crear ficheros: "+ e.getMessage()+"\n");
        }

        //MOSTRAR CONTENIDO
        try {
            System.out.println(" - ARCHIVO JSON-\n"+Files.readString(rutaJson));
        } catch (IOException e) {
            System.err.println ("Error al leer archivo de rutaJSON: "+ e.getMessage()+"\n");
        }
        try {
            System.out.println("- ARCHIVO XML -\n" + Files.readString(rutaXML));
        } catch (IOException e) {
            System.err.println ("Error al leer archivo de ruta XML: "+ e.getMessage()+"\n");
        }

        // BORRAR CONTENIDO
        try {
            Files.deleteIfExists(rutaJson);
            System.out.println("JSON eliminado\n");
        } catch (IOException e) {
            System.err.println("Error al eliminar archivo de rutaJSON: "+ e.getMessage()+"\n");
        }

        try {
            Files.deleteIfExists(rutaXML);
            System.out.println("XML eliminado\n");
        } catch (IOException e) {
            System.err.println("Error al eliminar archivo de ruta XML: "+ e.getMessage()+"\n");
        }
    }



        // ----------------------
        // Clase User
        //---------------------
        static class Usuario {
            private String nombre;
            private int edad;
            private String fecha_nacimiento;
            private List<String> lenguajes;

            public Usuario(String nombre, int edad, String fecha_nacimiento, List<String> lenguajes) {
                this.nombre = nombre;
                this.edad = edad;
                this.fecha_nacimiento = fecha_nacimiento;
                this.lenguajes = lenguajes;
            }

            @Override
            public String toString() {
                return "Usuario{" +
                        "nombre='" + nombre + '\'' +
                        ", edad='" + edad + '\'' +
                        ", fecha_nacimiento='" + fecha_nacimiento + '\'' +
                        ", lenguajes=" + lenguajes +
                        '}';
            }

            //Getters & Setters
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

            public String getFecha_nacimiento() {
                return fecha_nacimiento;
            }

            public void setFecha_nacimiento(String fecha_nacimiento) {
                this.fecha_nacimiento = fecha_nacimiento;
            }

            public List<String> getLenguajes() {
                return lenguajes;
            }

            public void setLenguajes(List<String> lenguajes) {
                this.lenguajes = lenguajes;
            }
        }
}