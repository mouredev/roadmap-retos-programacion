# ╔══════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado               ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 -  Python                       ║
# ╚══════════════════════════════════════╝

# ---------------------------------------
# 1. Asignación de variables "por valor":
# ---------------------------------------
# - se asigna el valor real de la variable a otra variable.
# - los cambios en una variable no afectarán a la otra.

# inicialización:
int1 = 111
boo1 = False
str1 = "Ben"

# asignación:
int2 = int1
boo2 = boo1
str2 = str1

# cambio:
int1 = 777
boo1 = True
str1 = "Bob"

# Las segundas variables no fueron afectadas.
print(int2, boo2, str2) # 111 False Ben

# -----------------------------
# ejemplo en una función:
def fun_v(en_int, en_boo, en_str):
    # cambio:
    en_int = 333
    en_boo = False
    en_str = "Ken"

# paso por valor
fun_v(int1, boo1, str1)

# no afectadas por los cambios en la función.
print(int1, boo1, str1) # 777 True "Bob"

# --------------------------------------------
# 2. Asignación de variables "por referencia":
# --------------------------------------------
# - se asigna la referencia o dirección de memoria 
#   de la variable a otra variable.
# - los cambios en una variable pueden afectar a la otra.

# inicialización:
lis1 = [444, True, "Dan"]
set1 = {444, True, "Dan"}
dic1 = {"name": "Dan"}

# asignación:
lis2 = lis1
set2 = set1
dic2 = dic1

# cambio:
lis1[0:3] = [888, False, "Zoe"]
set1.difference_update({444, "Dan"})
dic1["name"] = "Zoe"

# Las variables fueron afectadas por el cambio.
print(f"""
{lis2}
{set2}
{dic2}
""")

# -----------------------------
# ejemplo en una función:
def fun_r(en_lis, en_set, en_dic):
    # cambio:
    en_lis[0:3] = [333, True, "Jay"]
    en_set.update({333, "Jay"})
    en_dic["name"] = "Jay"

# paso por referencia
fun_r(lis2, set2, dic2)

# fueron afectadas por los cambios en la función.
print(f"""
{lis2}
{set2}
{dic2}
""")

# -------------
# 3. Ejercicio:
# -------------
'''
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
'''
s1 = "Ben"
s2 = "Zoe"
l1 = [12, 21]
l2 = ["Ben", "Zoe"]

print(f"""
Pre-Intercambio:
{s1} - {s2}
{l1} - {l2}
""")

def por_valor(str1, str2):
    temp = str1
    str1 = str2
    str2 = temp
    return str1, str2

def por_referencia(list1, list2):
    cambiar = list1
    list1 = list2
    list2 = cambiar
    return list1, list2

new_s1, new_s2 = por_valor(s1, s2)
new_l1, new_l2 = por_referencia(l1, l2)

print(f"""
Originales:
{s1} - {s2}
{l1} - {l2}

Nuevas:
{new_s1} - {new_s2}
{new_l1} - {new_l2}
""")
