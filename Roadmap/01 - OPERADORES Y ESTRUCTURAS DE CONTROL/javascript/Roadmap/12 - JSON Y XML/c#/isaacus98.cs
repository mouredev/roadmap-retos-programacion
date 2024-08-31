/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */


using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Xml;

namespace Roadmap
{
    internal class Reto11
    {
        static void Main(string[] args)
        {
            // JSON
            WriteJson();
            ReadJson();

            // XML
            Console.WriteLine();
            WriteXML();
            ReadXML();

            // Reto extra
            XMLToClass();
            JsonToClass();

            File.Delete(@"C:\Users\" + Environment.UserName + @"\Desktop\programmer.xml");
            File.Delete(@"C:\Users\" + Environment.UserName + @"\Desktop\programmer.json");
        }

        private static void ReadXML()
        {
            List<string> languages = new List<string>();
            using (XmlReader reader = XmlReader.Create(@"C:\Users\" + Environment.UserName + @"\Desktop\programmer.xml"))
            {
                while (reader.Read())
                {
                    if (reader.Name.ToString() == "Name")
                        Console.WriteLine($"Name: {reader.ReadString()}");

                    if (reader.Name.ToString() == "Age")
                        Console.WriteLine($"Age: {reader.ReadString()}");

                    if (reader.Name.ToString() == "Birthdate")
                        Console.WriteLine($"Birthdate: {reader.ReadString()}");

                    if (reader.Name.ToString() == "Language")
                        languages.Add(reader.ReadString());
                }

                Console.WriteLine($"Languages: {string.Join(", ", languages)}");
            }
        }

        private static void WriteXML()
        {
            using (XmlWriter writer = XmlWriter.Create(@"C:\Users\" + Environment.UserName + @"\Desktop\programmer.xml"))
            {
                writer.WriteStartElement("Programmer");
                writer.WriteElementString("Name", "Isaac");
                writer.WriteElementString("Age", "26");
                writer.WriteElementString("Birthdate", "1998-02-13");
                writer.WriteStartElement("ProgrammingLanguages");
                writer.WriteElementString("Language", "C#");
                writer.WriteElementString("Language", "Kotlin");
                writer.WriteEndElement();
                writer.WriteEndElement();
                writer.Flush();
            }
        }

        private static void ReadJson()
        {
            JObject o1 = JObject.Parse(File.ReadAllText(@"C:\Users\" + Environment.UserName + @"\Desktop\programmer.json"));
            Console.WriteLine($"Name: {o1.Value<string>("Name")}");
            Console.WriteLine($"Age: {o1.Value<int>("Age")}");
            Console.WriteLine($"Birthdate: {o1.Value<string>("Birthdate")}");
            Console.WriteLine($"Language: {o1.Value<JArray>("Language")}");
        }

        private static void WriteJson()
        {
            JObject programmer = new JObject(new JProperty("Name", "Isaac"), new JProperty("Age", 26), new JProperty("Birthdate", "1998-02-13"), new JProperty("Language", "C#", "Kotlin"));
            File.WriteAllText(@"C:\Users\" + Environment.UserName + @"\Desktop\programmer.json", programmer.ToString());
        }

        // Reto extra

        private static void XMLToClass()
        {
            Console.WriteLine();
            Console.WriteLine("XML deserialized to objet Programmer");

            string name = "";
            int age = 0;
            string birthdate = "";
            List<string> languages = new List<string>();

            using (XmlReader reader = XmlReader.Create(@"C:\Users\" + Environment.UserName + @"\Desktop\programmer.xml"))
            {
                while (reader.Read())
                {
                    if (reader.Name.ToString() == "Name")
                        name = reader.ReadString();

                    if (reader.Name.ToString() == "Age")
                        age = int.Parse(reader.ReadString());

                    if (reader.Name.ToString() == "Birthdate")
                        birthdate = reader.ReadString();

                    if (reader.Name.ToString() == "Language")
                        languages.Add(reader.ReadString());
                }
            }

            Programmer programmer = new(name, age, birthdate, languages.ToArray());
            Console.WriteLine(programmer.ToString());
        }

        private static void JsonToClass()
        {
            Console.WriteLine();
            Console.WriteLine("Json deserialized to objet Programmer");

            // Deserialize JSON to object
            Programmer programmer = JsonConvert.DeserializeObject<Programmer>(File.ReadAllText(@"C:\Users\" + Environment.UserName + @"\Desktop\programmer.json"));
            Console.WriteLine(programmer.ToString());
        }
    }

    public class Programmer
    {
        public string Name;
        public int Age;
        public string Birthdate;
        public string[] Language;

        public Programmer(string name, int age, string birthdate, string[] languages)
        {
            Name = name;
            Age = age;
            Birthdate = birthdate;
            Language = languages;
        }

        public override string ToString()
        {
            return $"Name: {Name}" + Environment.NewLine + $"Age: {Age}" + Environment.NewLine + $"Date: {Birthdate}" + Environment.NewLine + $"Languages: {string.Join(", ", Language)}";
        }
    }
}
