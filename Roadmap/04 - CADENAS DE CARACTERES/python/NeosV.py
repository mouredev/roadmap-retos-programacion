Ej_1 = ["Thirty","Days","Of","Python"]
join_1 = " ".join(Ej_1)
print(join_1)

Ej_2 = ["Coding","For","All"]
join_2 = " ".join(Ej_2)
print (join_2)

company = "Coding For All"
print (company)
print (len(company))
print (company.upper())
print (company.lower())
print (company.capitalize())
print (company.title())
print (company.swapcase())
print (company[6:])
print (company.find("Coding"))
print (company.replace ('Coding', 'Python'))
print (company.split())

variable = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print (variable.splitlines())

print (company[0])
print (company[-1])
print (company[10])

a, b ,c = company [0], company[7], company[11]
print (a,b,c) 

company_2 = "Python For All"

d, e ,f = company_2 [0], company_2[7], company_2[11]
print( d, e ,f)

print (company.find('C'))
print (company.find('f'))

company_3 = "Coding For All People"

print (company_3.rfind('p'))

company_4 = "You cannot end a sentence with because because because is a conjunction"

print (company_4.find('because'))
print (company_4.rfind('because'))
print (company_4 [31:54])

print (company.startswith('Coding'))
print (company.endswith('coding'))

variable_a = "30DaysOfPython"
variable_b = "thirty_days_of_python"

print (variable_a.isidentifier())
print (variable_b.isidentifier())

print('I am enjoying this challenge.\nI just wonder what is next. ?')

print( "Name\tAge\tCountry\t        City ")
print( "Andres\t22\tColombia\tBogota")

print ("radius = 10 \narea = 3.14 * radius ** 2 \nThe area of a circle with radius 10 is 314 meters square")

print ("8 + 6 = 14 \n8 - 6 = 2 \n8 * 6 = 48 \n8 / 6 = 1.33 \n8 % 6 = 2 \n8 // 6 = 1 \n8 ** 6 = 262144")

    


# Ejercicio Extra

def comprobador(palabra_1:str , palabra_2 : str):
   
   
   print (f"la palabra {palabra_1} es un palindromo? {palabra_1 == palabra_1[::-1]}")
   print (f"la palabra {palabra_2} es un palindromo? {palabra_2 == palabra_2[::-1]}")

   print (f"las palabras {palabra_1} y {palabra_2} son anagramas?: {sorted(palabra_2) == sorted(palabra_2)}")

   dictio = dict()
   for i in palabra_1:
      dictio [i] = dictio.get(i, 0)+1

      isograma = True
      valores = list(dictio.values())
      Isograma_len = valores[0]
      for i in valores:
         if i != Isograma_len:
            isograma = False
            break
   print (f"{palabra_2} es un Isograma? {len(palabra_2) == len(set(palabra_2))}") 

 




   
comprobador("amor" , "rada")


      
        