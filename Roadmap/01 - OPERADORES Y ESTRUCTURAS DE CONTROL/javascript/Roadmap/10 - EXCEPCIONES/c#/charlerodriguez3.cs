/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 */

 

Console.WriteLine("Vamos a dividir");
Console.WriteLine("digita un numero");
int num = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("digita otro numero");
int num2 = Convert.ToInt32(Console.ReadLine());

try
{
    Console.WriteLine("La division es" + num / num2);

}
catch(DivideByZeroException ex)
{
    Console.WriteLine("No puedes dividir entre cero: " + ex.Message);
}

Console.WriteLine("Volvemos a dividir (por defecto 1), Resultado:" + num / 1);




try
{
    processParametros(new List<int> {-1,1,2,7,4,5,12});
}
catch(InvalidDataException ex)
{
    Console.WriteLine("El cuarto elemento no puede tener valor de 3: " + ex.Message);
}catch(DivideByZeroException ex)
{
    Console.WriteLine("No puede dividir entre cero: " + ex.Message);
}catch(IndexOutOfRangeException ex)
{
    Console.WriteLine("No puede acceder a una posicion que no existe dentro de la lista: " + ex.Message);
}catch(Exception ex)
{
    Console.WriteLine("Ha ocurrido un error inesperado: " + ex.Message);
}
finally
{
    Console.WriteLine("Fin del programa");
}


static void processParametros(List<int> numeros)
{
    if (numeros[3] == 3)
    {
        throw new InvalidDataException();
    }else if (numeros[0] == 0)
    {
        throw new DivideByZeroException();
    }else if (numeros[6] == 10)
    {
        throw new IndexOutOfRangeException();
    }

    Console.WriteLine(numeros[3]);
    Console.WriteLine(numeros[4] /numeros[0]);
    Console.WriteLine(numeros[1]+numeros[3]);

}