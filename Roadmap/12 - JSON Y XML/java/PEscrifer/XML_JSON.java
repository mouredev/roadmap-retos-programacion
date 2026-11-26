import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import org.w3c.dom.Document;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import com.google.gson.Gson;

public class XML_JSON {
    public static void main(String[] args) {
        

        String contenidoXML = """
                <programmer>
                    <name>Pablo</name>
                    <age>35</age>
                    <birthdate>26-06-1991</birthdate>
                    <languages>
                        <language>Java</language>
                        <language>Phyton</language>
                        <language>JavaScript</language>
                    </languages>
                </programmer>
                """;
        
        String contenidoJSON = """
                {
                    "name":"Manuel",
                    "age":33,
                    "birthdate":"19-05-1993",
                    "languages":["Kotlin", "Swift", "Java"]
                }
                """;
        
        Path rutaXML = Paths.get("datosEjercicio.xml");
        Path rutaJSON = Paths.get("datosEjercicio.json");


        try {
            Files.writeString(rutaXML, contenidoXML);
            Files.writeString(rutaJSON, contenidoJSON);
    
            System.out.println("Archivos creados correctamente \n");

            System.out.println("---Leyendo el archivo XML:");
            String leidoXML = Files.readString(rutaXML);
            System.out.println(leidoXML);

            System.out.println("---Leyendo el archivo JSON:");
            String leidoJSON = Files.readString(rutaJSON);
            System.out.println(leidoJSON);

            Files.delete(rutaXML);
            Files.delete(rutaJSON);

            System.out.println("Archivos borrados correctamente.");
        } catch (IOException e) {
            e.printStackTrace();
        }

        /*
         -Dificultad extra
        */

        Gson robotGson = new Gson();

        Programmerr programadoJSON = robotGson.fromJson(contenidoJSON, Programmerr.class);

        System.out.println("--- Resultado de GSON ---");
        System.out.println("Nombre: " + programadoJSON.getName());
        System.out.println("Edad: " + programadoJSON.getAge());
        System.out.println("Fecha de nacimiento: " + programadoJSON.getBirthdate());
        System.out.println("Lenguajes de programación: " + programadoJSON.getLanguages());

        System.out.println("--- Resultado de XML ---");

        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder detective = factory.newDocumentBuilder();

            ByteArrayInputStream entradaXML = new ByteArrayInputStream(contenidoXML.getBytes("UTF-8"));
            Document documento = detective.parse(entradaXML);

            String nombreXML = documento.getElementsByTagName("name").item(0).getTextContent();
            String textoEdad = documento.getElementsByTagName("age").item(0).getTextContent();
            int edadXML = Integer.parseInt(textoEdad);

            System.out.println("Nombre desde XML: " + nombreXML);
            System.out.println("Edad desde XML: " + edadXML);
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class Programmerr{

    private String name;
    private int age;
    private String birthdate;
    private List<String> languages;

    public Programmerr(){

    }

	public String getName() {
		return name;
	}

	public int getAge() {
		return age;
	}

	public String getBirthdate() {
		return birthdate;
	}

	public List<String> getLanguages() {
		return languages;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public void setBirthdate(String birthdate) {
		this.birthdate = birthdate;
	}

	public void setLanguages(List<String> languages) {
		this.languages = languages;
	}

	@Override
	public String toString() {
		return "Programmerr [name=" + name + ", age=" + age + ", birthdate=" + birthdate + ", languages=" + languages
				+ "]";
	}

}


