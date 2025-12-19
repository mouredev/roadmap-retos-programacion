/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
*/

using System;
using System.Dynamic;
using System.Timers;

// Diferentes estructuras de datos en el Lenguaje de C#

// Listas:

List<string> usuarios = new();

usuarios.Add("Iván");
usuarios.Add("Juan");
usuarios.Add("Natalia");
usuarios.Add("Pablo");
usuarios.Add("Alfonso");

foreach (var usuariosLista in usuarios)
{
    Console.WriteLine($"Usuario: {usuariosLista}");
}

// Diccionarios:

Dictionary<int, string> productos = new();

productos.Add(1, "lapiz");
productos.Add(2, "goma");
productos.Add(3, "boli");

Console.WriteLine(productos[2]);


// Stacks:

Stack<string> sitiosWeb = new();

sitiosWeb.Push("www.google.com");
sitiosWeb.Push("www.amazon.es");
sitiosWeb.Push("www.github.com");

string ultima = sitiosWeb.Pop(); // Esto elimina el primer dato que introducimos anterior mente en el Stack en este caso -> www.google.com

// Queue: 

Queue<string> filaImpresion = new();

filaImpresion.Enqueue("Documento_1.pdf");
filaImpresion.Enqueue("Foto.jpg");

// Atendemos al primero que llegó
string procesando = filaImpresion.Dequeue();
Console.WriteLine($"Imprimiendo: {procesando}");


// Tuplas: Son listas que no se pueden modificar

var tuplaInt = (1, 2, 3, 4, 5);
Console.WriteLine(tuplaInt);

// Arrays:
var myArray = new string[] { "Iván", "Calero Moreno", "Juan Carlos" };
Console.WriteLine(myArray[1]);
myArray[1] = "21";
Console.WriteLine(myArray[1]);

// Sets (Conjuntos)
var mySet = new HashSet<string> { "Pepe", "Córdoba", "Sevilla" };
foreach (string elemento in mySet)
{
    Console.WriteLine(elemento);
}



// Agenda de contacto Ejercicio Extra.


var agendaContactos = new Dictionary<string, string>
{
    {"Iván", "111222333"},
    {"Pepe", "123456789"},
    {"Alberto", "987654321"},
    {"Miguel", "1234512345"},
};

Console.WriteLine("--------- Agenda de contactos -----------");

Console.WriteLine("Selecciona una acción a realizar en tu Agenda de contactos: ");
Console.WriteLine("1. Buscar contacto");
Console.WriteLine("2. Añadir contacto");
Console.WriteLine("3. Actualizar contacto");
Console.WriteLine("4. Eliminar contacto");
Console.WriteLine("5. Salir");
Console.Write("Elige una opción: ");

string entradaUsuario = Console.ReadLine() ?? "";

//bool continuar = true;



switch (entradaUsuario)
{
    case "1":
        Console.WriteLine("Introduce el nombre que quieras buscar en tu agenda.");
        string nombreBuscar = Console.ReadLine() ?? "";

        if (agendaContactos.ContainsKey(nombreBuscar))
        {
                Console.WriteLine($"El usuario {nombreBuscar} se encuentra en tu agenda de contactos.");
                Console.WriteLine($"Su numero de telefono es: {agendaContactos[nombreBuscar]}");
        } 
        else
        {
            Console.WriteLine("El nombre que has introducido no se encuentra en tu lista de contactos.");
        }
    break;

    case "2":
        Console.WriteLine("Introduce el nombre y del contacto que deseas añadir en tu agenda.");
        string nombreAñadir = Console.ReadLine() ?? "";
        string telefonoAñadir = TelefonoValido();
        if (agendaContactos.ContainsKey(nombreAñadir))
        {
            Console.WriteLine("Este contacto ya existe en tu agenda.");
        }
        else
        {
            agendaContactos.Add(nombreAñadir, telefonoAñadir);
            Console.WriteLine("Contacto guardado correctamente en tu agenda.");
        }
    break;

    case "3":
        Console.WriteLine("Introduce el nombre del contacto que quieras editar: ");
        string nombreEditar = Console.ReadLine() ?? "";

        if (agendaContactos.ContainsKey(nombreEditar))
        {   
            Console.WriteLine($"Ahora mismo se encuentra enditando {nombreEditar}.");
            Console.WriteLine("Selecciona el campo que quieres modificar al contacto.");
            Console.WriteLine("1.Nombre");
            Console.WriteLine("2.Telefono");
            string opcionEditar = Console.ReadLine() ?? "";
            switch (opcionEditar)
            {
                case "1":
                    Console.WriteLine("Introduce el nombre nuevo para este contacto: ");
                    string nombreEditado = Console.ReadLine() ?? "";
                    agendaContactos[nombreEditar] = nombreEditado;
                    Console.WriteLine("Nombre del contacto editado correctamente.");
                break;
                case "2":
                    string telefonoEditar = TelefonoValido();
                    agendaContactos[nombreEditar] = telefonoEditar;
                    Console.WriteLine("Telefono del contacto actualizado correctamente.");
                break;
            }
        } 
        else
        {
            Console.WriteLine("No puedes editar un contacto que no existe.");
        }
    break;

    case "4":
        Console.WriteLine("Introduce el nombre del contacto que quieres borrar: ");
        string nombreBorrar = Console.ReadLine() ?? "";
        if (agendaContactos.ContainsKey(nombreBorrar))
        {
            agendaContactos.Remove(nombreBorrar);
            Console.Write($"Eliminando {nombreBorrar}...");
            Console.Write($"Contacto elimidado con exito.");
        }
        else
        {
            Console.WriteLine("No puedes borrar un contacto que no existe.");
        }
    break;
    
    case "5":
        Console.WriteLine("Saliendo del programa....");
    break;

    default:
        Console.WriteLine("Opción no valida intentalo de nuevo.");
    break;
}


string TelefonoValido()
{
    string telefonoContacto = "";
    bool esValido = false;

    while (!esValido)
    {
        Console.WriteLine("Introduce un número de telefono para añadirlo al contacto.");
        telefonoContacto = Console.ReadLine() ?? "";
        
        bool esNumerico = telefonoContacto.All(char.IsDigit);

        if (!string.IsNullOrEmpty(telefonoContacto) && esNumerico && telefonoContacto.Length <= 11)
        {
            esValido = true;
        }
        else
        {
            Console.Write("Formato del número de telefono incorrecto. Intentalo de nuevo.");
        }
    }
    return telefonoContacto;
}
