import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class simonguzman {

    public static void main(String[] args) {
        createXMLFile();
        readXMLFile();
        deleteXMLFile();
        createPropertiesFile();
        readPropertiesFile();
        deletePropertiesFile();

        //Ejercicio adicional
        createXMLFileExtra();
        createPropertiesFileExtra();

        Persona personaDesdeXML = readXMLFileExtra();
        Persona personaDesdeProperties = readPropertiesFileExtra();

        System.out.println("Datos: leidos desde XML");
        personaDesdeXML.mostrarInformacion();
        System.out.println("\nDatos leídos desde JSON simulado (properties):");
        personaDesdeProperties.mostrarInformacion();

        deleteXMLFileExtra();
        deletePropertiesFileExtra();
    }

    static void createXMLFile(){
        try {
            DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
            
            //Raiz
            Document doc = docBuilder.newDocument();
            Element rootElement = doc.createElement("Persona");
            doc.appendChild(rootElement);

            //Nombre
            Element name = doc.createElement("Nombre");
            name.appendChild(doc.createTextNode("Simon"));
            rootElement.appendChild(name);

            //Edad
            Element age = doc.createElement("Edad");
            age.appendChild(doc.createTextNode("22"));
            rootElement.appendChild(age);

            //Fecha de nacimiento
            Element dateBirth = doc.createElement("Fecha_de_nacimiento");
            dateBirth.appendChild(doc.createTextNode("2001-11-28"));
            rootElement.appendChild(dateBirth);

            //Listado de lenguajes
            Element languajes = doc.createElement("Lenguajes");
            Element languaje1 = doc.createElement("Lenguaje");
            languaje1.appendChild(doc.createTextNode("Java"));
            languajes.appendChild(languaje1);
            Element languaje2 = doc.createElement("Lenguaje");
            languaje2.appendChild(doc.createTextNode("Python"));
            languajes.appendChild(languaje2);
            rootElement.appendChild(languajes);

            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
            DOMSource source = new DOMSource(doc);
            StreamResult result = new  StreamResult(new File("datos.xml"));
            transformer.transform(source, result);

        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }

    static void readXMLFile(){
        try {
            File inputFile = new File("datos.xml");
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(inputFile);
            doc.getDocumentElement().normalize();

            //Leer nombre
            NodeList nList = doc.getElementsByTagName("Persona");
            Node nNode = nList.item(0);
            Element eElement = (Element) nNode;

            System.out.println("Nombre: " + eElement.getElementsByTagName("Nombre").item(0).getTextContent());
            System.out.println("Edad: " + eElement.getElementsByTagName("Edad").item(0).getTextContent());
            System.out.println("Fecha de nacimiento: " + eElement.getElementsByTagName("Fecha_de_nacimiento").item(0).getTextContent());

            NodeList languajes = eElement.getElementsByTagName("Lenguaje");
            for (int temp = 0; temp < languajes.getLength(); temp++) {
                System.out.println("Lenguaje: "+languajes.item(temp).getTextContent());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void deleteXMLFile(){
        File file = new File("datos.xml");
        if(file.delete()){
            System.out.println("Archivo XML borrado correctamente.");
        }else{
            System.out.println("ERROR: No se pudo borrar el archivo XML.");
        }
    }

    static void createPropertiesFile(){
        Properties properties = new Properties();

        properties.setProperty("nombre", "Simon");
        properties.setProperty("edad", "22");
        properties.setProperty("fecha_de_nacimiento", "2001-11-28");

        properties.setProperty("lenguajes", "Java,Python");

        try (FileOutputStream output = new FileOutputStream("datos.properties")){
            properties.store(output, "Datos del usuario en formato JSON simulado");
            System.out.println("Archivo 'datos.properties' creado");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static void readPropertiesFile(){
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("datos.properties")){
            properties.load(input);

            System.out.println("Nombre: " + properties.getProperty("nombre"));
            System.out.println("Edad: " + properties.getProperty("edad"));
            System.out.println("Fecha de nacimiento: " + properties.getProperty("fecha_de_nacimiento"));

            String[] lenguajes = properties.getProperty("lenguajes").split(",");
            System.out.println("Lenguajes:");
            for (String lenguaje : lenguajes) {
                System.out.println("- " + lenguaje);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static void deletePropertiesFile(){
        File file = new File("datos.properties");
        if(file.delete()){
            System.out.println("Archivo JSON simulado fue eliminado.");
        }else{
            System.out.println("ERROR: No se pudo eliminar el archivo.");
        }

    }

    static class Persona{
        private String nombre;
        private int edad;
        private String fechaDeNacimiento;
        private List<String> lenguajes;

        // Constructor
        public Persona(String nombre, int edad, String fechaDeNacimiento, List<String> lenguajes) {
            this.nombre = nombre;
            this.edad = edad;
            this.fechaDeNacimiento = fechaDeNacimiento;
            this.lenguajes = lenguajes;
        }

        // Getters
        public String getNombre() {
            return nombre;
        }

        public int getEdad() {
            return edad;
        }

        public String getFechaDeNacimiento() {
            return fechaDeNacimiento;
        }

        public List<String> getLenguajes() {
            return lenguajes;
        }

        // Método para mostrar los datos
        public void mostrarInformacion() {
            System.out.println("Nombre: " + nombre);
            System.out.println("Edad: " + edad);
            System.out.println("Fecha de nacimiento: " + fechaDeNacimiento);
            System.out.println("Lenguajes: ");
            for (String lenguaje : lenguajes) {
                System.out.println("- " + lenguaje);
            }
        }
    }

    static void createXMLFileExtra(){
        try {
            DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
            
            //Raiz
            Document doc = docBuilder.newDocument();
            Element rootElement = doc.createElement("Persona");
            doc.appendChild(rootElement);

            //Nombre
            Element name = doc.createElement("Nombre");
            name.appendChild(doc.createTextNode("Simon"));
            rootElement.appendChild(name);

            //Edad
            Element age = doc.createElement("Edad");
            age.appendChild(doc.createTextNode("22"));
            rootElement.appendChild(age);

            //Fecha de nacimiento
            Element dateBirth = doc.createElement("Fecha_de_nacimiento");
            dateBirth.appendChild(doc.createTextNode("2001-11-28"));
            rootElement.appendChild(dateBirth);

            //Listado de lenguajes
            Element languajes = doc.createElement("Lenguajes");
            Element languaje1 = doc.createElement("Lenguaje");
            languaje1.appendChild(doc.createTextNode("Java"));
            languajes.appendChild(languaje1);
            Element languaje2 = doc.createElement("Lenguaje");
            languaje2.appendChild(doc.createTextNode("Python"));
            languajes.appendChild(languaje2);
            rootElement.appendChild(languajes);

            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
            DOMSource source = new DOMSource(doc);
            StreamResult result = new  StreamResult(new File("datos.xml"));
            transformer.transform(source, result);

        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }

    static Persona readXMLFileExtra(){
        try {
            File inputFile = new File("datos.xml");
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(inputFile);
            doc.getDocumentElement().normalize();

            //Leer nombre
            NodeList nList = doc.getElementsByTagName("Persona");
            Node nNode = nList.item(0);
            Element eElement = (Element) nNode;

            String nombre = eElement.getElementsByTagName("Nombre").item(0).getTextContent();
            int edad = Integer.parseInt(eElement.getElementsByTagName("Edad").item(0).getTextContent());
            String fechaDeNacimiento = eElement.getElementsByTagName("Fecha_de_nacimiento").item(0).getTextContent();

            NodeList lenguajesNodeList = eElement.getElementsByTagName("Lenguaje");
            List<String> lenguajes = new ArrayList<>();
            for (int temp = 0; temp < lenguajesNodeList.getLength(); temp++) {
                lenguajes.add(lenguajesNodeList.item(temp).getTextContent());
            }

            return new Persona(nombre, edad, fechaDeNacimiento, lenguajes);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    static void deleteXMLFileExtra(){
        File file = new File("datos.xml");
        if(file.delete()){
            System.out.println("Archivo XML borrado correctamente.");
        }else{
            System.out.println("ERROR: No se pudo borrar el archivo XML.");
        }
    }

    static void createPropertiesFileExtra(){
        Properties properties = new Properties();

        properties.setProperty("nombre", "Simon");
        properties.setProperty("edad", "22");
        properties.setProperty("fecha_de_nacimiento", "2001-11-28");

        properties.setProperty("lenguajes", "Java,Python");

        try (FileOutputStream output = new FileOutputStream("datos.properties")){
            properties.store(output, "Datos del usuario en formato JSON simulado");
            System.out.println("Archivo 'datos.properties' creado");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static Persona readPropertiesFileExtra(){
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("datos.properties")){
            properties.load(input);

            String nombre = properties.getProperty("nombre");
            int edad = Integer.parseInt(properties.getProperty("edad"));
            String fechaDeNacimiento = properties.getProperty("fecha_de_nacimiento");

            String[] lenguajesArray = properties.getProperty("lenguajes").split(",");
            List<String> lenguajes = new ArrayList<>();
            for (String lenguaje : lenguajesArray) {
                lenguajes.add(lenguaje);
            }

            return new Persona(nombre, edad, fechaDeNacimiento, lenguajes);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    static void deletePropertiesFileExtra(){
        File file = new File("datos.properties");
        if(file.delete()){
            System.out.println("Archivo JSON simulado fue eliminado.");
        }else{
            System.out.println("ERROR: No se pudo eliminar el archivo.");
        }
    }
}
