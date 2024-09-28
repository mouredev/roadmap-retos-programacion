// Pruebas unitarias

function suma(num1, num2)
{
    return num1 + num2
}

function test()
{
    let comprobar = suma(1, 2)

    if(typeof(comprobar) == "number")
    {
        console.log("La funcion se ejecuto correctamente");
    }
    else
    {
        console.log("La funcion no se ejecuto correctamente");
    }
}

test()

// DIFICULTAD EXTRA

let datos = {name: "Deyvid", age: 25, birth_date: "06-12-98", programming_languages: ['JavaScript', 'Python']}

function testCampos()
{
    let arrayTest = [ 'name', 'age', 'birth_date', 'programming_languages' ]

    for (let i = 0; i < Object.keys(datos).length; i++) 
    {
        if(Object.keys(datos)[i] == arrayTest[i])
        {
            console.log("test aprobado");
        }
    }
}

testCampos()

function testDatos()
{
    let arrayTest = [ 'Deyvid', 25, '06-12-98', ['JavaScript', 'Python'] ]
    
    for (let i = 0; i < Object.values(datos).length; i++) 
    {
        if(Object.values(datos)[i] == arrayTest[i])
        {
            console.log("test aprobado");
        }
        else if(typeof(Object.values(datos)[i]) == 'object')
        {
            for (let a = 0; a < Object.values(datos)[i].length; a++) 
            {
                if(Object.values(datos)[i][a] == arrayTest[i][a])
                {
                    console.log("test aprobado");
                }
            }
        }
    }
}

testDatos()