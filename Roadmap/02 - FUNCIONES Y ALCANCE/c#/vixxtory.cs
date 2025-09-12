using System;
public class Program
{

    /** FUNCIONES SEGUN VISIBILIDAD **/

    //01.Funcion static: pertenece a una clase en lugar de a una instancia espec�fica de esa clase. Son �tiles con tareas que no dependen de ning�n estado espec�fico de un objeto.
    public class ConversorTemperatura
    {
        public static double CelsiusToFahrenheit(double celsius)
        {
            return (celsius * 9 / 5) + 32;
        }
    }

    //02.Funcion public: puede ser accedida desde cualquier parte del c�digo, ya sea desde la misma clase, desde clases derivadas, o desde cualquier otra clase en el mismo ensamblado. 
    public class Circulo
    {
        public double Radio { get; set; }

        public Circulo(double radio)
        {
            Radio = radio;
        }

        public double CalcularArea()
        {
            return Math.PI * Radio * Radio;
        }
    }

    //03. Metodo private: solo son accesibles dentro de la misma clase donde est�n definidos.
    //04. Metodos protegidos:  similares a los privados, pero tambi�n son accesibles desde clases derivadas (subclases) de la clase donde est�n definidos.
    public class MiClase
    {
        private void MetodoPrivado()
        {
            Console.WriteLine("Este es un m�todo privado.");
        }

        protected void MetodoProtegido()
        {
            Console.WriteLine("Este es un m�todo protegido.");
        }
    }
    public class OtraClase : MiClase
    {
        public void AccesoDesdeClaseDerivada()
        {
            // No se puede llamar a MetodoPrivado desde aqu�, ya que es privado.
            MetodoProtegido(); // Pero se puede llamar a MetodoProtegido, ya que es protegido.
        }
    }

    /** FUNCIONES SEGUN TIPO DE RETORNO **
     * Estos pueden ser tipos de datos primitivos, tipos de datos personalizados (como clases), tipos anulables (Nullable<T>), enumeraciones, matrices, interfaces, delegados, entre otros.**/

    //01. Tipos de datos primitivos: int, float, double, bool, char, etc.
    public int ObtenerEntero()
    {
        return 42;
    }

    //02. Clases y estructuras: Una funci�n puede devolver una instancia de una clase o una estructura.
    public MiClase ObtenerInstancia()
    {
        return new MiClase();
    }

    //03. Tipos anulables (Nullable<T>): Permiten que un tipo de valor tenga un valor nulo adem�s de sus valores normales.
    public int? ObtenerEnteroNullable()
    {
        int? resultado = null;
        return resultado;
    }

    //04. Matrices: Una funci�n puede devolver una matriz de cualquier tipo.
    public int[] ObtenerArreglo()
    {
        return new int[] { 1, 2, 3, 4, 5 };
    }

    //05. Delegados: Una funci�n puede devolver un delegado que apunte a otra funci�n.
    public Func<int, int> ObtenerFuncion()
    {
        return x => x * x;
    }

    /** FUNCIONES SEGUN TIPO DE PARAMETRO QUE RECIBE */

    //01. Funciones sin par�metros: Realizan una tarea espec�fica basada �nicamente en su l�gica interna y no requieren datos de entrada externos.
    public void Saludar()
    {
        Console.WriteLine("�Hola!");
    }

    //02. Funciones con par�metros: Reciben uno o m�s par�metros que se utilizan para proporcionar datos de entrada a la funci�n.
    public void Sumar(int a, int b)
    {
        int resultado = a + b;
        Console.WriteLine("La suma de {0} y {1} es {2}", a, b, resultado);
    }

    //03. Funciones con par�metros opcionales: Se definen par�metros con un valor predeterminado, lo que los convierte en opcionales. Esto significa que puedes llamar a la funci�n sin proporcionar valores para esos par�metros, y se utilizar� el valor predeterminado en su lugar.
    public void Saludar(string nombre = "Mundo")
    {
        Console.WriteLine("�Hola, {0}!", nombre);
    }

