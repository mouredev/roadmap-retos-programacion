import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Josegs95 {

    private static final String XML_FILENAME = "Josegs95.xml";
    private static final String JSON_FILENAME = "Josegs95.json";

    public static void main(String[] args) {
        String name = "Jose";
        String age = "29";
        String birthdate = "28-02-1995";

        List<String> languageList = new ArrayList<>();
        languageList.add("Java");
        languageList.add("Python");

        Map<String, Object> dataMap = new HashMap<>();
        dataMap.put("name", name);
        dataMap.put("age", age);
        dataMap.put("birthdate", birthdate);
        dataMap.put("language_list", languageList);

        //El reto usa los archivos de los ejercicios XML y JSON, por eso la línea que borra
        //los ficheros está comentada.

        //XML
        exerciseXML(dataMap);

        //JSON
        exerciseJSON(dataMap);

        //Reto
        System.out.println("\n");
        retoFinal();
    }

    private static void exerciseXML(Map<String, Object> dataMap){
        try {
            //Creo el builder
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();

            //Obtengo el documento
            Document document = builder.newDocument();

            //Creo el elemento raiz
            Element root = document.createElement("datos");
            document.appendChild(root);

            //Creo los elementos para insertar los datos y los coloco bajo el elemento raiz

            for (Map.Entry<String, Object> entry : dataMap.entrySet()){
                Element element = document.createElement(entry.getKey());
                Object value = entry.getValue();
                if (value instanceof String)
                    element.appendChild(document.createTextNode((String) value));
                else if (value instanceof List<?>){
                    for (String itemText : ((List<String>) value)){
                        Element itemElement = document.createElement("language");
                        itemElement.appendChild(document.createTextNode(itemText));
                        element.appendChild(itemElement);
                    }
                } else
                    continue;

                root.appendChild(element);
            }

            //Creo el objeto transformer y lo preparo para escribir el documento con el que hemos trabajado
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            //transformer.setOutputProperty(OutputKeys.INDENT, "yes"); //Para ver de forma mas clara el XML
            DOMSource source = new DOMSource(document);

            //Escribo en el archivo con la ruta especificada
            File xmlFile = new File(XML_FILENAME);
            StreamResult result = new StreamResult(xmlFile);
            transformer.transform(source, result);

            //Leer el XML

            //Leemos el archivo de forma normal
            String xmlString = new String(Files.readAllBytes(xmlFile.toPath()));
            System.out.println(xmlString);

            //deleteFile(new File (XML_FILENAME));
        } catch (ParserConfigurationException e) {
            throw new RuntimeException(e);
        } catch (TransformerConfigurationException e) {
            throw new RuntimeException(e);
        } catch (TransformerException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static void exerciseJSON(Map<String, Object> dataMap){
        try {
            File jsonFile = new File (JSON_FILENAME);
            ObjectMapper objectMapper = new ObjectMapper();

            //Escribir en el fichero un mapa en formato JSON
            //objectMapper.writeValue(jsonFile, dataMap);
            objectMapper.writerWithDefaultPrettyPrinter().writeValue(jsonFile, dataMap);

            //Recuperar los datos de un JSON y meterlos en un mapa
            Map<String, Object> newDataMap = new HashMap<>();
            newDataMap = objectMapper.readValue(jsonFile, newDataMap.getClass());
            System.out.println(newDataMap);

            //deleteFile(jsonFile);
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static void retoFinal(){
        //XML
        File xmlFile = new File(XML_FILENAME);
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        try {
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse(xmlFile);

            //document.getDocumentElement().normalize();
            String name = document.getElementsByTagName("name").item(0).getTextContent();
            String age = document.getElementsByTagName("age").item(0).getTextContent();
            String birthdate = document.getElementsByTagName("birthdate").item(0).getTextContent();
            List<String> languageList = new ArrayList<>();

            Node languagesNode = document.getElementsByTagName("language_list").item(0);
            NodeList languagesNodeList = languagesNode.getChildNodes();
            for (int i = 0; i < languagesNodeList.getLength(); i++){
                Node node = languagesNodeList.item(i);
                languageList.add(node.getTextContent());
            }

            Person personFromXML = new Person(name, age, birthdate, languageList);
            System.out.println("Persona XML = " + personFromXML);
        } catch (ParserConfigurationException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (SAXException e) {
            throw new RuntimeException(e);
        }

        //JSON
        File jsonFile = new File (JSON_FILENAME);
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            Map<String, Object> dataMap = new HashMap<>();
            dataMap = objectMapper.readValue(jsonFile, dataMap.getClass());

            String name = (String) dataMap.get("name");
            String age = (String) dataMap.get("age");
            String birthdate = (String) dataMap.get("birthdate");
            List<String> languageList = (List<String>) dataMap.get("language_list");
            Person personFromJSON = new Person(name, age, birthdate, languageList);

            System.out.println("Persona JSOM = " + personFromJSON);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        deleteFile(xmlFile);
        deleteFile(jsonFile);
    }

    private static void deleteFile(File file){
        if (file.delete())
                System.out.println("Se ha borrado el archivo con éxito.");
            else
                System.out.println("No se ha podido borrar el archivo.");
    }

    public static class Person{
        private String name;
        private String age;
        private String birthdate;
        private List<String> languageList;

        public Person(String name, String age, String birthdate, List<String> languageList) {
            this.name = name;
            this.age = age;
            this.birthdate = birthdate;
            this.languageList = languageList;
        }

        public Person(){}

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getAge() {
            return age;
        }

        public void setAge(String age) {
            this.age = age;
        }

        public String getBirthdate() {
            return birthdate;
        }

        public void setBirthdate(String birthdate) {
            this.birthdate = birthdate;
        }

        public List<String> getLanguageList() {
            return languageList;
        }

        public void setLanguageList(List<String> languageList) {
            this.languageList = languageList;
        }

        @Override
        public String toString() {
            return "Nombre: " + name +
                    ", Edad: " + age +
                    ", Fecha de nacimiento: " + birthdate +
                    ", Lista de lenguajes: " + languageList;
        }
    }
}
