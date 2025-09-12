using System;
using System.Collections.Generic;

namespace R03___2024
{
    //Clase para dificultad adicional
    public class Contacto
    {
        private string nombre;
        private int numero;

        public string Nombre { get { return this.nombre; } set { this.nombre = value; } }
        public int Numero { get { return this.numero; } set { this.numero = value; } }
    }

    internal class Program
    {
        /*
         * EJERCICIO:
         * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
         * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
         *
         * DIFICULTAD EXTRA (opcional):
         * Crea una agenda de contactos por terminal.
         * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
         * - Cada contacto debe tener un nombre y un número de teléfono.
         * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
         *   los datos necesarios para llevarla a cabo.
         * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
         *   (o el número de dígitos que quieras)
         * - También se debe proponer una operación de finalización del programa.
         */

        static int MenuPrincipal()
        {
            int opcion;

            do
            {
                Console.WriteLine("\nBienvenido a tu agenda, escoge una opción:");
                Console.WriteLine("1 - Buscar contacto");
                Console.WriteLine("2 - Insertar contacto");
                Console.WriteLine("3 - Actualizar contacto");
                Console.WriteLine("4 - Eliminar contacto");
                Console.WriteLine("5 - Salir");

                if (!int.TryParse(Console.ReadLine(), out opcion))
                {
                    Console.WriteLine("Opción no válida. Por favor, ingrese un número entero.");
                }
                else if (opcion < 1 || opcion > 5)
                {
                    Console.WriteLine("Opción fuera de rango. Por favor, elija una opción del 1 al 5.");
                }

            } while (opcion < 1 || opcion > 5);

            return opcion;
        }

        static void BuscarContacto(List<Contacto> contactos)
        {
            Console.Write("Ingrese el nombre del contacto que desea buscar: ");
            string nombreBuscado = Console.ReadLine();

            bool encontrado = false;

            for (int i = 0; i < contactos.Count; i++)
            {
                if (contactos[i].Nombre.Equals(nombreBuscado, StringComparison.OrdinalIgnoreCase))
                {
                    Console.WriteLine("Contacto encontrado:");
                    Console.WriteLine($"Nombre: {contactos[i].Nombre}");
                    Console.WriteLine($"Número: {contactos[i].Numero}");
                    encontrado = true;
                    break; // Si encontramos el contacto, salimos del bucle
                }
            }

            if (!encontrado)
            {
                Console.WriteLine("Contacto no encontrado.");
            }
        }

        static Contacto AgregarContacto(List<Contacto> contactos)
        {
            Contacto contacto = new Contacto();
            string nombre; string numero;
            // Pedir y validar el nombre
            do
            {
                Console.Write("Nombre del contacto: ");
                nombre = Console.ReadLine();
                if (string.IsNullOrWhiteSpace(nombre))
                {
                    Console.WriteLine("El nombre está vacío. Por favor, ingréselo nuevamente.");
                }
            } while (string.IsNullOrWhiteSpace(nombre));

            do
            {
                Console.Write("Número de teléfono (hasta 11 dígitos): ");
                numero = Console.ReadLine();
                if (string.IsNullOrWhiteSpace(numero) || !EsNumero(numero) || numero.Length > 11)
                {
                    Console.WriteLine("Número de teléfono inválido. Debe contener hasta 11 dígitos numéricos.");
                }
            } while (string.IsNullOrWhiteSpace(numero) || !EsNumero(numero) || numero.Length > 11);

            if (ExisteContacto(nombre, numero, contactos))
            {
                Console.WriteLine("El contacto ya existe en la agenda.");
            }
            else
            {
                contacto.Nombre = nombre;
                contacto.Numero = int.Parse(numero);
                contactos.Add(contacto);
                Console.WriteLine("Contacto agregado correctamente.");
            }

            return contacto;
        }

        private static bool EsNumero(string str)
        {
            return int.TryParse(str, out _);
        }

        static bool ExisteContacto(string nombre, string numero, List<Contacto> contactos)
        {
            foreach (Contacto contacto in contactos)
            {
                if (contacto.Nombre == nombre || contacto.Numero == int.Parse(numero))
                {
                    return true;
                }
            }
            return false;
        }

        static void MostrarContactos(List<Contacto> contactos)
        {
            Console.WriteLine("Lista de contactos:");

            if (contactos.Count == 0)
            {
                Console.WriteLine("No hay contactos en la lista.");
            }
            else
            {
                foreach (var contacto in contactos)
                {
                    Console.WriteLine($"Nombre: {contacto.Nombre}, Número: {contacto.Numero}");
                }
            }
        }

        static void ActualizarContacto(List<Contacto> contactos)
        {
            Console.Write("Ingrese el nombre del contacto que desea actualizar: ");
            string nombreBuscado = Console.ReadLine();

            int indiceEncontrado = -1;

            for (int i = 0; i < contactos.Count; i++)
            {
                if (contactos[i].Nombre.Equals(nombreBuscado, StringComparison.OrdinalIgnoreCase))
                {
                    indiceEncontrado = i;
                    break;
                }
            }

            if (indiceEncontrado != -1)
            {
                Console.WriteLine("Contacto encontrado. Proporcione la nueva información:");

                // Solicitar y actualizar el nombre
                Console.Write("Nuevo nombre: ");
                string nuevoNombre = Console.ReadLine();
                contactos[indiceEncontrado].Nombre = string.IsNullOrWhiteSpace(nuevoNombre) ? contactos[indiceEncontrado].Nombre : nuevoNombre;

                // Solicitar y actualizar el número de teléfono
                Console.Write("Nuevo número de teléfono (hasta 11 dígitos): ");
                string nuevoNumero = Console.ReadLine();
                if (!string.IsNullOrWhiteSpace(nuevoNumero) && EsNumero(nuevoNumero) && nuevoNumero.Length <= 11)
                {
                    contactos[indiceEncontrado].Numero = int.Parse(nuevoNumero);
                }
                else
                {
                    Console.WriteLine("Número de teléfono inválido. No se actualizó el número.");
                }

                Console.WriteLine("Contacto actualizado correctamente.");
            }
            else
            {
                Console.WriteLine("Contacto no encontrado. No se puede actualizar.");
            }
        }

