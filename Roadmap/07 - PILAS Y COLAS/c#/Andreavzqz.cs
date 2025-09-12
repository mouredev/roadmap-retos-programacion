using System; 

namespace EjemploAsignacionYPaso
{
    class Persona
    {
        public string Nombre {get; set; }
    }

    class Program 
    {
    static void Main (string[] args)
    {
        //Ejemplo de asignacion por valor
        int a = 5;
        int b = a; //b es una copia de a
        b = 10;    // Cambiamos b, pero permanece igual
        Console.WriteLine($"a: {a}"); //Imprime 5
        Console.WriteLine($"b: {b}"); //Imprime 10

        //Ejemplo de asignacion por referencia
        Persona persona1 = new Persona();
        persona1.Nombre = "Juan";
        Persona.persona2 = persona1 // persona2 referencia el mismo objeto que persona1
        persona2.Nombre = "Pedro"; // Cambiamos el nombre a traves de persona2
        Console.WriteLine($"persona1.Nombre: {persona1.Nombre}"); //Imprime "Pedro"
        Console.WriteLine($"persona2.Nombre: {persona2.Nombre}"); //Imprime "Pedro"

        //Ejemplo de paso de parametro por valor
        int numero = 5;
        Incrementar(numero);
        Console.WriteLine($"numero despues de Incrementar: {numero}"); // Imprime 5

        // Ejemplo de paso de parametros por referencia
        IncrementarRef(ref numero);
        Console.WriteLine($"numero despues de IncrementarRef: {numero}"); // Imprime 6

        //Ejemplo de paso de parametros por referencia con objetos
        Persona persona = new Persona();
        Persona.Nombre = "Juan";
        CambiarNombre(persona);
        Console.WriteLine($"persona.Nombre despues de CambiarNombre: {persona.Nombre}"); // Imprime "Luis"

        // Ejemplo de modificazcion de la referencia del objeto
        crearNuevaPersona(ref persona);
        Console.WriteLine($"persona.Nombre despues de crearNuevaPersona: {persona.Nombre}"); // Imprime "Carlos"
    }

    //Funcion que recibe un parametro por valor
    static void Incrementar(int x)
        {
            x++;
            Console.WriteLine($"x en Incrementar: {x}"); // Imprime 6
        }

    //Funcion que recibe un parametro por referencia
    static void IncrementarRef(ref int x)
        {
            x++;
            Console.WriteLine($"x en IncremetarRef: {x}"); //Imprime 6
        }

    //Funcion que modifica una propiedad de un objeto
    static void CambiarNombre(Persona p)
    {
        p.Nombre = "Luis";
    }    

    //Funcion que cambia la referencia de un objeto
    static void crearNuevaPersona(ref Persona p)
    {
        p = new Persona();
        p.Nombre = "Carlos";
    }
    
  }
 /*

Explicación:

Asignación por Valor:
int a = 5; int b = a;: b es una copia de a.
Cambiar b no afecta a a.

Asignación por Referencia:
Persona persona1 = new Persona(); Persona persona2 = persona1;: persona2 referencia el mismo objeto que persona1.
Cambiar una propiedad a través de persona2 afecta a persona1.

Paso de Parámetros por Valor:
Incrementar(numero);: La función recibe una copia del valor.
Cambios dentro de Incrementar no afectan a numero fuera de la función.

Paso de Parámetros por Referencia:
IncrementarRef(ref numero);: La función trabaja directamente con la variable original.
Cambios dentro de IncrementarRef afectan a numero fuera de la función.

Paso de Parámetros por Referencia con Objetos:
CambiarNombre(persona);: La función modifica una propiedad del objeto referenciado.
Cambios dentro de CambiarNombre afectan al objeto persona fuera de la función.

Modificación de la Referencia del Objeto:
CrearNuevaPersona(ref persona);: La función cambia la referencia del objeto.
Después de CrearNuevaPersona, persona referencia a un nuevo objeto.

*/

}
