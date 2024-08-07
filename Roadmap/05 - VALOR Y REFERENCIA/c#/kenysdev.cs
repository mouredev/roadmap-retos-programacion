/* ╔══════════════════════════════════════╗
   ║ Autor:  Kenys Alvarado               ║
   ║ GitHub: https://github.com/Kenysdev  ║
   ║ 2024 -  C#                           ║
   ╚══════════════════════════════════════╝
   ----------------------------------------
   # VALOR Y REFERENCIA
   ----------------------------------------
// Asignación de variables "por valor"
   - se asigna el valor real de la variable a otra variable.
   - los cambios en una variable no afectarán a la otra. */

Console.WriteLine("Por valor");
int int1 = 111;
bool bool1 = false;
string str1 = "Ben";

// Asignación
int int2 = int1;
bool bool2 = bool1;
string str2 = str1;

// Cambio
int1 = 777;
bool1 = true;
str1 = "zoe";

// Las variables no fueron afectadas.
Console.WriteLine($"{int2} - {bool2} - {str2}");

// ejemplo con una función:
void fun_v(int int3, bool bool3, string str3)
{
    int3 = 333;
    bool3 = false;
    str3 = "Zoe";
}
// paso por valor
fun_v(int1, bool1, str1);
// no afectadas por los cambios en la función.
Console.WriteLine($"{int2} - {bool2} - {str2}");

/* _________________________________________
   Asignación de variables "por referencia"
   - se asigna la referencia o dirección de memoria
     de la variable a otra variable.
   - Los cambios en una variable pueden afectar a la otra. */
Console.WriteLine("Por referencia");
var list1 = new List<string> {"Bob", "Zoe", "Dan"};
var dic1 = new Dictionary<string, string> {{"name", "Dan"}};

// Asignación
var list2 = list1;
var dic2 = dic1;

// Cambio
list1[0] = "Tom";
dic1["name"] = "Zoe";

// Las variables fueron afectadas por el cambio.
string rList = string.Join(", ", list2);
Console.WriteLine($"{rList}) - {dic2["name"]}");

// Ejemplo en una función
void fun_r(List<string> list, Dictionary<string, string> dic)
{
    list[0] = "Bob";
    dic["name"] = "Dan";
}
// Paso por referencia
fun_r(list2, dic2);

// Fueron afectadas por los cambios en la función.
string rList2 = string.Join(", ", list2);
Console.WriteLine($"{rList2}) - {dic2["name"]}");

/* _________________________________________
Ejercicio:
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras. */
Console.WriteLine("Ejercicio:");
string s1 = "Ben";
string s2 = "Zoe";
var l1 = new List<object> {12, 21};
var l2 = new List<object> {"Ben", "Zoe"};

string rL1 = string.Join(", ", l1);
string rL2 = string.Join(", ", l2);
Console.WriteLine($"Pre-Intercambio:\r\n{s1} - {s2}\r\n{rL1} - {rL2}");

static(string, string) by_value(string str1, string str2)
{
    (str1, str2) = (str2, str1);
    return (str1, str2);
}

static(List<object>, List<object>)by_reference(List<object>list1, List<object> list2)
{
    (list1, list2) = (list2, list1);
    return (list1, list2);
}

var (new_s1, new_s2) = by_value(s1, s2);
var (new_l1, new_l2) = by_reference(l1, l2);

rL1 = string.Join(", ", l1);
rL2 = string.Join(", ", l2);
Console.WriteLine($"Originales:\r\n{s1} - {s2}\r\n{rL1} - {rL2}");

rL1 = string.Join(", ", new_l1);
rL2 = string.Join(", ", new_l2);
Console.WriteLine($"Nuevas:\r\n{new_s1} - {new_s2}\r\n{rL1} - {rL2}");
