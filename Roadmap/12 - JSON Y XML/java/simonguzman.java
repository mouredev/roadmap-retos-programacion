import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;
import org.w3c.dom.Document;
import org.w3c.dom.Element;



public class simonguzman {
    public static void main(String[] args) {
        createXMLFile();
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
            Element name = doc.createElement("nombre");
            name.appendChild(doc.createTextNode("Simon"));
            rootElement.appendChild(name);

            //Edad
            Element age = doc.createElement("Edad");
            age.appendChild(doc.createTextNode("22"));
            rootElement.appendChild(age);

            //Fecha de nacimiento
            Element dateBirth = doc.createElement("Fecha de nacimiento");
            dateBirth.appendChild(doc.createTextNode("2001-11-28"));
            rootElement.appendChild(dateBirth);

            //Listado de lenguajes
            Element languajes = doc.createElement("Lenguajes");
            Element languaje1 = doc.createElement("Lenguaje");
            languaje1.appendChild(doc.createElement("Java"));
            languaje1.appendChild(languaje1);
            Element languaje2 = doc.createElement("Lenguaje");
            languaje2.appendChild(doc.createElement("Python"));
            languaje2.appendChild(languaje2);
            languajes.appendChild(languajes);

            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new  StreamResult(new File("datos.xml"));
            transformer.transform(source, result);

        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
}
