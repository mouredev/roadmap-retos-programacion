/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* ITERACIONES
------------------------------------------
* EJERCICIO #1:
* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
* números del 1 al 10 mediante iteración.
*
* EJERCICIO #2:
* Escribe el mayor número de mecanismos que posea tu lenguaje
* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/
//_____________________________
Console.WriteLine("(1). for");
for (int n = 1; n <= 10; n++) {
    Console.WriteLine(n);
}

//_____________________________
Console.WriteLine("\n(2). while");
int num = 1;
while (num <= 10) {
    Console.WriteLine(num);
    num++;
}

//_____________________________
Console.WriteLine("\n(3). foreach");
foreach (int n in Enumerable.Range(1, 10)) {
    Console.WriteLine(n);
}

//_____________________________
Console.WriteLine("\n(4). do-while");
int nu = 1;
do {
    Console.WriteLine(nu);
    nu++;
} while (nu <= 10);

//_____________________________
Console.WriteLine("\n(5). Iteradores yield");
static IEnumerable<int> Nums() {
    for (int n = 1; n <= 10; n++) {
        yield return n;
    }
}

foreach (var n in Nums()) {
    Console.WriteLine(n);
}

