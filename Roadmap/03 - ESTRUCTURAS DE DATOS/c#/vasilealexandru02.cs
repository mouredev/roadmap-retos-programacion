public class vasilealexandru02
{
    static string regexTelefono = @"^\d{9}$";

    static List<Contacto> listaDeContactos = new List<Contacto>();

    static string rutaArchivoTxt = "";
    static void Main(string[] args)
    {
        rutaArchivoTxt = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Desktop), "contactos.txt");
        // Colas 
        // Es una colecci�n de tipo FIFO (First In First Out)

        Queue queue = new Queue();
        // Operaci�n inserci�n
        queue.Enqueue(1);
        queue.Enqueue(2);
        queue.Enqueue(3);

        Console.WriteLine("Imprimiendo elementos de la cola: ");
        foreach (var i in queue)
        {
            Console.WriteLine("Elemento " + i + " en la cola");
        }
        Console.WriteLine("");

        // Operaci�n de eliminaci�n o sacar de la cola
        queue.Dequeue();
        queue.Dequeue();

        Console.WriteLine("Cola despu�s de quitar elementos de la cola: ");
        foreach (var i in queue)
        {
            Console.WriteLine("Elemento " + i + " en la cola");
        }
        Console.WriteLine("");
        Console.WriteLine("M�todo para ver el siguiente elemento a sacar de la cola " + "Elemento " + queue.Peek());

        queue.Enqueue(1);
        queue.Enqueue(2);
        queue.Enqueue(3);
        Console.WriteLine("Valores de la cola antes de vaciarla: ");
        foreach (var i in queue)
        {
            Console.WriteLine("Elemento " + i + " en la cola");
        }

        Console.WriteLine("");
        queue.Clear();
        Console.WriteLine("Valores de la cola despu�s de vaciarla: ");
        foreach (var i in queue)
        {
            Console.WriteLine("Elemento " + i + " en la cola");
        }
        Console.WriteLine("");

        // Stack
        // Representa una colecci�n de tipo LIFO (Last In First Out)

        Stack stack = new Stack();

        // Operaci�n de inserci�n
        stack.Push("Primer elemento");
        stack.Push("Segundo elemento");
        stack.Push("Tercer elemento");
        stack.Push("Cuarto elemento");

        Console.WriteLine("Valores del stack: ");
        foreach (var i in stack)
        {
            Console.WriteLine("Elemento " + i + " en la cola");
        }
        Console.WriteLine("");

        // Operaci�n de eliminaci�n
        stack.Pop();
        stack.Pop();

        Console.WriteLine("Valores del stack despu�s sacar elementos: ");
        foreach (var i in stack)
        {
            Console.WriteLine("Elemento " + i + " en la cola");
        }
        Console.WriteLine("");


        // Arrays 

        var arrayAlimentos = new Alimento[10];

        // Operaci�n de inserci�n
        arrayAlimentos[0] = new Alimento { nombre = "Espinaca", precio = .8, calorias = 23 };
        arrayAlimentos[1] = new Alimento { nombre = "Salm�n", precio = 10, calorias = 208 };
        arrayAlimentos[2] = new Alimento { nombre = "Tofu", precio = 2, calorias = 144 };
        arrayAlimentos[3] = new Alimento { nombre = "Ar�ndanos", precio = 3, calorias = 57 };
        arrayAlimentos[4] = new Alimento { nombre = "Avena", precio = .5, calorias = 389 };
        arrayAlimentos[5] = new Alimento { nombre = "Almendras", precio = 5, calorias = 576 };
        arrayAlimentos[6] = new Alimento { nombre = "Quinoa", precio = 1.5, calorias = 120 };
        arrayAlimentos[7] = new Alimento { nombre = "Lentejas", precio = .9, calorias = 116 };
        arrayAlimentos[8] = new Alimento { nombre = "Aguacate", precio = 1, calorias = 160 };
        arrayAlimentos[9] = new Alimento { nombre = "Batata", precio = .75, calorias = 86 };

        Console.WriteLine("Imprimiendo elementos de la array: ");
        foreach (var alimento in arrayAlimentos)
        {
            Console.WriteLine($"Nombre: {alimento.nombre} | Calor�as: {alimento.calorias} | Precio: {alimento.precio}");
        }
        Console.WriteLine("");

        // Operaci�n de borrado 

        arrayAlimentos = arrayAlimentos.Where(a => a.nombre.StartsWith("A")).ToArray();

        Console.WriteLine("Imprimiendo elementos de la array despu�s del borrado: ");
        foreach (var alimento in arrayAlimentos)
        {
            Console.WriteLine($"Nombre: {alimento.nombre} | Calor�as: {alimento.calorias} | Precio: {alimento.precio}");
        }
        Console.WriteLine("");

        // Operaci�n de actualizaci�n 

        var alimentos = arrayAlimentos.ToList();

        foreach (var alimento in alimentos)
        {
            if (alimento.calorias > 150)
            {
                alimento.precio += 2;
            }

        }

        arrayAlimentos = alimentos.ToArray();

        Console.WriteLine("Imprimiendo elementos de la array despu�s de la actualizaci�n del precio: ");
        foreach (var alimento in arrayAlimentos)
        {
            Console.WriteLine($"Nombre: {alimento.nombre} | Calor�as: {alimento.calorias} | Precio: {alimento.precio}");
        }
        Console.WriteLine("");

        // Operaci�n de ordenaci�n

        arrayAlimentos = arrayAlimentos.OrderBy(a => a.calorias).ToArray();

        Console.WriteLine("Imprimiendo elementos de la array despu�s de la ordenaci�n por kcal: ");

        foreach (var alimento in arrayAlimentos)
        {
            Console.WriteLine($"Nombre: {alimento.nombre} | Calor�as: {alimento.calorias} | Precio: {alimento.precio}");
        }
        Console.WriteLine("");


        // Listas 

        var listaAlimentos = new List<Alimento>()
{
     new Alimento { nombre = "Manzana", precio = 0.5, calorias = 95 },
            new Alimento { nombre = "Pan", precio = 1, calorias = 265 },
            new Alimento { nombre = "Leche", precio = 0.9, calorias = 42 },
            new Alimento { nombre = "Queso", precio = 2.5, calorias = 405 },
            new Alimento { nombre = "Yogur", precio = 0.8, calorias = 59 },
            new Alimento { nombre = "Pollo", precio = 5, calorias = 215 },
            new Alimento { nombre = "Arroz", precio = .7, calorias = 130 },
            new Alimento { nombre = "Pasta", precio = 1.2, calorias = 131 }

};

        //Operaci�n de inserci�n 

        listaAlimentos.Add(
                    new Alimento { nombre = "Pepino", precio = 0.25, calorias = 16 });
        listaAlimentos.Add(new Alimento { nombre = "Tomate", precio = 0.30, calorias = 18 });


        Console.WriteLine("Imprimiendo elementos de la lista: ");
        listaAlimentos.ForEach(a => Console.WriteLine($"Nombre: {a.nombre} | Calor�as: {a.calorias}"));
        Console.WriteLine("");

        // Operaci�n de borrado

        listaAlimentos.RemoveAt(7);
        listaAlimentos.RemoveAt(8);

        Console.WriteLine("Imprimiendo elementos de la lista despu�s del borrado: ");
        listaAlimentos.ForEach(a => Console.WriteLine($"Nombre: {a.nombre} | Calor�as: {a.calorias}"));
        Console.WriteLine("");

        // Operaci�n de actualizaci�n

        foreach (var alimento in listaAlimentos)
        {
            if (alimento.precio < 1)
            {
                alimento.nombre = "Alimento asequible";
            }
        }


        Console.WriteLine("Imprimiendo elementos de la lista despu�s de la actualizaci�n del nombre: ");
        listaAlimentos.ForEach(a => Console.WriteLine($"Nombre: {a.nombre} | Calor�as: {a.calorias}"));
        Console.WriteLine("");


        // Operaci�n de ordenaci�n 
        listaAlimentos = listaAlimentos.OrderByDescending(a => a.calorias).ToList();

        Console.WriteLine("Imprimiendo elementos de la lista despu�s de ordenarlos por sus calor�as: ");
        listaAlimentos.ForEach(a => Console.WriteLine($"Nombre: {a.nombre} | Calor�as: {a.calorias}"));
        Console.WriteLine("");

        var alimentosQueComienzanPorP = listaAlimentos.Where(x => x.nombre.StartsWith("P"));


        // Hashshets 


        // Operaci�n de inserci�n

        HashSet<Alimento> hashSetAlimentos = new HashSet<Alimento>()
{
    new Alimento { nombre = "Aguacate", precio = 1.00, calorias = 160},
            new Alimento { nombre = "Tofu", precio = 0.50, calorias = 76},
            new Alimento { nombre = "Lentejas", precio = 0.35, calorias = 116},
            new Alimento { nombre = "Quinoa", precio = 1.10, calorias = 120},
            new Alimento { nombre = "Espinacas", precio = 0.40, calorias = 23},
            new Alimento { nombre = "Nueces", precio = 2.00, calorias = 654},
            new Alimento { nombre = "Ar�ndanos", precio = 1.50, calorias = 57}
};

        hashSetAlimentos.Add(new Alimento { nombre = "Garbanzos", precio = 0.33, calorias = 164 });
        hashSetAlimentos.Add(new Alimento { nombre = "Tempeh", precio = 1.75, calorias = 193 });
        hashSetAlimentos.Add(new Alimento { nombre = "Kale", precio = 0.90, calorias = 49 });

        Console.WriteLine("Imprimiendo elementos del hashset: ");

        foreach (var alimento in hashSetAlimentos)
        {
            Console.WriteLine($"Nombre: {alimento.nombre} | Calor�as: {alimento.calorias}");
        }
        Console.WriteLine("");

        // Operaci�n de eliminaci�n
        hashSetAlimentos.RemoveWhere(alimento => alimento.nombre.Equals("Tofu") || alimento.nombre.Equals("Nueces"));

        Console.WriteLine("Imprimiendo elementos del hashset despu�s de la eliminaci�n: ");

        foreach (var alimento in hashSetAlimentos)
        {
            Console.WriteLine($"Nombre: {alimento.nombre} | Calor�as: {alimento.calorias}");
        }
        Console.WriteLine("");


        // Operaci�n de actualizaci�n
        foreach (var alimento in hashSetAlimentos)
        {
            alimento.nombre += " modificado.";
        }


        Console.WriteLine("Imprimiendo elementos del hashset despu�s de la actualizaci�n del nombre: ");

        foreach (var alimento in hashSetAlimentos)
        {
            Console.WriteLine($"Nombre: {alimento.nombre} | Calor�as: {alimento.calorias}");
        }
        Console.WriteLine("");

        // Operaci�n de ordenaci�n


        hashSetAlimentos = hashSetAlimentos.OrderBy(alimento => alimento.calorias).ToHashSet();


        Console.WriteLine("Imprimiendo elementos del hashset despu�s de ordenarlos por sus calor�as: ");

        foreach (var alimento in hashSetAlimentos)
        {
            Console.WriteLine($"Nombre: {alimento.nombre} | Calor�as: {alimento.calorias}");
        }
        Console.WriteLine("");

        // Diccionarios


        // Operaci�n de inserci�n

        Dictionary<string, Alimento> diccionarioAlimentos = new Dictionary<string, Alimento>();
        diccionarioAlimentos.Add("0001", new Alimento { nombre = "Papaya", precio = 1.20, calorias = 59 });
        diccionarioAlimentos.Add("0002", new Alimento { nombre = "Mango", precio = 0.80, calorias = 60 });
        diccionarioAlimentos.Add("0003", new Alimento { nombre = "Espinaca", precio = 0.50, calorias = 23 });
        diccionarioAlimentos.Add("0004", new Alimento { nombre = "Almendra", precio = 2.50, calorias = 575 });
        diccionarioAlimentos.Add("0005", new Alimento { nombre = "Sardinas", precio = 1.00, calorias = 208 });
        diccionarioAlimentos.Add("0006", new Alimento { nombre = "Batata", precio = 0.45, calorias = 86 });
        diccionarioAlimentos.Add("0007", new Alimento { nombre = "K�fir", precio = 1.30, calorias = 99 });
        diccionarioAlimentos.Add("0009", new Alimento { nombre = "Cacao", precio = 2.00, calorias = 228 });
        diccionarioAlimentos.Add("0010", new Alimento { nombre = "Ch�a", precio = 1.50, calorias = 486 });
        diccionarioAlimentos.Add("0011", new Alimento { nombre = "Lino", precio = 0.75, calorias = 534 });


        Console.WriteLine("Imprimiendo elementos del diccionario: ");
        foreach (var elemento in diccionarioAlimentos)
        {
            Console.WriteLine($"Key/Clave: {elemento.Key} | Nombre alimento:  {elemento.Value.nombre} | Precio: {elemento.Value.precio}");
        }

        Console.WriteLine("");

        // Operaci�n de eliminaci�n

        diccionarioAlimentos.Remove("0001");
        diccionarioAlimentos.Remove("0007");

        Console.WriteLine("Imprimiendo elementos del diccionario despu�s de la eliminaci�n: ");
        foreach (var elemento in diccionarioAlimentos)
        {
            Console.WriteLine($"Key/Clave: {elemento.Key} | Nombre alimento:  {elemento.Value.nombre} | Precio: {elemento.Value.precio}");
        }

        Console.WriteLine("");


        // Operaci�n de actualizaci�n


        foreach (var alimento in diccionarioAlimentos)
        {
            alimento.Value.nombre += " modificado diccionario.";
        }


        Console.WriteLine("Imprimiendo elementos del diccionario despu�s de la actualizaci�n: ");
        foreach (var elemento in diccionarioAlimentos)
        {
            Console.WriteLine($"Key/Clave: {elemento.Key} | Nombre alimento:  {elemento.Value.nombre} | Precio: {elemento.Value.precio}");
        }

        Console.WriteLine("");

        // Operaci�n de ordenaci�n
        diccionarioAlimentos = diccionarioAlimentos.OrderByDescending(alimento => alimento.Value.precio).ToDictionary(pair => pair.Key, pair => pair.Value);

        Console.WriteLine("Imprimiendo elementos del diccionario despu�s de la ordenaci�n: ");
        foreach (var elemento in diccionarioAlimentos)
        {
            Console.WriteLine($"Key/Clave: {elemento.Key} | Nombre alimento:  {elemento.Value.nombre} | Precio: {elemento.Value.precio}");
        }

        Console.WriteLine("");

        leerContactos();
        agendaDeContactos();
        /* DIFICULTAD EXTRA (opcional):
         * Crea una agenda de contactos por terminal.
         * - Debes implementar funcionalidades de b�squeda, inserci�n, actualizaci�n y eliminaci�n de contactos.
         * - Cada contacto debe tener un nombre y un n�mero de tel�fono.
         * - El programa solicita en primer lugar cu�l es la operaci�n que se quiere realizar, y a continuaci�n
         *   los datos necesarios para llevarla a cabo.
         * - El programa no puede dejar introducir n�meros de tel�fono no n�mericos y con m�s de 11 d�gitos.
         *   (o el n�mero de d�gitos que quieras)
         * - Tambi�n se debe proponer una operaci�n de finalizaci�n del programa.
         */


        static void agendaDeContactos()
        {

            Console.WriteLine("---- AGENDA DE CONTACTOS ----");
            Console.WriteLine("�Qu� operacion quieres realizar?");
            Console.WriteLine("1. Buscar contactos\n" +
                "2. Introducir contacto\n" +
                "3. Actualizar contacto\n" +
                "4. Eliminar contacto\n" +
                "0. Salir del programa");

            bool opcionConvertida;
            int opcion;


            do
            {
                opcionConvertida = int.TryParse(Console.ReadLine(), out opcion);
                // Seg�n la opci�n elegida, con un switch elige cada uno de los m�todos

                switch (opcion)
                {
                    case 0:
                        if (!opcionConvertida)
                        {
                            Console.WriteLine("Opcion no v�lida!");
                        }
                        else
                        {
                            Console.WriteLine("Has salido del programa!");
                            Environment.Exit(0);
                        }
                        break;
                    case 1:
                        buscarContactos();
                        break;
                    case 2:
                        introducirContactos();
                        break;
                    case 3:
                        actualizarContacto();
                        break;
                    case 4:
                        eliminarContacto();
                        break;
                    default:
                        Console.WriteLine("Opci�n no v�lida");
                        break;
                }

            } while (!opcionConvertida || opcion != 0);
        }


        // Este m�todo elimina un contacto
        static void eliminarContacto()
        {

            if (!(listaDeContactos.Count == 0))
            {
                int idUsuario;
                bool idCorrecto;
                bool campoAModificarCorrecto;
                int campoAModificar;
                string mensajeActualizar = "Introduce el id del usuario que quieres eliminar: ";


                do
                {
                    Console.WriteLine(mensajeActualizar);
                    idCorrecto = int.TryParse(Console.ReadLine(), out idUsuario);
                    mensajeActualizar = "Por favor introduce un valor num�rico v�lido: ";

                } while (!idCorrecto);


                var contactoSeleccionado = listaDeContactos.Where(c => c.idContacto == idUsuario).FirstOrDefault();
                if (contactoSeleccionado != null)
                {
                    listaDeContactos.Remove(contactoSeleccionado);
                    Console.WriteLine("Contacto eliminado correctamente");

                }
                else
                {
                    Console.WriteLine("�Id introducida no encontrada!");
                }

            }
            else
            {
                Console.WriteLine("�La lista est� vac�a :(!");
            }
            vaciarArchivo();
            guardarContacto();
            agendaDeContactos();
        }

        // Este m�todo va a actualizar un contacto en concreto
        static void actualizarContacto()
        {
            if (!(listaDeContactos.Count == 0))
            {
                int idUsuario;
                bool idCorrecto;
                bool campoAModificarCorrecto;
                bool telefonoValido;
                int campoAModificar;
                string telefonoContacto;
                string mensajeTelefonoIncorrecto = "";

                string mensajeActualizar = "Introduce el id del usuario que quieres actualizar: ";


                do
                {
                    Console.WriteLine(mensajeActualizar);
                    idCorrecto = int.TryParse(Console.ReadLine(), out idUsuario);
                    mensajeActualizar = "Por favor introduce un valor num�rico v�lido: ";

                } while (!idCorrecto);


                var contactoSeleccionado = listaDeContactos.Where(c => c.idContacto == idUsuario).FirstOrDefault();
                if (contactoSeleccionado != null)
                {
                    Console.WriteLine("Por favor elige el campo a modificar: \n 1. Nombre\n" +
                  " 2. N�mero telef�nico");
                    campoAModificarCorrecto = int.TryParse(Console.ReadLine(), out campoAModificar);
                    if (campoAModificar == 1)
                    {
                        Console.WriteLine($"Valor actual: {contactoSeleccionado.nombre} | Nuevo valor: \n");
                        listaDeContactos.Where(c => c.idContacto == idUsuario).FirstOrDefault().nombre = Console.ReadLine();

                        Console.WriteLine("Nombre modificado correctamente.");
                    }
                    else if (campoAModificar == 2)
                    {

                        do
                        {
                            Console.WriteLine($"Valor actual: {contactoSeleccionado.numeroTelefono} | Nuevo valor: \n");
                            Console.WriteLine(mensajeTelefonoIncorrecto);
                            telefonoContacto = Console.ReadLine();
                            telefonoValido = Regex.IsMatch(telefonoContacto, regexTelefono);
                            mensajeTelefonoIncorrecto = "Introduce un n�mero de tel�fono v�lido!: ";

                        } while (!telefonoValido);

                        listaDeContactos.Where(c => c.idContacto == idUsuario).FirstOrDefault().numeroTelefono = telefonoContacto;

                        Console.WriteLine("Numero de tel�fono modificado correctamente.");
                    }
                    else
                    {
                        Console.WriteLine("Introduce un campo correcto");
                    }

                }
                else
                {
                    Console.WriteLine("�Id introducida no encontrada!");
                }

            }
            else
            {
                Console.WriteLine("�La lista est� vac�a :(!");
            }
            vaciarArchivo();
            guardarContacto();
            agendaDeContactos();

        }


        // Este m�todo a�ade contactos a nuestra lista
        static void introducirContactos()
        {
            Console.WriteLine("Introduce el nombre de tu contacto: ");
            string nombreContacto = Console.ReadLine();
            string telefonoContacto;
            bool numeroValido;

            Console.WriteLine("Introduce el n�mero de tel�fono de tu contacto");

            string mensaje = "";
            do
            {
                Console.WriteLine(mensaje);
                telefonoContacto = Console.ReadLine();
                numeroValido = Regex.IsMatch(telefonoContacto, regexTelefono);
                mensaje = "Por favor, introduce un n�mero de tel�fono v�lido: ";

            } while (!numeroValido);

            listaDeContactos.Add(new Contacto(nombreContacto, telefonoContacto));
            Console.WriteLine($"�El contacto con el nombre {nombreContacto} y el n�mero de tel�fono {telefonoContacto}  se ha introducido correctamente!");
            guardarContacto();
            agendaDeContactos();

        }

        // Este m�todo todos los contactos que hemos a�adidos
        static void buscarContactos()
        {
            if (listaDeContactos.Count == 0)
            {
                Console.WriteLine("Lista de contactos vac�a :(");

            }
            else
            {
                Console.WriteLine("\nLista de contactos: \n");
                foreach (Contacto contacto in listaDeContactos)
                {
                    Console.WriteLine($"Id: {contacto.idContacto} || Nombre: {contacto.nombre} | N�mero tlf: {contacto.numeroTelefono}");
                }
            }
            Console.WriteLine("");
            agendaDeContactos();
        }


        // Este m�todo guarda los contactos en un fichero de texto
        static void guardarContacto()
        {
            using (StreamWriter file = new StreamWriter(rutaArchivoTxt))
            {
                foreach (Contacto contacto in listaDeContactos)
                {
                    file.WriteLine(contacto.ToString());
                }
            }

        }
        // Este m�todo borra el contenido del fichero de texto 
        static void vaciarArchivo()
        {
            using (StreamWriter file = new StreamWriter(rutaArchivoTxt))
            {
                // No escribir nada en el archivo
            }
        }

        // Este m�todo los contactos del fichero de texto
        static void leerContactos()
        {
            try
            {
                using (StreamReader reader = new StreamReader(rutaArchivoTxt))
                {
                    string linea;
                    while ((linea = reader.ReadLine()) != null)
                    {
                        string[] partes = linea.Split(',');
                        if (partes.Length == 2)
                        {
                            Contacto contacto = new Contacto(partes[0], partes[1]);
                            listaDeContactos.Add(contacto);
                        }
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Error leyendo contactos del fichero");
            }
        }
    }

}
class Alimento
{
    public string nombre;
    public double precio;
    public int calorias;
}

class Contacto
{
    public static int idAutoIncrementable;
    public string nombre;
    public string numeroTelefono;
    public int idContacto;

    public Contacto(string nombre, string numeroTelefono)
    {
        idContacto = idAutoIncrementable;
        this.nombre = nombre;
        this.numeroTelefono = numeroTelefono;
        idAutoIncrementable++;
    }
    public override string ToString()
    {
        return $"{nombre},{numeroTelefono}";
    }
}


