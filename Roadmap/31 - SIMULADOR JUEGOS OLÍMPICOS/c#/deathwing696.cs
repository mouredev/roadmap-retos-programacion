using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Xml.Linq;

namespace reto31
{
    public class deathwing696
    {
        public class Participante
        {
            private string nombre;
            private string pais;

            public string Nombre { get { return nombre; } }
            public string Pais { get { return pais; } }

            public Participante(string nombre, string pais)
            {
                this.nombre = nombre;
                this.pais = pais;
            }

            public override bool Equals(object obj)
            {
                if (obj == null || GetType() != obj.GetType()) 
                    return false;

                Participante participante = obj as Participante;
                return this.nombre.Equals(participante.nombre) && this.pais.Equals(participante.pais);
            }

            public override int GetHashCode()
            {
                // Combina los códigos hash de las propiedades para producir un único código hash
                return (Nombre?.GetHashCode() ?? 0) ^ (Pais?.GetHashCode() ?? 0);
            }
        }

        public class Evento
        {
            private string nombre;
            private List<Participante> participantes;
            private List<Participante> medallas;
            public string Nombre { get { return nombre; } }

            public Evento()
            {
                this.participantes = new List<Participante>();
                this.medallas = new List<Participante>();
            }

            public Evento CreateEvent()
            {
                Console.Write("Introduce un nombre para el evento:");
                var name = Console.ReadLine();

                this.nombre = name;

                return this;
            }

            public void AddParticipant(Olimpiadas olimpic)
            {
                Console.Write("Escriba el nombre del participante:");
                var name = Console.ReadLine();
                Console.Write("Escriba el pais del participante:");
                var country = Console.ReadLine();
                Participante participante = new Participante(name, country);

                if (participantes != null && !participantes.Contains(participante))
                {
                    this.participantes.Add(participante);
                    Console.WriteLine("Participante registrado correctamente");
                    olimpic.AddCountry(country);
                }
                else
                {
                    Console.WriteLine($"El participante {participante.Nombre} del pais {participante.Pais} ya está participando en el evento {this.nombre}");
                }
            }

            public void Simulate(Olimpiadas olimpic)
            {
                if (this.participantes != null && this.participantes.Count >= 3 && this.medallas.Count != 3)
                {
                    Random random = new Random();
                    Participante participant;

                    for (int i = 0; i < 3; i++)
                    {
                        do
                        {
                            var pos = random.Next(0, this.participantes.Count);
                            participant = this.participantes[pos];
                        } while (this.medallas.Contains(participant));

                        this.medallas.Add(participant);
                        olimpic.UpdateRanking(participant.Pais);
                    }
                }
                else if (this.medallas.Count != 3)
                {
                    Console.WriteLine($"El evento {this.nombre} no contiene un mínimo de 3 participantes, así que no se simulará");
                }
            }

            public void ShowMedalReport()
            {
                if (this.medallas.Count == 3)
                {
                    Console.WriteLine($"EVENTO:{this.nombre}");
                    Console.WriteLine($"ORO:{this.medallas[0].Nombre} del pais {this.medallas[0].Pais}");
                    Console.WriteLine($"PLATA:{this.medallas[1].Nombre} del pais {this.medallas[1].Pais}");
                    Console.WriteLine($"BRONCE:{this.medallas[2].Nombre} del pais {this.medallas[2].Pais}");
                }
            }            
        }

        public class Olimpiadas
        {
            private static Olimpiadas instance;
            private List<Evento> events;
            private Dictionary<string, int> countryRanking;

            public List<Evento> Events { get { return events; } }
            public Dictionary<string, int> CountryRanking { get { return countryRanking; } }

            private Olimpiadas()
            {
                events = new List<Evento>();
                countryRanking = new Dictionary<string, int>();
            }

            public static Olimpiadas Instance
            {
                get
                {
                    if (instance == null)
                        instance = new Olimpiadas();
                    
                    return instance;
                }
            }

            public void AddCountry(string name)
            {
                var nameNormalized = NormalizeString(name);
                
                if (!this.countryRanking.ContainsKey(nameNormalized.ToString()))
                    this.countryRanking.Add(nameNormalized.ToString(), 0);
            }

            private string NormalizeString(string input)
            {
                if (input == null)
                {
                    return String.Empty;
                }
                else
                {
                    var nameLower = input.ToLower().Trim();
                    return Char.ToUpper(nameLower[0]) + nameLower.Substring(1);
                }
            }

            public  Evento ShowEvents()
            {
                int i = 1;

                foreach (Evento evento in this.Events)
                    Console.WriteLine($"{i}.{evento.Nombre}");

                Console.Write("Seleccione un evento:");
                var option = Int16.Parse(Console.ReadLine()) - 1;

                if (option >= 0 && option <= this.Events.Count - 1)
                    return this.Events[option];
                else
                    return null;
            }

            public void UpdateRanking(string country)
            {
                var countryNormalized = NormalizeString(country);

                if (countryRanking.ContainsKey(countryNormalized))
                    this.countryRanking[countryNormalized]++;
            }

            public void showMedals()
            {
                Console.WriteLine("Medallero por eventos");
                foreach (Evento evento in this.Events)
                    evento.ShowMedalReport();
            }

            public void showCountryRanking()
            {
                var countryRankingOrdered = countryRanking.OrderByDescending(c => c.Value);

                Console.WriteLine("Ranking de paises");

                var i = 1;

                foreach (var country in countryRankingOrdered)
                {
                    Console.WriteLine($"{i++}. {country.Key}: {country.Value} medallas");
                }
            }
        }
        static void Main(string[] args)
        {
            Olimpiadas olimpic = Olimpiadas.Instance;            

            while (true)
            {
                Console.WriteLine("1.Registro de eventos.");
                Console.WriteLine("2.Registro de participantes.");
                Console.WriteLine("3.Simulación de eventos.");
                Console.WriteLine("4.Creación de informes.");
                Console.WriteLine("5.Salir del programa.");
                Console.Write("Introduzca una opción:");
                var option = Int16.Parse(Console.ReadLine());

                switch (option)
                {
                    case 1:
                        Evento evento = new Evento();
                        evento.CreateEvent();
                        olimpic.Events.Add(evento);
                        Console.WriteLine("Evento registrado correctamente");
                        break;
                    case 2:
                        if (olimpic.Events.Count > 0)
                        { 
                            Evento selectedEvent = olimpic.ShowEvents();

                            if (selectedEvent != null)
                                selectedEvent.AddParticipant(olimpic);
                            else
                                Console.WriteLine("El evento seleccionado no es correcto");
                        }
                        else
                        {
                            Console.WriteLine("No hay eventos registrados todavía, por favor, primero registre un evento");
                        }
                        break;
                    case 3:
                        foreach (Evento e in olimpic.Events)
                        {
                            e.Simulate(olimpic);
                        }
                        break;
                    case 4:
                        olimpic.showMedals();
                        olimpic.showCountryRanking();
                        break;
                    case 5:
                        Console.WriteLine("Simulación terminada");
                        Console.ReadKey();
                        return;
                }
            }
        }                
    }
}
