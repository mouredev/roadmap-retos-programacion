public class Main {
    public static void main(String[] args) {
        //Datos a introducir en los documentos
        String name = "Abel";
        int age = 20;
        Date birthday = new GregorianCalendar(1994, Calendar.JUNE,16).getTime();
        String [] lenguages = new String[] {"Java", "PHP", "JavaScript"};

        //Para formatear la fecha
        DateFormat formatter = new SimpleDateFormat("dd-MM-yyyy");

        /*XML*/
        // Creamos una factoría para crear el documento
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder;
        Document doc;
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
            transformer.transform(source,result);

            System.out.println("XML creado satisfactoriamente");

        } catch (ParserConfigurationException | TransformerException e) {
            System.out.println("Error: "+e.getMessage());
        }

        /*JSON*/
        JsonObject json = new JsonObject();

        json.put("name",name);
        json.put("age",String.valueOf(age));
        json.put("birthday",formatter.format(birthday));

        JsonArray langs = new JsonArray();
        for (String language : lenguages) {
            langs.add(language);
        }
        json.put("languages",langs);

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
            System.out.println("Error: "+e.getMessage());
        }
    }
}
