using System;
using System.Collections.Generic;
using System.IO;
using System.Xml.Linq;
using Newtonsoft.Json;

namespace ArchivosXmlJson
{
    class Program
    {
        public class Persona
        {
            public string Nombre { get; set; }
            public int Edad { get; set; }
            public DateTime FechaNacimiento { get; set; }
            public List<string> LenguajesProgramacion { get; set; }
        }

        static void Main(string[] args)
        {
            // Datos a guardar
            Persona persona = new Persona
            {
                Nombre = "Andrea",
                Edad = 30,
                FechaNacimiento = new DateTime(1994, 5, 13),
                LenguajesProgramacion = new List<string> {"C#", "JavaScript", "Python" }
            };

            //Archivos
            string xmlFileName = "persona.xml";
            string jsonFileName = "persona.json";

            try
            {
                // Crear y guardar XML
                XElement personaXml = new XElement("Persona",
                    new XElement("Nombre", persona.Nombre),
                    new XElement("Edad", persona.Edad),
                    new XElement("FechaNacimiento", persona.FechaNacimiento.ToString("dd-MM-yyy")),
                    new XElement("LenguajeProgramacion",
                        new XElement("Lenguaje", persona.LenguajesProgramacion[0]),
                        new XElement("Lenguaje", persona.LenguajesProgramacion[1]),
                        new XElement("Lenguaje", persona.LenguajesProgramacion[2])
                    )
                );

                personaXml.Save(xmlFileName);

                //Crear y guardar JSON
                string personaJson = JsonConvert.SerializeObject(persona, Formatting.Indented);
                File.WriteAllText(jsonFileName, perosnaJson);

                //Mostrar contenido de los archivos 
                Console.WriteLine("Contenido del archivo XML:");
                Console.WriteLine(File.ReadAllText(jsonFileName));

                Console.WriteLine("\nContenido del archivo JSON:");
                Console.WriteLine(File.ReadAllText(jsonFileName));

                //Dificultad extra: Leer y transformar en clase personalizada
                Persona personaDesdeXml = LeerDesdeXml(xmlFileName);
                Persona personaDesdeJson = LeerDesdeJson(jsonFileName);

                //Mostrar datos de la clase personalizada
                Console.WriteLine("\nDatos leídos desde XML:");
                MostrarDatos(personaDesdeXml);

                Console.WriteLine("\nDatos leídos desde JSON:");
                MostrarDatos(personaDesdeJson);
            }
            finally
            {
                // Borrar archivos
                if (File.Exists(xmlFileName))
                {
                    File.Delete(xmlFileName);
                }

                if (File.Exists(jsonFileName));
                {
                    File.Delete(jsonFileName);
                }

                Console.WriteLine("\Archivos eliminados.");
            }
        }

        static Persona LeerDesdeXml(string fileName)
        {
            XElement personaXml = XElement.Load(fileName);
            Persona persona = new Persona
            {
                Nombre = personaXml.Element("Nombre")?.Value,
                Edad = int.Parse(personaXml.Element("Edad")?.Value),
                FechaNacimiento = DateTime.Parse(personaXml.Element("FechaNacimiento")?.Value),
                LenguajesProgramacion = new List<string>()
            };

            foreach(XElement lenguaje in personaXml.Element("LenguajesProgramacion").Element("Lenguaje"))
            {
                persona.LenguajesProgramacion.Add(lenguaje.Value);
            }

            return persona;
        }

        static Persona LeerDesdeJson(string fileName)
        {
            string personaJson = File.ReadAllText(fileName);
            return JsonCovert.DeserializeObject<Persona>(personaJson);
        }
        
        static void MostrarDatos(Persona persona)
        {
            Console.WriteLine($"Nombre: {persona.Nombre}");
            Console.WriteLine($"Edad: {persona.Edad}");
            Console.WriteLine($"Fecha de nacimiento: {persona.FechaNacimiento:dd-MM-yyyy}");
            Console.WriteLine($"Lenguajes de programacion: "+ string.Join(",", persona.LenguajesProgramacion));
        }
    }

  /*



- Explicación
Clase Persona:
Representa la estructura de los datos que queremos almacenar, con propiedades para nombre, edad, fecha de nacimiento y un listado de lenguajes de programación.

-Main:
Creación de XML:
Se crea un objeto XElement que representa la estructura XML de Persona y se guarda en el archivo persona.xml.

Creación de JSON:
Se convierte el objeto persona a JSON usando JsonConvert.SerializeObject y se guarda en persona.json.

Mostrar contenido de los archivos:
Se leen y muestran los contenidos de los archivos XML y JSON creados.

Leer desde XML y JSON:
Se implementan métodos para leer desde XML (LeerDesdeXml) y JSON (LeerDesdeJson) y transformar los datos en instancias de la clase Persona.

Mostrar datos de la clase personalizada:
Se imprimen los datos de las instancias de Persona obtenidas desde XML y JSON.

Borrar archivos:
Se eliminan los archivos XML y JSON al final.

-Métodos Auxiliares:

LeerDesdeXml: Carga y deserializa los datos desde un archivo XML en un objeto Persona.
LeerDesdeJson: Carga y deserializa los datos desde un archivo JSON en un objeto Persona.
MostrarDatos: Muestra los datos de una instancia de Persona.

*/
}
