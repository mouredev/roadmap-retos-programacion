namespace CSharpPractica1
{
    class Practica1
    {
        static void Main(String[] args)
        {
            /*
            Operadores
            */

            // Operadores aritméticos
            Console.WriteLine($"suma: 30 + 23 = {30 + 23}");
            Console.WriteLine($"resta: 30 - 23 = {30 - 23}");
            Console.WriteLine($"multiplicación: 30 * 23 = {30 * 23}");
            Console.WriteLine($"división: 30 / 23 = {30 / 23}");
            Console.WriteLine($"residuo: 30 % 23 = {30 % 23}");
            Console.WriteLine($"exponente: 30 ^ 23 = {Math.Pow(30, 23)}");
            
            // Operadores de comparación
            Console.WriteLine($"Igualdad: 30 == 23 = {30 == 23}");
            Console.WriteLine($"Desigualdad: 30 != 23 = {30 != 23}");
            Console.WriteLine($"Mayor que: 30 > 23 = {30 > 23}");
            Console.WriteLine($"Menor que: 30 < 23 = {30 < 23}");
            Console.WriteLine($"Mayor o igual que: 30 >= 23 = {30 >= 23}");
            Console.WriteLine($"Menor o igual que: 30 <= 23 = {30 <= 23}");

            // Operadores lógicos
            Console.WriteLine($"And: 27 + 3 == 30 && 33 - 3 == 30 = {(27 + 3 == 30) && (33 - 3 == 30)}");
            Console.WriteLine($"Or: 27 + 3 == 11 || 33 - 3 == 30 = {(27 + 3 == 30) || (33 - 3 == 30)}");
            Console.WriteLine($"Not: !(27 + 3 == 30) = {!(27 + 3 == 30)}");
            
            // Operadores de asignación
            int myInt = 30;
            Console.WriteLine(myInt);
            myInt += 1; // suma y asignación
            Console.WriteLine(myInt); 
            myInt -= 1; // resta y asignación
            Console.WriteLine(myInt);
            myInt *= 2; // multiplicación y asignación
            Console.WriteLine(myInt);
            myInt /= 2; // división y asignación
            Console.WriteLine(myInt);
            myInt %= 4; // módulo y asignación
            Console.WriteLine(myInt);

            // Operadores de identidad
            int myInt2 = myInt;
            Console.WriteLine($"myInt == myInt2 = {myInt == myInt2}");
            Console.WriteLine($"myInt != myInt2 = {myInt != myInt2}");

            // Operadores de pertenencia
            Console.WriteLine($"Curry pertenece a Chef Curry = {"Chef Curry".Contains("Curry")}");
            Console.WriteLine($"Kyrie no pertenece a Chef Curry = {"Chef Curry".Contains("Kyrie") == false}");

            // Operadores de bit 
            int myA = 10; // 1010
            int myB = 3; // 0011
            Console.WriteLine($"And: myA & myB = {myA & myB}"); // 0010
            Console.WriteLine($"Or: myA | myB = {myA | myB}"); // 1011
            Console.WriteLine($"Xor: myA ^ myB = {myA ^ myB}"); // 1001
            Console.WriteLine($"Not: ~myA = {~myA}"); // 0101
            Console.WriteLine($"Dezplazamiento izquierdo: myA << 2 = {myA << 2}"); // 10100
            Console.WriteLine($"Dezplazamiento derecho: myA >> 2 = {myA >> 2}"); // 0101
 
            /*
            Estructuras de control
            */

            // Condicionales
            
            String myString = "Curry";

            if (myString == "Curry")
            {
                Console.WriteLine("myString es igual a Curry");
            }

            else if (myString == "Kyrie")
            {
                Console.WriteLine("myString es igual a Kyrie");
            }

            else 
            {
                Console.WriteLine("myString no es igual a Curry ni a Kyrie");
            }

            // Iterativa

            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine(i);
            }

            int j = 0;
            while (j <= 10)
            {
                Console.WriteLine(j);
                j++;
            }

            foreach (char c in myString)
            {
                // Console.WriteLine(c);
            }   

            // manejo de excepciones

            try
            {
                int myInt3 = 30;
                int myInt4 = 0;
                Console.WriteLine(myInt3 / myInt4);
            }

            catch (Exception )
            {
                Console.WriteLine("Ocurrió un error");
            }

            finally
            {
                Console.WriteLine("Se ejecutó el bloque finally");
            }

            /*
            Extra
            */

            for (int i = 10; i <= 55 ; i++)
            {
                if ((i % 2 == 0 || i == 55) && (i % 3 != 0 && i != 16))
                {
                    Console.WriteLine(i);
                }
            }

        }
    }
}
