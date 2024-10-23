using System.Text.Json;
using System.Xml;
using System.Xml.Linq;

class Program
{
    static void Main(string[] args)
    {
        // JSON y XML

        //XML
        /*
         * Se puede crear un xml a partir usando la clase XElement
         */
        XElement xmlDoc = new XElement("XMLDoc",
            new XElement("Nombre", "Emilio Quezada"),
            new XElement("Edad", 27),
            new XElement("FechaNacimiento", new DateTime(1997, 07, 28).ToShortDateString()),
            new XElement("Lenguajes",
                new XElement("Lenguaje", "C#"),
                new XElement("Lenguaje", "Typescript"),
                new XElement("Lenguaje", "VB")));
        Console.WriteLine("---XML generado---");
        Console.WriteLine(xmlDoc);
        string ruta = "doc.xml";
        /*
         * La clase XElemento cuenta con el método Save()
        */
        xmlDoc.Save(ruta);

        // JSON
        /*
         * Se puede generar un JSON con la clase JsonSerializer
         * y el método Serialize()
         */
        var doc = new Persona
        {
            Nombre = "Emilio Quezada",
            Edad = 27,
            FechaNacimiento = new DateTime(1997, 07, 28).ToShortDateString(),
            Lenguajes = new List<string> { "C#", "TypeScript", "VB" }
        };
        ruta = "doc.json";

        string jsonDoc = JsonSerializer.Serialize(doc);
        Console.WriteLine("---JSON generado---");
        Console.WriteLine(jsonDoc);
        File.WriteAllText(ruta, jsonDoc);

        // Ejercicio Extra
        /*
         * La clase XElement cuenta con el método Load()
         * para leer un archivo xml y guardarlo como un XElement
         */
        ruta = "doc.xml";
        var personaXML = new Persona();
        xmlDoc = XElement.Load(ruta);
        /*
         * Para acceder a los nodos utilizamos el método Element()
         * y la propiedad Value
         */
        personaXML.Nombre = xmlDoc.Element("Nombre")?.Value;
        personaXML.Edad = int.Parse(xmlDoc.Element("Edad").Value);
        personaXML.FechaNacimiento = xmlDoc.Element("FechaNacimiento").Value;
        personaXML.Lenguajes = new List<string>();
        var lenguajes = xmlDoc.Elements("Lenguaje");
        /*
         * Podemos recorrer una lista de elementos dentro de un nodo utilizando
         * el método Elements() lo cual nos devuelve una colección IEnumerable
         * que puede ser iterada en un bucle foreach
         */
        foreach (var lenguaje in xmlDoc.Element("Lenguajes").Elements("Lenguaje"))
            personaXML.Lenguajes.Add(lenguaje.Value);
        Console.WriteLine("---Persona leída desde XML---");
        Console.WriteLine(personaXML.ToString());
        /*
         * Si el archivo existe lo eliminamos
         */
        if (File.Exists(ruta))
            File.Delete(ruta);

        ruta = "doc.json";
        /*
         * Utilizamos la clase StreamReader para poder
         * abrir un documento json
         */
        StreamReader jsonReader = File.OpenText(ruta);
        /*
         * Usamos el método ReadToEnd() para leer el archivo
         * y guardar el resultado en una variable string
         */
        var json = jsonReader.ReadToEnd();
        /*
         * La clase JsonSerializer cuenta también con el método
         * Deserializae<>() en el cual podemos indicar detro de
         * los símbolos <> la clase a la que queremos que transforme
         * los datos
         */
        var personaJSON = JsonSerializer.Deserialize<Persona>(json);
        Console.WriteLine("---Persona leída desde JSON---");
        Console.WriteLine(personaJSON.ToString());
        /*
         * Por último cerramos el StreamReader para poder
         * eliminar el archivo
         */
        jsonReader.Close();
        if (File.Exists(ruta))
            File.Delete(ruta);
    }

    
}
class Persona
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
    public string FechaNacimiento { get; set; }
    public List<string> Lenguajes { get; set; }

    /*
     * Sobreescribimos el método ToString()
     * para poder darle el formato que queremos
     */

    public override string ToString()
    {
        return $"Nombre: {Nombre}, Edad: {Edad}, Fecha Nacimiento: {FechaNacimiento}," +
            $" Lenguajes: {string.Join(", ", Lenguajes)}";
        /*
         * string.Join(", ", Lenguajes) => Utilizamos el método Join para
         * convertir nuestra lista de strings en un solo string
         */
    }
}