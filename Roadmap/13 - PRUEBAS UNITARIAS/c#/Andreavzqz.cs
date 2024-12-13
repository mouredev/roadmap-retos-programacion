using System;
using System.Collections.Generic;
using Xunit;

namespace EjercicioSuma
{
    public class Program
    {
        public static int sumar(int a, int b)
        {
            return a + b; 
        }

        public static Dictionary<string, object> CrearDiccionario()
        {
            return new Dictionary<string, object>
            {
                { "name", "Andrea" },
                { "age", 30 },
                {"birth_date", new DateTime(1994, 5, 13)},
                {"programming_languages", new List<string>{"C#", "JavaScript", "Python"}}
            };
        }
    }

    public class PruebasUnitarias
    {
        [Fact]
        public void TestSumaCorrecta()
        {
            int resultado = Program.sumar(3, 4);
            Assert.Equal(7, resultado);
        }

        [Fact]
        public void TestDiccionarioCamposExisten()
        {
            var diccionario = Program.CrearDiccionario();

            Assert.True(diccionario.ContainsKey("name"));
            Assert.True(diccionario.ContainsKey("age"));
            Assert.True(diccionario.ContainsKey("birth_date"));
            Assert.True(diccionario.ContainsKey("programming_languages"));
        }

        [Fact]
        public void TestDiccionarioCamposCorrectos()
        {
            
            var diccionario = Program.CrearDiccionario();

            Assert.Equal("Andrea", diccionario["name"]);
            Assert.Equal(30, diccionario["age"]);
            Assert.Equal(new DateTime(1994, 5, 13), diccionario["birth_date"]);
            Assert.Equal(new List<string> {"C#", "JavaScrip", "Python" }, diccionario["programming_languages"]);
        }
    }

  /*

-Explicación

Función Sumar:
Esta función toma dos números enteros como argumentos y retorna su suma.

Función CrearDiccionario:
Crea y retorna un diccionario con claves y valores que incluyen nombre, edad, fecha de nacimiento y una lista de lenguajes de programación.

Clase PruebasUnitarias:
TestSumaCorrecta: Verifica que la función Sumar retorna el resultado correcto al sumar dos números.
TestDiccionarioCamposExisten: Verifica que el diccionario creado por CrearDiccionario contiene todas las claves esperadas.
TestDiccionarioDatosCorrectos: Verifica que los valores del diccionario coinciden con los datos esperados.

*/
}
