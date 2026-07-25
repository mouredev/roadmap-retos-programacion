import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;
import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.*;
import javax.xml.transform.stream.*;
import org.w3c.dom.*;

public class AnaLauDB {

    // Nombres de archivo
    private static final String ARCHIVO_XML = "AnaLauDB_data.xml";
    private static final String ARCHIVO_JSON = "AnaLauDB_data.json";

    public static void main(String[] args) {
        try {

            Persona p = new Persona(
                    "Ana Laura Doroteo Barrientos",
                    23,
                    "09-05-2002",
                    Arrays.asList("Java", "Python", "JavaScript", "C", "CSS"));

            // 1) Crear archivos
            crearXML(p, ARCHIVO_XML);
            crearJSON(p, ARCHIVO_JSON);

            // 2) Mostrar contenidos crudos
            System.out.println("=== Contenido XML creado ===");
            imprimirArchivo(ARCHIVO_XML);
            System.out.println("\n=== Contenido JSON creado ===");
            imprimirArchivo(ARCHIVO_JSON);

            // 3) Leer y transformar en la misma clase Persona
            System.out.println("\n=== Convirtiendo XML a Persona ===");
            Persona desdeXml = leerXML(ARCHIVO_XML);
            System.out.println(desdeXml);

            System.out.println("\n=== Convirtiendo JSON a Persona ===");
            Persona desdeJson = leerJSON(ARCHIVO_JSON);
            System.out.println(desdeJson);

            // 4) Borrar archivos
            borrarArchivo(ARCHIVO_XML);
            borrarArchivo(ARCHIVO_JSON);
            System.out.println("\nArchivos borrados. Fin de la ejecución.");

        } catch (Exception e) {
            // Capturamos todo de forma segura para que no se caiga el programa
            System.out.println("Ocurrió un error: " + e.getClass().getSimpleName() + " - " + e.getMessage());
            e.printStackTrace();
        }
    }

    // ==========================
    // Métodos para crear archivos
    // ==========================
    private static void crearXML(Persona p, String ruta) throws Exception {
        // Build DOM
        DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = docFactory.newDocumentBuilder();

        // Documento
        Document doc = docBuilder.newDocument();
        Element rootElement = doc.createElement("persona");
        doc.appendChild(rootElement);

        // Nombre
        Element nombre = doc.createElement("nombre");
        nombre.appendChild(doc.createTextNode(p.nombre));
        rootElement.appendChild(nombre);

        // Edad
        Element edad = doc.createElement("edad");
        edad.appendChild(doc.createTextNode(String.valueOf(p.edad)));
        rootElement.appendChild(edad);

        // Fecha de nacimiento
        Element dob = doc.createElement("fechaNacimiento");
        dob.appendChild(doc.createTextNode(p.fechaNacimiento));
        rootElement.appendChild(dob);

        // Lenguajes
        Element lenguajes = doc.createElement("lenguajes");
        for (String lang : p.lenguajes) {
            Element langElem = doc.createElement("lenguaje");
            langElem.appendChild(doc.createTextNode(lang));
            lenguajes.appendChild(langElem);
        }
        rootElement.appendChild(lenguajes);

        // Escribir a archivo
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        // Opcional: formato legible
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "2");

