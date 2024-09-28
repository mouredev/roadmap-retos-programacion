""" OPERACIONES CON CADENAS DE CARACTERES """

# Concatenación y repetición
S1 = "Había una vez, "
S2 = "un barquito chiquitito "
S3 = "que no podía, "
S4 = "que no podía navegar."
print((S1 + S2) * 2 + (S3 * 2) + S4)

# Función str()
NOMBRE = "María"
EDAD = 22
print("Mi hermana se llama " + NOMBRE + " y su edad es " + str(EDAD))

# Método .format()
NOMBRE2 = "Ricardo"
NUMERO_GATOS = 3
print(f"Mi abuelo se llama {NOMBRE2} y tiene {NUMERO_GATOS} gatos")

# Acceso a caracteres específicos, o a varios caracteres
S = "Soy fan de los videojuegos"
print(S[3])
print(S[-1]) # Último elemento
print(S[4:7]) # Del quinto al séptimo
print(S[-10:]) # Diez últimos caracteres

# Cambio a minúsculas, mayúsculas, capitalizar y titular cada palabra
S5 = "Me ENCANTAN el chocolate y las galletas"
print(S5.lower())
print(S5.upper())
print(S5.capitalize())
print(S5.title())

# Cambios de mayúsculas a minúsculas y viceversa
print(S5.swapcase())

# Método .count()
print(S5.count("s"))

# Método replace
print(S5.replace("galletas", "pastas"))

# Método split
print(S5.split("e"))

# Método .strip(), .rstrip() y lstrip()
S6 = "       El elefante tiene las orejas muy grandes        "
print(S6.strip())
print(S6.rstrip())
print(S6.lstrip())

# Método .find(), .index() y .rindex()
print(S6.find("e", 7))
print(S6.index("e", 3))
print(S6.rindex("e"))

# Función len()
print(len(S6))

# Recorrer un string
for c in S6.strip():
    print(c, end="#")

# Verificación
S7 = "verificacion"
N = 0
LETTER = "c"
print("\nLa letra '{}' {} está en la palabra".format(LETTER, "sí" if LETTER in S7 else "no"))


# DIFICULTAD EXTRA

class WordAnalisys():
    """
    Clase para analizar las palabras pasadas, unas con otras e
    individualmente
    """
    def __init__(self, w1, w2):
        self.w1 = w1.lower()
        self.w2 = w2.lower()
        self.reverse_w = str()
        self.reverse_w2 = str()
        self.dicc_w1 = {}
        self.dicc_w2 = {}
        self.dicc_result = {}

    def are_palindrome(self):
        """
        Método que determina si dos palabras son palíndromas,
        se leen igual en ambos sentidos
        """
        for character in self.w2:
            self.reverse_w2 = character + self.reverse_w2

        if self.w1 == self.reverse_w2:
            return True
        return None

    def is_palindrome(self, w):
        """
        Método para determinar si una palabra es palíndroma,
        se lee igual en ambos sentidos
        """
        for character in w:
            self.reverse_w = character + self.reverse_w

        if w == self.reverse_w:
            return True
        return None

    def are_anagram(self):
        """
        Método que determina si dos palabras son anagramas,
        usan las mismas letras para formar palabras distintas
        """
        for character in self.w1:
            self.dicc_w1.setdefault(character, self.w1.count(c))

        for letter in self.w2:
            self.dicc_w2.setdefault(letter, self.w1.count(letter))

        if dict(sorted(self.dicc_w1.items())) == dict(sorted(self.dicc_w2.items())):
            return True
        return None

    def are_isogram(self):
        """
        Método que determina si dos palabras son isogramas,
        tienen repetidas el mismo número de veces las letras
        """
        self.are_anagram()
        first_value_dicc_w1 = self.dicc_w1.get(list(self.dicc_w1.keys())[0])
        first_value_dicc_w2 = self.dicc_w2.get(list(self.dicc_w2.keys())[0])
        if (self.is_isogram(self.w1) is True and self.is_isogram(self.w2) is True and
            first_value_dicc_w1 == first_value_dicc_w2):
            return True
        return None

    def is_isogram(self, s):
        """
        Función para determinar si un texto tiene las letras repetidas
        el mismo número de veces
        """
        iso = False
        new_s = s.replace(" ", "").lower()
        letters = []
        for letter in new_s:
            letters.append(letter) if letter not in letters else None
        for item in letters:
            if new_s.count(item) == new_s.count(letters[0]):
                iso = True
            else:
                iso = False
                break

        return iso

    def result(self):
        """
        Método que devuelve el resultado del análisis realizado
        """
        self.dicc_result = {"ANÁLISIS COMPARANDO LAS PALABRAS": "",
        "¿Son palíndromos la una de la otra?": "Si"if self.are_palindrome() is True else "No",
        "¿Son anagramas la una de la otra?": "Si" if self.are_anagram() is True else "No",
        "¿Son isogramas la una de la otra?":"Si" if self.are_isogram() is True else "No",
        "\nANÁLISIS INDIVIDUAL DE LAS PALABRAS": "",
        f"¿{self.w1.capitalize()} es palíndromo?":
        "Si" if self.is_palindrome(self.w1) is True else "No",
        f"¿{self.w2.capitalize()} es palíndromo?":
        "Si" if self.is_palindrome(self.w2) is True else "No",
        f"¿{self.w1.capitalize()} es isograma?": "Si" if self.is_isogram(self.w1) is True else "No",
        f"¿{self.w2.capitalize()} es isograma?": "Si" if self.is_isogram(self.w2) is True else "No"}

        print(f"Las palabras a analizar son '{self.w1.capitalize()}' y '{self.w2.capitalize()}'\n")
        for key, value in self.dicc_result.items():
            print(key, value)

# EJEMPLO

analisys = WordAnalisys("Abalaba", "Marta")
analisys.result()
