namespace exs44;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
44 CUENTA ATRÁS MOUREDEV PRO
------------------------------------

* EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente.
*/

using System;
using System.Threading;

class ReverseTimer
{
    private readonly DateTime _endDate;
    private readonly Thread _countdownThread;
    private volatile bool _isRunning = true;

    public ReverseTimer(string endDate)
    {
        _endDate = DateTime.Parse(endDate).ToUniversalTime();
        _countdownThread = new Thread(RunCountdown);
    }

    private TimeSpan TimeRemaining 
        => _endDate > DateTime.UtcNow ? _endDate - DateTime.UtcNow : TimeSpan.Zero;

    private void RunCountdown()
    {
        while (_isRunning && TimeRemaining > TimeSpan.Zero)
        {
            Console.Clear();
            Console.WriteLine("Tiempo restante:");
            Console.WriteLine(FormatTimeRemaining());

            Thread.Sleep(1000);
        }

        if (TimeRemaining <= TimeSpan.Zero)
        {
            Console.WriteLine("¡Cuenta atrás finalizada!");
        }
    }

    private string FormatTimeRemaining()
    {
        var delta = TimeRemaining;
        return $"{delta.Days} dias, {delta.Hours} horas, {delta.Minutes} minutos, {delta.Seconds} segundos.";
    }

    public void Start()
    {
        _countdownThread.Start();
    }

    public void Stop()
    {
        _isRunning = false;
        _countdownThread.Join();
    }

    public static void Main()
    {
        var endDate = "2024-12-31T23:59:59.999999";
        var timer = new ReverseTimer(endDate);
        
        timer.Start();
        //timer.Stop();
    }
}
