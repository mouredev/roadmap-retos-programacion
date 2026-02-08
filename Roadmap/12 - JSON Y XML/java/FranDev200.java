import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import com.google.gson.*;
import org.w3c.dom.*;
import org.xml.sax.SAXException;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class FranDev200 {

    // PARA EL APARTADO DE JSON, USO EL .jar DE GSON

    static int contador = 0;

    static void main(String[] args) {

        /*
         * EJERCICIO:
         * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
         * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
         * - Nombre
         * - Edad
         * - Fecha de nacimiento
         * - Listado de lenguajes de programación
         * Muestra el contenido de los archivos.
         * Borra los archivos.

         */

        if (crearXML()) return;

        if (leerXML()) return;

        File fileJson = crearJson();
        if (fileJson == null) return;

        leerJson(fileJson);

        /*

         * DIFICULTAD EXTRA (opcional):
         * Utilizando la lógica de creación de los archivos anteriores, crea un
         * programa capaz de leer y transformar en una misma clase custom de tu
         * lenguaje los datos almacenados en el XML y el JSON.
         * Borra los archivos.

         */

        System.out.println("\n\n===============");
        System.out.println("EJERCICIO EXTRA");
        System.out.println("===============\n");

        crearXML();

        ArrayList<Alumno> listaAlumnos = new ArrayList<>();

        leerXML(listaAlumnos);

        System.out.println("INFORMACION DE LOS ALUMNOS DEL INSTITUTO");
        System.out.println("[Información obtenida a partir de un XML]");
        System.out.println("========================================");
        System.out.println("Numero de alumnos: " +  listaAlumnos.size());
        System.out.println("- - - - - - - - - - - -");
        for(Alumno a : listaAlumnos){
            a.infoAlumno();
        }

        listaAlumnos.clear();

        fileJson = crearJson();
        if (fileJson == null) return;

        leerJson(fileJson, listaAlumnos);

        System.out.println("INFORMACION DE LOS ALUMNOS DEL INSTITUTO");
        System.out.println("[Información obtenida a partir de un Json]");
        System.out.println("========================================");
        System.out.println("Numero de alumnos: " +  listaAlumnos.size());
        System.out.println("- - - - - - - - - - - -");
        for(Alumno a : listaAlumnos){
            a.infoAlumno();
        }

    }

    static class Alumno{
        private int id;
        private String nombre;
        private int edad;
        private String fechaNacimiento;
        private ArrayList<String> lenguajes = new ArrayList<>();

        Alumno(){
            contador++;
            this.id = contador;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public int getEdad() {
            return edad;
        }

        public void setEdad(int edad) {
            this.edad = edad;
        }

        public String getFechaNacimiento() {
            return fechaNacimiento;
        }

        public void setFechaNacimiento(String fechaNacimiento) {
            this.fechaNacimiento = fechaNacimiento;
        }

        public ArrayList<String> getLenguajes() {
            return lenguajes;
        }

        public void setLenguajes(ArrayList<String> lenguajes) {
            this.lenguajes = lenguajes;
        }

        public void infoAlumno() {

            System.out.println("============");
            System.out.println(" - Alumno " + id);
            System.out.println("------------");
            System.out.println("   Nombre: " + getNombre());
            System.out.println("   Edad: " + getEdad());
            System.out.println("   FechaNacimiento: " + getFechaNacimiento());
            System.out.println("   Lenguajes favoritos:");
            for (String l: getLenguajes()){
                System.out.println("\t - " + l);
            }

        }
    }

    // EJERCICIO EXTRA
    private static boolean leerXML(ArrayList<Alumno> alumnosArrayList) {
        // LEER EL DOCUMENTO XML

        Alumno a = null;

        File file = new  File("Alumnos.xml");

        try {

            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(file);

            doc.getDocumentElement().normalize();

            NodeList alumnos = doc.getElementsByTagName("Alumno");

            for(int i = 0; i < alumnos.getLength(); i++){

                a = new Alumno();

                Element alumno = (Element) alumnos.item(i);

                String nombre = alumno.getElementsByTagName("Nombre").item(0).getTextContent();
                int idAlumno = Integer.parseInt(alumno.getAttribute("ID"));
                int edad  = Integer.parseInt(alumno.getElementsByTagName("Edad").item(0).getTextContent());
                String fecha = alumno.getElementsByTagName("FechaNacimiento").item(0).getTextContent();
                ArrayList<String> leng = new ArrayList<>();

                NodeList lenguajes = alumno.getElementsByTagName("Lenguaje");

                for(int j = 0; j < lenguajes.getLength(); j++){
                    Element l = (Element) lenguajes.item(j);

                    String lenguaje = l.getTextContent();
                    leng.add(lenguaje);

                }

                a.setNombre(nombre);
                a.setEdad(edad);
                a.setFechaNacimiento(fecha);
                a.setLenguajes(leng);

                alumnosArrayList.add(a);

            }

            file.delete();

        }catch (ParserConfigurationException e){
            e.printStackTrace();
            return true;
        }catch (IOException e){
            e.printStackTrace();
            return true;
        }catch (SAXException e){
            e.printStackTrace();
            return true;
        }
        return false;
    }

    // EJERCICIO EXTRA
    private static void leerJson(File fileJson, ArrayList<Alumno> alumnosArrayList) {

        Alumno a = null;

        try(FileReader fr = new FileReader(fileJson)){

            JsonObject raiz = JsonParser.parseReader(fr).getAsJsonObject();

            JsonArray alumnosLeer = raiz.getAsJsonArray("Alumnos");

            for(JsonElement alumnoElem: alumnosLeer){

                a  = new Alumno();

                JsonObject alum =  alumnoElem.getAsJsonObject();

                String nombre = alum.get("Nombre").getAsString();
                int edad = alum.get("Edad").getAsInt();
                String fecha = alum.get("FechaNacimiento").getAsString();
                ArrayList<String> leng = new ArrayList<>();

                JsonArray lenguajesLeer = alum.get("Lenguaje").getAsJsonArray();

                for(JsonElement lenguajeElem: lenguajesLeer){

                    leng.add(lenguajeElem.getAsString());
                }

                a.setNombre(nombre);
                a.setEdad(edad);
                a.setFechaNacimiento(fecha);
                a.setLenguajes(leng);

                alumnosArrayList.add(a);

            }

            fileJson.deleteOnExit();

        }catch (IOException e){
            e.printStackTrace();
        }
    }

    private static void leerJson(File fileJson) {
        try(FileReader fr = new FileReader(fileJson)){

            System.out.println("\nINFORMACION DE LOS ALUMNOS");
            System.out.println("=========================");

            JsonObject raiz = JsonParser.parseReader(fr).getAsJsonObject();

            JsonArray alumnosLeer = raiz.getAsJsonArray("Alumnos");

            int contador = 1;

            for(JsonElement alumnoElem: alumnosLeer){

                JsonObject alum =  alumnoElem.getAsJsonObject();

                String nombre = alum.get("Nombre").getAsString();
                int edad = alum.get("Edad").getAsInt();
                String fecha = alum.get("FechaNacimiento").getAsString();

                System.out.println("============");
                System.out.println(" - Alumno " + contador);
                System.out.println("------------");
                System.out.println("   Nombre: " + nombre);
                System.out.println("   Edad: " + edad);
                System.out.println("   FechaNacimiento: " + fecha);
                System.out.println("   Lenguajes favoritos:");

                JsonArray lenguajesLeer = alum.get("Lenguaje").getAsJsonArray();

                for(JsonElement lenguajeElem: lenguajesLeer){

                    System.out.println("\t - " + lenguajeElem.toString());
                }

                contador++;
            }

            fileJson.deleteOnExit();

        }catch (IOException e){
            e.printStackTrace();
        }
    }

    private static File crearJson() {
        // CREAR EL DOCUMENTO JSON

        JsonObject json = new JsonObject();
        JsonArray alumnos = new JsonArray();
        JsonObject alumno = new JsonObject();
        JsonArray lenguajes =  new JsonArray();

        // Alumno 1
        alumno.addProperty("Nombre", "Inmaculada");
        alumno.addProperty("Edad", "18");
        alumno.addProperty("FechaNacimiento", "05-04-2007");

        lenguajes.add("Java");
        lenguajes.add("CSS");
        lenguajes.add("C++");

        alumno.add("Lenguaje", lenguajes);
        alumnos.add(alumno);

        // Alumno 2
        alumno =  new JsonObject(); // Para "reiniciar" el objeto del alumno
        lenguajes =  new JsonArray(); // Para "reiniciar" el array de los lenguajes
        alumno.addProperty("Nombre", "Zaira");
        alumno.addProperty("Edad", "17");
        alumno.addProperty("FechaNacimiento", "07-03-2007");

        lenguajes.add("Go");
        lenguajes.add("Angular");
        lenguajes.add("React");

        alumno.add("Lenguaje", lenguajes);
        alumnos.add(alumno);

        json.add("Alumnos", alumnos);

        Gson gson = new GsonBuilder().setPrettyPrinting().create();

        File fileJson = new  File("Alumnos.json");
        try (FileWriter fw = new FileWriter(fileJson);){

            gson.toJson(json, fw);

        }catch (IOException e){
            e.printStackTrace();
            return null;
        }

        System.out.println("\n\nDocumento JSON creado con exito.");
        return fileJson;
    }

    private static boolean leerXML() {
        // LEER EL DOCUMENTO XML

        File file = new  File("Alumnos.xml");

        try {

            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(file);

            doc.getDocumentElement().normalize();

            NodeList alumnos = doc.getElementsByTagName("Alumno");

            System.out.println("\nINFORMACION DE LOS ALUMNOS");
            System.out.println("==========================");

            for(int i = 0; i < alumnos.getLength(); i++){

                Element alumno = (Element) alumnos.item(i);

                String nombre = alumno.getElementsByTagName("Nombre").item(0).getTextContent();
                int idAlumno = Integer.parseInt(alumno.getAttribute("ID"));
                int edad  = Integer.parseInt(alumno.getElementsByTagName("Edad").item(0).getTextContent());
                String fecha = alumno.getElementsByTagName("FechaNacimiento").item(0).getTextContent();

                System.out.println("============");
                System.out.println(" - Alumno " + idAlumno);
                System.out.println("------------");
                System.out.println("   Nombre: " + nombre);
                System.out.println("   Edad: " + edad);
                System.out.println("   FechaNacimiento: " + fecha);
                System.out.println("   Lenguajes favoritos:");

                NodeList lenguajes = alumno.getElementsByTagName("Lenguaje");

                for(int j = 0; j < lenguajes.getLength(); j++){
                    Element l = (Element) lenguajes.item(j);

                    String lenguaje = l.getTextContent();

                    System.out.println("\t - " + lenguaje);
                }

            }

            file.delete();

        }catch (ParserConfigurationException e){
            e.printStackTrace();
            return true;
        }catch (IOException e){
            e.printStackTrace();
            return true;
        }catch (SAXException e){
            e.printStackTrace();
            return true;
        }
        return false;
    }

    private static boolean crearXML() {
        try{

            // CREAR EL DOCUMENTO XML

            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.newDocument();

            Element raiz = doc.createElement("Alumnos");
            doc.appendChild(raiz);

            // ALUMNO 1
            Element alumno = doc.createElement("Alumno");
            alumno.setAttribute("ID", "1");
            raiz.appendChild(alumno);

            Element nombre = doc.createElement("Nombre");
            nombre.setTextContent("Francisco");
            alumno.appendChild(nombre);

            Element edad = doc.createElement("Edad");
            edad.setTextContent("20");
            alumno.appendChild(edad);

            Element fchNacimiento = doc.createElement("FechaNacimiento");
            fchNacimiento.setTextContent("13-12-2005");
            alumno.appendChild(fchNacimiento);

            Element lenguajes = doc.createElement("Lenguajes");
            alumno.appendChild(lenguajes);

            Element java =  doc.createElement("Lenguaje");
            java.setTextContent("Java");
            lenguajes.appendChild(java);
            Element python = doc.createElement("Lenguaje");
            python.setTextContent("Python");
            lenguajes.appendChild(python);
            Element sql = doc.createElement("Lenguaje");
            sql.setTextContent("SQL");
            lenguajes.appendChild(sql);
            Element html = doc.createElement("Lenguaje");
            html.setTextContent("HTML");
            lenguajes.appendChild(html);

            // ALUMNO 2
            alumno = doc.createElement("Alumno");
            alumno.setAttribute("ID", "2");
            raiz.appendChild(alumno);

            nombre = doc.createElement("Nombre");
            nombre.setTextContent("David");
            alumno.appendChild(nombre);

            edad = doc.createElement("Edad");
            edad.setTextContent("17");
            alumno.appendChild(edad);

            fchNacimiento = doc.createElement("FechaNacimiento");
            fchNacimiento.setTextContent("20-04-2008");
            alumno.appendChild(fchNacimiento);

            lenguajes = doc.createElement("Lenguajes");
            alumno.appendChild(lenguajes);

            Element kotlin =  doc.createElement("Lenguaje");
            kotlin.setTextContent("Kotlin");
            lenguajes.appendChild(kotlin);
            python = doc.createElement("Lenguaje");
            python.setTextContent("Python");
            lenguajes.appendChild(python);
            Element php = doc.createElement("Lenguaje");
            php.setTextContent("PHP");
            lenguajes.appendChild(php);
            Element css = doc.createElement("Lenguaje");
            css.setTextContent("CSS");
            lenguajes.appendChild(css);

            Transformer transformer = TransformerFactory.newInstance().newTransformer();
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
            transformer.transform(
                    new DOMSource(doc),
                    new StreamResult(new File("Alumnos.xml"))
            );

        }catch (ParserConfigurationException e){
            e.printStackTrace();
            return true;
        }catch (TransformerException e){
            e.printStackTrace();
            return true;
        }

        System.out.println("Documento XML creado con exito\n");
        return false;
    }

}
