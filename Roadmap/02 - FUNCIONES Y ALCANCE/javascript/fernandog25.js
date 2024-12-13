//Función sin parámetros ni retorno
function texto()
{
    console.log("Hola mundo");
}

texto();

//Función con parámetros
function suma(num1,num2)
{
    console.log(num1 + num2);
}

suma(2,3);

//Función con parámetro y retorno
function cuadrado(x)
{
    return x*x;
}

console.log(cuadrado(4));

//Función dentro de otra función
{
    function cubo(f,m)
    {
        resultado = [];
        for(var i=0; i<m.length; i++)
            resultado[i] = f(m[i]);
        return resultado;
    }

    const f = function (num)
    {
        return num*num*num;
    }

    var matriz = [1,2,3,4]
    console.log(cubo(f, matriz));
}

//Ejemplo de función creada por el lenguaje

var aleatorio = Math.random(); // Math.random es una función que genera un número aleatorio entre 0 y 1
console.log(aleatorio);

//Variable global y local

var x = 8;

function numero()
{
    var x = 6;

    console.log(x); //Muestra el valor de la variable local
}

console.log(x); //Muestra el valor de la variable global
numero();

/*DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos. */

function lista(multiplo3, multiplo5)
{
    for(var i=1; i<101; i++)
        {
            if(i % 3 == 0 && i % 5 == 0)
                console.log(multiplo3 + " y " + multiplo5);
            else if(i % 3 == 0)
                console.log(multiplo3);
            else if(i % 5 == 0)
                console.log(multiplo5);
            else
            console.log(i);
        }
}

lista("múltiplo de 3", "múltiplo de 5");