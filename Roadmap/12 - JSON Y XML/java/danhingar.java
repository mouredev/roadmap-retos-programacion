
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class danhingar {

    public static void main(String[] args) throws Exception {
        createJSON();
        createXML();
        readJson("danhingar.json");
        readXML("danhingar.xml");

        Files.delete(Path.of("danhingar.json"));
        Files.delete(Path.of("danhingar.xml"));
        loadDataFromJson();
        loadDataFromXML();
    }

    private static void readJson(String path) {
        try {
            Path path2 = Path.of(path);
            Files.readAllLines(path2).stream().forEach(line -> System.out.println(line));
        } catch (Exception e) {
            System.out.println("Error al leer el fichero JSON");
        }
    }

    private static void readXML(String filename) throws Exception {
        DocumentBuilder builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
        Document doc = builder.parse(new File(filename));
        DOMSource dom = new DOMSource(doc);

        Transformer transformer = TransformerFactory.newInstance().newTransformer();
        transformer.transform(dom, new StreamResult(System.out));
        System.out.println("");
    }

    private static void createXML() {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder;
            Document doc = null;
            builder = factory.newDocumentBuilder();
            doc = builder.newDocument();
            Element root = doc.createElement("user");
            doc.appendChild(root);

            Element name = doc.createElement("name");
            name.appendChild(doc.createTextNode("Daniel"));
            root.appendChild(name);

            Element age = doc.createElement("age");
            age.appendChild(doc.createTextNode("27"));
            root.appendChild(age);

            Element birthDate = doc.createElement("birthDate");
            birthDate.appendChild(doc.createTextNode("29-04-1997"));
            root.appendChild(birthDate);

            Element lenguages = doc.createElement("programmingLanguages");
            for (String language : List.of("Java", "Dart", "Swift")) {
                Element languageItem = doc.createElement("language");
                languageItem.setTextContent(language);
                lenguages.appendChild(languageItem);
            }

            root.appendChild(lenguages);

            DOMSource dom = new DOMSource(doc);
            Transformer transformer = TransformerFactory.newInstance()
                    .newTransformer();

            StreamResult result = new StreamResult(new File("danhingar.xml"));
            transformer.transform(dom, result);
        } catch (Exception e) {
            System.out.println("Error al crear el fichero XML");
        }
    }

    private static void createJSON() {
        String jsonContent = "{\n" +
                "    \"name\": \"Daniel\",\n" +
                "    \"age\": 27,\n" +
                "    \"birthDate\": \"29-04-1997\",\n" +
                "    \"programmingLanguages\": [\"Java\", \"Dart\", \"Swift\"]\n" +
                "}";

        try {
            Path path = Path.of("danhingar.json");
            Files.writeString(path, jsonContent);
        } catch (IOException e) {
            System.out.println("Error al crear el archivo JSON: " + e.getMessage());
        }
    }

    // Extra
    private static void loadDataFromJson() {
        createJSON();
        try {
            Path path2 = Path.of("danhingar.json");
            List<String> lines = Files.readAllLines(path2);
            Map<String, Object> properties = new HashMap<>();
            for (int i = 1; i < lines.size() - 1; i++) {
                String[] keyValue = lines.get(i).split(":");
                String key = keyValue[0].trim().replaceAll("\"", "");
                String value = keyValue[1].trim().replaceAll("\"", "");
                properties.put(key, value);
            }

            String name = properties.get("name").toString().replaceAll(",", "");
            Integer age = Integer.parseInt(properties.get("age").toString().replaceAll(",", ""));
            Date birthDate = toDate(properties.get("birthDate").toString().replaceAll(",", ""));
            String[] languages = properties.get("programmingLanguages").toString().split(",");
            List<String> languagesList = List.of(languages);

            Data data = new Data(name, age, birthDate, languagesList);

            System.out.println(data.toString());
        } catch (Exception e) {
            System.out.println("Error al crear la clase Data desde el fichero JSON");
        }
    }

    private static void loadDataFromXML() {
        createXML();
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            StringBuilder contenido = new StringBuilder();

            try (BufferedReader br = new BufferedReader(new FileReader("danhingar.xml"))) {
                String linea;

                while ((linea = br.readLine()) != null) {
                    contenido.append(linea).append("\n");
                }
            }
            InputStream is = new ByteArrayInputStream(contenido.toString().getBytes("UTF-8"));
            Document document = builder.parse(is);

            Element root = document.getDocumentElement();

            String name = root.getElementsByTagName("name").item(0).getTextContent();
            Integer age = Integer.parseInt(root.getElementsByTagName("age").item(0).getTextContent());
            Date birthDate = toDate(root.getElementsByTagName("birthDate").item(0).getTextContent());
            NodeList languages = root.getElementsByTagName("language");
            List<String> languagesList = new ArrayList<>();
            for (int i = 0; i < languages.getLength(); i++) {
                languagesList.add(languages.item(i).getTextContent());
            }

            Data data = new Data(name, age, birthDate, languagesList);

            System.out.println(data.toString());

        } catch (Exception e) {
            System.out.println("Error al crear la clase Data desde el fichero XML");
        }

    }

    public static class Data {
        private String name;
        private Integer age;
        private Date birthDate;
        private List<String> programmingLanguages;

        public Data(String name, Integer age, Date birthDate, List<String> programmingLanguages) {
            this.name = name;
            this.age = age;
            this.birthDate = birthDate;
            this.programmingLanguages = programmingLanguages;
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

        public Date getBirthDate() {
            return birthDate;
        }

        public void setBirthDate(Date birthDate) {
            this.birthDate = birthDate;
        }

        public List<String> getProgrammingLanguages() {
            return programmingLanguages;
        }

        public void setProgrammingLanguages(List<String> programmingLanguages) {
            this.programmingLanguages = programmingLanguages;
        }

        @Override
        public String toString() {
            return "Data [name=" + name + ", age=" + age + ", birthDate=" + birthDate + ", programmingLanguages="
                    + programmingLanguages + "]";
        }
    }

    private static Date toDate(String dateString) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");

        try {
            Date date = dateFormat.parse(dateString);
            return date;
        } catch (ParseException e) {
            System.err.println("Invalid date format: " + e.getMessage());
            return null;
        }
    }
}
