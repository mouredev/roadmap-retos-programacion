'''
EJERCICIO:
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
 * - Isogramas'''

 def multi(w1,w2):
    valor=0
    if w1==w2[::-1]:
        print(w2[::-1],w1)
        print('son palindromas.')
    w1_1=sorted(w1)
    w2_2=sorted(w2)
    if w1_1==w2_2:
        print('son anagramas')
    for i in range(1,len(w1)):
      print(w1[i],w1[:i])
      if w1[i] in w1[:i]:
        valor+=1
    if valor ==0:
      print(f'{w1} es un isograma')