/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  C#                            ║
╚═══════════════════════════════════════╝
-----------------------------------------------
* JSON Y XML
-----------------------------------------------
- son formatos de intercambio de datos que estructuran información.
- JSON (JavaScript Object Notation) y XML (eXtensible Markup Language)
*/
using System.IO;
using System.Text.Json;
using System.Xml;
using System.Xml.Linq;
#pragma warning disable CA1050
public class Program {
    static void Main() {

        var userDic = new Dictionary<string, object> {
            {"name", "Ken"},
            {"age", 121},
            {"dob", "1903-03-19"},
            {"prog_langs", new List<string> { "cs", "py", "vb", "rs", "js" }}
        };
        // _______________________________________________
        // * JSON
        // serializar
        var options = new JsonSerializerOptions {
            WriteIndented = true
        };

        string json = JsonSerializer.Serialize(userDic, options);
        File.WriteAllText("user.json", json);

        // Deserializar
        string readJson = File.ReadAllText("user.json");
        var DesUserJson = JsonSerializer.Deserialize<Dictionary<string, object>>(readJson);
        Console.WriteLine(DesUserJson["name"]);

        // _______________________________________________
        // * XML
        // serializar
        userDic["prog_langs"] = "cs,py,vb,rs,js";
        using (XmlTextWriter writer = new XmlTextWriter("user.xml", null)) {
            writer.Formatting = Formatting.Indented;
            writer.WriteStartDocument();
            writer.WriteStartElement("user");

            foreach (var pair in userDic) {
                writer.WriteStartElement(pair.Key);
                writer.WriteValue(pair.Value);
                writer.WriteEndElement();
            }

            writer.WriteEndElement();
            writer.WriteEndDocument();
        }
        
        // Deserializar
        XDocument doc = XDocument.Load("user.xml");
        XElement userElement = doc.Root;
        string name = userElement.Element("name").Value;                                
        Console.WriteLine(name);
        
        /* _______________________________________________
         * EJERCICIO
         * Utilizando la lógica de creación de los archivos anteriores, crea un
         * programa capaz de leer y transformar en una misma clase custom de tu 
         * lenguaje los datos almacenados en el XML y el JSON.
         * Borra los archivos.
        */  
        var theFile = new XmlOrJson("user.json");
        var dicUser = theFile.AsDictionary();
        Console.WriteLine("\nDocumento JSON");
        foreach (var kv in dicUser) {
            if (kv.Key != "prog_langs") {
                Console.WriteLine($"{kv.Key}: {kv.Value}");
            }
        }
        var progLangs = (List<string>)dicUser["prog_langs"];
        Console.WriteLine(string.Join(", ", progLangs));

        //_________
        var theFile2 = new XmlOrJson("user.xml");
        var dicUser2 = theFile2.AsDictionary();
        Console.WriteLine("\nDocumento XML");
        foreach (var kv in dicUser2) {
            if (kv.Key != "prog_langs") {
                Console.WriteLine($"{kv.Key}: {kv.Value}");
            }
        }
        var progLangs2 = (List<string>)dicUser2["prog_langs"];
        Console.WriteLine(string.Join(", ", progLangs2));

        //_________
        Console.WriteLine("\nAcceder a sus propiedades");
        Console.WriteLine(theFile2.name);
        Console.WriteLine(theFile2.age);
        Console.WriteLine(theFile2.dob);
        File.Delete("user.json");
        File.Delete("user.xml");
    }

    public class XmlOrJson {
        private string path;
        private string extension;
        private Dictionary<string, object> dicUser;
        public string name;
        public int age;
        public string dob;
        public List<string> langs;
        
        public XmlOrJson(string path) {
            this.path = path;
            this.extension = Path.GetExtension(path).ToLower();
            this.dicUser = new Dictionary<string, object>();
            this.name = string.Empty;
            this.age = 0;
            this.dob = string.Empty;
            this.langs = new List<string>();
        }

        private void addToDic() {
            dicUser["name"] = name;
            dicUser["age"] = age;
            dicUser["dob"] = dob;
            dicUser["prog_langs"] = langs;
        }
        public Dictionary<string, object> AsDictionary() {
            try {
                if (extension == ".json") {
                    string readJson = File.ReadAllText(path);
                    using (var document = JsonDocument.Parse(readJson)) {
                        var root = document.RootElement;
                        name = root.GetProperty("name").GetString();
                        age = root.GetProperty("age").GetInt32();
                        dob = root.GetProperty("dob").GetString();
                        foreach (JsonElement lang in root.GetProperty("prog_langs").EnumerateArray()) {
                            langs.Add(lang.GetString());
                        }
                        addToDic();
                        return dicUser;
                    }                    

                } else if (extension == ".xml") {
                    var doc = XDocument.Load("user.xml");
                    var userElement = doc.Root;
                    name = userElement.Element("name").Value;
                    age = int.Parse(userElement.Element("age").Value);
                    dob = userElement.Element("dob").Value;
                    langs = userElement.Element("prog_langs").Value.Split(',').ToList();
                    
                    addToDic();
                    return dicUser;
                } else {
                    Console.WriteLine("Archivo no compatible.");
                    return null;
                }
            }
            catch (Exception ex) {
                Console.WriteLine($"Exception: {ex.GetType()}");
                return null;
            }
        }
    }    
}

