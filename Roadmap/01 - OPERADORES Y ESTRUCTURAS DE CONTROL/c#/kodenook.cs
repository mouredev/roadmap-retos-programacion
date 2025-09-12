/*
    Arithmetic Operators
*/

Console.WriteLine("Arithmetic Operators");
Console.WriteLine($"2 + 2 = {2 + 2}");
Console.WriteLine($"2 - 2 = {2 - 2}");
Console.WriteLine($"2 * 2 = {2 * 2}");
Console.WriteLine($"2 / 2 = {2 / 2}");
Console.WriteLine($"2 % 2 = {2 % 2}");

/*
        Bitwise Operators
    */

Console.WriteLine($"Bitwise Operators");
Console.WriteLine($"&: 5 & 2 = {5 & 2}");
Console.WriteLine($"|: 5 | 2 = {5 | 2}");
Console.WriteLine($"^: 5 ^ 2 = {5 ^ 2}");
Console.WriteLine($">>: 5 >> 2 = {5 >> 2}");
Console.WriteLine($"<<: 5 << 2 = {5 << 2}");

/*
    Assignment Operators
*/

Console.WriteLine("Assignment Operators");
Console.WriteLine("x = 5");
Console.WriteLine("x += 5, x = x + 5");
Console.WriteLine("x -= 5, x = x - 5");
Console.WriteLine("x *= 5, x = x * 5");
Console.WriteLine("x /= 5, x = x / 5");
Console.WriteLine("x ~/= 5, x = x ~/ 5");
Console.WriteLine("x %= 5, x = x % 5");
Console.WriteLine("x &= 5, x = x & 5");
Console.WriteLine("x |= 5, x = x | 5");
Console.WriteLine("x ^= 5, x = x ^ 5");
Console.WriteLine("x >>= 5, x = x >> 5");
Console.WriteLine("x <<= 5, x = x << 5");
Console.WriteLine("x >>>= 5, x = x >>> 5");

/*
    Comparison Operators
*/

Console.WriteLine("Comparison Operators");
Console.WriteLine($"Equal to 4 == 5, {4 == 5}");
Console.WriteLine($"Not Equal to 4 != 5, {4 != 5}");
Console.WriteLine($"Grater Than 4 > 5, {4 > 5}");
Console.WriteLine($"Less Than 4 < 5, {4 <= 5}");
Console.WriteLine($"Grater Than Or Equal to 4 >= 5, {4 >= 5}");
Console.WriteLine($"Less Than Or Equal to 4 <= 5, {4 <= 5}");

/*
    Logical Operators
*/

Console.WriteLine("Logical Operators");
Console.WriteLine($"&&, 3 < 5 && 3 < 10, {3 < 5 && 3 < 10}");
Console.WriteLine($"||, 3 < 5 || 3 < 10, {3 < 5 || 3 < 10}");
Console.WriteLine($"!, !(4 < 5), {!(4 < 5)}");

/*
    If
*/

int time = 22;
if (time < 10)
{
    Console.WriteLine("Good morning.");
}
else if (time < 20)
{
    Console.WriteLine("Good day.");
}
else
{
    Console.WriteLine("Good evening.");
}

/*
    Switch
*/

int day = 4;
switch (day)
{
    case 6:
        Console.WriteLine("Today is Saturday.");
        break;
    case 7:
        Console.WriteLine("Today is Sunday.");
        break;
    default:
        Console.WriteLine("Looking forward to the Weekend.");
        break;
}

/*
    While
*/

int i = 0;
while (i < 5)
{
    Console.WriteLine(i);
    i++;
}

/*
    Do While
*/

do
{
    Console.WriteLine(i);
    i--;
}
while (i > 0);

/*
    For
*/

for (int j = 0; j < 5; j++)
{
    Console.WriteLine(j);
}

string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
foreach (string l in cars)
{
    Console.WriteLine(l);
}

/*
    Exercise
*/

for (int e = 10; e < 56; e += 2)
{
    if (e % 3 != 0 || e == 16)
    {
        continue;
    }
    Console.WriteLine(e);
}