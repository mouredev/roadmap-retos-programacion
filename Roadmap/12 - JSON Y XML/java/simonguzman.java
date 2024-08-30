import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;
import org.w3c.dom.Document;
import org.w3c.dom.Element;



public class simonguzman {
    public static void main(String[] args) {
        createXMLFile();
        readXMLFile();
        deleteXMLFile();
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
}
