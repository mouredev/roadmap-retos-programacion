//Author: Sandra Baigorri Saez
using System;
using System.Security.Cryptography;


namespace _01OperadoresyEsctructurasDeControl
{
    internal class Program
    {
        static void Main(string[] args)
        {      
            /* Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
             *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
             *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)*/
            int num = 5, num2 = 3;
            // ------------------------- ARITMETICOS -------------------------
            int suma = num + 1; //sumo 1 a un num
            Console.WriteLine("La suma es: " + suma);
            int resta = num - 1; //resto 1 a un num
            Console.WriteLine("La resta es: " + resta);
            int division = num / 2; //divido num entre 2
            Console.WriteLine("La division es: " + division);
            int multiplicacion = num * 2; //multiplico num por 2
            Console.WriteLine("La multiplicacion es: " + multiplicacion);
            int resto = num % 2; //% nos da el resto de dividir num entre 2
            Console.WriteLine("El resto es: " + resto);

            // ------------------------- LOGICOS -------------------------
            Console.WriteLine(num == num2 && num == num2);//&& se tienen que dar las dos condiciones de los lados para que sea verdadero, con que una no se cumpla es falso

            Console.WriteLine(num == num2 || num == num2);//|| si se cumple una de las dos condiciones de los lados sedría verdadero, cuando no se cumple ninguna de las condiciones es falso
            Console.WriteLine(!(num == num2));//si num es igual a num2 dara falso porque ! niega la condicion verdadero y se convierte en falso
                                              //si num es distinto a num2 dara verdadero porque ! niega la condicion false y se convierte en verdadero

            // ------------------------- COMPARACION -------------------------
            Console.WriteLine(7 < 5);   // MENOR QUE: output: False
            Console.WriteLine(7 > 5);   // MAYOR QUE: output: True
            Console.WriteLine(0 <= 5);   // MENOR O IGUAL: output: True
            Console.WriteLine(0 >= 5);   // MAYOR O IGUAL: output: False
            Console.WriteLine(0 == 5);   // IGUAL: output: False
            Console.WriteLine(0 != 5);   // DISTINTO: output: True

            // ------------------------- ASIGNACION -------------------------
            Console.WriteLine(num = num2); //asigno a num el valor de num3
            Console.WriteLine(num++); //sumo 1 a un número o num-; le resto 1
            Console.WriteLine(num -= num2); // le resto num2 a num y con la suma ( num += num2), multiplicación ( num *= num2), division ( num /= num2) y resto ( num %= num2)


            // ------------------------- BITS -------------------------
            uint a = 0b_0000_1111_0000_1111_0000_1111_0000_1100;
            uint b = ~a;
            Console.WriteLine(b = a << 2);
            Console.WriteLine(b = a >> 2);
            Console.WriteLine(b = a & b);
            Console.WriteLine(b = a ^ b);
            Console.WriteLine(b = a | b);


            /*Utilizando las operaciones con operadores que tú quieras, crea ejemplos
             *que representen todos los tipos de estructuras de control que existan
             *en tu lenguaje:
             *Condicionales, iterativas, excepciones...*/
            if(num == num2) 
            { 
                Console.WriteLine("Son iguales");
            }
            else 
            {
                Console.WriteLine("Son distintos");
            }
            while(num < 7)
            {
                Console.WriteLine("El numero del while es: " + num);
                num++;
            }

            do 
            {
                Console.WriteLine("El numero del do while es: " + num);
                num--;
            } 
            while(num!=0);

            switch(num) 
            { 
                case 0:
                    Console.WriteLine("Número del swith es: " + num);
                    break;
                case 1:
                    Console.WriteLine("Número del swith es: " + num);
                    break;
                case 2:
                    Console.WriteLine("Número del swith es: " + num);
                    break;
                default:
                    Console.WriteLine("default");
                    break;
            }

            
            int[] numeros = new int[5];
            for (int i = 0; i <= numeros.Length - 1; i++)
            {
                numeros[i] = i;
            }
            foreach (int i in numeros)
            {
                Console.WriteLine("Números foreach: " + numeros[i]);
            }


            /*DIFICULTAD EXTRA(opcional):
             *Crea un programa que imprima por consola todos los números comprendidos
             *entre 10 y 55(incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/
            for (int i = 10; i <= 55; i++)
            {
                if(i%2 == 0)
                {
                    if((i != 16) && (i%3!=0))
                    {
                        Console.WriteLine("Número: " + i);
                    }                    
                }                
            }
        }
    }
}
