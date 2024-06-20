import com.github.cliftonlabs.json_simple.JsonArray;
import com.github.cliftonlabs.json_simple.JsonException;
import com.github.cliftonlabs.json_simple.JsonObject;
import com.github.cliftonlabs.json_simple.Jsoner;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.*;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

/*
    <dependencies>
        <dependency>
            <groupId>com.github.cliftonlabs</groupId>
            <artifactId>json-simple</artifactId>
            <version>3.1.0</version>
        </dependency>
    </dependencies>
*/

public class Main {
    public static void main(String[] args) {
        //Datos a introducir en los documentos
        String name = "Abel";
        int age = 20;
        Date birthday = new GregorianCalendar(1994, Calendar.JUNE, 16).getTime();
        String[] lenguages = new String[]{"Java", "PHP", "JavaScript"};

        //Para formatear la fecha
        DateFormat formatter = new SimpleDateFormat("dd-MM-yyyy");

        /*XML*/
        // Creamos una factoría para crear el documento
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder;
        Document doc = null;
        try {
            builder = factory.newDocumentBuilder();
            doc = builder.newDocument();
            //Creamos el elemento root y lo añadimos al documento xml
            Element rootElement = doc.createElement("programador");
            doc.appendChild(rootElement);

            //Añadimos en nombre
            Element nameElement = doc.createElement("name");
            nameElement.setTextContent(name);
            rootElement.appendChild(nameElement);

            //Añadimos la edad
            Element ageElement = doc.createElement("age");
            ageElement.setTextContent(Integer.toString(age));
            rootElement.appendChild(ageElement);

            //Añadimos la fecha de cumpleaños
            Element birthdayElement = doc.createElement("birthday");
            birthdayElement.setTextContent(formatter.format(birthday));
            rootElement.appendChild(birthdayElement);

            //Añadimos un elemento que englobará los lenguajes
            Element languagesElement = doc.createElement("languages");
            for (String language : lenguages) {
                Element languageElement = doc.createElement("language");
                languageElement.setTextContent(language);
                languagesElement.appendChild(languageElement);
            }
            rootElement.appendChild(languagesElement);

            //Asocio el source con el Document
            Source source = new DOMSource(doc);

            //Creo el Result, indicando que fichero se va a crear
            Result result = new StreamResult(new File("abel.xml"));

            //Creo un transformer, se crea el fichero XML
            Transformer transformer = TransformerFactory.newInstance().newTransformer();
            transformer.transform(source, result);

            System.out.println("XML creado satisfactoriamente");

        } catch (ParserConfigurationException | TransformerException e) {
            System.out.println("Error: " + e.getMessage());
        }

        /*JSON*/
        JsonObject json = new JsonObject();

        json.put("name", name);
        json.put("age", String.valueOf(age));
        json.put("birthday", formatter.format(birthday));

        JsonArray langs = new JsonArray();
        for (String language : lenguages) {
            langs.add(language);
        }
        json.put("languages", langs);

        File jsonFile = new File("abel.json");
        try {
            if (!jsonFile.exists()) {
                jsonFile.createNewFile();
            }

            FileWriter fileWriter = new FileWriter(jsonFile);
            fileWriter.write(json.toJson());
            fileWriter.close();

            System.out.println("JSON creado satisfactoriamente");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }

        /*DIFICULTAD EXTRA -- CREAR CLASES A PARTIR DE DOCUMENTOS*/

        /*Crear clase a partir de XML*/
        String nameXML = null;
        int ageXML = 0;
        Date birthdayXML = null;
        String[] lenguagesXML = null;

        //Recupero datos del archivo
        if (doc != null) {
            NodeList programador = doc.getDocumentElement().getChildNodes();
            for (int i = 0; i < programador.getLength(); i++) {
                Element element = (Element) programador.item(i);
                switch (element.getTagName()) {
                    case "name":
                        nameXML = element.getTextContent();
                        break;
                    case "age":
                        ageXML = Integer.parseInt(element.getTextContent());
                        break;
                    case "birthday":
                        try {
                            birthdayXML = formatter.parse(element.getTextContent());
                        } catch (ParseException e) {
                            System.out.println("Error: " + e.getMessage());
                        }
                        break;
                    case "languages":
                        NodeList languages = element.getChildNodes();
                        lenguagesXML = new String[languages.getLength()];
                        for (int j = 0; j < languages.getLength(); j++) {
                            Element language = (Element) languages.item(j);
                            lenguagesXML[j] = language.getTextContent();
                        }
                        break;
                }
            }
        }

        //Creo el objeto programador
        Programmer programmer = new Programmer(nameXML, ageXML, birthdayXML, lenguagesXML);

        //Muestro sus datos por consola
        System.out.println(programmer);
        System.out.println("Lenguajes de programación: ");
        for (String language : lenguagesXML) {
            System.out.println(language);
        }

        //Elimino el documento
        File xmlFile = new File("abel.xml");
        xmlFile.delete();

        /*Crear clase a partir de JSON*/
        String nameJSON = null;
        int ageJSON = 0;
        Date birthdayJSON = null;
        String[] lenguagesJSON = null;

        try {
            //Recupero datos del archivo
            FileReader fileReader = new FileReader("abel.json");
            HashMap<String, Object> map = (HashMap<String, Object>) Jsoner.deserialize(fileReader);
            nameJSON = (String) map.get("name");
            ageJSON = Integer.parseInt((String) map.get("age"));
            birthdayJSON = formatter.parse((String) map.get("birthday"));
            String array = map.get("languages").toString();
            array = array.replace('[', ' ').replace(']', ' ').trim();
            lenguagesJSON = array.split(", ");

            //Creo el objeto programador
            Programmer programmer1 = new Programmer(nameJSON, ageJSON, birthdayJSON, lenguagesJSON);

            //Muestro sus datos por consola
            System.out.println(programmer1);
            System.out.println("Lenguajes de programación: ");
            for (String language : lenguagesJSON) {
                System.out.println(language);
            }

            //Elimino el documento
            jsonFile.delete();

        } catch (FileNotFoundException | ParseException | JsonException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

class Programmer {
    String name;
    int age;
    Date birthday;
    String[] lenguages;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public String[] getLenguages() {
        return lenguages;
    }

    public void setLenguages(String[] lenguages) {
        this.lenguages = lenguages;
    }

    public Programmer(String name, int age, Date birthday, String[] lenguages) {
        this.name = name;
        this.age = age;
        this.birthday = birthday;
        this.lenguages = lenguages;
    }

    @Override
    public String toString() {
        return "Soy " + name + ", con edad: " + age + ".";
    }
}
