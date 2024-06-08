using System;

namespace RetosDeProgramacion
{
    internal class Operadores
    {
        public void aritmetic() {

            // Operadores aritmeticos
            int suma = 4 + 5;
            int resta = 4 + 5;
            suma++;
            resta--;
            Console.WriteLine($"esto es una suma: {4 + 5}");
            Console.WriteLine($"esto es una Resta: {4 - 5}");
            Console.WriteLine($"esto es una Multiplicacion: {4 * 5}");
            Console.WriteLine($"esto es una Division: {10 / 5}");
            Console.WriteLine($"esto es un Modulo: {4 % 5}");
            Console.WriteLine($"esto es un Incremento: {suma}");
            Console.WriteLine($"esto es un Decremento: {resta}");


        }
        //operadores de asignacion
        public void assignement()
        {
            int x = 5;
            int y = 5;
            y ^= 3;
            x |= 3;
            Console.WriteLine($"Operador de asignacion X = 5 {x}");
            Console.WriteLine($"Operador de asignacion X +=3 {x+=3}");
            Console.WriteLine($"Operador de asignacion X -=3 {x -= 3}");
            Console.WriteLine($"Operador de asignacion X *=3 {x *= 3}");
            Console.WriteLine($"Operador de asignacion X /=3 {x /= 3}");
            Console.WriteLine($"Operador de asignacion X %=3 {x %= 3}");
            Console.WriteLine($"Operador de asignacion X &=3 {x &= 3}");
            Console.WriteLine($"Operador de asignacion X |=3 {x}");
            Console.WriteLine($"Operador de asignacion X ^=3 {y}");
            Console.WriteLine($"Operador de asignacion X >>=3 {x >>= 3}");
            Console.WriteLine($"Operador de asignacion X <<=3 {x <<= 3}");

        }
        //Operadores de comparacion
        public void comparison()
        {
            int x = 5;
            int y = 3;
            Console.WriteLine($"Operador de asignacion Igual que == {x == y}");
            Console.WriteLine($"Operador de asignacion No Igual  != {x != y}");
            Console.WriteLine($"Operador de asignacion Mayor que > {x > y}");
            Console.WriteLine($"Operador de asignacion Menor que < {x < y}");
            Console.WriteLine($"Operador de asignacion Mayor Igual que >= {x >= y}");
            Console.WriteLine($"Operador de asignacion Menor Igual que <= {x <= y}");


        }
        //Operadores Logicos
        public void logicos() {

            int x = 5;
            int y = 3;
            Console.WriteLine($"Operador Logico AND && {x>4 && y<4}");
            Console.WriteLine($"Operador Logico OR || {x > 4 || y < 1}");
            Console.WriteLine($"Operador Logico NOT ! {!(x > 4 && y < 4)}");
            Console.WriteLine();

            int a = 1; int b= 2;
            if (a==1)
            {
                Console.WriteLine($"ejemplo condicinal if {a}");
            }
            else
            {
                Console.WriteLine($"Ejemplo condicional else {b}");
            }
            Console.WriteLine();
            int diaSemana = 6;
            switch (diaSemana)
            {
                case 0: Console.WriteLine("Esto es un switch");
                break;
                case 1: 
                    Console.WriteLine("Lunes");
                break;
                case 2:
                    Console.WriteLine("Martes");
                    break;
                case 3:
                    Console.WriteLine("Miercoles");
                    break;
                case 4: 
                    Console.WriteLine("Jueves");
                    break;
                case 5:
                    Console.WriteLine("Viernes");
                    break;
                 case 6:
                    Console.WriteLine("Sabado");
                    break;
            }
            Console.WriteLine("Esto es una excepcion ");
            try
            {
                int[] myNumbers = { 1, 2, 3 };
                Console.WriteLine(myNumbers[10]);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }


        }
        public void iteradores() { 

            for (int i = 0; i < 5; i++) {
                Console.WriteLine($"Esto es un bucle for: {i}");
            }
            Console.WriteLine("");
            int f = 0;
            while (f<5) {
                
                Console.WriteLine($"Esto es un bucle While {f}");
                f++;
            }
            Console.WriteLine();    
            int g = 0;
            do { 
                Console.WriteLine($"Esto es un Bucle Do-While {g}");
                g++;
            } while (g<5);

            Console.WriteLine();

            string[] carros = {"mazda","renault","Chevrolet","BMW","Mercedes" };
            foreach (var car in carros)
            {
                Console.WriteLine($"Este es el bluche ForEach {car}");
            }
            
        }
        public void extra() {

            for (int i = 10; i <= 55; i++)
            {
                if (i%2==0 && i !=16 && i%3 !=0)
                {
                    Console.WriteLine($"Los numeros pares: {i}");
                }
            }
        
        }
    }
}
