// funciones básicas
function noRetotnoNiParametro()
{
    console.log("Esta funcion no tiene parámetros ni retorna nada")
}

noRetotnoNiParametro()

function conParemetros(parametro, parametro2)
{
    console.log("Esta funcion tiene el parametro ", parametro, " y este es otro parametro ", parametro2);
}

conParemetros("parametro no. 1", "parametro no. 2")

function conRetorno()
{
    return "Esta funcion retorna este mensaje"
}

console.log(conRetorno());

// funcion dentro de funcion
function padre()
{
    function hijo()
    {
        console.log("Esta funcion esta dentro de otra funcion");
    }
    hijo()
}

padre()

// Funciones ya creadas

let texto = "One Piece"
let decimal = 5.5555
console.log(decimal.toFixed(2));
console.log(Math.random());
console.log(texto.split(" "));

// variable LOCAL y GLOBAL
function local()
{
    let varLocal = "Esta variable solo se puede usar dentro de esta funcion"
    console.log(varLocal);
}

local()

let varGlobal 
function global()
{
    varGlobal = "Esta variable se puede usar en cualquier parte del codigo"
}

global()
console.log(varGlobal);

// DIFICULTAD EXTRA
function extra(texto, texto2)
{
    let contador = 0

    for(let i=1; i<=20; i++)
    {
        if(i%3 == 0 && i%5 == 0)
        {
            console.log(texto + " y "+ texto2);
        }
        else if (i%3 == 0) 
        {
            console.log(texto);
        }
        else if(i%5 == 0)
        {
            console.log(texto2);
        }
        else
        {
            console.log(i);
            contador++
        }
    }
    return contador
}

let funcionExtra = extra("Los gatos son felinos", "Los perros son caninos")

console.log("La funcion retorna: ", funcionExtra);