        DOMSource source = new DOMSource(doc);
        StreamResult result = new StreamResult(new File(ruta));
        transformer.transform(source, result);
    }

    private static void crearJSON(Persona p, String ruta) throws IOException {
        // Generamos JSON manualmente (formato controlado)
        StringBuilder sb = new StringBuilder();
        sb.append("{\n");
        sb.append("  \"nombre\": ").append(escapeJson(p.nombre)).append(",\n");
        sb.append("  \"edad\": ").append(p.edad).append(",\n");
        sb.append("  \"fechaNacimiento\": ").append(escapeJson(p.fechaNacimiento)).append(",\n");
        sb.append("  \"lenguajes\": [\n");
        for (int i = 0; i < p.lenguajes.size(); i++) {
            sb.append("    ").append(escapeJson(p.lenguajes.get(i)));
            if (i < p.lenguajes.size() - 1)
                sb.append(",");
            sb.append("\n");
        }
        sb.append("  ]\n");
        sb.append("}\n");

        Files.write(Paths.get(ruta), sb.toString().getBytes());
    }

    // Simple helper to wrap strings as JSON string with escaping of
    // quotes/backslashes
    private static String escapeJson(String s) {
        String escaped = s.replace("\\", "\\\\").replace("\"", "\\\"");
        return "\"" + escaped + "\"";
    }

    // ==========================
    // Mostrar archivo por consola
    // ==========================
    private static void imprimirArchivo(String ruta) {
        try {
            List<String> lines = Files.readAllLines(Paths.get(ruta));
            for (String l : lines)
                System.out.println(l);
        } catch (IOException e) {
            System.out.println("No se pudo leer " + ruta + ": " + e.getMessage());
        }
    }

    // ==========================
    // Parseo XML -> Persona
    // ==========================
    private static Persona leerXML(String ruta) {
        try {
            File fXmlFile = new File(ruta);
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(fXmlFile);
            doc.getDocumentElement().normalize();

            String nombre = getTagValue("nombre", doc.getDocumentElement());
            int edad = Integer.parseInt(getTagValue("edad", doc.getDocumentElement()));
            String fecha = getTagValue("fechaNacimiento", doc.getDocumentElement());

            List<String> langs = new ArrayList<>();
            NodeList nl = doc.getElementsByTagName("lenguaje");
            for (int i = 0; i < nl.getLength(); i++) {
                Node node = nl.item(i);
                if (node.getNodeType() == Node.ELEMENT_NODE) {
                    langs.add(node.getTextContent());
                }
            }
            return new Persona(nombre, edad, fecha, langs);
        } catch (Exception e) {
            System.out.println("Error leyendo XML: " + e.getMessage());
            return null;
        }
    }

    private static String getTagValue(String tag, Element element) {
        NodeList nodeList = element.getElementsByTagName(tag);
        if (nodeList != null && nodeList.getLength() > 0) {
            Node node = nodeList.item(0);
            return node.getTextContent();
        }
        return "";
    }

    // ==========================
    // Parseo JSON -> Persona (parsing simple y controlado)
    // ==========================
    private static Persona leerJSON(String ruta) {
        try {
            String content = new String(Files.readAllBytes(Paths.get(ruta)));

            // Extraer nombre
            String nombre = extractJsonString(content, "\"nombre\"\\s*:\\s*\"([^\"]*)\"");
            // Extraer edad (número)
            String edadStr = extractJsonString(content, "\"edad\"\\s*:\\s*(\\d+)");
            int edad = edadStr.isEmpty() ? 0 : Integer.parseInt(edadStr);
            // Extraer fecha
            String fecha = extractJsonString(content, "\"fechaNacimiento\"\\s*:\\s*\"([^\"]*)\"");
            // Extraer lenguajes (lista)
            List<String> langs = new ArrayList<>();
            // Buscamos el array completo entre "lenguajes": [ ... ]
            Pattern p = Pattern.compile("\"lenguajes\"\\s*:\\s*\\[(.*?)\\]", Pattern.DOTALL);
            Matcher m = p.matcher(content);
            if (m.find()) {
                String inside = m.group(1); // contenido entre corchetes
                // Buscar strings entre comillas dentro
                Pattern strPat = Pattern.compile("\"([^\"]*)\"");
                Matcher mm = strPat.matcher(inside);
                while (mm.find()) {
                    langs.add(mm.group(1));
                }
            }

            return new Persona(nombre, edad, fecha, langs);
        } catch (IOException e) {
            System.out.println("Error leyendo JSON: " + e.getMessage());
            return null;
        }
    }

    // Helper regex extractor: devuelve primer grupo si encuentra, sino ""
    private static String extractJsonString(String text, String regex) {
        Pattern p = Pattern.compile(regex);
        Matcher m = p.matcher(text);
        if (m.find()) {
            return m.group(1);
        }
        return "";
    }

    // ==========================
    // Borrar archivo
    // ==========================
    private static void borrarArchivo(String ruta) {
        try {
            Files.deleteIfExists(Paths.get(ruta));
            System.out.println("Archivo borrado: " + ruta);
        } catch (IOException e) {
            System.out.println("No se pudo borrar " + ruta + ": " + e.getMessage());
        }
    }

    // ==========================
    // Clase Persona (custom)
    // ==========================
    public static class Persona {
        public String nombre;
        public int edad;
        public String fechaNacimiento;
        public List<String> lenguajes;

        public Persona(String nombre, int edad, String fechaNacimiento, List<String> lenguajes) {
            this.nombre = nombre;
            this.edad = edad;
            this.fechaNacimiento = fechaNacimiento;
            this.lenguajes = new ArrayList<>(lenguajes);
        }

        @Override
        public String toString() {
            return "Persona{" +
                    "nombre='" + nombre + '\'' +
                    ", edad=" + edad +
                    ", fechaNacimiento='" + fechaNacimiento + '\'' +
                    ", lenguajes=" + lenguajes +
                    '}';
        }
    }
}
