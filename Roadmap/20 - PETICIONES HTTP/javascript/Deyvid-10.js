// Peticiones HTTP

fetch("https://www.youtube.com/")
.then(salida => {
    console.log(`Codigo estado HTTP: ${salida.status}`)
    fetch("https://www.youtube.com/")
    .then(res => res.text())
    .then(salida => {
    console.log(`Contenido:`)
    console.log(salida);
    })
    .catch(error => console.error(error))
})
.catch(error => console.error(error))

// DIFICULTAD EXTRA

function pokemon(id_Nombre)
{
    fetch(`https://pokeapi.co/api/v2/pokemon/${id_Nombre}`)
    .then(res => res.json())
    .then(salida => {
        console.log(`Nombre: ${salida.forms[0].name}`);
        console.log(`Id: ${salida.id}`);
        console.log(`Altura: ${salida.height}`);
        console.log(`Peso: ${salida.weight} libras`);

        let tipos = []

        for (let t of salida.types) 
        {
            tipos.push(t.type.name)
        }

        console.log(`Tipo(s): ${tipos}`);

        let juegos = []

        for (let g of salida.game_indices) 
        {
            juegos.push(`Pokemon ${g.version.name}`)
        }

        console.log(`Juegos: ${juegos}`);
    })
    .catch(error => console.error(error))

    fetch(`https://pokeapi.co/api/v2/pokemon-species/${id_Nombre}`)
    .then(res => res.json())
    .then(salida => {
        fetch(salida.evolution_chain.url)
        .then(res => res.json())
        .then(salida => {
            console.log("Cadena de evolucion:");
            console.log("-" + salida.chain.species.name);

            let cadenaEvolutiva = salida.chain

           function evolucion(cadena)
           {
                if("evolves_to" in cadena && cadena.evolves_to.length != 0)
                {   
                    for (let c of cadena.evolves_to) 
                    {
                        console.log("-" + c.species.name);
                        evolucion(c)
                    }
                }
           }

           evolucion(cadenaEvolutiva)

        })
        .catch(error => console.error(error))
    })
    .catch(error => console.error(error))
}

// pokemon("charmander")
// pokemon("eevee")
// pokemon("poliwhirl")
// pokemon("wurmple")
// pokemon("ralts")
// pokemon("slowpoke")