        static void EliminarContacto(List<Contacto> contactos)
        {
            Console.Write("Ingrese el nombre del contacto que desea eliminar: ");
            string nombreBuscado = Console.ReadLine();

            int indiceEncontrado = -1;

            for (int i = 0; i < contactos.Count; i++)
            {
                if (contactos[i].Nombre.Equals(nombreBuscado, StringComparison.OrdinalIgnoreCase))
                {
                    indiceEncontrado = i;
                    break;
                }
            }

            if (indiceEncontrado != -1)
            {
                Console.WriteLine("Contacto encontrado. ¿Está seguro de que desea eliminarlo? (S/N)");

                if (Console.ReadKey().Key == ConsoleKey.S)
                {
                    contactos.RemoveAt(indiceEncontrado);
                    Console.WriteLine("\nContacto eliminado correctamente.");
                }
                else
                {
                    Console.WriteLine("\nContacto no eliminado.");
                }
            }
            else
            {
                Console.WriteLine("Contacto no encontrado. No se puede eliminar.");
            }
        }

        static void Main(string[] args)
        {
            //Ejemplo array 3 elementos:
            int[] arrayInt = new int[3];

            //Rellena elementos:
            arrayInt[0] = 3; arrayInt[1] = 2; arrayInt[2] = 1;

            //Ordena elementos, en este caso para los arrays en c# se puede hacer con el método sort, pero en muchos otros no hay métodos, os muestro como crear una función manual,
            //se puede hacer de varias formas , en mi caso haré el algoritmo bubble (uno de los más fáciles).:
            int aux = arrayInt[0];
            for (int i = 0; i < arrayInt.Length; i++)
            {
                for (int j = i + 1; j < arrayInt.Length; j++)
                {
                    if (arrayInt[j] < arrayInt[i])
                    {
                        aux = arrayInt[i];
                        arrayInt[i] = arrayInt[j];
                        arrayInt[j] = aux;
                    }
                }
            }
            //Ordenacion con método:
            Array.Sort(arrayInt);

            //Actualización:
            arrayInt[2] = 4;

            // Borrado (desplazamiento hacia la izquierda):
            int posicionABorrar = 3;
            for (int i = posicionABorrar; i < arrayInt.Length - 1; i++)
            {
                arrayInt[i] = arrayInt[i + 1];
            }
            // Se establece el último elemento como 0 (o cualquier valor por defecto)
            arrayInt[arrayInt.Length - 1] = 0;

            //Muestra elementos por consola
            foreach (int i in arrayInt)
            {
                Console.WriteLine(i);
            }


            //Ejemplo lista altamente tipada, a diferencia del array no tiene límite.
            List<int> list = new List<int>();
            //Rellena elementos:
            list.Add(24); list.Add(25); list.Add(26);

            //Ordenar lista:
            list.Sort();

            //Borrado, en este caso no es necesario borrar el último elemento.
            list.RemoveAt(list.Count - 1);

            //Mostrar elementos lista:
            foreach (int i in list)
            {
                Console.WriteLine(i);
            }

            //Cola o queue:
            Queue<string> cola = new Queue<string>();

            //Rellenar elementos:
            cola.Enqueue("Elemento1");
            cola.Enqueue("Elemento2");
            cola.Enqueue("Elemento3");

            //La cola no es la mejor estructura para actualizar debido a su falta de índice

            //Borrado de elementos:
            cola.Dequeue(); //Borra el primer elemento

            //Mostrar elementos:
            Console.WriteLine("\nElementos de la cola:");
            foreach (string elemento in cola)
            {
                Console.WriteLine(elemento);
            }
            Console.WriteLine();

            // Pila o stack:
            Stack<string> pila = new Stack<string>();

            // Rellenar elementos:
            pila.Push("Elemento1");
            pila.Push("Elemento2");
            pila.Push("Elemento3");

            // Borrado de elementos (elimina el elemento en la cima de la pila):
            pila.Pop();

            // Mostrar elementos:
            Console.WriteLine("Elementos de la pila:");
            foreach (string elemento in pila)
            {
                Console.WriteLine(elemento);
            }
            Console.WriteLine();
            Console.WriteLine("Pulsa una tecla para ir a la dificultad extra:");
            Console.ReadKey();
            Console.Clear();

            //DIFICULTAD EXTRA:
            int opcion;
            List<Contacto> contactos = new List<Contacto>();
            do
            {
                opcion = MenuPrincipal();
                switch (opcion)
                {
                    case 1:
                        BuscarContacto(contactos);
                        break;
                    case 2:
                        AgregarContacto(contactos);
                        break;
                    case 3:
                        ActualizarContacto(contactos);
                        break;
                    case 4:
                        EliminarContacto(contactos);
                        break;
                    case 5: break;
                }
                Console.WriteLine("Pulsa una tecla para continuar");
                Console.ReadKey();
                Console.Clear();
            } while (opcion != 5);


        }
    }

}
