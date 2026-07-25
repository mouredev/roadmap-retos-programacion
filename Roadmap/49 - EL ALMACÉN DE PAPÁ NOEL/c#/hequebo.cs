class Program
{
    static void Main(string[] args)
    {
        Random random = new Random();
        List<char> chars = new List<char>{ 'a', 'b', 'c', '1', '2', '3' };
        var secretPassword = string.Join("", chars.OrderBy(c =>  random.Next()).ToList().Slice(0, 4));

        int attempts = 0;

        while (attempts < 10)
        {
            Console.WriteLine($"----INTENTO {attempts + 1}----");
            Console.WriteLine("Ingresa la contraseña");
            string? password = Console.ReadLine();
            attempts++;
            if (string.IsNullOrEmpty(password))
            {
                Console.WriteLine("No se ingreso ninguna contraseña...");
                continue;
            }
            if (password.Length != 4)
            {
                Console.WriteLine("La contraseña debe de ser de 4 caracteres...");
                continue;
            }
            if (password.Where(p => chars.Contains(p)).Count() != 4)
            {
                Console.WriteLine($"La contraseña solo permite los siguientes carácters: {string.Join(",", chars)}");
                continue;
            }
            if (password == secretPassword)
            {
                Console.WriteLine("¡Contraseña correcta!");
                break;
            }
            else
            {
                foreach ((char c, int index) in password.Select((item, index) => (item, index)))
                {
                    if (c == secretPassword[index])
                        Console.WriteLine($"{c}: Correcto.");
                    else if (secretPassword.Contains(c))
                        Console.WriteLine($"{c}: Se encuentra en la contraseña.");
                    else
                        Console.WriteLine($"{c}: Incorecto");
                }
            }
        }
        if (attempts >= 10)
            Console.WriteLine("Se han fallado los 10 intentos");
    }
}