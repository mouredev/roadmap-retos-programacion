/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */
Avion avion1 = new();

//Instanciado por el constructor
avion1.DescripcionAeronave();

//Llenado de atributos

avion1.NroMatricula = "HKT-243KD";
avion1.NumeroMotores = 2;
avion1.TipoMotor = "Turbina";

avion1.DescripcionAeronave();




public class Avion
{
    public int NumeroMotores { get; set; }
    public string NroMatricula{ get; set; }
    public string TipoMotor {  get; set; }

    public Avion()
    {
        NumeroMotores = 1;
        NroMatricula = String.Empty;
        TipoMotor = "Turbo-Helice";
    }

    public void DescripcionAeronave()
    {
        Console.WriteLine("El avion 1 tiene las siguientes caracteristicas");
        Console.WriteLine($"Numero de motores: {NumeroMotores}, Numero de matricula: {NroMatricula} y Tipo de motor es: {TipoMotor} \n");
    }

}