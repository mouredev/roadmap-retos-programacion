/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
47  CALENDARIO DE ADVIENTO
------------------------------------

 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 * 
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño 
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *   
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
*/

string[,] mtx = new string[4, 6];
for (int i = 0; i < 4; i++)
{
    for (int j = 0; j < 6; j++)
    {
        mtx[i, j] = $"*{(i * 6 + j + 1):00}*";
    }
}

string ln = string.Join(" ", Enumerable.Repeat("****", 6));

while (true)
{
    for (int i = 0; i < 4; i++)
    {
        Console.WriteLine(ln);
        int currentRow = i;

        for (int j = 0; j < 6; j++)
        {
            Console.Write(mtx[currentRow, j] + " ");
        }
        Console.WriteLine("\n" + ln + "\n");
    }

    Console.Write("Día a descubrir: ");
    string? day = Console.ReadLine();

    if (!int.TryParse(day, out int dayInt))
    {
        Console.WriteLine("Entrada inválida. Debe ser un número.");
        continue;
    }

    if (dayInt < 1 || dayInt > 24)
    {
        Console.WriteLine("Día inválido, debe ser entre 1 y 24.");
        continue;
    }

    int r = (dayInt - 1) / 6;
    int c = (dayInt - 1) % 6;

    if (mtx[r, c] == "****")
    {
        Console.WriteLine($"El día {day} ya está descubierto.");
        continue;
    }

    mtx[r, c] = "****";
}
