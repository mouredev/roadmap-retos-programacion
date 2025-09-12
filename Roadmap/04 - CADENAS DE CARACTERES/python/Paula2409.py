""" 
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
 """
 
def characters():
    first_word = input('Ingrese una palabra para analizar: ')
    second_word = input('Ingrese otra palabra para analizar: ')
    print(f'La primer palabra tiene un largo de {len(first_word)}')
    print(f'La primer letra de la primer palabra es la {first_word[0]} y la ultima letra de la segunda es la {second_word[-1]}')
    print(f'La inversa de la primer palabra es {first_word[::-1]}')
    print(f'Dos veces la segunda palabra es {2*second_word}')
    print(f'La concatenacion se realiza sumando la primer palabra {first_word + " y la segunda palabra " + second_word}')
    print(f'Podemos separar los caracteres de la primer palabra en una lista con el metodo split: {first_word.split()}')
    my_list = []
    for char in second_word:
        my_list.append(char)
    print(f'Tambien se puede realizar lo mismo recorriendo la segunda palabra con un for: {my_list}')
    print(f'Primer palabra en mayusculas: {first_word.upper()}')
    print(f'Segunda palabra en minuscula: {second_word.lower()}')
    print(f'Indicamos la primer letra de la primer palabra como mayuscula: {first_word.capitalize()}')
    sentence = 'hola mundo python'
    print(f'Ejemplo de indicar formato titulo en una oracion {sentence}: {sentence.title()}')
    # Las cadenas de caracteres son tipos de datos inmutables, por lo que no pueden ser modificadas, sino que cualquier cambio debe guardarse dentro de otra referencia de variable:
    first_word = first_word.replace(first_word[0],"1")
    second_word = second_word.replace(second_word[0],"2")
    print(f'Podemos reemplazar un caracter: {first_word}')
    print(f'Podemos reemplazar un caracter: {second_word}')
    print(f'Chequeamos caracteres, si es alfabetico: {first_word.isalpha()}')
    print(f'Chequeamos caracteres, si es alfanumerico: {first_word.isalnum()}')
    print(f'Chequeamos caracteres, si es numerico: {first_word.isdigit()}')
    print(f'"1" existe en la primer palabra: {"1" in first_word}')
    print(f'"2" existe en la segunda palabra: {"2" in second_word}')

#characters()
    
def analyze_word():
    word_first = input('Ingrese una palabra: ')
    word_second = input('Ingrese otra palabra: ')
    
    def is_palindrom(word_first,word_second):
        # Palindrom
        word_first = word_first.lower()
        word_second = word_second.lower()
        
        if word_first == word_first[::-1]:
            print(f'La palabra {word_first} es palindromo')
        else:
            print(f'La palabra {word_first} no es palindromo')
        if word_second == word_second[::-1]:
            print(f'La palabra {word_second} es palindromo')
        else:
            print(f'La palabra {word_second} no es palindromo')
    
    def is_anagram(word_first,word_second):   
        # Anagram. Using dict
        first_anagram = {}
        second_anagram = {}
        
        for char in word_first:
            if char in first_anagram:
                first_anagram[char] +=1
            else:
                first_anagram[char] = 1
        
        for char in word_second:
            if char in second_anagram:
                second_anagram[char] +=1
            else:
                second_anagram[char] = 1
        
        if first_anagram == second_anagram:
            print(f'La palabra {word_first} es un anagrama de {word_second}')
        else:
            print('No son anagramas')
            
        # Anagram with sort
        if sorted(word_first) == sorted(word_second):
            print(f'Metodo sorted: La palabra {word_first} es anagrama de {word_second}')
        else:
            print('Metodo sorted: No son anagramas')  
    
    def is_isogram(word):    
        # Isogram
        word_dict = {}
        
        for char in word:
            if char in word_dict:
                word_dict[char] += 1
            else:
                word_dict[char] = 1
        analyze_value = word_dict.get(word[0]) 
        for value in word_dict.values():
            if value != analyze_value:
                return f"La palabra {word} no es isograma"
        return f"La palabra {word} es un isograma"   
      
    is_palindrom(word_first,word_second)
    is_anagram(word_first,word_second) 
    print(is_isogram(word_first))
    print(is_isogram(word_second))
             
analyze_word()
    