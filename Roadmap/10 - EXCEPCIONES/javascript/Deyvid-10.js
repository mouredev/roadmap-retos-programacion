// Excepciones

try
{
    f()
}
catch(err)
{
    console.error(err.name, ":", err.message);
}
finally
{
    console.log("Se manejo correctamente");
}

console.log("El programa no se detuvo");