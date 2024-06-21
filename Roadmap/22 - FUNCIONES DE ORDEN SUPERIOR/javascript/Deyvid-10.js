// Funciones de orden superior

// #1

function funcion1(num, funcion2) {
    console.log(num + funcion2(2));
}

function funcion2(num2)
{
    return num2
}

funcion1(2, funcion2)

// #2

let numero = [1,2,3,4,5]

let filtro = numero.filter(function(num){
    return num % 2 == 0 
})

console.log(filtro);

// #3

function funcion3(funcion4)
{
    return funcion4()
}

function funcion4()
{
    console.log("Soy la funcion 4");
}

funcion3(funcion4)


// DIFICULTAD EXTRA

let estudiantes = [["Deyvid Marmolejo", "Daniel Amparo", "Hector Sanchez"], 
                ["1997-05-26", "1996-08-16", "1998-11-25"], 
                [{"espanol": 9, "matematicas": 9.5, "biologia": 9, "historia": 9},
                {"espanol": 8, "matematicas": 7, "biologia": 9, "historia": 9},
                {"espanol": 10, "matematicas": 8, "biologia": 9, "historia": 8}
                ]]

function promedio(listaEstudiantes)
{
    return [listaEstudiantes[0], listaEstudiantes[2].map(num =>
        Object.values(num).reduce((acumulado, suma)=>acumulado+suma, 0)/Object.values(num).length
    )]
}

function mejoresEstudiantes(listaEstudiantes, promedio)
{
    let resumenPromedio = promedio(listaEstudiantes)
    let mejoresEstudiantes = []

    for(let i=0; i<resumenPromedio[1].length; i++)
    {
        if(resumenPromedio[1][i] >= 9)
        {
            mejoresEstudiantes.push(resumenPromedio[0][i])
        }
    }

    return mejoresEstudiantes

}

function nacimiento(listaEstudiantes)
{

    return listaEstudiantes[1].sort((x, y) =>{
        let fechaX = new Date(x)
        let fechaY = new Date(y)

        return fechaX - fechaY
    })
}

function mayor(listaEstudiantes)
{
    return [listaEstudiantes[0], listaEstudiantes[2].map(num => Object.values(num).sort((x, y) => x-y)[listaEstudiantes[0].length])]     
}

console.log(promedio(estudiantes));
console.log(mejoresEstudiantes(estudiantes , promedio));
console.log(nacimiento(estudiantes));
console.log(mayor(estudiantes));
