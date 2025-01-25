import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.stream.XMLOutputFactory;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamWriter;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

public class JimsimroDev {
  // Nombres de los archivos XML y JSON
  private final static String XML_FILENAME = "backendDeveloper.xml";
  private final static String JSON_FILENAME = "backendDeveloper.json";

  // Record para almacenar datos
  public static record MyTuple(
      String name,
      int age,
      LocalDate birthDate,
      List<String> programmingLanguages) {
  }

  // Clase para manejar los datos
  public static class Data {
    private String name;
    private int age;
    private LocalDate birthDate;
    List<String> programmingLanguages;

    public Data(String name, int age, LocalDate birthDate, List<String> programmingLanguages) {
      this.name = name;
      this.age = age;
      this.birthDate = birthDate;
      this.programmingLanguages = programmingLanguages;
    }

    public String getName() {
      return this.name;
    }

    public void setName(String name) {
      this.name = name;
    }

    public int getAge() {
      return this.age;
    }

    public void setAge(int age) {
      this.age = age;
    }

    public LocalDate getBirthDate() {
      return this.birthDate;
    }

    public void setBirthDate(LocalDate birthDate) {
      this.birthDate = birthDate;
    }

    public List<String> getProgrammingLanguages() {
      return this.programmingLanguages;
    }

    public void setProgrammingLanguages(List<String> programmingLanguages) {
      this.programmingLanguages = programmingLanguages;
    }
  }

  // Método para crear un archivo XML
  private static void createXML(MyTuple data, String xmlFilename) throws IOException, XMLStreamException {
    XMLOutputFactory outputFactory = XMLOutputFactory.newInstance();
    XMLStreamWriter writer = outputFactory.createXMLStreamWriter(new FileWriter(xmlFilename));

    writer.writeStartDocument("UTF-8", "1.0");
    writer.writeStartElement("data");

    writer.writeStartElement("name");
    writer.writeCharacters(data.name());
    writer.writeEndElement();

    writer.writeStartElement("age");
    writer.writeCharacters(String.valueOf(data.age()));
    writer.writeEndElement();

    writer.writeStartElement("birthDate");
    writer.writeCharacters(data.birthDate().toString());
    writer.writeEndElement();

    writer.writeStartElement("programmingLanguages");
    Iterator<String> it = data.programmingLanguages().iterator();
    while (it.hasNext()) {
      String item = it.next();
      writer.writeStartElement("item");
      writer.writeCharacters(item);
      writer.writeEndElement();
    }

    writer.writeEndElement();

    writer.writeEndElement();
    writer.writeEndDocument();

    writer.flush();
    writer.close();
    System.out.println("XML file created successfully.");
    getFile(xmlFilename);
    // deleteFile(xmlFilename);
  }

  // Método para crear un archivo JSON
  private static void createJson(MyTuple data) throws IOException {
    File jsonFile = new File(JSON_FILENAME);

    StringBuilder json = new StringBuilder();
    json.append("{\n");
    json.append(" \"name\": \"" + data.name() + "\",\n");
    json.append(" \"age\": " + data.age() + ",\n");
    json.append(" \"birthDate\": \"" + data.birthDate() + "\",\n");

    json.append(" \"programmingLanguages\": [\n");
    for (int i = 0; i < data.programmingLanguages.size(); i++) {
      json.append("     \"" + data.programmingLanguages.get(i) + "\"");
      if (i < data.programmingLanguages.size() - 1) {
        json.append(",");
      }
      json.append("\n");
    }
    json.append("  ]");
    json.append("\n}");

    System.out.println("JSON file created successfully.");

    // Escribir el archivo JSON
    try (BufferedWriter br = new BufferedWriter(new FileWriter(jsonFile))) {
      br.write(json.toString());
    }
    getFile(JSON_FILENAME);
    // deleteFile(JSON_FILENAME);
  }

  // Método para leer un archivo y mostrar su contenido
  private static void getFile(String fileName) throws IOException, FileNotFoundException {
    FileReader file = new FileReader(fileName);
    try (BufferedReader bf = new BufferedReader(file)) {
      String line = "";
      while ((line = bf.readLine()) != null) {
        System.out.println(line);
      }
    }
  }

