using static System.Runtime.InteropServices.JavaScript.JSType;

namespace RetosProgramacion {
    class Program
    {
        static void Main(string[] args)
        {
            //Tipos de variables POR VALOR: el operando de la izquierda recibe el valor del de la derecha.
            //Se almacenan en el tipo de memoria Stack
            //Son los struct, los tipos primitivos y enum.
            int var1 = 15;
            int var2 = var1;
            var1 = 10; //aunque se modifique el valor de var1, var2 mantiene su valor.
            Console.WriteLine(var1);
            Console.WriteLine(var2);

            Empleado empleado1 = new Empleado(1500, "Sebastian"); //se crea una copia de struct empleado en Stack
            empleado1.incrementarSalario(1000);
            Console.WriteLine(empleado1);
            Empleado empleado2 = empleado1;
            empleado2.incrementarSalario(3000); //al modificar empleado2 no se modifica empleado1.
            Console.WriteLine(empleado2);
            Console.WriteLine(empleado1);

            //Tipos de variables POR REFERENCIA: la asignación copia la referencia al objeto.
            //Los objetos se guardan en la memoria Heap y su referencia en el Stack.
            //Los tipos de variable por valor son las clases, los records, los string, las matrices,
            //los delegados, las interfaces, los tipos dinamicos.
            Auto auto1 = new Auto("Nissan", 0);
            Auto auto2 = new Auto("Peugueot", 15000);
            auto2 = auto1;
            Console.WriteLine("Auto 2: " + auto2); //auto2 apunta a la direccion de memoria de auto1
            auto2.sumarKms(150);
            Console.WriteLine("Auto 1: " + auto1);
            Console.WriteLine("Auto 2: " + auto2);

            //Funciones con paso de parametros por valor
            int numero = 5;
            Console.WriteLine($"Antes de PasarPorValor: {numero}");
            PasarPorValor(numero);
            Console.WriteLine($"Después de PasarPorValor: {numero}");

            //Funciones con paso de parametros por referencia

            int[] numeros = { 1, 2, 3, 4, 5 };
            Console.WriteLine("Array antes de modificar:");
            ImprimirArray(numeros);
            ModificarArray(numeros);
            Console.WriteLine("Array después de modificar:");
            ImprimirArray(numeros);

            // EXTRA -------------------------------------
            int valor1 = 10;
            int valor2 = 50;
            var retornoValor = intercambiarValor(valor1, valor2);

            Console.WriteLine($"Variables originales: {valor1} {valor2}");
            Console.WriteLine($"Variables nuevas: {retornoValor.Item1} {retornoValor.Item2}");


            Auto auto3 = new Auto("BMW", 100);
            Auto auto4 = new Auto("Fiat", 2000);
            var retornoReferencia = intercambiarReferencia(auto3, auto4);

            Console.WriteLine($"Variables originales: \n {auto3} \n {auto4}");
            Console.WriteLine($"Variables nuevas: \n {retornoReferencia.Item1} \n {retornoReferencia.Item2}");

        }

        static void PasarPorValor(int x)
        {
            x = 10; // Esto no afecta la variable original
            Console.WriteLine($"Dentro de PasarPorValor: {x}");
        }
        static void ModificarArray(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] *= 2;
            }
        }

        static void ImprimirArray(int[] arr)
        {
            foreach (int num in arr)
            {
                Console.Write(num + " ");
            }
            Console.WriteLine();
        }

        //EXTRA
        static (int, int) intercambiarValor(int x, int y)
        {
            int intermediario = x;
            x = y;
            y = intermediario;
            return (x, y);
        }
        static (Auto, Auto) intercambiarReferencia(Auto auto1, Auto auto2)
        {
            Auto autoIntermedio = auto1;
            auto1 = auto2;
            auto2 = autoIntermedio;

            return (auto1, auto2);
        }
    }
    public struct Empleado //se crea un struct inmutable en la memoria Stack
        {
            public double salario { get; set; }
            public string nombre { get; set; }
            public Empleado(double salario, string nombre)
            {
                this.salario = salario;
                this.nombre = nombre;
            }

            public override string ToString() => $"El salario del empleado {nombre} es {salario}";
            public void incrementarSalario(double incremento)
            {
            this.salario += incremento;
            }
        }
    public class Auto //hasta que no se instancia una clase no se crea el objeto en la memoria head
    {
        string marca { get; set; }
        double kms { get; set; }
        public Auto(string marca, double kms)
        {
            this.marca = marca;
            this.kms = kms;
        }
        public void sumarKms(double incrementoDeKms)
        {
            this.kms += incrementoDeKms;
        }
        public override string ToString()
        {
            return $"El auto marca {marca} tiene recorridos {kms} kilometros";
        }
               
    } 
}


