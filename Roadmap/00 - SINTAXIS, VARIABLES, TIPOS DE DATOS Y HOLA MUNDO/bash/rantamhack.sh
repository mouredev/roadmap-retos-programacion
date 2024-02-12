#!/bin/bash

# La pagina oficial de bash es https://gnu.org/software/bash

# Para comentar una sola línea se usa el símbolo  "#"
# Bash ignora todas las líneas que comiencen con este símbolo excepto la primera línea que define el script y se llama shebang


<< 'Comment' 
    El heredoc se usa para pasar entradas multilíneas a un
    comando. Se puede aprovechar para hacer un comentario
    multilinea al no pasarselo a ningún comando aunque no
    es lo mas apropiado. De hechos Visual Code lo adminte pero
    lo señala como error
Comment




# Constante
declare -r CONSTANTE=100

# También se puede expresar así:
declare --readonly CONSTANTE2=99


# Variables

# Entera (Int)
entera=5

# Decimal (float)
decimal=3,14

# String (str)
string="mi cadena de texo"

# Booleana (bool)
booleana=True

# Saludo al lenguaje que quiero aprender
Lenguaje="Bash"

echo $CONSTANTE
echo $CONSTANTE2
echo $entera
echo $decimal
echo $string
echo $booleana
echo "Hola, $Lenguaje!!"