    //04. Funciones con par�metros de salida (out): Pueden devolver m�s de un valor como resultado. Los par�metros de salida se declaran con la palabra clave out y deben ser inicializados dentro de la funci�n antes de que �sta retorne.
    public void Dividir(int dividendo, int divisor, out int cociente, out int residuo)
    {
        cociente = dividendo / divisor;
        residuo = dividendo % divisor;
    }

    //05. Funciones con par�metros de referencia (ref): Similar a los par�metros de salida, pero los par�metros de referencia (ref) permiten que los valores se pasen a la funci�n y se modifiquen dentro de ella, y esos cambios se reflejan fuera de la funci�n.
    public void Incrementar(ref int numero)
    {
        numero++;
    }

    /** No es posible definir funciones dentro funciones como en JavaScript. Sin embargo, puedes lograr un comportamiento similar utilizando clases internas o delegados anidados.**/

    //02. Delegados anidados: Se puede usar delegados anidados para definir funciones dentro de otras funciones, pero estas funciones estar�an limitadas a ser m�todos dentro de una clase.
    public class Clase
    {
        public delegate void Metodo();

        public void MetodoExterno()
        {
            Console.WriteLine("M�todo externo");

            Metodo metodoInterno = () =>
            {
                Console.WriteLine("M�todo interno");
            };

            metodoInterno();
        }
    }

    /** ALGUNOS EJEMPLOS DE FUNCIONES PREDETERMINADAS */

    //01. Console.ReadLine(): Lee una l�nea de texto desde la entrada est�ndar (generalmente la consola) y la devuelve como una cadena
    string entrada = Console.ReadLine();

    //02. string.Format(): Esta funci�n est�tica de la clase string formatea una cadena de texto utilizando un patr�n y una lista de argumentos.
    private static string nombre = "Juan";
    private static int edad = 30;
    string mensaje = string.Format("Hola, me llamo {0} y tengo {1} a�os.", nombre, edad);
    
    
    /** VARIABLE LOCAL Y GLOBAL */

    //Variable local: Se declara dentro de un bloque de c�digo, como una funci�n o un bloque { } y solo puede ser utilizada dentro de ese bloque
    public void MiFuncion()
    {
        int x = 10; // Variable local
        Console.WriteLine(x); // Se puede acceder dentro de la funci�n
    }

    // Console.WriteLine(x); // Esto causar�a un error, ya que x no es visible aqu�

    //Variable global: Es aquella que se declara fuera de cualquier funci�n o bloque, generalmente al comienzo del programa y  puede ser accedida y modificada desde cualquier parte del c�digo.
    // (Se recomienda utilizar variables locales siempre que sea posible y limitar el uso de variables globales a casos donde sean realmente necesarias.)

    /** DIFICULTAD EXTRA */
    public static int ImprimirNumeros(string texto1, string texto2)
    {
        int contador = 0;
        for (int i = 1; i <= 100; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                Console.WriteLine(texto1 + texto2);
            }
            else if (i % 3 == 0)
            {
                Console.WriteLine(texto1);
            }
            else if (i % 5 == 0)
            {
                Console.WriteLine(texto2);
            }
            else
            {
                Console.WriteLine(i);
                contador++;
            }
        }
        return contador;
    }


    public static void Main(string[] args)
    {
        /** //01
        double temperaturaCelsius = 20;
        double temperaturaFahrenheit = ConversorTemperatura.CelsiusToFahrenheit(temperaturaCelsius);
        Console.WriteLine("{0} grados Celsius son {1} grados Fahrenheit", temperaturaCelsius, temperaturaFahrenheit);

        //02
        Circulo circulo = new Circulo(5);
        double area = circulo.CalcularArea();
        Console.WriteLine("El �rea del c�rculo es: {0}", area); */

        //DIFICULTAD EXTRA
        string texto1 = "Fizz";
        string texto2 = "Buzz";
        int vecesImpreso = ImprimirNumeros(texto1, texto2);
        Console.WriteLine("El n�mero de veces que se imprimi� un n�mero en lugar de los textos es: " + vecesImpreso);
    }
}