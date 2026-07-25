class Timer
{
    private DateTime _targetDate;
    private Thread _thread;

    public Timer(DateTime targetDate)
    {
        _targetDate = targetDate.ToUniversalTime();
        _thread = new Thread(CountDown);
    }
    public void Start()
    {
        _thread.Start();
    }
    void CountDown()
    {
        bool reached = false;
        var currentDate = DateTime.UtcNow;
        do
        {
            var remainingTime = _targetDate.Subtract(currentDate);
            Console.Clear();
            if (remainingTime.TotalSeconds <= 0)
                reached = true;
            else
            {
                int days = remainingTime.Days;
                int hours = remainingTime.Hours;
                int minutes = remainingTime.Minutes;
                int seconds = remainingTime.Seconds;


                Console.WriteLine("---Tiempo Restante---");
                Console.WriteLine($"{days} días, {hours} horas, {minutes} minutos, {seconds} segundos");

                Thread.Sleep(1000);
                currentDate = DateTime.UtcNow;
            }

        } while (!reached);
        Console.WriteLine("¡Cuenta atrás finalizada!");
    }

}
class Program
{
    static void Main(string[] args)
    {
        Timer timer = new Timer(new DateTime(2024, 12, 20, 13, 1, 00).ToUniversalTime());
        timer.Start();
    }
    
}