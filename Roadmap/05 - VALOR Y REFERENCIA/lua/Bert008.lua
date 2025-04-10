--[[
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
]]

-- asignacion por valor
a = 10
b = a
print("a: ", a)
print("b: ", b)

-- asignacion por referencia
lista = {1, 2, 3, 4, 5}
a = lista[1]
b = lista[2]
c = lista[3]
d = lista[4]
e = lista[5]

print(a, b, c, d, e)

function suma(a, b)
    return a + b
end
c = suma(1, 2)
print("el resultado de suma es: ", c)

lista1 = {1, 2, 3, 4, 5}

function listas(lista1)
    for i in ipairs(lista1) do
        print(i)
    end

end
    

-- Extras
function xyyx(x, y)
    return y, x
end

function listas(lista1, lista2)
    
    
end