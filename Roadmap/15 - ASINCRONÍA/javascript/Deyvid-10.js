// asincronia

async function asincrona(nombre, tiempo)
{
    console.log(`Inicio: ${new Date().toLocaleTimeString()}`);
    console.log(`Nombre: ${nombre}`);
    console.log(`Duracion: ${tiempo} segundos`);
    let esperar =  await new Promise(texto => setTimeout(() => {texto(nombre)}, tiempo * 1000))
    console.log(esperar);
    console.log(`Fin: ${new Date().toLocaleTimeString()}`);
}

asincrona("Asincrono", 2)

// DIFICULTAD EXTRA

async function extra()
{
    await Promise.all([asincrona("C", 3), asincrona("B", 2), asincrona("A", 1)])
    await asincrona("D", 1)
}

extra()


  