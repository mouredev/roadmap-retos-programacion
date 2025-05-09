import java.io.*;
import java.util.*;
import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.*;
import javax.xml.transform.stream.*;
import org.w3c.dom.*;
import org.json.simple.*;
import org.json.simple.parser.*;

public class eulogioep {
    public static void main(String[] args) {
        // Datos de ejemplo
        String nombre = "Juan";
        int edad = 30;
        String fechaNacimiento = "1993-05-15";
        List<String> lenguajesProgramacion = Arrays.asList("Java", "Python", "JavaScript");

        // Crear y mostrar archivo XML
        crearArchivoXML(nombre, edad, fechaNacimiento, lenguajesProgramacion);
        System.out.println("Contenido del archivo XML:");
        mostrarContenidoArchivo("datos.xml");

        // Crear y mostrar archivo JSON
        crearArchivoJSON(nombre, edad, fechaNacimiento, lenguajesProgramacion);
        System.out.println("\nContenido del archivo JSON:");
        mostrarContenidoArchivo("datos.json");

        // Borrar archivos
        borrarArchivo("datos.xml");
        borrarArchivo("datos.json");

        // DIFICULTAD EXTRA
        // Crear archivos nuevamente para la lectura
        crearArchivoXML(nombre, edad, fechaNacimiento, lenguajesProgramacion);
        crearArchivoJSON(nombre, edad, fechaNacimiento, lenguajesProgramacion);

        // Leer y transformar datos
        Persona personaXML = leerXML("datos.xml");
        Persona personaJSON = leerJSON("datos.json");

        System.out.println("\nDatos leídos del XML:");
        System.out.println(personaXML);
        System.out.println("\nDatos leídos del JSON:");
        System.out.println(personaJSON);

        // Borrar archivos nuevamente
        borrarArchivo("datos.xml");
        borrarArchivo("datos.json");
    }

    // Método para crear el archivo XML
    public static void crearArchivoXML(String nombre, int edad, String fechaNacimiento, List<String> lenguajesProgramacion) {
        try {
            DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = docFactory.newDocumentBuilder();

            // Crear el elemento raíz
            Document doc = docBuilder.newDocument();
            Element rootElement = doc.createElement("persona");
            doc.appendChild(rootElement);

            // Agregar elementos hijos
            Element nombreElement = doc.createElement("nombre");
            nombreElement.setTextContent(nombre);
            rootElement.appendChild(nombreElement);

            Element edadElement = doc.createElement("edad");
            edadElement.setTextContent(String.valueOf(edad));
            rootElement.appendChild(edadElement);

            Element fechaNacimientoElement = doc.createElement("fechaNacimiento");
            fechaNacimientoElement.setTextContent(fechaNacimiento);
            rootElement.appendChild(fechaNacimientoElement);

            Element lenguajesElement = doc.createElement("lenguajesProgramacion");
            for (String lenguaje : lenguajesProgramacion) {
                Element lenguajeElement = doc.createElement("lenguaje");
                lenguajeElement.setTextContent(lenguaje);
                lenguajesElement.appendChild(lenguajeElement);
            }
            rootElement.appendChild(lenguajesElement);

            // Escribir el contenido en un archivo XML
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File("datos.xml"));
            transformer.transform(source, result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Método para crear el archivo JSON
    @SuppressWarnings("unchecked")
    public static void crearArchivoJSON(String nombre, int edad, String fechaNacimiento, List<String> lenguajesProgramacion) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("nombre", nombre);
        jsonObject.put("edad", edad);
        jsonObject.put("fechaNacimiento", fechaNacimiento);
        jsonObject.put("lenguajesProgramacion", lenguajesProgramacion);

        try (FileWriter file = new FileWriter("datos.json")) {
            file.write(jsonObject.toJSONString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Método para mostrar el contenido de un archivo
    public static void mostrarContenidoArchivo(String nombreArchivo) {
        try (BufferedReader br = new BufferedReader(new FileReader(nombreArchivo))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Método para borrar un archivo
    public static void borrarArchivo(String nombreArchivo) {
        File archivo = new File(nombreArchivo);
        if (archivo.delete()) {
            System.out.println("El archivo " + nombreArchivo + " ha sido borrado.");
        } else {
            System.out.println("No se pudo borrar el archivo " + nombreArchivo);
        }
    }

    // DIFICULTAD EXTRA

    // Clase personalizada para almacenar los datos
    static class Persona {
        String nombre;
        int edad;
        String fechaNacimiento;
        List<String> lenguajesProgramacion;

        @Override
        public String toString() {
            return "Persona{" +
                    "nombre='" + nombre + '\'' +
                    ", edad=" + edad +
                    ", fechaNacimiento='" + fechaNacimiento + '\'' +
                    ", lenguajesProgramacion=" + lenguajesProgramacion +
                    '}';
        }
    }

    // Método para leer el archivo XML y convertirlo a la clase Persona
    public static Persona leerXML(String nombreArchivo) {
        Persona persona = new Persona();
        try {
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(new File(nombreArchivo));
            doc.getDocumentElement().normalize();

            persona.nombre = doc.getElementsByTagName("nombre").item(0).getTextContent();
            persona.edad = Integer.parseInt(doc.getElementsByTagName("edad").item(0).getTextContent());
            persona.fechaNacimiento = doc.getElementsByTagName("fechaNacimiento").item(0).getTextContent();

            persona.lenguajesProgramacion = new ArrayList<>();
            NodeList lenguajesList = doc.getElementsByTagName("lenguaje");
            for (int i = 0; i < lenguajesList.getLength(); i++) {
                persona.lenguajesProgramacion.add(lenguajesList.item(i).getTextContent());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return persona;
    }

    // Método para leer el archivo JSON y convertirlo a la clase Persona
    public static Persona leerJSON(String nombreArchivo) {
        Persona persona = new Persona();
        JSONParser parser = new JSONParser();

        try (FileReader reader = new FileReader(nombreArchivo)) {
            JSONObject jsonObject = (JSONObject) parser.parse(reader);

            persona.nombre = (String) jsonObject.get("nombre");
            persona.edad = ((Long) jsonObject.get("edad")).intValue();
            persona.fechaNacimiento = (String) jsonObject.get("fechaNacimiento");
            persona.lenguajesProgramacion = (List<String>) jsonObject.get("lenguajesProgramacion");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return persona;
    }
}