  // Método para parsear un JSON a un objeto Data
  private static Data parseJsonToData(String jsonString) {
    try {
      String name = jsonString.split("\"name\"\\s*:\\s*\"")[1].split("\"")[0];
      int age = Integer.parseInt(jsonString.split("\"age\"\\s*:\\s*")[1].split(",")[0]);
      String birthDate = jsonString.split("\"birthDate\"\\s*:\\s*\"")[1].split("\"")[0];
      String languagesString = jsonString.split("\"programmingLanguages\"\\s*:\\s*\\[")[1].split("\\]")[0];
      List<String> programmingLanguages = new ArrayList<>();
      for (String lang : languagesString.split(",")) {
        programmingLanguages.add(lang.replace("\"", "").trim());
      }
      return new Data(name, age, LocalDate.parse(birthDate), programmingLanguages);
    } catch (ArrayIndexOutOfBoundsException e) {
      System.err.println("Error parsing JSON: " + e.getMessage());
      e.printStackTrace();
      return null;
    }
  }

  // Método para eliminar un archivo
  private static void deleteFile(String file) {
    Path path = Paths.get(file);
    try {
      Files.delete(path);
    } catch (IOException e) {
      System.out.println(e.getClass().getName() + " generated: " + e.getMessage());
      e.printStackTrace();
    }
  }

  // Método principal
  public static void main(String[] args) throws Exception, IOException, XMLStreamException {
    // Datos de ejemplo
    String name = "Jimmis Jhaon";
    int age = 29;
    LocalDate birthDate = LocalDate.of(1995, 07, 28);
    String[] languages = { "Java", "Kotlin", "Elixir", "Lua" };
    List<String> programmingLanguages = Arrays.asList(languages);

    MyTuple data = new MyTuple(name, age, birthDate, programmingLanguages);

    // Crear archivos XML y JSON
    createXML(data, XML_FILENAME);
    createJson(data);

    // Leer y parsear el archivo JSON
    FileReader file = new FileReader(JSON_FILENAME);
    try (BufferedReader bf = new BufferedReader(file)) {
      StringBuilder jsonBuilder = new StringBuilder();
      String line = "";
      while ((line = bf.readLine()) != null) {
        jsonBuilder.append(line);
      }
      String jsonString = jsonBuilder.toString();
      Data jsonData = parseJsonToData(jsonString);
      System.out.println("Name: " + jsonData.getName());
      System.out.println("Age: " + jsonData.getAge());
      System.out.println("BirthDate: " + jsonData.getBirthDate());
      System.out.println("Languages: " + jsonData.getProgrammingLanguages());
    }

    // Leer y parsear el archivo XML
    DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    DocumentBuilder builder = factory.newDocumentBuilder();
    Document document = builder.parse(new File(XML_FILENAME));

    NodeList nodeList = document.getDocumentElement().getChildNodes();
    String name1 = nodeList.item(0).getTextContent(); // Obtener el nombre del nodo
    int age1 = Integer.parseInt(nodeList.item(1).getTextContent()); // Obtener la edad del nodo
    LocalDate birthDate1 = LocalDate.parse(nodeList.item(2).getTextContent()); // Obtener la fecha de nacimiento del
                                                                               // nodo

    NodeList languages1 = nodeList.item(3).getChildNodes(); // Obtener los lenguajes de programación del nodo
    List<String> languagesList = new ArrayList<>(); // Convertir a lista
    for (int i = 0; i < languages1.getLength(); i++) {
      languagesList.add(languages1.item(i).getTextContent());
    }

    Data xmlData = new Data(name1, age1, birthDate1, languagesList);

    System.out.println("Name: " + xmlData.getName());
    System.out.println("Age: " + xmlData.getAge());
    System.out.println("BirthDate: " + xmlData.getBirthDate());
    System.out.println("Languages: " + String.join(", ", xmlData.getProgrammingLanguages()));

    // Eliminar archivos creados
    deleteFile(XML_FILENAME);
    deleteFile(JSON_FILENAME);
  }
}
