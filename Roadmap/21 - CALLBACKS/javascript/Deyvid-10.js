// callbacks

function tomarDatos(nombre, apellido, edad)
{
    console.log("Nombre: " + nombre);
    console.log("Apellido: " + apellido);
    console.log("Edad: " + edad);
}

function esperarDatos(callback)
{
    callback("Deyvid", "Marmolejo", 25)
}

esperarDatos(tomarDatos)


// DIFICULTAD EXTRA

async function procesarPedido(plato, callbackConfirmacion, callbackListo, callbackEntrega)
{
    await callbackConfirmacion(plato)
    await callbackListo(plato)
    await callbackEntrega(plato)
}

function confirmacion(plato)
{
    return new Promise (resolver => setTimeout(()=>{
    console.log(`El pedido del plato ${plato} esta en prepraracion`)
    resolver()
    } , Math.ceil(Math.random() * 10000)))
}

function listo(plato)
{
    return new Promise (resolver => setTimeout(()=>{
    console.log(`El plato ${plato} esta listo para entregar`)
    resolver()
    } , Math.ceil(Math.random() * 10000)))
}

function entregado(plato)
{
    return new Promise (resolver => setTimeout(()=>{
    console.log(`El plato ${plato} fue entregado`)
    resolver()
    } , Math.ceil(Math.random() * 10000)))
}

procesarPedido("Sopa", confirmacion, listo, entregado)

